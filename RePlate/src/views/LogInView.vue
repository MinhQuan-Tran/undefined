<script lang="ts">
  export default {
    data() {
      return {};
    }
  };
</script>

<template>
  <div class="container" style="background-color: green">
    <h1>Log In</h1>
    <label for="user">Username</label>
    <input type="text" placeholder="Enter Username" name="user" required>

    <br> <br>

    <label for="pw">Password</label>
    <input type="password" placeholder="Enter Password" name="pw" required>
    
  </div>
</template>

<style scoped>
  .template {
    text-align: center;
  }
</style>