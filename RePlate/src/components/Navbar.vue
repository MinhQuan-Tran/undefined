<script lang="ts">
  import { mapStores } from "pinia";
  import { useUserStore } from "@/stores/user";

  export default {
    computed: {
      ...mapStores(useUserStore)
    }
  };
</script>

<template>
  <nav id="navbar" class="py-5 px-5 border-b border-gray-200 fixed top-0 left-0 right-0 w-full h-px-48 m-0 bg-white">
    <div class="w-full">
      <div class="flex justify-around">
        <RouterLink to="/feed">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke-width="1.5" stroke="currentColor" class="size-6">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M8.25 21v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21m0 0h4.5V3.545M12.75 21h7.5V10.75M2.25 21h1.5m18 0h-18M2.25 9l4.5-1.636M18.75 3l-1.5.545m0 6.205 3 1m1.5.5-1.5-.5M6.75 7.364V3h-3v18m3-13.636 10.5-3.819"
            />
          </svg>
        </RouterLink>

        <h1>RePlate</h1>

        <RouterLink to="/profile/edit">
          <img
            v-if="userStore.profilePicture"
            class="profile-picture size-6"
            :src="userStore.profilePicture"
            alt="Profile picture"
            loading="lazy"
          />
          <svg
            v-else
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"
            />
          </svg>
        </RouterLink>
      </div>
    </div>
  </nav>
</template>

<style scoped>
  .template {
    text-align: center;
  }

  #navbar {
    z-index: 1000;
    margin: 0;
  }

  .profile-picture {
    border-radius: 50%;
  }
</style>
