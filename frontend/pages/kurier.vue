<template>
    <main>
        <aside>
            <div>Pozostało czasu:</div>
            <div>Ilość zrealizowanych zamówień</div>
            <div>Zarobiono:</div>
            <div>Ocena:</div>
        </aside>
        <article >
            <div class="new-order">Nowe zamówienie</div>
            <div class="order-details">
                <div>Restauracja: Nazwa</div>
                <div>Opis: Duże/Lekkie/Ciężkie/Małe</div>
            </div>
            <div class="client-address">
                Adres Klienta
            </div>
            <div class="accept-order">
                <Button>Dostarczone</Button>
            </div>
        </article>
    </main>
</template>

<style>
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
        width: 100%;
    }

    aside {
        display: flex;
        justify-content: space-between;
        width: 80%;
        margin-bottom: 20px;
        font-size: 1rem;
        font-weight: bold;
    }

    aside > div {
        border: 1px solid black;
        padding: 10px;
        text-align: center;
        width: 23%;
    }

    article {
        display: grid;
        grid-template-columns: 1fr 2fr 1fr;
        grid-template-rows: auto auto auto;
        gap: 20px;
        width: 80%;
        border: 2px solid black;
        padding: 20px;
        background-color: #f9f9f9;
    }

    .new-order {
        grid-column: 1 / 2;
        grid-row: 1 / 2;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid black;
        padding: 10px;
        text-align: center;
    }

    .order-details {
        grid-column: 2 / 3;
        grid-row: 1 / 2;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 1px solid black;
        padding: 10px;
    }

    .client-address {
        grid-column: 3 /4;
        grid-row: 1 / 2;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid black;
        padding: 10px;
        text-align: center;
    }

    .accept-order {
        grid-column: 1 / 4;
        grid-row: 3 / 4;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        text-align: center;
    }
</style>