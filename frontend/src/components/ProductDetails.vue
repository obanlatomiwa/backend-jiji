<template>
  <div class=" container main-text" v-if ="productdetailitem.name !== null">
    <div class="row text-left text-justify" >
        <div class="col-md-12 card " style="width: 100%;">
        <img v-bind:src="productdetailitem.image" 
            class="card-img-top md-10"
            alt="" 
            style="width: 100%; height: 60%; margin: 0 auto 0 auto;">
        <div class="card-body">
            <p class="card-title"><span class= "span-text">Product: </span> {{ productdetailitem.name }}</p>
            <p class="card-text"> <span class= "span-text">Description:</span> {{ productdetailitem.description }}</p>
            <p class="card-text"> <span class= "span-text">Price: </span>{{productdetailitem.price}} NGN</p>
            <p class="card-text"> <span class= "span-text">Location:</span> {{productdetailitem.location}}</p>
            <button class="btn-sm btn-danger mt-2 mb-3" v-if="token!==null" v-on:click="productDelete(productdetailitem)" @click="$emit('deleted', productdetailitem)">Delete Product</button>
            <button class="btn-sm btn-danger mt-2 mb-3" v-if="token==null" v-on:click="contactSeller(productdetailitem)" @click="$emit('deleted', productdetailitem)">Contact Seller</button>
        </div>
        </div>
      </div>
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
    },
    contactSeller(productdetailitem){
        axios.get(`http://127.0.0.1:8000/admin/jiji_clone_api/users/${this.productdetailitem.id}/change/`)
        .then(res => (this.seller) = res.data)
        .catch(err => console.log(err))
        console.log(this.seller)
    }
  },
  created(){
    let token;
    this.token = tokenService.getToken();
  },

}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Varta:wght@300;400;500&display=swap');
  .main-text {
    font-family: 'Varta', sans-serif;
    font-size: 20px;
    color: black; 
  }
  .span-text {
    color: blue;
    font-family: 'Varta', sans-serif;
  }
</style>