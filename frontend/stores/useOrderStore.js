import { defineStore } from "pinia";
import { ref } from "vue";

export const useOrderStore = defineStore(
    'order',
    () => {
        /* Logic behind this variable:
         * 1 - Let's user choose a restaruant, based on what they're selling
         * 2 - Goes to that restaurant's menu and lets user decide based on that
         * 3 - Summary and finalizing the order. Now it's going to get recorded in the db
         */
        const orderStage = ref(0);
        const orderRestaurant = ref({});
        const foodInOrder = ref([]);

        function addFoodToOrder(food) {
            /* The food is supposed to be of type FoodOrder. 
             * My bad for not writting it in TS, but it's too late, the deadline is in less than in a week, so..
             * ..so we're going to trus ourselves not to mess this up. 
             * Only this once 
             */
            foodInOrder.value.push(food)
            /* Well ,this part is not needed, because it's being added from a checkbox list, so it cannot be added multiple times. My bad */
            // if (foodInOrder.value.length == 0) {
            //     foodInOrder.value.push(food)
            // }
            // else {
            //     const result = foodInOrder.value.find(e => e.foodId == food.foodId);
            //     if (!result) {
            //         foodInOrder.value.push(food);
            //     }
            // }
        }

        function removerFoodFromOrder(food) {
            /* As in case of previous function, I'll naively assume that it received a FoodOrder object.
             */
            if (!(foodInOrder.value.length == 0)) {
                for (let i = 0; i < foodInOrder.value.length; i++) {
                    if (foodInOrder.value[i].foodId == food.foodId) {
                        foodInOrder.value.pop(i);
                        break;
                    }
                }
            }
        }

        function getTotalPrice() {
            let sum = 0.0;
            foodInOrder.value.forEach(food => sum += food.price);
            return sum;
        }

        function resetOrder() {
            orderStage.value = 0;
            orderRestaurant.value = {};
            foodInOrder.value = [];
        }

        return {foodInOrder, orderStage, orderRestaurant, addFoodToOrder, removerFoodFromOrder, resetOrder, getTotalPrice};
    }
    // ,
    // {
    //     persist: true
    // }
);
