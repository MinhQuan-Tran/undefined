<script lang="ts">
import { ref } from "vue";
import CreatePostView from "./CreatePostView.vue";
import CreateRequestView from "./CreateRequestView.vue";

export default {
  components: {
    CreatePostView,
    CreateRequestView,
  },
  data() {
    return {
      showPostModal: false,
      showRequestModal: false,
    };
  },
  methods: {
    closePostModal() {
      this.showPostModal = false;
      document.body.classList.remove('modal-open');
    },
    closeRequestModal() {
      this.showRequestModal = false;
      document.body.classList.remove('modal-open');
    },
    openPostModal() {
      this.showPostModal = true;
      document.body.classList.add('modal-open');
    },
    openRequestModal() {
      this.showRequestModal = true;
      document.body.classList.add('modal-open');
    },
    handleEscape(event) {
      if (event.key === 'Escape') {
        if (this.showPostModal) this.closePostModal();
        if (this.showRequestModal) this.closeRequestModal();
      }
    },
    handleOutsideClick(event) {
      if (event.target.classList.contains('modal-overlay')) {
        if (this.showPostModal) this.closePostModal();
        if (this.showRequestModal) this.closeRequestModal();
      }
    }
  },
  mounted() {
    document.addEventListener('keydown', this.handleEscape);
  },
  unmounted() {
    document.removeEventListener('keydown', this.handleEscape);
  }
};
</script>

