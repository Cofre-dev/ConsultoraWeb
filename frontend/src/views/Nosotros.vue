<template>
  <div class="py-16 bg-white" id="nosotros">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center">
        <h2 class="text-base font-semibold text-blue-600 tracking-wide uppercase">Nuestro Equipo</h2>
        <p class="mt-2 text-3xl font-extrabold text-gray-900 sm:text-4xl">
          Los expertos detrás de tu éxito
        </p>
      </div>
      
      <div v-if="loading" class="text-center py-12">Cargando...</div>
      <div v-else-if="error" class="text-center py-12 text-red-600">Error al cargar el equipo.</div>
      
      <div v-else class="mt-12 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
        <TeamMemberCard 
          v-for="member in team" 
          :key="member.id"
          :member="member"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import apiService, { type TeamMember } from '../services/apiService';
import TeamMemberCard from '../components/TeamMemberCard.vue';

const team = ref<TeamMember[]>([]);
const loading = ref(true);
const error = ref(false);

onMounted(async () => {
  try {
    const data = await apiService.fetchTeamMembers();
    team.value = data.results;
  } catch (err) {
    console.error("Error al obtener el equipo:", err);
    error.value = true;
  } finally {
    loading.value = false;
  }
});
</script>
