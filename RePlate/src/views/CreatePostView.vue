<script setup lang="ts">
import { ref } from "vue";

const imageUrl = ref<string | null>(null);

const loadFile = (event: Event) => {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files[0]) {
    imageUrl.value = URL.createObjectURL(input.files[0]);
  }
};
</script>

<template>
  <div class="container" style="background-color: lightgoldenrodyellow">
    <div class="create_post">
      <h2 class="title" style="color: black; font-weight: 800">Make a Post:</h2>
      
      <label for="description" style="font-weight: 500; color: black">Description:</label>
      <input type="text" placeholder="Describe your food product" name="description" required />
      
      <p></p>
      <input type="file" accept="image/*" name="image" id="file" @change="loadFile" style="display: none;" />
      <p><label for="file" style="cursor: pointer; font-weight: 500; color: black">Upload Image</label></p>
      <p v-if="imageUrl"><img :src="imageUrl" width="200" /></p>

      <p></p>
      <label for="location" style="font-weight: 500; color: black">Location:</label>
    </div>
  </div>
</template>


