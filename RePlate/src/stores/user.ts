import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({
    name: "",
    userType: "",
    profilePicture: "",
    rating: 0
  }),

  getters: {
    isLoggedIn: (state) => state.name !== ""
  },

  actions: {
    async authUser(token: string) {
      return await fetch("http://44.211.65.112:8000/api/auth/google/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token })
      })
        .then((res) => res.json())
        .then((data) => {
          console.log("Authenticated: ", data);
          this.name = data["name"];
          this.userType = data["user_type"];
          this.profilePicture = data["profile_picture"];
          this.rating = data["rating"];
        });
    }
  }
});
