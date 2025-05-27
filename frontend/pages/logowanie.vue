<script setup>
    import { ref } from 'vue';

    const loginEmail = ref('');
    const loginPassword = ref('');
    const loginResult = ref('');
    const loginSuccessful = ref(false);

    async function login() {
        if (loginPassword.value.length > 0) {
            try {
                let result = await $fetch(`http://localhost:8000/login/`, {
                    method: 'GET',
                    params: {
                        email: loginEmail.value
                    }
                });
                loginResult.value = result;
                loginSuccessful.value = true;
                console.log(loginResult.value?.email);
            }
            catch (e) {
                loginResult.value = "Błędne logowanie";
                loginSuccessful.value = true;
                console.log(loginResult.value);
            }
        }
        else {
            loginResult.value = "Nie podano hasła.";
            loginSuccessful.value = true;
        }
    }
</script>

<template>
    <form>
        <label for="email">E-mail:</label>
        <input v-model="loginEmail" type="email" id="email" placeholder="elożelo@student.polsl.pl">
        <label for="password">Hasło:</label>
        <input v-model="loginPassword" type="password" id="password" placeholder="********">
        <Button @click="login" class="login-button">Zaloguj się</Button>
        <Button class="login-button">Zapomniałem hasła</Button>
        <Button class="login-button" targetUrl="/rejestracja">Zarejestruj się</Button>
        <p v-if="loginSuccessful">{{ loginResult }}</p>
    </form>
</template>

<style scoped>
    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 2px solid black;
        padding: 20px;
        width: 400px;
        background-color: #f9f9f9;
    }

    input {
        margin: 10px 0;
        padding: 10px;
        width: 100%;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 1rem;
    }

    .login-button {
        margin: 5px 0;
    }

    form > p {
        text-align: center;
    }
</style>