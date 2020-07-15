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
      <button class="btn-sm btn-danger mt-2 mb-3" v-on:click="productDelete(productdetailitem)" @click="$emit('deleted', productdetail)">Delete Product</button>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import {tokenService} from '../storage/service'
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
    productDelete(productdetailitem){
      console.log(this.token)
      const postData = {
        product: this.productdetailitem.id,
      }
      let axiosConfig = {
        headers: {
          'Authorization': 'Token' + this.token
        }
      }
      axios.delete(`http://127.0.0.1:8000/api/products/${this.productdetailitem.id}`, axiosConfig)
      .then(res => console.log(res.data))
      .catch(err => console.log(err))
    }
  },
  created(){
    let token;
    this.token = tokenService.getToken();
  }
}
</script>

<style scoped>

</style>