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
      showPostModal: false, // Controls visibility for CreatePostView modal
      showRequestModal: false, // Controls visibility for CreateRequestView modal
    };
  },
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
      <<div v-for="post in posts" :key="post.id" class="post_card">
        <div class="image-container">
          <img
          :src="post.image"
          :alt="`Image of ${post.title}`"
          class="post_image"
          />
        </div>
        <h3 style="font-size: large; font-weight: bold;">{{ post.title }}</h3>
        <p>{{ post.description }}</p>
        <p><strong>Location:</strong> {{ post.location }}</p>
        <p><strong>Expiry:</strong> {{ post.expiry }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const posts = ref([
  { id: 1, title: "Box of Pears", description: "Fresh pears available! Atleast 15, must be picked up by tomorrow", image: new URL('@/assets/Pears.jpg', import.meta.url).href, location: "Melbourne", expiry: "17/03/2025 11:00:AM"},
  { id: 2, title: "Hokkein Noodles", description: "Yummy hokkein noodles available until late tonight.", image: new URL("@/assets/hokkeinnoodles.jpg", import.meta.url).href, location: "Melbourne", expiry: "17/03/2025 11:00:PM" },
  { id: 3, title: "Leftover Greek", description: "Leftover Greek food, available until Tuesday", image: new URL("@/assets/LeftoverGreek.jpg", import.meta.url).href, location: "Echuca", expiry: "19/03/2025 05:00:PM" },
]);
</script>

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
</style>



<!-- <script lang="ts">
import { ref } from "vue";
import CreatePostView from "./CreatePostView.vue";
import CreateRequestView from "./CreateRequestView.vue";
import SocialFeed from "./SocialFeed.vue";

export default {
  components: {
    CreatePostView,
    CreateRequestView,
    SocialFeed,
  },
  data() {
    return {
      showPostModal: false, // Controls visibility for CreatePostView modal
      showRequestModal: false, // Controls visibility for CreateRequestView modal
      showFeed: true,
    };
  },
};
</script>

<template>
  <div class="sidebar">
    <button @click="showPostModal = true" style="color: darkolivegreen; font-size: x-large;">Share Food</button>
    <button @click="showRequestModal = true" style="color: darkolivegreen; font-size: x-large;">Request Food</button>
    <button @click="showFeed = true" style="color: darkolivegreen; font-size: x-large;">Show Feed</button>

     Create Post Modal -->
    <!-- <div v-if="showPostModal" class="modal">
      <div class="modal-content">
        <CreatePostView />
        <button @click="showPostModal = false" class="close-button">Close</button>
      </div>
    </div>
    Create Request Modal -->
    <!-- <div v-if="showRequestModal" class="modal">
      <div class="modal-content">
  
        <CreateRequestView />
        <button @click="showRequestModal = false" class="close-button">Close</button>
        
      </div>
    </div>

    <div v-if="showFeed" class="modal">
      <div class="modal-content">
        <SocialFeedView />
        <button @click="showFeed = false" class="close-button">Close</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;
  justify-self: left;
}
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
</style> -->