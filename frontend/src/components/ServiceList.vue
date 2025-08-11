<template>
  <div class="service-list-container">
    <div class="service-list-inner">
      <div class="service-list-header">
        <h2 class="service-list-title">Nuestros Servicios</h2>
        <p class="service-list-subtitle">Contabilidad, optimización tributario de la mano de expertos</p>
      </div>

      <!-- Muestra un indicador de carga mientras se obtienen los datos -->
      <div v-if="loading" class="service-list-loading">
        <p>Cargando servicios...</p>
      </div>
      
      <!-- Muestra un mensaje de error si la API falla -->
      <div v-else-if="error" class="service-list-error">
        <p>No se pudieron cargar los servicios. Intente de nuevo más tarde.</p>
      </div>

      <!-- Renderiza la lista de servicios -->
      <div v-else class="service-list-grid">
        <!-- Iteramos sobre la lista de servicios y creamos una tarjeta para cada uno -->
        <div v-for="service in services" :key="service.id">
          <ServiceCard :service="service" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import apiService, { type Service } from '../services/apiService';

  const services = ref<Service[]>([]);
  const loading = ref(true);
  const error = ref(false);

  onMounted(async () => {
    try {
      const data = await apiService.fetchServices();
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
.service-list-container {
  background: #ffffff;
  padding: 48px 0;
}
.service-list-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}
.service-list-header {
  text-align: center;
}
.service-list-title {
  font-size: 2rem;
  font-weight: bold;
  color: #222;
  margin-bottom: 8px;
}
.service-list-subtitle {
  font-size: 1.1rem;
  color: #666;
  margin-bottom: 24px;
}
.service-list-loading,
.service-list-error {
  text-align: center;
  padding: 32px 0;
  color: #c00;
}
.service-list-loading {
  color: #222;
}
.service-list-grid {
  margin-top: 40px;
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 32px;
}
@media (min-width: 600px) {
  .service-list-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (min-width: 900px) {
  .service-list-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
.service-list-card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  padding: 32px 24px;
  transition: box-shadow 0.3s, transform 0.3s;
}
.service-list-card:hover {
  box-shadow: 0 8px 32px rgba(0,0,0,0.12);
  transform: translateY(-4px);
}
.service-list-card-title {
  font-size: 1.2rem;
  font-weight: bold;
  color: #222;
  margin-bottom: 12px;
}
.service-list-card-desc {
  color: #666;
  font-size: 1rem;
}
</style>
