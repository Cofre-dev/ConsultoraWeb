<template>
  <!-- Contenedor principal de la sección de Héroe -->
  <div class="hero-section" id="inicio">
    <div class="hero-container">
      
      <div class="hero-text-content">
        <h1 class="hero-title">
          Expertos en Asesoría <span class="highlight-text">Tributaria y Contable</span>
        </h1>
        <!-- <p class="hero-subtitle">
          Expertos en tributación
        </p> -->
        <a href="#servicios" class="hero-button">
          Ver Nuestros Servicios
        </a>
      </div>

      <div class="hero-image-content">
        <!-- Usamos un placeholder. Reemplaza el 'src' con la ruta a tu imagen. -->
        <img src="../assets/carlos.jpg" alt="Consultor experto" class="hero-image">
      </div>

    </div>
  </div>
</template>

<style scoped>
/* Estilos CSS para la sección de Héroe */
.hero-section {
  background-color: #ffffff;
  padding: 4rem 1rem; /* Espaciado generoso */
  width: 100%;
  box-sizing: border-box;
}

.hero-container {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: 2rem; /* Espacio entre texto e imagen */
}

.hero-text-content {
  flex: 1; /* Ocupa el 50% del espacio */
  padding-right: 2rem;
}

.hero-title {
  font-size: 3.75rem; /* 60px */
  font-weight: 800; /* Extra bold */
  color: #111827; /* Casi negro */
  line-height: 1.2;
}

.hero-title .highlight-text {
  color: #2563eb; /* Azul primario */
}

.hero-subtitle {
  margin-top: 1.5rem; /* 24px */
  font-size: 1.25rem; /* 20px */
  color: #4b5563; /* Gris oscuro */
  max-width: 500px;
}

.hero-button {
  display: inline-block;
  margin-top: 2.5rem; /* 40px */
  background-color: #2563eb;
  color: white;
  font-weight: 600;
  padding: 0.875rem 2.5rem; /* 14px 40px */
  border-radius: 0.5rem; /* 8px */
  transition: all 0.3s ease;
  box-shadow: 0 4px 14px 0 rgba(37, 99, 235, 0.4);
}

.hero-button:hover {
  background-color: #1d4ed8;
  transform: translateY(-3px);
  box-shadow: 0 7px 20px 0 rgba(37, 99, 235, 0.4);
}

.hero-image-content {
  flex: 1; /* Ocupa el otro 50% */
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-image {
  width: 100%;
  max-width: 500px;
  height: auto;
  border-radius: 1rem; /* 16px */
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

/* --- Media Queries para Responsive --- */
@media (max-width: 768px) {
  .hero-container {
    flex-direction: column; /* Apila las columnas en vertical */
    text-align: center;
  }

  .hero-text-content {
    padding-right: 0;
    order: 2; /* El texto va después de la imagen en móvil */
  }

  .hero-image-content {
    order: 1; /* La imagen va primero */
    margin-bottom: 2rem;
  }

  .hero-title {
    font-size: 2.5rem; /* 40px */
  }

  .hero-subtitle {
    margin-left: auto;
    margin-right: auto;
  }
}
</style>