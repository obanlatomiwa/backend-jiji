<template>
  <div class="">
    <div class="row">
        <div class="col-md-10">
            <p>Name: {{productdetailitem.name}}</p>
            <p>Description: {{productdetailitem.description}}</p>
            <p>Image: {{productdetailitem.image}}</p>
            <p>Price: {{productdetailitem.price}}</p>
            <p>Location: {{productdetailitem.location}}</p>
        </div>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";

export default {
  name: 'ProductDetails',
  components: {
    
  },
  props: {
      productdetailitem: {}
  },
  data() {
    return {
    }
  },
  methods: {

  }
}
</script>

<style scoped>

</style>