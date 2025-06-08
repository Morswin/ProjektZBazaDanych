<script setup>
    import { ref } from 'vue';

    const description = ref("");

    async function makeTicket() {
        if (description.value.length == 0) {
            alert("Nie zgłaszamy pustych ticketów! >:(");
        }
        else {
            try {
                const response = await $fetch(`http://localhost:8000/ticket`, {
                    method: 'POST',
                    body: {
                        description: description.value
                    }   
                });
                console.log("Zgłoszono!");
                console.log(response);
            }
            catch (e) {
                console.error("Nie udało się zgłosić problemu:", e);
            }
        }
    }
</script>

<template>
    <form>
        <label for="incident">Co się stało:</label>
        <select name="incident" id="">
            <option value="kraciez">Skradziono jedzenie</option>
            <option value="problem">Problem z zamowieniem</option>
            <option value="inne">Inne</option>
        </select>
        <label for="description">Opis zdarzenia</label>
        <textarea v-model="description" name="description" placeholder="Opisz zdarzenie..." id=""></textarea>
        <Button @click="makeTicket" class="przycisk">Zgłoś zdarzenie</Button>
    </form>
</template>

<style scoped>
    form {
        width: 50%;
        border: 2px solid black;
        padding: 20px;
        background-color: #f9f9f9;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    select {
        width: 80%;
        padding: 10px;
        font-size: 1rem;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    textarea {
        width: 95%;
        height: 100px;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        resize: none;
    }

    .przycisk {
        width: 50%;
    }
</style>