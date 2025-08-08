<template>
  <!-- Contenedor principal de la tarjeta con estilos de Tailwind -->
  <div class="bg-white rounded-xl shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1 overflow-hidden group">
    <div class="p-6">

      <div class="flex items-center space-x-4">
        <div class="flex-shrink-0 w-12 h-12 bg-gradient-to-br from-blue-500 to-blue-600 rounded-lg flex items-center justify-center">
          <!-- Aquí podrías usar un ícono real basado en `service.icon` -->
          <span class="text-white font-bold text-2xl">{{ service.title.charAt(0) }}</span>
        </div>

        <!-- Título del servicio -->
        <div>
          <h3 class="text-lg font-bold text-gray-900 group-hover:text-blue-600 transition-colors duration-30">
            {{ service.title }}
          </h3>
        </div>
      </div>

      <p class="mt-4 text-gray-600 text-sm">
        {{ service.short_description }}
      </p>
    </div>

    <!-- Pie de la tarjeta con un enlace "Ver más" que aparece al hacer hover -->
    <div class="bg-gray-50 px-6 py-3 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
      <a href="#" class="text-sm font-semibold text-blue-600 hover:text-blue-800">
        Ver más &rarr;
      </a>
    </div>
  </div>

</template>

<script setup lang="ts">
    // Importamos 'defineProps' para poder recibir datos desde el componente padre
    import { defineProps } from 'vue';

    // Definimos una interfaz para asegurar que los datos que recibimos son correctos
    interface Service {
      id: number;
      title: string;
      short_description: string;
      ver_mas: string;
    }

    // 'defineProps' declara que este componente espera recibir una prop llamada 'service'
    defineProps<{
      service: Service
    }>();

</script>
