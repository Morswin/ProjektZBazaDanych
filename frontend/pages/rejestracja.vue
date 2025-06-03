<script setup>
    import { ref } from 'vue';

    const formData = ref({
        name: '',
        surename: '',
        gender: '',
        password: '',
        confirmPassword: '',
        email: '',
        phone: '',
        address: ''
    });

    async function register() {
        if (formData.value.password != formData.value.confirmPassword) {
            alert("Hasła się nie zgadzają!");
            return;
        }
        try {
            const response = await $fetch(`http://localhost:8000/register`, {
                method: 'POST',
                body: {
                    name: formData.value.name,
                    surename: formData.value.surename,
                    gender: 1,
                    email: formData.value.email,
                    phone: formData.value.phone,
                    address: formData.value.address,
                    user_type: 1
                }
            });
            console.log('Zarejestronano użytkownika', response);
        }
        catch (e) {
            console.error('Błąd rejestracji', e)
        }
    }
</script>

<template>
    <main>
        <div class="top-left">
            <label for="first-name">
                Imię: <span style="color: red;">*</span>
            </label>
            <input v-model="formData.name" type="text" id="first-name" placeholder="Jan">
            <label for="last-name">
                Nazwisko: <span style="color: red;">*</span>
            </label>
            <input v-model="formData.surename" type="text" id="last-name" placeholder="Kowalski">
            <label for="gender">
                Płeć: <span style="color: red;">*</span>
            </label>
            <select id="gender" v-model="formData.gender">
                <option value="">Wybierz płeć</option>
                <option value="male">Mężczyzna</option>
                <option value="female">Kobieta</option>
                <option value="other">Inne</option>
            </select>
        </div>
        <div class="top-right">
            <label for="password">
                Hasło: <span style="color: red;">*</span>
            </label>
            <input v-model="formData.password" type="password" id="password" placeholder="****************">
            <label for="confirm-password">
                Powtórz Hasło: <span style="color: red;">*</span>
            </label>
            <input v-model="formData.confirmPassword" type="password" id="confirm-password" placeholder="****************">
        </div>
        <div class="bottom-left">
            <label for="email">
                E-mail: <span style="color: red;">*</span>
            </label>
            <input v-model="formData.email" type="email" id="email" placeholder="jan.kowalski@elozelo.pl">
            <label for="phone">
                Telefon:
            </label>
            <input v-model="formData.phone" type="tel" id="phone" placeholder="123456789">
        </div>
        <div class="bottom-right">
            <label for="address">
                Address: <span style="color: red;">*</span>
            </label>
            <input v-model="formData.address" type="text" id="address" placeholder="ul. Przykładowa 1/2">
        </div>
        <div class="center">
            <Button @click="register">Zarejestruj się</Button>
        </div>
    </main>
</template>

<style scoped>
    main {
    display: grid;
    grid-template-areas: 
        "top-left       top-right"
        "bottom-left    bottom-right"
        "center         center"; 
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto auto auto;
        gap: 20px;
        border: 2px solid black;
        padding: 20px;
        width: 73%;
        background-color: #f9f9f9;
        margin: 0 auto;
    }

    input, select {
        margin: 0;
        padding: 10px;
        width: 50%;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 1rem;
    }

    div.top-left, 
    div.top-right,
    div.bottom-left,
    div.bottom-right {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    div.center {
        grid-area: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>