<script setup lang="ts">
import { ref } from "vue";
import { useGeolocation } from '@vueuse/core';

const { coords } = useGeolocation();
const title = ref("");
const description = ref("");
const imageUrl = ref<string | null>(null);
const expiry = ref("");
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

// Format coordinates to be more readable
const formatCoordinates = (coord: number): string => {
  return coord.toFixed(6);
};

// Check if coordinates are valid
const hasValidCoordinates = (): boolean => {
  return coords.latitude !== Infinity && 
         coords.longitude !== Infinity && 
         coords.latitude !== null &&
         coords.longitude !== null;
};
</script>

<template>
  <div class="create-post">
    <form @submit.prevent>
      <div class="form-group">
        <label for="title" class="form-label">Food Title</label>
        <input
          type="text"
          id="title"
          v-model="title"
          class="form-input"
          placeholder="e.g. Fresh Vegetables, Homemade Pasta"
          required
        />
      </div>

      <div class="form-group">
        <label for="description" class="form-label">Description</label>
        <textarea
          id="description"
          v-model="description"
          class="form-input textarea"
          placeholder="What do you have?"
          rows="3"
          required
        ></textarea>
        <small class="helper-text">Ensure you list all allergens, quantity, and any defects.</small>
      </div>

      <div class="form-group">
        <label class="form-label">
          <span>Food Photo</span>
          <span class="label-tip">Clear photos help people identify your food</span>
        </label>
        
        <div v-if="!imageUrl" class="upload-container">
          <input
            type="file"
            accept="image/*"
            id="post-file"
            @change="loadFile"
            class="file-input"
          />
          <label for="post-file" class="file-label" :class="{ 'uploading': isUploading }">
            <span v-if="!isUploading" class="upload-icon">🍲</span>
            <span v-else class="upload-spinner"></span>
            <span v-if="!isUploading">Upload Photo</span>
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
        <label class="form-label">Location</label>
        <div class="location-container">
          <div v-if="hasValidCoordinates()" class="location-data">
            <div class="location-coordinates">
              <div class="coordinate">
                <span class="coordinate-label">Latitude:</span>
                <span class="coordinate-value">{{ formatCoordinates(coords.latitude) }}</span>
              </div>
              <div class="coordinate">
                <span class="coordinate-label">Longitude:</span>
                <span class="coordinate-value">{{ formatCoordinates(coords.longitude) }}</span>
              </div>
            </div>
            <div class="location-status success">
              <span class="status-icon">✓</span>
              <span>Location detected</span>
            </div>
          </div>
          <div v-else class="location-status loading">
            <span class="location-spinner"></span>
            <span>Detecting your location...</span>
          </div>
        </div>
      </div>

      <div class="form-group">
        <label for="expiry" class="form-label">Expiry</label>
        <input
          type="datetime-local"
          id="expiry"
          v-model="expiry"
          class="form-input"
          required
        />
      </div>
      
      <button class="post-button">POST</button>
    </form>
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
  color: #558b2f;
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
  color: #33691e;
}

.coordinate-value {
  font-family: monospace;
  background-color: #e8f5e9;
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
</style>