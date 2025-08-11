<template>
  <div class="team-card">
    <img class="team-card-photo" :src="member.photo" :alt="`Foto de ${member.name}`">
    <h3 class="team-card-name">{{ member.name }}</h3>
    <p class="team-card-position">{{ member.position }}</p>
    <p v-if="member.bio" class="team-card-bio">{{ member.bio }}</p>
    <a v-if="member.linkedin_url" :href="member.linkedin_url" target="_blank" class="team-card-link">
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

<style scoped>
.team-card {
  text-align: center;
  background: #fff;
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  transition: box-shadow 0.3s, transform 0.3s;
  overflow: hidden;
}
.team-card:hover {
  box-shadow: 0 8px 32px rgba(0,0,0,0.12);
  transform: scale(1.05);
}
.team-card-photo {
  width: 128px;
  height: 128px;
  border-radius: 50%;
  object-fit: cover;
  margin: 0 auto 16px auto;
  display: block;
}
.team-card-name {
  font-size: 1.25rem;
  font-weight: bold;
  color: #222;
  margin-bottom: 8px;
}
.team-card-position {
  color: #2563eb;
  font-weight: 600;
  margin-bottom: 8px;
}
.team-card-bio {
  margin-top: 8px;
  color: #666;
  font-size: 0.95rem;
}
.team-card-link {
  margin-top: 16px;
  display: inline-block;
  color: #2563eb;
  font-weight: 500;
  text-decoration: none;
  transition: color 0.2s;
  font-size: 1rem;
}
.team-card-link:hover {
  color: #1d4ed8;
}
</style>