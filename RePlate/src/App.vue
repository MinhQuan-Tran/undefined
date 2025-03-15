<script lang="ts">
  import { RouterLink, RouterView } from "vue-router";
  import HelloWorld from "./components/HelloWorld.vue";
  import Navbar from "./components/Navbar.vue";

  export default {
    components: {
      Navbar
    }
  };
</script>

<template>
  <header v-if="['/', '/about', '/auth'].includes($route.path)">
    <img alt="Vue logo" class="logo" src="@/assets/replate-logo.png" width="250" height="250" />

    <div class="wrapper">
      <HelloWorld msg="RePlate" />

      <nav>
        <RouterLink to="/">About</RouterLink>
        <!-- <RouterLink to="/about">About</RouterLink> -->
        <RouterLink to="/auth">Login/Signup</RouterLink>
      </nav>
    </div>
  </header>

  <Navbar v-else></Navbar>

  <RouterView />
</template>

<style scoped>
  header {
    line-height: 1.5;
    max-height: 100vh;
  }
  .app-container {
    background-color: white;
    min-height: 100vh;
    width: 100%;
  }

  .logo {
    display: block;
    margin-bottom: 1.5rem;
    border-radius: 50%;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  }


  nav {
    width: 100%;
    font-size: 12px;
    text-align: center;
    margin-top: 2rem;
  }

  nav a.router-link-exact-active {
  color: white;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 8px 16px;
  border-radius: 8px;
  border: 2px solid white;
}

nav a.router-link-exact-active:hover {
  background-color: rgba(255, 255, 255, 0.3);
}


  nav a {
    display: inline-block;
    padding: 0 1rem;
    color: white;
    border-left: 1px solid var(--color-border);
  }

  nav a:first-of-type {
    border: 0;
  }

  @media (min-width: 1024px) {
    header {
      display: flex;
      place-items: center;
      padding-right: calc(var(--section-gap) / 2);
    }

    .logo {
      margin: 0 2rem 0 0;
    }

    header .wrapper {
      display: flex;
      place-items: flex-start;
      flex-wrap: wrap;
    }

    nav {
      text-align: left;
      font-size: 1rem;

      padding: 1rem 0;
    }
  }
</style>
