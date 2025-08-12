<template>
  <!-- Contenedor principal que reacciona al clic para activar el giro -->
  <div class="card-container" @click="isFlipped = !isFlipped">
    <div class="card-inner" :class="{ 'is-flipped': isFlipped }">
      
      <!-- CARA FRONTAL -->
      <div class="card-face card-face-front">
        <img class="card-photo" :src="member.photo" :alt="`Foto de ${member.name}`">
        <div class="card-front-info">
          <h3 class="card-name">{{ member.name }}</h3>
          <p class="card-position">{{ member.position }}</p>
        </div>
      </div>

      <!-- CARA TRASERA -->
      <div class="card-face card-face-back">
        <div class="card-back-content">
          <h3 class="card-name-back">{{ member.name }}</h3>
          <p v-if="member.bio" class="card-bio">{{ member.bio }}</p>
          <a v-if="member.linkedin_url" :href="member.linkedin_url" target="_blank" rel="noopener noreferrer" class="card-link">
            Ver Perfil en LinkedIn
          </a>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue';

// Estado para controlar si la tarjeta está girada o no
const isFlipped = ref(false);

// Definimos las 'props' que el componente espera recibir
defineProps({
  member: {
    type: Object,
    required: true
  }
});
</script>

<style scoped>
/* Estilos para el efecto de giro 3D */
.card-container {
  width: 100%;
  height: 400px; /* Altura fija para consistencia */
  perspective: 1000px; /* Activa la perspectiva 3D */
  cursor: pointer;
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.7s;
  transform-style: preserve-3d;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  border-radius: 1rem; 
}

.card-container:hover .card-inner {
  box-shadow: 0 20px 35px rgba(0, 0, 0, 0.15);
}

.is-flipped {
  transform: rotateY(180deg); /* El giro de 180 grados */
}

.card-face {
  position: absolute;
  width: 100%;
  height: 400px;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden; 
  border-radius: 1rem;
  overflow: hidden;
}

/* Estilos de la cara frontal */
.card-face-front {
  background-color: white;
  display: flex;
  flex-direction: column;
}

.card-photo {
  width: 100%;
  height: 70%;
  object-fit: cover;
}

.card-front-info {
  padding: 1.5rem;
  text-align: center;
}

.card-name {
  font-size: 1.25rem; /* 20px */
  font-weight: 700;
  color: #111827;
}

.card-position {
  color: #2563eb;
  font-weight: 600;
}

/* Estilos de la cara trasera */
.card-face-back {
  background-color: #111827; /* Fondo oscuro para contraste */
  color: white;
  transform: rotateY(180deg); /* La posicionamos girada por defecto */
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 2rem;
  text-align: center;
}

.card-name-back {
  font-size: 1.25rem;
  font-weight: 700;
  color: white;
}

.card-bio {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: #d1d5db; /* Gris claro */
  flex-grow: 1;
}

.card-link {
  display: inline-block;
  margin-top: 1.5rem;
  background-color: #2563eb;
  color: white;
  padding: 0.5rem 1.5rem;
  border-radius: 9999px; /* Píldora */
  text-decoration: none;
  transition: background-color 0.3s;
}

.card-link:hover {
  background-color: #1d4ed8;
}
</style>
