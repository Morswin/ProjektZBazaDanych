<script setup>
    import { ref, onMounted } from 'vue';

    const selectedRestaurant = ref(false);
    const restaurants = ref([]);
    const restaurant = ref({});
    const restaurantAvailableFood = ref([]);

    const foodName = ref("");
    const foodPrice = ref("");

    async function getRestaurants() {
        try {
            let result = await $fetch(`http://localhost:8000/restaurants`, {
                method: 'GET'
            });
            restaurants.value = result;
        }
        catch (e) {
            console.error("Popsuło sie, sorry: ", e);
        }
    }
    onMounted(getRestaurants);

    async function getRestaurant(id) {
        try {
            let result = await $fetch(`http://localhost:8000/restaurant`, {
                method: 'GET',
                params: {
                    restaurant_id: id
                }
            });
            restaurant.value = result;
            selectedRestaurant.value = true;
        }
        catch (e) {
            console.log("Nie pykło: ", e);
        }
        try {
            let result = await $fetch(`http://localhost:8000/availablefood`, {
                method: 'GET',
                params: {
                    restaurant_id: id
                }
            });
            restaurantAvailableFood.value = result;
        }
        catch (e) {
            console.error("Błąd z listą jedzenia ", e)
        }
    }

    async function dodajJedzenie() {
        try {
            let result = await $fetch(`http://localhost:8000/newfood`, {
                method: 'POST',
                body: {
                    restaurant_id: restaurant.value.id,
                    price: parseFloat(foodPrice.value),
                    name: foodName.value
                }
            });
            console.log(result);
            foodPrice.value = "";
            foodName.value = "";
        }
        catch (e) {
            console.error("Dodawanie jedzenia nie powiodło się:", e);
        }
        try {
            let result = await $fetch(`http://localhost:8000/availablefood`, {
                method: 'GET',
                params: {
                    restaurant_id: restaurant.value.id
                }
            });
            restaurantAvailableFood.value = result;
        }
        catch (e) {
            console.error("Błąd z listą jedzenia ", e)
        }
    }
</script>

<template>
    <main v-if="!selectedRestaurant">
        <div class="wybierz-restauracje">
            <Button @click="() => {getRestaurant(restaurant.id)}" v-for="restaurant in restaurants" :key="restaurant.id" class="wybierz-restauracje-przycisk">
                {{ restaurant.name }}
            </Button>
        </div>
    </main>
    <main v-else>
        <div>
            <h3>Menu</h3>
            <table>
                <thead>
                    <tr>
                        <th>Jedzenie</th>
                        <th>Cena</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="food in restaurantAvailableFood" :key="food.id">
                        <td>{{ food.name }}</td>
                        <td>{{ `${food.price.toFixed(2)} zł` }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div>
            <h3>Dodaj do menu</h3>
            <div class="dodaj-do-menu">
                <div>
                    <input v-model="foodName" type="text" placeholder="Jedzenie">
                    <input v-model="foodPrice" type="text" placeholder="Cena">
                    <Button @click="dodajJedzenie">Dodaj</Button>
                </div>
            </div>
        </div>
    </main>
</template>

<style scoped>
    main {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
    }

    main > div {
        border: 2px solid black;
        background-color: #f9f9f9;
        padding: 20px;
        display: flex;
        align-items: center;
        flex-direction: column;
    }

    table {
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid black;
        padding: 10px;
        text-align: center;
    }

    div.dodaj-do-menu {
        display: flex;
        gap: 10px;
    }

    div.dodaj-do-menu > div {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    input, textarea {
        padding: 10px;
        font-size: 1rem;
    }

    textarea {
        height: 100%;
    }

    div.wybierz-restauracje {
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .wybierz-restauracje-przycisk {
        font-size: 2rem;
    }
</style>