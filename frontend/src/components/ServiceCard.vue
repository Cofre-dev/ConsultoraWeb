<template>
  <div class="service-card">
    <div class="service-card-content">
      <div class="service-card-header">
        <div class="service-card-icon">
          <span class="service-card-icon-text">{{ service.title.charAt(0) }}</span>
        </div>
        <div>
          <h3 class="service-card-title">
            {{ service.title }}
          </h3>
        </div>
      </div>
      <p class="service-card-description">
        {{ service.short_description }}
      </p>
    </div>
    <div class="service-card-footer">
      <a href="#" class="service-card-link">
        Ver más &rarr;
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';
import type { Service } from '../services/apiService';

defineProps<{
  service: Service
}>();

</script>

<style scoped>
.service-card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  transition: box-shadow 0.3s, transform 0.3s;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.service-card:hover {
  box-shadow: 0 8px 32px rgba(0,0,0,0.12);
  transform: translateY(-4px);
}
.service-card-content {
  padding: 24px;
}
.service-card-header {
  display: flex;
  align-items: center;
  gap: 16px;
}
.service-card-icon {
  flex-shrink: 0;
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #2563eb, #1e40af);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.service-card-icon-text {
  color: #fff;
  font-weight: bold;
  font-size: 1.5rem;
}
.service-card-title {
  font-size: 1.1rem;
  font-weight: bold;
  color: #222;
  margin: 0;
  transition: color 0.2s;
}
.service-card:hover .service-card-title {
  color: #2563eb;
}
.service-card-description {
  margin-top: 16px;
  color: #666;
  font-size: 0.95rem;
}
.service-card-footer {
  background: #f7f7f7;
  padding: 16px 24px;
  opacity: 0;
  transition: opacity 0.3s;
}
.service-card:hover .service-card-footer {
  opacity: 1;
}
.service-card-link {
  color: #2563eb;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  transition: color 0.2s;
}
</style>
