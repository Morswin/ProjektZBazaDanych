<script setup>
    import {ref} from 'vue';
    import { useOrderStore } from '@/stores/useOrderStore';
    import { FoodOrder } from '@/libs/foodOrder';

    const orderStore = useOrderStore();

    const restaurants = ref([]);
    const restaurant_available_food = ref([]);

    const orderAddress = ref("");
    const orderEmail = ref("");

    async function goToRestaurantList() {
        // get the restaurants
        try {
            let result = await $fetch(`http://localhost:8000/restaurants`, {
                method: 'GET'
            });
            restaurants.value = result;
        }
        catch (e) {
            console.error("Nie udało się uzyskać listy restauracji", e);
        }
        // move to next stage
        orderStore.orderStage = 1;
    }

    async function getRestaurantData(id) {
        try {
            let result = await $fetch(`http://localhost:8000/restaurant`, {
                method: 'GET',
                params: {
                    restaurant_id: id
                }
            });
            orderStore.orderRestaurant = result;
        }
        catch (e) {
            console.error('Błąd z danymi restauracji: ', e)
        }
        try {
            let result = await $fetch(`http://localhost:8000/availablefood`, {
                method: 'GET',
                params: {
                    restaurant_id: id
                }
            });
            restaurant_available_food.value = result;
        }
        catch (e) {
            console.error("Błąd z listą jedzenia ", e)
        }
        orderStore.orderStage = 2;
    }

    function updateFoodOrderList(event, food) {
        if (event.target.checked) {
            // Checkbox was checked
            orderStore.addFoodToOrder(food);
        }
        else {
            // Checkbox was unchecked
            orderStore.removerFoodFromOrder(food);
        }
    }

    function createOrder() {
        orderStore.orderStage = 3;
    }

    function resetOrder() {
        orderStore.resetOrder();
    }

    async function finalizeOrder() {
        if (orderAddress.value.length == 0) {
            alert("Nie podano adresu");
        }
        else if (orderEmail.value.length == 0) {
            alert("Nie podano E-maila");
        }
        // Request o utworzenie orderu
        else {
            console.log(orderStore.getArrayOfFoodId());
            try {
                const response = await $fetch(`http://localhost:8000/order`, {
                    method: 'POST',
                    body: {
                        food_id: orderStore.getArrayOfFoodId(),
                        price: orderStore.getTotalPrice(),
                        restaurant_id: orderStore.orderRestaurant.id
                    }
                });
                console.log("Złożono zamówienie: ");
                console.log(response);
            }
            catch (e) {
                console.error("Nie dało się utworzyć zamówienia: ", e);
            }
        }
    }
</script>

<template>
    <main>
        <div v-if="orderStore.orderStage==0" class="przed-zamowieniem">
            <Button @click="goToRestaurantList">Zamów Jedzenie</Button>
        </div>
        <div v-else-if="orderStore.orderStage==1" class="wybor-restauracji">
            <div @click="() => getRestaurantData(restaurant.id)" v-for="restaurant in restaurants" :key="restaurant.id" class="restaurant-simplified">
                <h1>{{ restaurant.name }}</h1>
            </div>
        </div>
        <div v-else-if="orderStore.orderStage==2" class="wybor-jedzenia">
            <h1>{{ orderStore.orderRestaurant.name }}</h1>
            <table>
                <thead>
                    <tr>
                        <th>Jedzenie</th>
                        <th>Cena</th>
                        <th>Zaznacz</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="food in restaurant_available_food" :key="food.id">
                        <td>{{ food.name }}</td>
                        <td>{{ `${food.price.toFixed(2)}zł` }}</td>
                        <td><input @change="updateFoodOrderList($event, food)" type="checkbox"></td>
                    </tr>
                </tbody>
            </table>
            <Button @click="createOrder">Zamów</Button>
        </div>
        <div v-else-if="orderStore.orderStage==3" class="finalizacja-zamowienia">
            <div class="finalizacja-zamowienia-dane">
                <div>
                    <h3>Wymagane dane</h3>
                    <label for="address">Adres: <span style="color: red;">*</span></label>
                    <input v-model="orderAddress" type="text" id="address">
                    <label for="phone">Telefon:</label>
                    <input type="text" id="phone">
                    <label for="email">E-mail: <span style="color: red;">*</span></label>
                    <input v-model="orderEmail" type="text" id="email">
                </div>
                <div>
                    <h3>Zamówienie do "{{ orderStore.orderRestaurant.name }}"</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Jedzenie</th>
                                <th>Cena</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="food in orderStore.foodInOrder" :key="food.foodId">
                                <td>
                                    {{ food.name }}
                                </td>
                                <td>
                                    {{ food.price.toFixed(2) }}
                                </td>
                            </tr>
                            <tr>
                                <td>Suma:</td>
                                <td>
                                    {{ orderStore.foodInOrder.length>0 ? `${orderStore.getTotalPrice().toFixed(2)}zł` : "0,00zł" }}
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div>
                    <h3>Metoda płatności <span style="color: red;">*</span></h3>
                    <label>
                        <input type="radio" name="payment" value="blik"> Blik
                    </label>
                    <label>
                        <input type="radio" name="payment" value="przelewy24"> Przelewy24
                    </label>
                    <label>
                        <input type="radio" name="payment" value="gotowka"> Gotówka
                    </label>
                </div>
            </div>
            <div class="finalizacja-zamowienia-przyciski">
                <Button @click="finalizeOrder">Zamów</Button>
                <Button @click="resetOrder">Anuluj Zamówienie</Button>
            </div>
        </div>
        <Button @click="resetOrder" v-if="(!orderStore.orderStage==0) && (!orderStore.orderStage==3)" id="reset-order-button">Reset Zamówienia</Button>
    </main>
</template>

<style scoped>
    main {
        width: 60vw;
        display: flex;
        justify-content: center;
    }

    div.przed-zamowieniem {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    div.wybor-restauracji {
        display: flex;
        justify-content: center;
        flex-direction: column;
        width: 80%;
        border: 2px solid black;
        background-color: #f9f9f9;
        padding: 20px;
        margin-top: 100px;
    }

    div.restaurant-simplified {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #ccc;
        padding: 10px;
        margin-bottom: 10px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    div.restaurant-simplified:hover {
        background-color: #e0e0e0;
    }

    div.wybor-jedzenia {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    table {
        width: 80%;
        border-collapse: collapse;
        margin-bottom: 20px;
    }

    th, td {
        border: 1px solid black;
        padding: 10px;
        text-align: center;
    }

    div.finalizacja-zamowienia {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
    }

    div.finalizacja-zamowienia-dane {
        display: grid;
        grid-template-columns: 2fr 2fr 1fr;
        gap: 20px;
        width: 80vw;
        border: 2px solid black;
        padding: 20px;
        background-color: #f9f9f9;
    }

    div.finalizacja-zamowienia-dane > div {
        border: 1px solid black;
        padding: 10px;
        display: flex;
        flex-direction: column;
    }

    div.finalizacja-zamowienia-dane > div > h3 {
        margin-left: auto;
        margin-right: auto;
    }

    div.finalizacja-zamowienia-przyciski {
        display: flex;
        justify-content: space-around;
        width: 80vw;
        margin-top: 20px;
    }

    #reset-order-button {
        position: absolute;
        top: 80px;
        left: 20px;
    }
</style>