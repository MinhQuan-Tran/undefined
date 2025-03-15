import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({
    name: String,
    userType: String,
    profilePic: String
  }),

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
        })
        .catch((err) => {
          console.error("Error registering: ", err);
        });
    }
  }
});
