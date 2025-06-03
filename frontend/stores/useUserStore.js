import { defineStore } from "pinia";

export const useUserStore = defineStore(
    'user', () => {
        const userName = ref('Elożelo');
        const loggedIn = ref(false);

        function logIn(newUserName) {
            userName.value = newUserName;
            loggedIn.value = true;
        };

        return {userName, loggedIn, logIn};
    },
    {
        persist: true
    }
);
