<template>
  <div class="home">
    <img alt="Jiji logo" src="../assets/jij2.png">
    <ListProducts msg="Welcome to Jiji"/>
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
