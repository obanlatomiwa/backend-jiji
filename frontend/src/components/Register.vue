<template>
  <div class="">
      <h1>Registration</h1>
      <form id="form-product" @submit:prevent="createUser">
          <!-- <p>
            <label for="firstname">First Name</label>
            <input class="ml-2" type="text" name="firstname" id="firstname" v-model="firstname">
          </p>

          <p>
            <label for="lastname">Last Name</label>
            <input class="ml-2" type="text" name="lastname" id="lastname" v-model="lastname">
          </p>

          <p>
            <label for="email">Email</label>
            <input class="ml-2" type="email" name="email" id="email" v-model="email">
          </p>

          <p>
            <label for="residence">State of Residence</label>
            <input class="ml-2" type="text" name="residence" id="residence" v-model="residence">
          </p> -->

          <p>
            <label for="username">Username</label>
            <input class="ml-2" type="text" name="username" id="username" v-model="username">
          </p>

          <p>
            <label for="password">Password</label>
            <input class="ml-2" type="password" name="password" id="password" v-model="password">
          </p>

          <p>
              <input type="submit" value="Submit" >
          </p>

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
        // firstname: null,
        // lastname: null,
        // email: null,
        // residence: null,
        username: null,
        password: null, 
      }
  },
  methods: {
      createUser(){
          console.log(this.username)
          axios.post('http://127.0.0.1:8000/api/users/', {
            //   firstname: this.firstname,
            //   lastname: this.lastname,
            //   email: this.email,
            //   residence: this.residence,
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
