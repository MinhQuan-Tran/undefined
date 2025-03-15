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
      <button class="btn primary">Location</button>
      <button class="btn primary">Display</button>
      <button class="btn primary">Clear Cache</button>
      <button class="btn primary">Clear History</button>
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

.button-group {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-top: 25px;
  width: 80%;
  max-width: 320px;
}

.btn {
  padding: 12px;
  width: 100%;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.3s ease-in-out;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}

.btn.primary {
  background: white;
  color: #333;
  border: 1px solid #8a8a8a;
}

.btn.primary:hover {
  background: #e0e0e0;
  transform: translateY(-2px);
}

.btn.danger {
  background: #e74c3c;
  border-radius: 25px;
  color: white;
  border: none;
}

.btn.danger:hover {
  background: #c0392b;
  transform: translateY(-2px);
}
</style>
