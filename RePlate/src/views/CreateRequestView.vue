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
    <div class="create_request">
      <h2 class="title">Post a Request:</h2>

      <label for="description">Description:</label>
      <input
        type="text"
        class="input"
        placeholder="What are you looking for?"
        name="description"
        required
      />

      <input
        type="file"
        accept="image/*"
        name="image"
        id="file"
        @change="loadFile"
        style="display: none;"
      />
      <label for="file" class="file_label">Upload Photo</label>
      <p v-if="imageUrl"><img :src="imageUrl" class="uploaded_image" /></p>

      <label for="location">Location:</label>
      <!-- Placeholder -->

      <label for="expiry">When do you need it by?</label>
      <input
        type="datetime-local"
        class="input"
        placeholder="When do you need it by?"
      />

      <button class="post_button">POST</button>
    </div>
  </div>
</template>

<style>
.container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  height: min-content;
  background-color: rgb(245, 245, 229);
  font-family: 'Arial', sans-serif;
}

.title {
  color: #2e8b57;
  font-size: 2rem;
  margin-bottom: 20px;
}

.create_request {
  background: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
}

label {
  font-weight: bold;
  color: #333;
  margin-top: 10px;
  display: block;
}

.input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 5px;
  margin-bottom: 15px;
  font-size: 16px;
}

.file_label {
  display: inline-block;
  background: #2e8b57;
  color: #fff;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.3s ease-in-out;
}

.file_label:hover {
  background: #1e6843;
}

.uploaded_image {
  margin-top: 15px;
  max-width: 100%;
  border-radius: 5px;
}

.post_button {
  width: 100%;
  padding: 10px;
  background: #2e8b57;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}

.post_button:hover {
  background: #1e6843;
}
</style>
