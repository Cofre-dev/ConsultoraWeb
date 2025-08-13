<template>
  <div class="team-section" id="nosotros">
    <div class="container">
      <h2 class="section-title">Nuestro Equipo</h2>
      <p class="section-subtitle">Los expertos detrás de tu éxito</p>
      
      <div v-if="loading" class="loading-message">Cargando equipo...</div>
      <div v-else-if="error" class="error-message">No se pudo cargar la información del equipo.</div>
      
      <div v-else class="team-grid">
        <TeamMemberCard 
          v-for="member in team" 
          :key="member.id" 
          :member="member" 
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
import TeamMemberCard from './TeamMemberCard.vue'; // Importamos la tarjeta

// CAMBIO CLAVE:
// Eliminamos onMounted, ref, apiService.
// Ahora el componente solo define las 'props' que espera recibir de su padre.
defineProps({
  team: {
    type: Array,
    required: true
  },
  loading: {
    type: Boolean,
    default: false
  },
  error: {
    type: Boolean,
    default: false
  }
});
</script>

<style scoped>
.team-section {
  padding: 2rem 0.5rem;
  background-color: #f9fafb;
}
.container {
  max-width: 1000px;
  margin: 0 auto;
  text-align: center;
}
.section-title {
  font-size: 2.25rem;
  font-weight: 800;
  color: #111827;
}
.section-subtitle {
  font-size: 1.25rem;
  color: #6b7280;
  margin-top: 0.5rem;
  margin-bottom: 4rem;
}
.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 2rem; 
}

.loading-message, .error-message {
  padding: 2rem;
  color: #6b7280;
  font-size: 1.25rem;
}
</style>