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
import { ref, onMounted } from 'vue';
import apiService from '../services/apiService';
import TeamMemberCard from './TeamMemberCard.vue';

const team = ref([]);
const loading = ref(true);
const error = ref(false);

onMounted(async () => {
  try {
    const data = await apiService.fetchTeamMembers();
    team.value = data.results;
  } catch (err) {
    console.error("Error al cargar el equipo:", err);
    error.value = true;
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.team-section {
  padding: 5rem 1rem;
  background-color: #f9fafb; /* Gris muy claro */
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  text-align: center;
}

.section-title {
  font-size: 2.25rem; /* 36px */
  font-weight: 800;
  color: #111827;
}

.section-subtitle {
  font-size: 1.25rem; /* 20px */
  color: #6b7280;
  margin-top: 0.5rem;
  margin-bottom: 4rem;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(1, 1fr); /* Una columna en móvil */
  gap: 2.5rem; /* 40px */
}

/* Media queries para hacer la cuadrícula responsive */
@media (min-width: 640px) {
  .team-grid {
    grid-template-columns: repeat(2, 1fr); /* Dos columnas en tablets */
  }
}

@media (min-width: 1024px) {
  .team-grid {
    grid-template-columns: repeat(3, 1fr); /* Tres columnas en desktop */
  }
}

.loading-message, .error-message {
  padding: 2rem;
  color: #6b7280;
}
</style>
