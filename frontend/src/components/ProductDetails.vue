<template>
  <div class="">
    <div class="row">
        <div class="col-lg-10">
            <b-card
              title= ''
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              style="max-width: 100rem;"
              class="md-10"
            >
              <b-card-text>
                <p > <strong> {{productdetailitem.name}} </strong></p>
                <p>Description: {{productdetailitem.description}}</p>
                <p>Price: {{productdetailitem.price}} NGN</p>
                <p>Location: {{productdetailitem.location}}</p>
              </b-card-text>
              <button class="btn-sm btn-danger mt-2 mb-3" v-on:click="productDelete(productdetailitem)" @click="$emit('deleted', productdetailitem)">Delete Product</button>
            </b-card>
            <p>Name: {{productdetailitem.name}}</p>
            <p>Image: {{productdetailitem.image}}</p>
        </div>
      </div>
      <button class="btn-sm btn-danger mt-2 mb-3" v-on:click="productDelete(productdetailitem)" @click="$emit('deleted', productdetailitem)">Delete Product</button>
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
  .row {
    @import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;0,900;1,300&display=swap');
    font-size: 26px;
    font-family: 'Lato', sans-serif;
    align-items: center;
    display: flex;
    padding: 1.5rem 3rem;
    transition: all .3s;
    text-decoration: none;


  }
</style>