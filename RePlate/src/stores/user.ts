import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({
    name: "",
    userType: "",
    profilePicture: "",
    rating: 0,
    token: localStorage.getItem("auth_token") || "" // Retrieve token if it exists
  }),

  getters: {
    isLoggedIn: (state) => !!state.token
  },

  actions: {
    async authUser(token: string) {
      return await fetch("https://44.211.65.112:8000/api/auth/google/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token })
      })
        .then((res) => res.json())
        .then((data) => {
          console.log("Authenticated: ", data);

          this.token = data["token"];
          this.name = data["name"];
          this.userType = data["user_type"];
          this.profilePicture = data["profile_picture"];
          this.rating = data["rating"];

          localStorage.setItem("auth_token", this.token);
        });
    },

    logout() {
      this.token = "";
      this.name = "";
      this.userType = "";
      this.profilePicture = "";
      this.rating = 0;
      localStorage.removeItem("auth_token");
    },

    async fetchUserData() {
      if (!this.token) return;

      try {
        // 127.0.0.1:8000
        // 44.211.65.112:8000
        const res = await fetch("https://44.211.65.112:8000/api/user/", {
          method: "GET",
          headers: {
            "Authorization": `Bearer ${this.token}`,
            "Content-Type": "application/json"
          }
        });

        const data = await res.json();
        this.name = data["name"];
        this.userType = data["user_type"];
        this.profilePicture = data["profile_picture"];
        this.rating = data["rating"];
      } catch (error) {
        console.error("Failed to fetch user data", error);
      }
    }
  }
});
