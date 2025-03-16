<script lang="ts">
  import { ref } from "vue";
  import CreatePostView from "./CreatePostView.vue";
  import CreateRequestView from "./CreateRequestView.vue";

  export default {
    components: {
      CreatePostView,
      CreateRequestView
    },
    data() {
      return {
        showPostModal: false,
        showRequestModal: false,
        locationCache: {} as Record<string, string>, // Caching locations
        posts: [] as {
          id: number;
          description: string;
          imageUrls: string[];
          location: string;
          expireAt: string;
        }[],
        loading: true // Added loading state
      };
    },
    methods: {
      closePostModal() {
        this.showPostModal = false;
        document.body.classList.remove("modal-open");
      },
      closeRequestModal() {
        this.showRequestModal = false;
        document.body.classList.remove("modal-open");
      },
      openPostModal() {
        this.showPostModal = true;
        document.body.classList.add("modal-open");
      },
      openRequestModal() {
        this.showRequestModal = true;
        document.body.classList.add("modal-open");
      },
      handleEscape(event) {
        if (event.key === "Escape") {
          if (this.showPostModal) this.closePostModal();
          if (this.showRequestModal) this.closeRequestModal();
        }
      },
      handleOutsideClick(event) {
        if (event.target.classList.contains("modal-overlay")) {
          if (this.showPostModal) this.closePostModal();
          if (this.showRequestModal) this.closeRequestModal();
        }
      },
      async getLocationName(latitude: number, longitude: number) {
        try {
          const cacheKey = `${latitude},${longitude}`;
          if (this.locationCache[cacheKey]) {
            return this.locationCache[cacheKey];
          }

          const response = await fetch(
            `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`
          );

          if (!response.ok) throw new Error("Failed to fetch location");

          const data = await response.json();
          const address = data.display_name;

          if (!address) throw new Error("Invalid location data");

          return address;
        } catch (error) {
          console.error("Error fetching location:", error);
          return "Unknown Location";
        }
      },

      async parseLocation(location: string) {
        try {
          if (typeof location === "string" && !location.includes("{")) {
            return location; // Already formatted
          }

          const loc = JSON.parse(location);
          if (!loc.latitude || !loc.longitude) throw new Error("Invalid coordinates");

          return await this.getLocationName(loc.latitude, loc.longitude);
        } catch (error) {
          console.error("Error parsing location:", error);
          return location; // Fallback to original string
        }
      }
    },
    async mounted() {
      try {
        const response = await fetch("http://127.0.0.1:8000/posts/");
        if (!response.ok) throw new Error("Failed to fetch posts");

        const data = await response.json();

        // Use Promise.all to resolve all async operations
        this.posts = await Promise.all(
          data.map(
            async (post: {
              id: number;
              author: string;
              description: string;
              location: string;
              quantity: number;
              expire_at: string;
              created_at: string;
              image_urls: string[];
            }) => ({
              id: post.id,
              author: post.author,
              description: post.description,
              location: await this.parseLocation(post.location),
              quantity: post.quantity,
              expireAt: post.expire_at,
              createdAt: post.created_at,
              imageUrls: post.image_urls.map((url) => `http://127.0.0.1:8000${url}`)
            })
          )
        );
      } catch (error) {
        console.error("Error fetching posts:", error);
      } finally {
        this.loading = false; // Set loading to false after fetching
      }
    },
    mounted() {
      document.addEventListener("keydown", this.handleEscape);
    },
    unmounted() {
      document.removeEventListener("keydown", this.handleEscape);
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
      <h2 class="feed_title">Social Feed</h2>
      <!-- Show loading screen while fetching -->
      <div v-if="loading" class="loading-container">
        <div class="loading-spinner"></div>
        <p>Loading posts...</p>
      </div>
      <div class="feed-posts">
        <div v-for="post in posts" :key="post.id" class="post_card">
          <div class="image-container">
            <img :src="post.image" :alt="`Image of ${post.title}`" class="post_image" />
          </div>
          <h3 style="font-size: large; font-weight: bold">{{ post.title }}</h3>
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
            <button class="collect-btn">Collect</button>
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

<style scoped>
  /* Layout Styles */
  .layout {
    display: flex;
    min-height: 100vh;
    background-color: #f9fafb;
  }
/* Layout Styles */
.layout {
  display: flex;
  min-height: 100vh;
  background-color: #f8f9f4;
  font-family: 'Roboto', sans-serif;
}

  /* Sidebar Styles */
  .sidebar {
    width: 20%;
    background: #ffffff;
    padding: 20px;
    border-right: 1px solid #ccc;
    display: flex;
    flex-direction: column;
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

  .sidebar_button {
    background: #2e8b57;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
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

  .sidebar_button:hover {
    background: #1e6843;
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
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: auto;
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

  .modal-content {
    background-color: rgb(245, 245, 229);
    padding: 20px;
    border-radius: 20px;
    width: 90%;
    max-width: 500px;
    display: flex;
    flex-direction: column;
    overflow: auto;
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

  .close-button {
    background-color: burlywood;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    margin-top: 10px;
  }

  /* Feed Section Styles */
  .feed {
    width: 80%;
    padding: 20px;
    overflow-y: auto;
    color: black;
    font-size: medium;
  }

  .feed_title {
    color: #2e8b57;
    font-size: 1.5rem;
    margin-bottom: 20px;
  }

  .post_card {
    background: beige;
    padding: 15px;
    margin: 15px 0;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
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

  }
  .image-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }

  /* Loading Screen */
  .loading-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 50px;
    font-size: 1.2rem;
    color: #2e8b57;
  }

  /* Spinner Animation */
  .loading-spinner {
    width: 50px;
    height: 50px;
    border: 5px solid #d3d3d3;
    border-top: 5px solid #2e8b57;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 10px;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>