<template>
  <div class="layout">
    <!-- Sidebar Section -->
    <div class="sidebar">
      <div class="sidebar-content">
        <h2 class="sidebar-title">Food Share</h2>
        <button @click="openPostModal" class="sidebar-button">
          <span class="button-icon">🥗</span>
          Share Food
        </button>
        <button @click="openRequestModal" class="sidebar-button">
          <span class="button-icon">🔍</span>
          Request Food
        </button>
      </div>
    </div>

    <!-- Social Feed Section -->
    <div class="feed">
      <h2 class="feed-title">Social Feed</h2>
      <div class="feed-posts">
        <div v-for="post in posts" :key="post.id" class="post-card">
          <h3 class="post-title">{{ post.title }}</h3>
          <div class="image-container">
            <img :src="post.image" :alt="`Image of ${post.title}`" class="post-image" />
          </div>
          <p class="post-text">{{ post.description }}</p>
          <div class="post-meta">
            <div class="meta-item">
              <span class="meta-icon">📍</span>
              <span>{{ post.location }}</span>
            </div>
            <div class="meta-item">
              <span class="meta-icon">⏱️</span>
              <span>{{ post.expiry }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Create Post Modal -->
    <transition name="fade">
      <div v-if="showPostModal" class="modal-overlay" @click="handleOutsideClick">
        <div class="modal-container">
          <div class="modal-header">
            <h2 class="modal-title">Share Food</h2>
            <button @click="closePostModal" class="modal-close" aria-label="Close modal">×</button>
          </div>
          <div class="modal-body">
            <CreatePostView />
          </div>
          <div class="modal-footer">
            <button @click="closePostModal" class="modal-button cancel-button">Cancel</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Create Request Modal -->
    <transition name="fade">
      <div v-if="showRequestModal" class="modal-overlay" @click="handleOutsideClick">
        <div class="modal-container">
          <div class="modal-header">
            <h2 class="modal-title">Request Food</h2>
            <button @click="closeRequestModal" class="modal-close" aria-label="Close modal">×</button>
          </div>
          <div class="modal-body">
            <CreateRequestView />
          </div>
          <div class="modal-footer">
            <button @click="closeRequestModal" class="modal-button cancel-button">Cancel</button>
            <button class="modal-button submit-button">Post Request</button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
const posts = ref([
  { id: 1, title: "Box of Pears", description: "Fresh pears available! At least 15, must be picked up by tomorrow", image: new URL('@/assets/Pears.jpg', import.meta.url).href, location: "Melbourne", expiry: "17/03/2025 11:00 AM"},
  { id: 2, title: "Hokkien Noodles", description: "Yummy Hokkien noodles available until late tonight. Contains sesame", image: new URL("@/assets/hokkeinnoodles.jpg", import.meta.url).href, location: "Melbourne", expiry: "17/03/2025 11:00 PM" },
  { id: 3, title: "Leftover Greek", description: "Leftover Greek food, available until Tuesday", image: new URL("@/assets/LeftoverGreek.jpg", import.meta.url).href, location: "Echuca", expiry: "19/03/2025 05:00 PM" },
]);
</script>

<style scoped>
/* Layout Styles */
.layout {
  display: flex;
  min-height: 100vh;
  background-color: #f8f9f4;
  font-family: 'Roboto', sans-serif;
}

/* Sidebar Styles */
.sidebar {
  width: 25%;
  background: linear-gradient(135deg, #d7e9ca, #e8f5e9);
  padding: 20px;
  border-right: 1px solid #c5e1a5;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sidebar-content {
  position: sticky;
  top: 20px;
  width: 100%;
}

.sidebar-title {
  color: #2e7d32;
  text-align: center;
  margin-bottom: 30px;
  font-weight: 700;
  font-size: 1.8rem;
}

.sidebar-button {
  background: #4caf50;
  color: white;
  padding: 14px 20px;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 18px;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.button-icon {
  margin-right: 10px;
  font-size: 18px;
}

.sidebar-button:hover {
  background: #388e3c;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.sidebar-button:active {
  transform: translateY(0);
}

/* Feed Section Styles */
.feed {
  width: 75%;
  padding: 30px;
  overflow-y: auto;
  color: #33691e;
  background: #ffffff;
}

.feed-title {
  color: #2e7d32;
  font-size: 2rem;
  margin-bottom: 30px;
  font-weight: 700;
  border-bottom: 2px solid #c5e1a5;
  padding-bottom: 10px;
}

.feed-posts {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.post-card {
  background: #f1f8e9;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.post-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
}

.post-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #33691e;
  margin-bottom: 16px;
}

.image-container {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 16px;
  overflow: hidden;
  border-radius: 12px;
}

.post-image {
  width: 100%;
  max-height: 300px;
  object-fit: cover;
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.post-image:hover {
  transform: scale(1.03);
}

.post-text {
  font-size: 1rem;
  line-height: 1.6;
  color: #33691e;
  margin-bottom: 16px;
}

.post-meta {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  font-size: 0.9rem;
  color: #558b2f;
}

.meta-item {
  display: flex;
  align-items: center;
  background: #e8f5e9;
  padding: 6px 12px;
  border-radius: 20px;
}

.meta-icon {
  margin-right: 6px;
}

/* Modal Styles */
body.modal-open {
  overflow: hidden;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-container {
  background-color: #ffffff;
  width: 90%;
  max-width: 550px;
  border-radius: 16px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  max-height: 90vh;
}

.modal-header {
  background: linear-gradient(90deg, #4caf50, #8bc34a);
  color: white;
  padding: 16px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-title {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.modal-close {
  background: none;
  border: none;
  color: white;
  font-size: 28px;
  cursor: pointer;
  padding: 0;
  margin: 0;
  line-height: 1;
  transition: transform 0.2s ease;
}

.modal-close:hover {
  transform: scale(1.2);
}

.modal-body {
  padding: 24px;
  overflow-y: auto;
  max-height: 60vh;
}

.modal-footer {
  padding: 16px 24px;
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  background-color: #f1f8e9;
  border-top: 1px solid #e0e0e0;
}

.modal-button {
  padding: 10px 24px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.cancel-button {
  background-color: transparent;
  color: #4caf50;
  border: 1px solid #4caf50;
}

.cancel-button:hover {
  background-color: #e8f5e9;
}

/* Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>