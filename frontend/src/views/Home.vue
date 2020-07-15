<template>
  <div class="home">
    <ListProducts/>
  </div>
</template>

<script>
// @ is an alias to /src
import ListProducts from '@/components/ListProducts.vue'

export default {
  name: 'Home',
  components: {
    ListProducts
  }
}
</script>
