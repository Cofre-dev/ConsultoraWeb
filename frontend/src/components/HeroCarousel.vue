<template>
  <!-- Contenedor Principal con nuestra propia clase CSS -->
  <div v-if="slides.length > 0" class="carousel-container" id="inicio">
    
    <!-- Contenedor de las Diapositivas -->
    <div class="slides-wrapper">
      
      <!-- Bucle para cada diapositiva -->
      <template v-for="(slide, index) in slides" :key="slide.id">
        <!-- Componente de Transición de Vue para el efecto de fundido -->
        <transition
          enter-active-class="transition-fade-enter-active"
          enter-from-class="transition-fade-enter-from"
          leave-active-class="transition-fade-leave-active"
          leave-to-class="transition-fade-leave-to"
        >
          <!-- Contenido de una Diapositiva -->
          <div v-if="index === currentIndex" class="slide">
            <!-- Imagen de fondo -->
            <img :src="slide.image" class="slide-image" :alt="slide.title">
            <!-- Capa oscura para mejorar contraste del texto -->
            <div class="slide-overlay"></div>
            
            <!-- Contenido de texto con animación -->
            <div class="slide-text-container">
              <h2 
                class="slide-title"
                :class="{ 'slide-text-visible': index === currentIndex }"
              >
                {{ slide.title }}
              </h2>
              <p 
                class="slide-subtitle"
                :class="{ 'slide-text-visible': index === currentIndex }"
              >
                {{ slide.subtitle }}
              </p>
              <a 
                v-if="slide.link_url" 
                :href="slide.link_url" 
                class="slide-button"
                :class="{ 'slide-text-visible': index === currentIndex }"
              >
                {{ slide.link_text }}
              </a>
            </div>
          </div>
        </transition>
      </template>
    </div>

    <!-- Controles de Navegación -->
    <button @click="prevSlide" class="control-button prev">
      &#10094;
    </button>
    <button @click="nextSlide" class="control-button next">
      &#10095;
    </button>

    <!-- Indicadores de Diapositiva -->
    <div class="indicator-container">
      <button 
        v-for="(slide, index) in slides" 
        :key="`dot-${slide.id}`"
        @click="goToSlide(index)"
        class="indicator-dot"
        :class="{ 'active': index === currentIndex }"
        aria-label="Ir a la diapositiva"
      ></button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import apiService from '../services/apiService';

const slides = ref([]);
const currentIndex = ref(0);
let slideInterval;

const nextSlide = () => {
  if (slides.value.length > 0) {
    currentIndex.value = (currentIndex.value + 1) % slides.value.length;
  }
};

const prevSlide = () => {
  if (slides.value.length > 0) {
    currentIndex.value = (currentIndex.value - 1 + slides.value.length) % slides.value.length;
  }
};

const goToSlide = (index) => {
  currentIndex.value = index;
};

onMounted(async () => {
  try {
    const data = await apiService.fetchCarouselSlides();
    slides.value = data.results;
    
    slideInterval = window.setInterval(nextSlide, 8000); 
  } catch (error) {
    console.error("Error al cargar las diapositivas del carrusel:", error);
  }
});

onUnmounted(() => {
  clearInterval(slideInterval);
});
</script>

<style scoped>
/* Estilos CSS tradicionales para el carrusel */
.carousel-container {
  position: relative;
  width: 100%;
  border-radius: 0.5rem; /* 8px */
  overflow: hidden;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.slides-wrapper {
  position: relative;
  height: 24rem; /* 384px */
  background-color: #1f2937; /* bg-gray-800 */
}

.slide {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.slide-image {
  width: 100%;
  height: 100%;
  object-fit: cover; /* Asegura que la imagen cubra el área sin deformarse */
}

.slide-overlay {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-image: linear-gradient(to top, rgba(0,0,0,0.6), rgba(0,0,0,0.2));
}

.slide-text-container {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: white;
  padding: 1rem;
}

.slide-title, .slide-subtitle, .slide-button {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 700ms;
  transform: translateY(-20px);
  opacity: 0;
}

.slide-subtitle {
  transition-delay: 200ms;
}

.slide-button {
  transition-delay: 300ms;
}

.slide-text-visible {
  transform: translateY(0);
  opacity: 1;
}

.slide-title {
  font-size: 2.25rem; /* 36px */
  font-weight: 700;
}

.slide-subtitle {
  margin-top: 1rem;
  font-size: 1.125rem; /* 18px */
  max-width: 42rem; /* 672px */
}

.slide-button {
  margin-top: 2rem;
  background-color: #2563eb; /* bg-blue-600 */
  color: white;
  font-weight: 700;
  padding: 0.75rem 2rem;
  border-radius: 0.5rem;
  box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
  transition-property: all;
  transition-duration: 300ms;
}

.slide-button:hover {
  background-color: #1d4ed8; /* hover:bg-blue-700 */
  transform: scale(1.05);
}

.control-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(4px);
  border-radius: 9999px;
  color: white;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  opacity: 0;
  transition: all 0.3s ease;
  z-index: 10;
  cursor: pointer;
}

.carousel-container:hover .control-button {
  opacity: 1;
}

.control-button:hover {
  background-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-50%) scale(1.1);
}

.control-button.prev {
  left: 1rem;
}

.control-button.next {
  right: 1rem;
}

.indicator-container {
  position: absolute;
  bottom: 1.25rem; /* 20px */
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 0.75rem; /* 12px */
  z-index: 10;
}

.indicator-dot {
  width: 10px;
  height: 10px;
  border-radius: 9999px;
  background-color: rgba(255, 255, 255, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.5);
  transition: all 0.3s ease;
  cursor: pointer;
}

.indicator-dot.active {
  background-color: white;
  width: 24px;
  border-radius: 10px;
}

h2, p {
  text-shadow: 0px 2px 5px rgba(0, 0, 0, 0.6);
}

/* Transiciones de Vue */
.transition-fade-enter-active,
.transition-fade-leave-active {
  transition: opacity 1s ease-in-out;
}
.transition-fade-enter-from,
.transition-fade-leave-to {
  opacity: 0;
}
.transition-fade-leave-active {
  position: absolute;
}


/* Media Queries para Responsive */
@media (min-width: 768px) {
  .slides-wrapper {
    height: 600px;
  }
  .slide-title {
    font-size: 3.75rem; /* 60px */
  }
  .slide-subtitle {
    font-size: 1.25rem; /* 20px */
  }
}
</style>
