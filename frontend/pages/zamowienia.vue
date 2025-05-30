<script setup>
    import {ref} from 'vue';

    /* Logic behind this variable:
     * 1 - Let's user choose a restaruant, based on what they're selling
     * 2 - Goes to that restaurant's menu and lets user decide based on that
     * 3 - Summary and finalizing the order. Now it's going to get recorded in the db
     */
    const orderingStage = ref(0);
    const restaurants = ref([]);
    const restaurant = ref({});
    const restaurant_available_food = ref([]);

    async function goToRestaurantList() {
        // get the restaurants
        try {
            let result = await $fetch(`http://localhost:8000/restaurants`, {
                method: 'GET'
            });
            console.log(result);
            restaurants.value = result;
        }
        catch (e) {
            console.error("Nie udało się uzyskać listy restauracji", e);
        }
        // move to next stage
        orderingStage.value = 1;
    }

    async function getRestaurantData(id) {
        // restaurantId.value = id;
        console.log(id)
        try {
            let result = await $fetch(`http://localhost:8000/restaurant`, {
                method: 'GET',
                params: {
                    restaurant_id: id
                }
            });
            restaurant.value = result;
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
            console.log(result);
            restaurant_available_food.value = result;
        }
        catch (e) {
            console.error("Błąd z listą jedzenia ", e)
        }
        orderingStage.value = 2;
    }
</script>

<template>
    <main>
        <div v-if="orderingStage==0" class="przed-zamowieniem">
            <Button @click="goToRestaurantList">Zamów Jedzenie</Button>
        </div>
        <div v-else-if="orderingStage==1" class="wybor-restauracji">
            <div @click="() => getRestaurantData(restaurant.id)" v-for="restaurant in restaurants" :key="restaurant.id" class="restaurant-simplified">
                <h1>{{ restaurant.name }}</h1>
            </div>
        </div>
        <div v-else-if="orderingStage==2" class="wybor-jedzenia">
            <h1>{{ restaurant.name }}</h1>
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
                        <td><input type="checkbox"></td>
                    </tr>
                </tbody>
            </table>
            <Button>Zamów</Button>
        </div>
    </main>
</template>

<style scoped>
    main {
        width: 60%;
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
</style>