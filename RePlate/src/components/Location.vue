<script setup lang="ts">
import { useGeolocation } from '@vueuse/core'

const { coords, locatedAt, error} = useGeolocation()
</script>

<template>
  <div class="display-location">
    <h1>Your location: </h1>
    <h2 v-if="coords.latitude && coords.longitude">
      Latitude: {{coords.latitude}}
      <br>
      Longitude: {{coords.longitude}}
    </h2>

    <h2 v-else>
      Locating...
    </h2>
  </div>
</template>

<style scoped>
.display-location {
  margin: 20px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
}
</style>