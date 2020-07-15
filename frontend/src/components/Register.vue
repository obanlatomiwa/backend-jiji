<template>
  <div class="container">
      <form id="form-product" @submit:prevent="createUser">
        <div class="card">
          <div><h1>Registration</h1></div>
          <div class="form-group">
            <label for="firstname">First Name</label>
            <input class="ml-4 form-control" type="text" name="firstname" id="firstname" v-model="firstname">
          </div>

          <div class="form-group">
            <label for="lastname">Last Name</label>
            <input class="ml-4 form-control" type="text" name="lastname" id="lastname" v-model="lastname">
          </div>

          <div class="form-group">
            <label for="email">Email</label>
            <input class="ml-4 form-control" type="email" name="email" id="email" aria-describedby="emailHelp" v-model="email">
          </div>

          <div class="form-group">
            <label for="residence">State of Residence</label>
            <input class="ml-4 form-control" type="text" name="residence" id="residence" v-model="residence">
          </div>

          <div class="form-group">
            <label for="username">Username</label>
            <input class="ml-4 form-control" type="text" name="username" id="username" v-model="username">
          </div>

          <div class="form-group">
            <label for="password">Password</label>
            <input class="ml-4 form-control" type="password" name="password" id="password" v-model="password">
          </div>

          <div class="form-group">
              <input type="submit"  class="btn btn-primary" value="Submit" >
          </div>
        </div>
      </form>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'register',
  components: {
    
  },
  data() {
      return {
        firstname: null,
        lastname: null,
        email: null,
        residence: null,
        username: null,
        password: null, 
      }
  },
  methods: {
      createUser(){
          console.log(this.username)
          axios.post('http://127.0.0.1:8000/api/users/', {
              firstname: this.firstname,
              lastname: this.lastname,
              email: this.email,
              residence: this.residence,
              username: this.username,
              password: this.password,
          })
          .then(res => console.log(res))
          .catch(err => console.log(err))
          this.$router.push('/')
      }
  }
}
</script>

<style scoped>
  .container {
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