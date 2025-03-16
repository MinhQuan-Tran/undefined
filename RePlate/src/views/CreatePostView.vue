<script setup lang="ts">
  import { mapStores } from "pinia";
  import { useUserStore } from "@/stores/user";

import { ref } from "vue";
import { useGeolocation } from '@vueuse/core'

const { coords } = useGeolocation()
const imageUrl = ref<string | null>(null);
const imageFile = ref<File | null>(null); //

// Add reactive state for all form fields
const description = ref("");
const location = ref("");
const expireAt = ref("");

const userStore = useUserStore();

const loadFile = (event: Event) => {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files[0]) {
    imageUrl.value = URL.createObjectURL(input.files[0]);
  }
};


async function handlePost() {
  console.log("handlePost function called");
  try {
  const formData = new FormData();

    formData.append("description", description.value);
    if (coords.value.latitude !== Infinity && coords.value.longitude !== Infinity) {
      const locationData = {
        latitude: coords.value.latitude,
        longitude: coords.value.longitude
      };

      formData.append("location", JSON.stringify({
        locationData
      }));
    }
  
  formData.append("expire_at", expireAt.value);

  if (imageFile.value) {
      formData.append("image", imageFile.value);
    }

    const auth_token = userStore.token;

    // 44.211.65.112:8000
    const response = await fetch("http://127.0.0.1:8000/posts/create/", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${auth_token}`,
        "Content-Type": "application/json"
      },
      body: formData
      // body: JSON.stringify({
      //   "description": description,
      //   "expire_at": expireAt,
      //   "location": location,
      //   "images": imageFile
      // })
    });
    
    const data = await response.json();
    
    if (response.ok) {
      console.log("Post created successfully:", data);
      // Reset form
      description.value = "";
      expireAt.value = "";
      imageUrl.value = null;
      imageFile.value = null;
      // You could add a success message or redirect here
    } else {
      console.error("Error creating post:", data);
      // Handle error (show message to user)
    }
  } catch (error) {
    console.error("Error submitting form:", error);
    // Handle network errors
  }

  }
</script>

<template>
  <div class="container">
    <div class="create_post">
      <h2 class="title">Create a Listing:</h2>
      <form @submit.prevent="handlePost"> //creation of form to submit

        <label for="description">Description:</label> 
      <input
        type="text"
        class="input"
        placeholder="What do you have?"
        name="description"
        v-model = "description"
        required
      />
      <small style="color: black;">Ensure you list all allergens, quantity, and any defects.</small>

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

      <div class="display-location">
        <label for="location">Location:</label>
      <p v-if="coords.latitude!== Infinity && coords.longitude!== Infinity">
      Latitude: {{coords.latitude}}
      <br>
      Longitude: {{coords.longitude}}
      </p>
      <p v-else>
      Locating...
      </p>
      </div>

      <label for="expiry">Expiry:</label>
      <input
        type="datetime-local"
        class="input"
        placeholder="What is the item's expiry?"
        v-model="expireAt"
      />

      <button class="post_button" @click="handlePost">POST </button>
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
  font-family: 'Arial', sans-serif;
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
