<template>
    <Navigation />
    <main>
        <slot />
    </main>
</template>

<style scoped>
    * {
        margin: 0px;
    }

    main {
        display: flex;
        align-items: center;
        justify-content: center;
        height: calc(100vh - 60px);
        overflow: scroll;
    }
</style>
