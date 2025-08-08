<template>
  <!-- Contenedor principal de la aplicación -->
  <div id="app-layout">
    <NavBar />
    <main>
      <RouterView />
    </main>
    
    <!-- <Footer /> -->
  </div>
</template>

<script setup lang="ts">
  import { RouterView } from 'vue-router';
  import NavBar from './components/NavBar.vue';
</script>

<style scoped>
  #app-layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background-color: #f9fafb; 
  }
  main {
    flex-grow: 1; 
  }
</style>
