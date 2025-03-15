import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({
    name: "",
    userType: "",
    profilePic: "",
    rating: 0
  }),

  getters: {
    isLoggedIn: (state) => state.name !== ""
  },

  actions: {
    async authUser(token: string) {
      fetch("http://127.0.0.1:8000/api/auth/google/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token })
      })
        .then((res) => res.json())
        .then((data) => {
          console.log("Authenticated: ", data);
          this.name = data.name;
          this.userType = data.userType;
          this.profilePic = data.profilePic;
          this.rating = data.rating;
        })
        .catch((err) => {
          console.error("Error registering: ", err);
        });
    }
  }
});
