<script>
  import { mapStores } from "pinia";
  import { useUserStore } from "@/stores/user";

  export default {
    data() {
      return {
        clientId: "648036916024-0habpslihj4isq59snnglv8gd7vdip7l.apps.googleusercontent.com",
        error: null
      };
    },

    computed: {
      ...mapStores(useUserStore)
    },

    mounted() {
      this.loadGoogleScript();
    },

    methods: {
      loadGoogleScript() {
        if (!window.google) {
          const script = document.createElement("script");
          script.src = "https://accounts.google.com/gsi/client";
          script.async = true;
          script.defer = true;
          script.onload = this.initGoogleSignIn;
          document.head.appendChild(script);
        } else {
          this.initGoogleSignIn();
        }
      },

      initGoogleSignIn() {
        if (window.google) {
          window.google.accounts.id.initialize({
            client_id: this.clientId,
            callback: (response) => this.handleCredentialResponse(response) // Fix the callback function
          });
          window.google.accounts.id.renderButton(document.querySelector(".g_id_signin"), {
            theme: "outline",
            size: "large"
          });
        }
      },

      async handleCredentialResponse(response) {
        console.log("Google response:", response);
        if (response.credential) {
          await this.sendTokenToBackend(response.credential);
        }
      },

      async sendTokenToBackend(token) {
        this.error = null;

        this.userStore
          .authUser(token)
          .then(() => {
            this.$router.push("/feed");
          })
          .catch((error) => {
            this.error = error.message;
          });
      }
    }
  };
</script>

<template>
  <div class="auth-view">
    <h1>RePlate</h1>

    <div
      id="g_id_onload"
      :data-client_id="clientId"
      data-callback="handleCredentialResponse"
      data-auto_prompt="false"
    ></div>
    <div class="g_id_signin" data-type="standard"></div>

    <div class="error" v-if="error">
      {{ error }}
    </div>
  </div>
</template>

<style scoped>
  .auth-view {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    height: 100vh;
  }

  .error {
    background-color: rgba(255, 0, 0, 0.1);
    border: 1px solid red;
    padding: 1rem;
    border-radius: 0.5rem;
    color: red;
  }
</style>
