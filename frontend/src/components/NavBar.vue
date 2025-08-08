<template>
  <!-- Navbar principal con sombra y sticky (se queda arriba al hacer scroll) -->
  <nav class="bg-white shadow-lg sticky top-0 z-50">
    <!-- Container para centrar contenido con max-width -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Flex container para logo y menú -->
      <div class="flex justify-between h-20">
        
        <!-- LADO IZQUIERDO: Logo y nombre de la empresa -->
        <div class="flex items-center">
          <div class="flex-shrink-0 flex items-center">
            <!-- Puedes reemplazar esto con una imagen de logo -->
            <div class="flex items-center space-x-3">
              <!-- Icono temporal - reemplazar con logo real -->
              <div class="w-14 h-10 bg-gradient-to-br from-blue-600 to-blue-700 rounded-lg flex items-center justify-center">
                <span class="text-white font-bold text-xl">A&B</span>
              </div>
              <!-- Nombre de la empresa -->
              <div>
                <h1 class="text-xl font-bold text-gray-900">
                  Ara y bustamante consultores
                </h1>
                <p class="text-xs text-gray-600">Expertos en tributación</p>
              </div>
            </div>
          </div>
        </div>

        <!-- CENTRO/DERECHA: Menú de navegación (desktop) -->
        <div class="hidden md:flex items-center space-x-8">
          <!-- Enlaces de navegación -->
          <a 
            v-for="item in menuItems" 
            :key="item.name"
            :href="item.href"
            class="text-gray-700 hover:text-blue-600 transition-colors duration-200 font-medium"
            @click="handleNavClick"
          >
            {{ item.name }}
          </a>
          
          <!-- Botón CTA (Call to Action) -->
          <button class="bg-gradient-to-r from-blue-600 to-blue-700 text-white px-6 py-2.5 rounded-lg hover:from-blue-700 hover:to-blue-800 transition-all duration-200 shadow-md hover:shadow-lg transform hover:-translate-y-0.5 ">
            Portal Clientes
          </button>
        </div>

        <!-- BOTÓN HAMBURGUESA: Solo visible en móvil -->
        <div class="md:hidden flex items-center">
          <button 
            @click="toggleMobileMenu"
            class="text-gray-700 hover:text-gray-900 focus:outline-none focus:text-gray-900"
            aria-label="Abrir menú"
          >
            <!-- Icono hamburguesa animado -->
            <svg 
              class="mt-10 h-8 w-8 transition-transform duration-200"
              :class="{ 'rotate-90': mobileMenuOpen }"
              fill="none" 
              viewBox="0 0 24 24" 
              stroke="currentColor"
            >
              <path 
                v-if="!mobileMenuOpen"
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="3" 
                d="M4 6h16M4 12h16M4 18h16" 
              />
              <path 
                v-else
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2" 
                d="M6 18L18 6M6 6l12 12" 
              />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- MENÚ MÓVIL: Se muestra/oculta la animación -->
    <Transition
      enter-active-class="transition ease-out duration-200"
      enter-from-class="opacity-0 -translate-y-1"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition ease-in duration-150"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-1"
    >
      <div 
        v-if="mobileMenuOpen" 
        class="md:hidden bg-white border-t border-gray-200"
      >
        <div class="px-10 pt-10 pb-10 space-y-1">
          <a 
            v-for="item in menuItems"
            :key="item.name"
            :href="item.href"
            class="block px-10 py-2 text-gray-700 hover:bg-gray-50 hover:text-blue-600 rounded-lg transition-colors duration-200"
            @click="closeMobileMenu"
          >
            {{ item.name }}
          </a>
          <!-- Botón portal en móvil -->
          <button class="w-full mt-4 bg-gradient-to-r from-blue-600 to-blue-700 text-white px-4 py-2 rounded-lg">
            Portal Clientes
          </button>
        </div>
      </div>
    </Transition>
  </nav>
</template>

<script setup lang="ts">
    import { ref } from 'vue'

    // ESTADO REACTIVO
    // ref() crea una variable reactiva - cuando cambia, la UI se actualiza
    const mobileMenuOpen = ref(false)

    // DATOS DEL MENÚ
    const menuItems = [
      { name: 'Inicio', href: '#inicio' },
      { name: 'Servicios', href: '#servicios' },
      { name: 'Nosotros', href: '#nosotros' },
      { name: 'Testimonios', href: '#testimonios' },
      { name: 'Contacto', href: '#contacto' }
    ]

    // FUNCIONES/MÉTODOS
    const toggleMobileMenu = () => {
      mobileMenuOpen.value = !mobileMenuOpen.value
    }

    const closeMobileMenu = () => {
      mobileMenuOpen.value = false
    }

    // Smooth scroll cuando se hace click en un enlace
    const handleNavClick = (e: Event) => {
        e.preventDefault()
        const target = (e.target as HTMLAnchorElement).getAttribute('href')
        if (target && target.startsWith('#')) {
            const element = document.querySelector(target)
            if (element) {
            element.scrollIntoView({ behavior: 'smooth' })
            }
        }
    closeMobileMenu()
    }
</script>

<style scoped>
</style>