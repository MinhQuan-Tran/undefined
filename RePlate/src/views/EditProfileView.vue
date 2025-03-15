<template>
  <div class="profile-container">
    <div class="profile-card">
      <img :src="user.avatar" alt="Profile Picture" class="profile-pic" @click="fileInput.click()" />
      <input type="file" ref="fileInput" accept="image/*" style="display: none" @change="updateProfilePicture" />
      <h2>{{ user.name }}</h2>
      <p class="category">{{ user.category }}</p>

      <div class="edit-form">
        <label>Username</label>
        <input v-model="user.name" placeholder="Username" />
        <label>User Type</label>
        <input v-model="user.userType" placeholder="User Type" />
        <label>Location</label>
        <input v-model="user.location" placeholder="Location" />
        <!-- <label>Phone Number</label>
        <input v-model="user.phone" placeholder="Phone Number" /> -->
        <label>Join Date</label>
        <input v-model="user.join" placeholder="Join Date" />
        <label>Rating</label>
        <input v-model="user.rating" placeholder="Rating" disabled />
      </div>

      <div class="button-group">
        <button class="btn save-btn" @click="saveProfile">Save</button>
        <button class="btn cancel-btn" @click="$router.push('/profile')">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapStores } from "pinia";
  import { useUserStore } from "@/stores/user";

  export default {
    data() {
      return {
        user: {
          name: this.userStore.name,
          userType: this.userStore.userType,
          location: "",
          phone: "",
          join: this.userStore.createdAt,
          rating: this.userStore.rating ? this.userStore.rating + "/5" : "N/A",
          avatar: "/src/assets/profile-icon.png"
        }
      };
    },
    computed: {
      ...mapStores(useUserStore)
    },
    created() {
      const savedUser = localStorage.getItem("userProfile");
      if (savedUser) {
        this.user = JSON.parse(savedUser);
      }
    },
    methods: {
      saveProfile() {
        localStorage.setItem("userProfile", JSON.stringify(this.user));
        this.$router.push("/profile");
      },
      updateProfilePicture(event) {
        if (event.target.files[0]) {
          const reader = new FileReader();
          reader.onload = () => {
            this.user.avatar = reader.result;
          };
          reader.readAsDataURL(file);
        }
      }
    }
  };
</script>

<style scoped>
  .profile-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
  }

  .profile-card {
    width: 400px;
    padding: 30px;
    text-align: center;
    background: white;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
    transition: transform 0.3s ease-in-out;
  }

  .profile-card:hover {
    transform: translateY(-5px);
  }

  .profile-pic {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #000000;
    transition: transform 0.3s ease-in-out;
    cursor: pointer; /* Indicating it's clickable */
  }

  .profile-pic:hover {
    transform: scale(1.08);
  }

  h2 {
    margin-top: 15px;
    font-size: 24px;
    color: #333;
  }

  .category {
    font-size: 16px;
    color: #555;
    font-weight: bold;
  }

  .edit-form {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 20px;
    text-align: left;
  }

  .edit-form label {
    font-weight: 600;
    font-size: 14px;
    color: #444;
  }

  .edit-form input {
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #ccc;
    width: 100%;
    transition: border 0.3s;
  }

  .edit-form input:focus {
    border-color: #42b983;
    outline: none;
  }

  .button-group {
    display: flex;
    gap: 10px;
    margin-top: 20px;
  }

  .btn {
    padding: 12px;
    width: 100%;
    border: none;
    border-radius: 25px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s ease-in-out;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  }

  .save-btn {
    background: #42b983;
    color: white;
  }

  .save-btn:hover {
    background: #369d77;
    transform: translateY(-2px);
  }

  .cancel-btn {
    background: #ff6b6b;
    color: white;
  }

  .cancel-btn:hover {
    background: #e74c3c;
    transform: translateY(-2px);
  }
</style>
