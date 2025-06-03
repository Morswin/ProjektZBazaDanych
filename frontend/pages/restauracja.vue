<template>
    <main>
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
                    <tr>
                        <td>Test</td>
                        <td>21,37zł</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div>
            <h3>Dodaj do menu</h3>
            <div class="dodaj-do-menu">
                <div>
                    <input type="text" placeholder="Jedzenie">
                    <input type="text" placeholder="Cena">
                    <Button>Dodaj</Button>
                </div>
            </div>
        </div>
        <!-- <div>
            <h3>Dane</h3>
            <table>
                <thead>
                    <tr>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
            </table>
        </div> -->
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
</style>