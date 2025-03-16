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

<style scoped>
  .create-post {
    width: 100%;
  }

  .form-group {
    margin-bottom: 20px;
  }

  .form-label {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 8px;
    font-weight: 600;
    color: #33691e;
  }

  .label-tip {
    font-size: 0.8rem;
    font-weight: normal;
    color: #689f38;
    font-style: italic;
  }

  .form-input {
    width: 100%;
    padding: 12px;
    border: 1px solid #c5e1a5;
    border-radius: 8px;
    font-size: 16px;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
    background-color: #ffffff;
  }

  .form-input:focus {
    outline: none;
    border-color: #4caf50;
    box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.2);
  }

  .helper-text {
    display: block;
    margin-top: 4px;
    font-size: 0.85rem;
    color: #33691e;
  }

  .textarea {
    resize: vertical;
    min-height: 80px;
  }

  .file-input {
    width: 0.1px;
    height: 0.1px;
    opacity: 0;
    overflow: hidden;
    position: absolute;
    z-index: -1;
  }

  .upload-container {
    width: 100%;
  }

  .file-label {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    background-color: #e8f5e9;
    color: #33691e;
    border: 2px dashed #a5d6a7;
    border-radius: 8px;
    padding: 24px;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 100%;
  }

  .file-label:hover {
    background-color: #d7e9ca;
    border-color: #4caf50;
  }

  .upload-icon {
    font-size: 24px;
  }

  .upload-spinner {
    width: 24px;
    height: 24px;
    border: 3px solid rgba(76, 175, 80, 0.2);
    border-top: 3px solid #4caf50;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
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

  .remove-image {
    position: absolute;
    top: 8px;
    right: 8px;
    width: 28px;
    height: 28px;
    background-color: rgba(255, 255, 255, 0.9);
    border: none;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    cursor: pointer;
    color: #e53935;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    transition: all 0.2s ease;
  }

  .remove-image:hover {
    background-color: #ffffff;
    transform: scale(1.1);
  }

  /* Location styles */
  .location-container {
    background-color: #f1f8e9;
    border: 1px solid #c5e1a5;
    border-radius: 8px;
    padding: 12px;
  }

  .location-data {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .location-coordinates {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
  }

  .coordinate {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .coordinate-label {
    font-weight: 600;
    color: #2e7d32;
  }

  .coordinate-value {
    font-family: monospace;
    background-color: #e8f5e9;
    color: #1b5e20;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.9rem;
  }

  .location-status {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 6px;
    font-size: 0.9rem;
  }

  .status-icon {
    color: #4caf50;
    font-weight: bold;
  }

  .location-spinner {
    width: 16px;
    height: 16px;
    border: 2px solid rgba(76, 175, 80, 0.2);
    border-top: 2px solid #4caf50;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  .success {
    color: #4caf50;
  }

  .loading {
    color: #757575;
  }

  .post-button {
    width: 100%;
    padding: 14px;
    background: #4caf50;
    color: #fff;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    margin-top: 10px;
  }

  .post-button:hover {
    background: #388e3c;
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  }

  .post-button:active {
    transform: translateY(0);
  }

  /* New Location Verification Styles */
  .display-location {
    width: 100%;
  }

  .location-verification-container {
    background-color: #e8f5e9;
    border: 1px solid #c5e1a5;
    border-radius: 8px;
    padding: 12px;
  }

  .coordinates-display {
    margin: 0;
    line-height: 1.6;
  }

  .verification-value {
    font-family: monospace;
    font-weight: 500;
    color: #1b5e20;
    background-color: #f1f8e9;
    padding: 2px 6px;
    border-radius: 4px;
  }

  .locating-message {
    margin: 0;
    color: #33691e;
    font-style: italic;
  }
</style>
