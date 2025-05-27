<script setup>
    const props = defineProps(['targetUrl']);
</script>

<template>
    <a :href="targetUrl">
        <slot />
    </a>
</template>

<style scoped>
    a {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px 20px;
        border: 2px solid black;
        font-size: 1rem;
        font-weight: bold;
        text-decoration: none;
        color: black;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
        font-family: Arial, sans-serif;
    }
    
    a:hover {
        background-color: #e0e0e0;
        transform: scale(1.05);
    }
</style>