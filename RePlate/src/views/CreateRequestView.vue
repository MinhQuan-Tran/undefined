<script setup lang="ts">
import { ref } from "vue";

const imageUrl = ref<string | null>(null);
const description = ref("");
const location = ref("");
const neededBy = ref("");
const isUploading = ref(false);

const loadFile = (event: Event) => {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files[0]) {
    isUploading.value = true;
    
    // Simulate upload delay
    setTimeout(() => {
      imageUrl.value = URL.createObjectURL(input.files![0]);
      isUploading.value = false;
    }, 800);
  }
};

const removeImage = () => {
  imageUrl.value = null;
};

// Sample locations for dropdown
const locations = [
  "Melbourne CBD",
  "Richmond",
  "St Kilda",
  "Brunswick",
  "Fitzroy",
  "South Yarra",
  "Footscray",
  "Carlton",
  "Echuca",
  "Bendigo"
];
</script>

<template>
  <div class="create-request">
    <form @submit.prevent>
      <div class="form-group">
        <label for="description" class="form-label">What are you looking for?</label>
        <textarea
          id="description"
          v-model="description"
          class="form-input textarea"
          placeholder="Describe the food you're requesting..."
          rows="3"
          required
        ></textarea>
      </div>

      <div class="form-group">
        <label class="form-label">
          <span>Upload a photo (optional)</span>
          <span class="label-tip">Helps others understand what you need</span>
        </label>
        
        <div v-if="!imageUrl" class="upload-container">
          <input
            type="file"
            accept="image/*"
            id="file"
            @change="loadFile"
            class="file-input"
          />
          <label for="file" class="file-label" :class="{ 'uploading': isUploading }">
            <span v-if="!isUploading" class="upload-icon">📷</span>
            <span v-else class="upload-spinner"></span>
            <span v-if="!isUploading">Select Image</span>
            <span v-else>Uploading...</span>
          </label>
        </div>
        
        <div v-else class="image-preview-container">
          <img :src="imageUrl" class="image-preview" />
          <button type="button" @click="removeImage" class="remove-image">
            <span>×</span>
          </button>
        </div>
      </div>

      <div class="form-group">
        <label for="location" class="form-label">Your location</label>
        <select
          id="location"
          v-model="location"
          class="form-input select"
          required
        >
          <option value="" disabled selected>Select your location</option>
          <option v-for="loc in locations" :key="loc" :value="loc">{{ loc }}</option>
        </select>
      </div>

      <div class="form-group">
        <label for="neededBy" class="form-label">When do you need it by?</label>
        <input
          type="datetime-local"
          id="neededBy"
          v-model="neededBy"
          class="form-input"
          required
        />
      </div>
    </form>
  </div>
</template>

<style scoped>
.create-request {
  width: 100%;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #33691e;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
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

.textarea {
  resize: vertical;
  min-height: 80px;
}

.select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2333691e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 16px;
  padding-right: 40px;
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
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.uploading {
  pointer-events: none;
  opacity: 0.7;
}

.image-preview-container {
  position: relative;
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  margin-top: 8px;
}

.image-preview {
  width: 100%;
  max-height: 200px;
  object-fit: cover;
  border-radius: 8px;
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
</style>