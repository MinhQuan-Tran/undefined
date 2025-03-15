<template>
  <div>
    <div
      id="g_id_onload"
      :data-client_id="clientId"
      data-callback="handleCredentialResponse"
      data-auto_prompt="false"
    ></div>
    <div class="g_id_signin" data-type="standard"></div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        clientId: "648036916024-0habpslihj4isq59snnglv8gd7vdip7l.apps.googleusercontent.com"
      };
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
        try {
          const res = await fetch("http://127.0.0.1:8000/api/auth/google/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ token })
          });
          const data = await res.json();
          console.log("Authenticated:", data);
        } catch (error) {
          console.error("Error:", error);
        }
      }
    }
  };
</script>
