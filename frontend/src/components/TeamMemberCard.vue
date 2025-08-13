<template>
  <div class="card-container" @click="isFlipped = !isFlipped">
    <div class="card-inner" :class="{ 'is-flipped': isFlipped }">
      <div class="card-face card-face-front">
        <img class="card-photo" :src="member.photo" :alt="`Foto de ${member.name}`">
        <div class="card-front-info">
          <h3 class="card-name">{{ member.name }}</h3>
          <p class="card-position">{{ member.position }}</p>
        </div>
      </div>
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
const isFlipped = ref(false);
defineProps({
  member: { type: Object, required: true }
});
</script>
<style scoped>
/* --- Contenedor Principal y Giro --- */

.card-container {
  /* Modelo de Caja */
  width: 100%;
  aspect-ratio: 4 / 5;

  /* Animación y Perspectiva */
  perspective: 1200px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;

  /* Misceláneo */
  cursor: pointer;
}

.card-container:hover {
  /* Animación y Apariencia */
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.card-inner {
  /* Posicionamiento */
  position: relative;

  /* Modelo de Caja */
  width: 100%;
  height: 100%;

  /* Apariencia */
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
  border-radius: 1rem;

  /* Animación y 3D */
  transform-style: preserve-3d;
  transition: transform 0.8s cubic-bezier(0.76, 0, 0.24, 1);
}

.is-flipped {
  /* Animación */
  transform: rotateY(180deg);
}

/* --- Estilos de las Caras --- */

.card-face {
  /* Posicionamiento */
  position: absolute;
  box-sizing: border-box;

  /* Modelo de Caja */
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;

  /* Apariencia */
  border-radius: 1rem;
  overflow: hidden;

  /* Animación y 3D */
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden; /* Soporte para Safari */
}

.card-face-front {
  /* Apariencia */
  background-color: #ffffff;
}

.card-face-back {
  /* Modelo de Caja */
  /* El display:flex ya lo hereda de .card-face */
  justify-content: center;
  padding: 2rem;

  /* Tipografía */
  color: #ffffff;
  text-align: center;

  /* Apariencia */
  background-color: #1a202c;

  /* Animación */
  transform: rotateY(180deg);
}


/* --- Contenido de la Cara Frontal --- */

.card-photo {
  /* Modelo de Caja */
  width: 100%;
  height: 75%;

  /* Apariencia */
  object-fit: cover;
  object-position: center top;
}

.card-front-info {
  /* Modelo de Caja */
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex-grow: 1;
  padding: 1rem 1.5rem;

  /* Tipografía */
  text-align: left;
}


/* --- Contenido de la Cara Trasera --- */
.card-bio {
  width: 100%;
  height: 50%;

  flex-grow: 0.5;

  /* Tipografía */
  font-size: 0.9rem;
  line-height: 1.6;
  color: #e2e8f0;
}

.card-link {
  /* Modelo de Caja */
  display: inline-block;
  margin-top: 1rem;
  padding: 0.6rem 1rem;

  /* Tipografía */
  font-weight: 600;
  color: #ffffff;
  text-decoration: none;

  /* Apariencia */
  background-color: #2563eb;
  border-radius: 9999px;

  /* Animación */
  transition: background-color 0.2s, transform 0.2s;
}

.card-link:hover {
  /* Apariencia */
  background-color: #1d4ed8;

  /* Animación */
  transform: scale(1.05);
}

/* --- Textos (Comunes y Específicos) --- */
.card-name {
  /* Modelo de Caja */
  margin: 0;

  /* Tipografía */
  font-size: 1.15rem;
  font-weight: 700;
  color: #111827;
}

.card-position {
  /* Modelo de Caja */
  margin: 0.25rem 0 0;

  /* Tipografía */
  font-size: 0.9rem;
  font-weight: 500;
  color: #2563eb;
}

.card-name-back {
  /* Modelo de Caja */
  margin-bottom: 1rem;

  /* Tipografía */
  font-size: 1.15rem;
  font-weight: 700;
  color: #ffffff;
}
</style>