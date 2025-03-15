<template>
    <div class="profile-container">
      <div class="profile-card">
        <img :src="user.avatar" alt="Profile Picture" class="profile-pic" />
        <h2>{{ user.name }}</h2>
        <p class="category">{{ user.category }}</p>
  
        <div class="edit-form">
          <label>Username</label>
          <input v-model="user.name" placeholder="Username" />
          <label>Category</label>
          <input v-model="user.category" placeholder="Category" />
          <label>Location</label>
          <input v-model="user.location" placeholder="Location" />
          <label>Phone Number</label>
          <input v-model="user.phone" placeholder="Phone Number" />
          <label>Join Date</label>
          <input v-model="user.join" placeholder="Join Date" />
  
          <button class="save-btn" @click="saveProfile">Save</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        user: {
          name: "",
          category: "",
          location: "",
          phone: "",
          join: ""
        }
      };
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
    background: #f4f4f4;
  }
  
  .profile-card {
    width: 350px;
    padding: 25px;
    text-align: center;
    background: white;
    border-radius: 12px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
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
    border: 3px solid #42b983;
  }
  
  h2 {
    margin: 10px 0;
    font-size: 22px;
    color: #333;
  }
  
  .category {
    font-size: 16px;
    color: #666;
    font-weight: bold;
  }
  
  .location, .phone, .join {
    font-size: 14px;
    color: #444;
    margin: 5px 0;
  }
  
  button {
    margin-top: 15px;
    padding: 10px;
    width: 100%;
    border: none;
    border-radius: 6px;
    background: #42b983;
    color: white;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s;
  }
  
  button:hover {
    background: #369d77;
  }
  
  .edit-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 15px;
    text-align: left;
  }
  
  .edit-form label {
    font-weight: bold;
    font-size: 14px;
    color: #444;
  }
  
  .edit-form input {
    padding: 8px;
    border-radius: 5px;
    border: 1px solid #ccc;
    width: 100%;
    transition: border 0.3s;
  }
  
  .edit-form input:focus {
    border-color: #42b983;
    outline: none;
  }
  
  .save-btn {
    background: #007bff;
  }
  
  .save-btn:hover {
    background: #0056b3;
  }

  .other-btn {
    background: #ffffff;
  }
  .other-btn {
    background: #d4d3d3;
  }
  </style>
  
