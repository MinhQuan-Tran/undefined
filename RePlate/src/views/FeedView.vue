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
  <div class="sidebar">
    <button @click="showPostModal = true" style="color: darkolivegreen; font-size: large;">Share Food</button>
    <button @click="showRequestModal = true" style="color: darkolivegreen; font-size: large;">Request Food</button>

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
  <!-- <div class="right-side" >
    Hello
  </div> -->
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

/* Styling for the right-side div
.right-side {
  position: fixed;
  right: 0;
  top: 20px;
  font-size: 24px;
  color: white;
  padding: 10px;
} */
</style>
