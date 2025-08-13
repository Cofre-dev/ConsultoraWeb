<template>
  <div class="service-card">
    <div class="service-icon-wrapper">
      <!-- Aquí podrías usar un ícono real en el futuro -->
      <span class="service-icon-letter">{{ service.title.charAt(0) }}</span>
    </div>
    <h3 class="service-title">{{ service.title }}</h3>
    <p class="service-description">{{ service.short_description }}</p>
    <a href="#" class="service-link">
      Saber más &rarr;
    </a>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  service: {
    type: Object,
    required: true
  }
});
</script>

<style scoped>
.service-card {
  background-color: white;
  padding: 2.5rem 2rem; /* 40px 32px */
  border-radius: 0.75rem; /* 12px */
  text-align: center;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease-in-out;
  border: 1px solid #e5e7eb;
}

.service-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  border-color: #3b82f6; /* Azul primario */
}

.service-icon-wrapper {
  margin: 0 auto 1.5rem;
  width: 4rem; /* 64px */
  height: 4rem;
  border-radius: 50%;
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 2rem;
  font-weight: 700;
}

.service-title {
  font-size: 1.25rem; /* 20px */
  font-weight: 700;
  color: #111827; /* Casi negro */
  margin-bottom: 0.75rem;
}

.service-description {
  color: #4b5563; /* Gris oscuro */
  line-height: 1.6;
  min-height: 80px; /* Altura mínima para consistencia */
}

.service-link {
  display: inline-block;
  margin-top: 1.5rem;
  color: #2563eb;
  font-weight: 600;
  text-decoration: none;
  position: relative;
}

.service-link::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: -4px;
  left: 0;
  background-color: #2563eb;
  transition: width 0.3s;
}

.service-link:hover::after {
  width: 100%;
}
</style>
