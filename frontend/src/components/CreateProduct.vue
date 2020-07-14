<template>
  <div class="">
      <div class="row">
          <div class="col-md-6">
              <div class="card">
                  <div class="card-body">
                      <form id="form-product-id" @submit:prevent="checkForm">
                          <p>
                              <label for="name">Name of Product</label>
                              <input class="ml-2" type="text" name="name" id="name" v-model="name">
                          </p>
                          <p>
                              <label for="description">Description</label>
                              <input class="ml-2" type="textarea" name="description" id="description" v-model="description">
                          </p>
                          <p>
                              <label for="image">Image</label>
                              <input class="ml-2" type="text" name="image" accept="image/*" alt="Upload" width="48" height="48" id="image" v-model="image">
                          </p>
                          <p>
                              <label for="price">Price</label>
                              <input class="ml-2" type="number" name="price" id="price" v-model="price">
                          </p>
                          <p>
                              <label for="location">Location</label>
                              <input class="ml-2" type="text" name="location" id="location" v-model="location">
                          </p>
                          <p>
                              <input class="ml-2" type="submit" value="Submit">
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
