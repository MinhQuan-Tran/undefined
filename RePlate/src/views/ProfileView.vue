<script>
import { RouterLink } from 'vue-router';

export default {
  data() {
    return {
      user: {
        name: "",
        category: "",
        location: "",
        phone: "",
        join: "",
        avatar: ""
      }
    };
  },
  created() {
    const savedUser = localStorage.getItem("userProfile");
    if (savedUser) {
      this.user = JSON.parse(savedUser);
    }
  }
};
</script>

<template>
  <div class="profile-container">
    <img :src="user.avatar" alt="Profile Picture" class="profile-pic" />
    <h2>{{ user.name }}</h2>
    <p class="category">{{ user.category }}</p>

    <div class="button-group">
      <RouterLink to="/profile/edit">
        <button class="btn primary">Edit Profile</button>
      </RouterLink>
      <button class="btn secondary">Location</button>
      <button class="btn secondary">Display</button>
      <button class="btn secondary">Clear Cache</button>
      <button class="btn secondary">Clear History</button>
      <button class="btn danger">Logout</button>
    </div>
  </div>
</template>

<style scoped>
/* Background with soft gradient */
.profile-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  padding: 20px;
  background: #eeeeee;
  text-align: center;
}

/* Profile picture */
.profile-pic {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #000000;
  transition: transform 0.3s ease-in-out;
}

.profile-pic:hover {
  transform: scale(1.08);
}

/* Text styling */
h2 {
  margin-top: 15px;
  font-size: 26px;
  color: #333;
}

.category {
  font-size: 18px;
  color: #666;
  font-weight: bold;
}

/* Buttons container */
.button-group {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-top: 25px;
  width: 80%;
  max-width: 320px;
}

/* Button styles */
.btn {
  padding: 12px;
  width: 100%;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.3s ease-in-out;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}

/* Primary button */
.btn.primary {
  background: #42b983;
  color: white;
}

.btn.primary:hover {
  background: #369d77;
  transform: translateY(-2px);
}

/* Secondary buttons */
.btn.secondary {
  background: white;
  color: #333;
  border: 1px solid #ddd;
}

.btn.secondary:hover {
  background: #e0e0e0;
  transform: translateY(-2px);
}

/* Danger button */
.btn.danger {
  background: #e74c3c;
  color: white;
}

.btn.danger:hover {
  background: #c0392b;
  transform: translateY(-2px);
}
</style>
