<script setup lang="ts">
import { useGeolocation } from '@vueuse/core'
import {ref, computed} from 'vue'

const { coords } = useGeolocation() //holds users current lat and long
const searchRadius = ref(5) //reactive variable that holds distance of valid post radius
const posts = ref([]) //reactive variable that stores all available posts (empty init)

const availablePosts = computed(() => {
  if (!coords.value.latitude || !coords.value.longitude) return [];

  return filterPosts( //reactive function that filters posts every time input coords change
    coords.value.latitude,
    coords.value.longitude,
    posts,
    searchRadius
  );

});

function HaversineDistance(lat1:number, lon1:number, lat2:number, lon2:number) {
  const R = 6371; // Earth's radius in kilometers
  const dLat = (lat2 - lat1) * Math.PI / 180;
  const dLon = (lon2 - lon1) * Math.PI / 180;
  
  const a = 
    Math.sin(dLat/2) * Math.sin(dLat/2) +
    Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) * 
    Math.sin(dLon/2) * Math.sin(dLon/2);
    
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  return R * c; // Distance in kilometers
}

function filterPosts(userLat, userLng, posts, searchRadius) {
  return posts.filter(post => {
    const distance = HaversineDistance(
      userLat, 
      userLng, 
      post.latitude, 
      post.longitude
    );
    
    return distance <= searchRadius;
  });
}

console.log(coords.value.latitude, coords.value.longitude)

</script>

<!-- <template>
   <UseGeolocation v-slot="{ coords: { latitude, longitude } }">
     Latitude: {{ latitude }}
     Longitude: {{ longitude }}
   </UseGeolocation>
</template>  -->

<!-- <template>
  <div class="display-location">
    <h1>Your location: </h1>
    <h2 v-if="coords.latitude && coords.longitude">
      Latitude: {{coords.latitude}}
      <br>
      Longitude: {{coords.longitude}}
    </h2>

    <h2 v-else>
      Locating...
    </h2>
  </div>
</template> -->

<style scoped>
.display-location {
  margin: 20px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
}
</style> 