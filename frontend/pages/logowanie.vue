<template>
    <form>
        <label for="email">E-mail:</label>
        <input type="email" id="email" placeholder="elożelo@student.polsl.pl">
        <label for="password">Hasło:</label>
        <input type="password" id="password" placeholder="********">
        <Button class="login-button">Zaloguj się</Button>
        <Button class="login-button">Zapomniałem hasła</Button>
        <Button class="login-button" targetUrl="/rejestracja">Zarejestruj się</Button>
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
</style>