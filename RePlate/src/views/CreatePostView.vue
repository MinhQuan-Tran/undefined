<script setup lang="ts">
  import { mapStores } from "pinia";
  import { useUserStore } from "@/stores/user";

  import { ref } from "vue";
  import { useGeolocation } from "@vueuse/core";

  const { coords } = useGeolocation();
  const imageUrl = ref<string | null>(null);
  const imageFile = ref<File | null>(null); //

  // Add reactive state for all form fields
  const description = ref("");
  const location = ref("");
  const expireAt = ref("");
  const quantity = ref(0);
  const imageFiles = ref<File[]>([]);
  const imagePreviews = ref<string[]>([]);

  const userStore = useUserStore();

  function loadFiles(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files) {
      imageFiles.value = Array.from(input.files); // Convert FileList to array
      imagePreviews.value = imageFiles.value.map((file) => URL.createObjectURL(file)); // Generate image previews
    }
  }

  async function handlePost() {
    try {
      const formData = new FormData();

      // Add text fields (JSON data)
      formData.append("description", description.value);
      formData.append("expire_at", expireAt.value);
      formData.append("quantity", quantity.value.toString());

      if (coords.value.latitude !== Infinity && coords.value.longitude !== Infinity) {
        formData.append(
          "location",
          JSON.stringify({
            latitude: coords.value.latitude,
            longitude: coords.value.longitude
          })
        );
      }

      // Add multiple image files
      imageFiles.value.forEach((file) => {
        formData.append("images", file); // Append each file
      });

      const auth_token = userStore.token;

      const response = await fetch("http://127.0.0.1:8000/posts/create/", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${auth_token}`
        },
        body: formData // `multipart/form-data` automatically set
      });

      const data = await response.json();

      if (response.ok) {
        console.log("Post created successfully:", data);
        description.value = "";
        expireAt.value = "";
        imageFiles.value = [];
        imagePreviews.value = [];
      } else {
        console.error("Error creating post:", data);
      }
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  }
</script>

<template>
  <div class="container">
    <div class="create_post">
      <h2 class="title">Create a Listing:</h2>
      <form @submit.prevent="handlePost">
        //creation of form to submit

        <label for="description">Description:</label>
        <input
          type="text"
          class="input"
          placeholder="What do you have?"
          name="description"
          v-model="description"
          required
        />
        <small style="color: black">Ensure you list all allergens, quantity, and any defects.</small>

        <input
          type="file"
          accept="image/*"
          name="images"
          id="file"
          multiple
          @change="loadFiles"
          style="display: none"
        />
        <label for="file" class="file_label">Upload Photo</label>
        <div v-if="imagePreviews.length">
          <p v-for="(image, index) in imagePreviews" :key="index">
            <img :src="image" class="uploaded_image" />
          </p>
        </div>

        <div class="display-location">
          <label for="location">Location:</label>
          <p v-if="coords.latitude !== Infinity && coords.longitude !== Infinity">
            Latitude: {{ coords.latitude }}
            <br />
            Longitude: {{ coords.longitude }}
          </p>
          <p v-else>Locating...</p>
        </div>

        <label for="expiry">Expiry:</label>
        <input type="datetime-local" class="input" placeholder="What is the item's expiry?" v-model="expireAt" />

        <button class="post_button" @click="handlePost">POST</button>
      </form>
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
    background-color: #f9fafb;
    font-family: "Arial", sans-serif;
  }

  .title {
    color: #2e8b57;
    font-size: 2rem;
    margin-bottom: 20px;
  }

  .create_post {
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
