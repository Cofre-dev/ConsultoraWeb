<template>
  <div class="text-center bg-white p-8 rounded-lg shadow-md transition-transform transform hover:scale-105">
    <img class="w-32 h-32 rounded-full mx-auto mb-4 object-cover" :src="member.photo" :alt="`Foto de ${member.name}`">
    <h3 class="text-xl font-bold text-gray-900">{{ member.name }}</h3>
    <p class="text-blue-600 font-semibold">{{ member.position }}</p>
    <p v-if="member.bio" class="mt-2 text-gray-500 text-sm">{{ member.bio }}</p>
    <a v-if="member.linkedin_url" :href="member.linkedin_url" target="_blank" class="mt-4 inline-block text-blue-500 hover:text-blue-700">
      Ver en LinkedIn
    </a>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';
import type { TeamMember } from '../services/apiService';

defineProps<{
  member: TeamMember
}>();
</script>