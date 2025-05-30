<template>
    <nav>
        <Button targetUrl="/">Strona Główna</Button>
        <Button targetUrl="/logowanie">Logowanie</Button>
        <Button targetUrl="/rejestracja">Rejestracja</Button>
        <Button targetUrl="/zamowienia">Zamówienia</Button>
        <Button targetUrl="/kurier">Widok Kuriera</Button>
        <Button targetUrl="/restauracja">Widok Restauracji</Button>
        <Button targetUrl="/kontakt">Kontakt</Button>
    </nav>
</template>

<style scoped>
    nav {
        display: flex;
        align-items: center;
        background-color: #f4f4f4;
        padding: 10px 20px;
        border-bottom: 2px solid black;
        justify-content: center;
        gap: 10px;
    }
</style>