<template>
  <div class="">
      <div class="row card">
          <div class="col-md-6">
              <div class="">
                  <div class="card-body">
                      <form id="form-product-id" @submit:prevent="checkForm">
                          <p class="form-group">
                              <label for="name">Name of Product</label>
                              <input class="ml-2 form-control" type="text" name="name" id="name" v-model="name">
                          </p>
                          <p class="form-group"> 
                              <label for="description">Description</label>
                              <input class="ml-2 form-control" type="textarea" name="description" id="description" v-model="description">
                          </p>
                          <p class="form-group">
                              <label for="image">Image</label>
                              <input class="ml-2 form-control-file" type="file" name="image" accept="image/*" alt="Upload" width="48" height="48" id="image">
                          </p>
                          <p class="form-group">
                              <label for="price">Price</label>
                              <input class="ml-2 form-control" type="number" name="price" id="price" v-model="price">
                          </p>
                          <p class="form-group"> 
                              <label for="location">Location</label>
                              <input class="ml-2 form-control" type="text" name="location" id="location" v-model="location">
                          </p>
                          <p>
                              <input class="ml-2 form-control" type="submit" value="Submit" @click="$emit('createdProduct')">
                          </p>
                      </form>
                  </div> 
              </div>
          </div>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

export default {
  name: 'CreateProduct',
  components: {
  },
  data(){
      return {
          name: null,
          description: null,
          image: null,
          price: null,
          location: null,
      }
  },
  methods: {
      checkForm(){
          axios.post('http://127.0.0.1:8000/api/products/', {
              name: this.name,
              description: this.description,
              image: this.image,
              price: this.price,
              location: this.location,
          })
          .then(res => console.log(res))
          .catch(err => console.log(err))
      }
  }
}
</script>
