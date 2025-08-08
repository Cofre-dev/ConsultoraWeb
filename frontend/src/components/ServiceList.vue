<template>
  <div class="service-list-container py-12 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center">
        <h2 class="text-3xl font-extrabold text-gray-900">Nuestros Servicios</h2>
        <p class="mt-4 text-lg text-gray-500">Contabilidad, optimización tributario de la mano de expertos</p>
      </div>

      <!-- Muestra un indicador de carga mientras se obtienen los datos -->
      <div v-if="loading" class="text-center py-8">
        <p>Cargando servicios...</p>
      </div>
      
      <!-- Muestra un mensaje de error si la API falla -->
      <div v-else-if="error" class="text-center py-8 text-red-600">
        <p>No se pudieron cargar los servicios. Intente de nuevo más tarde.</p>
      </div>

      <!-- Renderiza la lista de servicios -->
      <div v-else class="mt-10 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
        <!-- Iteramos sobre la lista de servicios y creamos una tarjeta para cada uno -->
        <div v-for="service in services" :key="service.id" class="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300">
          <h3 class="text-xl font-bold text-gray-900">{{ service.title }}</h3>
          <p class="mt-2 text-gray-600">{{ service.short_description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  // --- 1. Importamos nuestro servicio y la interfaz que define la estructura de los datos ---
  import apiService, { type Service } from '../services/apiService';

  // --- 2. Definimos el estado reactivo del componente ---
  const services = ref<Service[]>([]);
  const loading = ref(true);
  const error = ref(false);

  // --- 3. Usamos el servicio cuando el componente se monta ---
  onMounted(async () => {
    try {
      // Usamos la función 'fetchServices' de nuestro servicio para obtener los datos.
      const data = await apiService.fetchServices();
      // Guardamos los resultados en nuestra variable reactiva.
      services.value = data.results;
    } catch (err) {
      console.error("Error al obtener los servicios:", err);
      error.value = true;
    } finally {
      loading.value = false;
    }
  });
</script>

<style scoped>
/* Aquí puedes añadir estilos específicos si Tailwind no es suficiente */
</style>
