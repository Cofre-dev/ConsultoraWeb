<template>
  <TeamSection 
    :team="team"
    :loading="loading"
    :error="error"
  />
</template>

<script setup lang="ts">
// La lógica de carga de datos se mantiene aquí, en la vista principal.
import { ref, onMounted } from 'vue';
import apiService, { type TeamMember } from '../services/apiService';
import TeamSection from '../components/TeamSection.vue'; // Importamos nuestro componente de sección

const team = ref<TeamMember[]>([]);
const loading = ref(true);
const error = ref(false);

onMounted(async () => {
  try {
    const data = await apiService.fetchTeamMembers();
    // CAMBIO IMPORTANTE: Asegúrate de que los datos de la API coincidan con
    // lo que espera la tarjeta (name, position, photo, bio, linkedin_url).
    // Si los nombres de los campos son diferentes, deberás mapearlos aquí.
    // Por ejemplo: team.value = data.results.map(item => ({ name: item.nombre, ... }))
    team.value = data.results; 
  } catch (err) {
    console.error("Error al obtener el equipo:", err);
    error.value = true;
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
/* Esta vista ya no necesita estilos propios, ya que toda la presentación
  está encapsulada dentro del componente TeamSection. ¡Más limpio!
*/
</style>