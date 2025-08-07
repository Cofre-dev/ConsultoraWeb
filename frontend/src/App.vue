<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Header de prueba -->
    <header class="bg-blue-600 text-white p-6 shadow-lg">
      <h1 class="text-4xl font-bold">Prueba de Tailwind CSS</h1>
      <p class="text-blue-100 mt-2">Si ves colores y estilos, funciona correctamente</p>
    </header>

    <!-- Contenido principal -->
    <main class="container mx-auto p-8">
      <!-- Cards de prueba -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-xl transition-shadow">
          <div class="w-12 h-12 bg-green-500 rounded-full mb-4"></div>
          <h2 class="text-xl font-semibold text-gray-800">Card Verde</h2>
          <p class="text-gray-600 mt-2">Esta card debe tener sombra</p>
        </div>

        <div class="bg-gradient-to-br from-purple-500 to-pink-500 text-white rounded-lg p-6">
          <h2 class="text-xl font-semibold">Card Gradiente</h2>
          <p class="mt-2">Fondo con gradiente púrpura a rosa</p>
        </div>

        <div class="border-2 border-red-500 border-dashed rounded-lg p-6">
          <h2 class="text-xl font-semibold text-gray-800">Card con Borde</h2>
          <p class="text-gray-600 mt-2">Borde rojo punteado</p>
        </div>
      </div>

      <!-- Botones de prueba -->
      <div class="flex gap-4 flex-wrap">
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Botón Azul
        </button>
        <button class="bg-transparent hover:bg-green-500 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-500 hover:border-transparent rounded">
          Botón Verde
        </button>
        <button class="bg-red-500 text-white px-6 py-3 rounded-full shadow-lg hover:shadow-xl transform hover:scale-105 transition-all">
          Botón Rojo
        </button>
      </div>

      <!-- Alerta -->
      <div class="mt-8 bg-yellow-100 border-l-4 border-yellow-500 text-yellow-700 p-4">
        <p class="font-bold">¡Atención!</p>
        <p>Si ves todos estos estilos, Tailwind está funcionando perfectamente.</p>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
  console.log("✅ Vue + TypeScript funcionando")
  console.log("🎨 Verificando Tailwind CSS...")
</script>
