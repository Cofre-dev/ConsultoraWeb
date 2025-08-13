<template>
  <nav class="navbar">
    <div class="navbar-container">
      <div class="navbar-flex">
        <!-- LADO IZQUIERDO: Logo y nombre de la empresa -->
        <div class="navbar-logo-area">
          <div class="navbar-logo">
            <RouterLink to="/">
              <img src="../assets/ayb.jpg" alt="Ara y bustamante consultores">
            </RouterLink>
          </div>
          <div class="navbar-title">
            <h1 class="company-name">
              Ara y bustamante consultores
            </h1>
            <p class="company-desc">Expertos en tributación</p>
          </div>
        </div>

        
        <!-- CENTRO/DERECHA: Menú de navegación (desktop) -->
        <div class="navbar-menu">
          <!-- CAMBIO: Se reemplazó <a> por <RouterLink> y :href por :to -->
          <RouterLink 
            v-for="item in menuItems" 
            :key="item.name"
            :to="item.path"
            class="navbar-link"
          >
            {{ item.name }}
          </RouterLink>
          <button class="navbar-cta">
            Portal Clientes
          </button>
        </div>

        <!-- BOTÓN HAMBURGUESA: Solo visible en móvil -->
        <div class="navbar-hamburger">
          <button 
            @click="toggleMobileMenu"
            class="hamburger-btn"
            aria-label="Abrir menú"
          >
            <svg 
              class="hamburger-icon"
              :class="{ 'rotate': mobileMenuOpen }"
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

   <!-- MENÚ MÓVIL -->
    <Transition name="fade">
      <div v-if="mobileMenuOpen" class="mobile-menu">
        <div class="mobile-menu-content">
          <!-- CAMBIO: También se usa RouterLink aquí -->
          <RouterLink 
            v-for="item in menuItems"
            :key="item.name"
            :to="item.path"
            class="mobile-menu-link"
            @click="closeMobileMenu"
          >
            {{ item.name }}
          </RouterLink>
          <button class="mobile-menu-cta">
            Portal Clientes
          </button>
        </div>
      </div>
    </Transition>
  </nav>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import {ref} from 'vue';

const mobileMenuOpen = ref(false)

const menuItems = [
  { name: 'Inicio', path: '/' },
  { name: 'Servicios', path: '/servicios' },
  { name: 'Nosotros', path: '/nosotros' },
  { name: 'Testimonios', path: '/testimonios' },
  { name: 'Contacto', path: '/contacto' }
]

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const closeMobileMenu = () => {
  mobileMenuOpen.value = false
}

</script>

<style scoped>
/* Tu CSS no necesita cambios, solo se ajusta el comportamiento del HTML y JS */

.navbar {
  background: #fefefe;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: sticky;
  top: 0; /* Corregido para que se quede pegado arriba */
  z-index: 50;
  width: 100%;
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

.navbar-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 80px;
}

.navbar-logo-area {
  display: flex;
  align-items: center;
  gap: 16px;
}

.navbar-logo img {
  height: 75px; 
  width: auto; 
  display: block;
}

.navbar-title .company-name {
  font-size: 1.5rem; /* Ajustado para mejor legibilidad */
  font-weight: bold;
  color: #000000;
  margin: 0;
}
.navbar-title .company-desc {
  font-size: 0.875rem; /* Ajustado */
  color: #6b7280;
  margin: 0;
}
.navbar-menu {
  display: none; /* Oculto por defecto, se muestra en desktop */
}
.navbar-link {
  color: #333;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
  padding: 4px 0;
  position: relative;
}
.navbar-link:hover {
  color: #13ab1f;
}
/* Efecto de subrayado al pasar el mouse */
.navbar-link::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    bottom: -4px;
    left: 0;
    background-color: #13ab1f;
    transition: width 0.3s;
}
.navbar-link:hover::after {
    width: 100%;
}

.navbar-cta {
  background: linear-gradient(90deg, #2563eb, #1e40af);
  color: #fff;
  padding: 10px 24px;
  border-radius: 8px;
  border: none;
  font-weight: 500;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  transition: all 0.2s;
}
.navbar-cta:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.12);
  transform: translateY(-2px);
}
.navbar-hamburger {
  display: flex;
  align-items: center;
}
.hamburger-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}
.hamburger-icon {
  width: 32px;
  height: 32px;
  transition: transform 0.2s;
}
.hamburger-icon.rotate {
  transform: rotate(90deg);
}

/* Responsive */
@media (min-width: 900px) {
  .navbar-menu {
    display: flex;
    align-items: center;
    gap: 32px;
  }
  .navbar-hamburger {
    display: none;
  }
}

/* Mobile menu */
.mobile-menu {
  display: block;
  background: #fff;
  border-top: 1px solid #eee;
  width: 100%;
  position: absolute;
  left: 0;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.mobile-menu-content {
  padding: 16px 24px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.mobile-menu-link {
  color: #444;
  text-decoration: none;
  font-size: 1rem;
  padding: 12px;
  border-radius: 6px;
  transition: all 0.2s;
}
.mobile-menu-link:hover {
  background: #f5f5f5;
  color: #2563eb;
}
.mobile-menu-cta {
  width: 100%;
  margin-top: 16px;
  background: linear-gradient(90deg, #2563eb, #1e40af);
  color: #fff;
  padding: 12px 0;
  border-radius: 8px;
  border: none;
  font-weight: 500;
  cursor: pointer;
}

/* Transition classes */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s, transform 0.2s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>