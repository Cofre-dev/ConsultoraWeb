<template>
  <nav class="navbar">
    <div class="navbar-container">
      <div class="navbar-flex">
        <!-- LADO IZQUIERDO: Logo y nombre de la empresa -->
        <div class="navbar-logo-area">
          <div class="navbar-logo">
            <span class="logo-text">
              <img src="../assets/ayb.jpg" alt="">
            </span>
          </div>
          <div class="navbar-title">
            <h1 class="company-name">
              Ara y bustamante consultores
            </h1>
            <p class="company-desc">Expertos en tributación</p>
          </div>
        </div>

        <!-- CENTRO/DERECHA: Menú de navegación (desktop) -->
        <div class="navbar-menu" v-if="!mobileMenuOpen">
          <a 
            v-for="item in menuItems" 
            :key="item.name"
            :href="item.href"
            class="navbar-link"
            @click="handleNavClick"
          >
            {{ item.name }}
          </a>
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
    <Transition
      enter-active-class="fade-enter-active"
      enter-from-class="fade-enter-from"
      enter-to-class="fade-enter-to"
      leave-active-class="fade-leave-active"
      leave-from-class="fade-leave-from"
      leave-to-class="fade-leave-to"
    >
      <div 
        v-if="mobileMenuOpen" 
        class="mobile-menu"
      >
        <div class="mobile-menu-content">
          <a 
            v-for="item in menuItems"
            :key="item.name"
            :href="item.href"
            class="mobile-menu-link"
            @click="closeMobileMenu"
          >
            {{ item.name }}
          </a>
          <button class="mobile-menu-cta">
            Portal Clientes
          </button>
        </div>
      </div>
    </Transition>
  </nav>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const mobileMenuOpen = ref(false)

const menuItems = [
  { name: 'Inicio', href: '#inicio' },
  { name: 'Servicios', href: '#servicios' },
  { name: 'Nosotros', href: '#nosotros' },
  { name: 'Testimonios', href: '#testimonios' },
  { name: 'Contacto', href: '#contacto' }
]

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const closeMobileMenu = () => {
  mobileMenuOpen.value = false
}

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

.navbar {
  background: #fefefe;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: sticky;
  top: -100%;
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

.navbar-logo {
  display: flex; 
  align-items: center;
  height: 100%; 
}

/* Estilos para la imagen del logo */
.navbar-logo img {
  height: 75px; 
  width: auto; 
  display: block;
}

.logo-text {
  color: #f6f5f5;
  font-weight: bold;
  font-size: 1.25rem;
}
.navbar-title .company-name {
  font-size: 2rem;
  font-weight: bold;
  color: #000000;
  margin: 0;
  margin-right: 15px;
}
.navbar-title .company-desc {
  font-size: 1.2rem;
  color: #000000;
  margin: 0;
}
.navbar-menu {
  display: flex;
  align-items: center;
  gap: 32px;
}
.navbar-link {
  color: #000000;
  text-decoration: none;
  font-weight: 520;
  transition: color 0.2s;
  padding: 4px 0;
}
.navbar-link:hover {
  color: #13ab1f;
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
  transition: background 0.2s, box-shadow 0.2s, transform 0.2s;
}
.navbar-cta:hover {
  background: linear-gradient(90deg, #1e40af, #2563eb);
  box-shadow: 0 4px 12px rgba(0,0,0,0.12);
  transform: translateY(-2px);
}
.navbar-hamburger {
  display: none;
}
.hamburger-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}
.hamburger-icon {
  margin-top: 10px;
  width: 32px;
  height: 32px;
  transition: transform 0.2s;
}
.hamburger-icon.rotate {
  transform: rotate(90deg);
}

/* Responsive */
@media (max-width: 900px) {
  .navbar-container {
    padding: 0 12px;
  }
  .navbar-flex {
    height: 64px;
  }
  .navbar-logo {
    width: 40px;
    height: 32px;
  }
  .navbar-title .company-name {
    font-size: 1rem;
  }
}

@media (max-width: 768px) {
  .navbar-menu {
    display: none;
  }
  .navbar-hamburger {
    display: flex;
    align-items: center;
  }
}

/* Mobile menu */
.mobile-menu {
  display: block;
  background: #fbf3f3;
  border-top: 1px solid #eee;
  width: 100%;
}
.mobile-menu-content {
  padding: 32px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.mobile-menu-link {
  color: #444;
  text-decoration: none;
  font-size: 1rem;
  padding: 12px 0;
  border-radius: 6px;
  transition: background 0.2s, color 0.2s;
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
.fade-enter-to, .fade-leave-from {
  opacity: 1;
  transform: translateY(0);
}
</style>