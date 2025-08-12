<template>
  <footer class="footer">
    <div class="footer-inner">
      <div class="footer-copy">
        &copy; {{ new Date().getFullYear() }} Ara y Bustamante Consultores. Todos los derechos reservados.
        <br>
        <br>
        <span> <strong>Ubicación: </strong></span>Isidora Goyenechea 3250, oficina 1102. El golf. 
      </div>
    </div>
  </footer>
</template>

<style scoped>

.footer {
  background: #021657;
  color: #fff;
  padding: 50px 0 24px 0;
  width: 100%;
}

.footer-copy {
  font-size: 1.02rem;
  color: #ffffff;
  text-align: center;
  margin-top: -24px;
}

@media (max-width: 600px) {
  .footer-inner {
    gap: 16px;
    padding: 0 8px;
}
    .footer-links {
      gap: 16px;
      flex-wrap: wrap;
      justify-content: center;
    }
}

</style>