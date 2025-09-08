<!-- ServiceSection.vue - Ajustar el onMounted -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import ServiceCard from './ServiceCard.vue'
import apiService, { type Service } from '../services/apiService'

const services = ref<Service[]>([])
const loading = ref(true)
const error = ref(false)

onMounted(async () => {
  try {
    const data = await apiService.fetchServices()
    services.value = data  // ← Ahora data ya es Service[], no { results: Service[] }
    console.log('Servicios cargados:', data)
  } catch (err) {
    console.error("Error al obtener los servicios:", err)
    error.value = true
  } finally {
    loading.value = false
  }
})
</script>