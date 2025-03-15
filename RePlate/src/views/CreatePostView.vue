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
  <div class="container">
    <div class="create_post">
      <h2 class="title">Create a Listing:</h2>
      
      <label for="description" style="font-weight: 500; color: black">Description:</label>
      <p></p>
      <input type="text" style="height: 100px; width:400px; border: 10px; color: black;" placeholder="What do you have?" name="description" required />
      <p style="font-size: x-small; color:black;">Ensure you list all allergens, quantity and any defects.</p>
      <p></p>
      <input type="file" accept="image/*" name="image" id="file" @change="loadFile" style="display: none;" />
      <p><label for="file" style="cursor: pointer; font-weight: 500; color: black; align-self: center;">Photo</label></p>
      <p v-if="imageUrl"><img :src="imageUrl" width="200" /></p>

      <p></p>
      <label for="location" style="font-weight: 500; color: black">Location:</label>
      <!-- For later -->

      <p></p>
      <label for="expiry" style="font-weight: 500; color: black">Expiry:</label>
      <input type="datetime-local" placeholder="What is the item's expiry?" style="height: 50px; width:auto; border: 10px;"/>

      <p></p>
      <button style="height: 40px; width:auto; background-color: grey; align-self: center;">POST</button>
      <!-- placeholder -->

    </div>
  </div>
</template>


<style>
@media (min-width: 1024px) {
  .container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
  .title {
    color: forestgreen;
    font-size: 2rem;
    margin-bottom: 20px;
    justify-content: center;
  }
}
</style>

