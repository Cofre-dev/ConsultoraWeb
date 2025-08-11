<template>
  <div v-if="slides.length > 0" class="relative w-full" id="inicio">
    <!-- Contenedor de las diapositivas -->
    <div class="relative h-96 md:h-[500px] overflow-hidden">
      <div v-for="(slide, index) in slides" :key="slide.id">
        <transition
          enter-active-class="transition-opacity duration-1000 ease-in-out"
          enter-from-class="opacity-0"
          enter-to-class="opacity-100"
          leave-active-class="transition-opacity duration-1000 ease-in-out"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <div v-if="index === currentIndex" class="absolute inset-0">
            <img :src="slide.image" class="w-full h-full object-cover" :alt="slide.title">
            <div class="absolute inset-0 bg-black bg-opacity-50"></div>
            <div class="absolute inset-0 flex flex-col justify-center items-center text-center text-white p-4">
              <h2 class="text-4xl md:text-6xl font-bold">{{ slide.title }}</h2>
              <p class="mt-4 text-lg md:text-xl max-w-2xl">{{ slide.subtitle }}</p>
              <a v-if="slide.link_url" :href="slide.link_url" class="mt-8 bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg transition-transform transform hover:scale-105">
                {{ slide.link_text }}
              </a>
            </div>
          </div>
        </transition>
      </div>
    </div>

    <!-- Controles de Navegación -->
    <button @click="prevSlide" class="absolute top-1/2 left-4 transform -translate-y-1/2 bg-white bg-opacity-50 hover:bg-opacity-75 rounded-full p-2 text-gray-800">
      &#10094;
    </button>
    <button @click="nextSlide" class="absolute top-1/2 right-4 transform -translate-y-1/2 bg-white bg-opacity-50 hover:bg-opacity-75 rounded-full p-2 text-gray-800">
      &#10095;
    </button>
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

onMounted(async () => {
  try {
    const data = await apiService.fetchCarouselSlides();
    slides.value = data.results;
    
    // Iniciar el carrusel automático
    slideInterval = window.setInterval(nextSlide, 8000); 
  } catch (error) {
    console.error("Error al cargar las diapositivas del carrusel:", error);
  }
});

onUnmounted(() => {
  clearInterval(slideInterval);
});
</script>
