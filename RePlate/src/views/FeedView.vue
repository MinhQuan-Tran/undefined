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
          const address = data.address;

          if (!address) throw new Error("Invalid location data");

          const locationName = `${address.city || address.town || address.village || "Unknown City"}, ${
            address.state || "Unknown State"
          }, ${address.country || "Unknown Country"}`;

          this.locationCache[cacheKey] = locationName; // Cache result

          return locationName;
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
    }
  };
</script>

<template>
  <div class="layout">
    <!-- Sidebar Section -->
    <div class="sidebar">
      <button @click="showPostModal = true" class="sidebar_button">Share Food</button>
      <button @click="showRequestModal = true" class="sidebar_button">Request Food</button>

      <!-- Create Post Modal -->
      <div v-if="showPostModal" class="modal">
        <div class="modal-content">
          <CreatePostView />
          <button @click="showPostModal = false" class="close-button">Close</button>
        </div>
      </div>

      <!-- Create Request Modal -->
      <div v-if="showRequestModal" class="modal">
        <div class="modal-content">
          <CreateRequestView />
          <button @click="showRequestModal = false" class="close-button">Close</button>
        </div>
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

      <!-- Show posts once loaded -->
      <div v-else>
        <div v-for="post in posts" :key="post.id" class="post_card">
          <div class="image-container">
            <img v-for="url in post.imageUrls" :src="url" :alt="`Image`" class="post_image" />
          </div>
          <p>{{ post.description }}</p>
          <p><strong>Location:</strong> {{ post.location }}</p>
          <p><strong>Expiry:</strong> {{ post.expireAt }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  /* Layout Styles */
  .layout {
    display: flex;
    min-height: 100vh;
    background-color: #f9fafb;
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

  .sidebar_button:hover {
    background: #1e6843;
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
    overflow: hidden;
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

  .post_image {
    max-width: 300px;
    max-height: 300px;
    border-radius: 5px;
    margin-bottom: 10px;
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
