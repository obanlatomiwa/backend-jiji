<template>
  <div class="">
    <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#" src="../assets/jij2.png">Jiji.ng</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">Link</b-nav-item>
        <b-nav-item href="#" disabled>Disabled</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form @submit.prevent="login" v-if="token==null">
            <b-form-input id="username" size="sm" class="mr-sm-2" placeholder="Username" name="username" v-model="username"></b-form-input>
            <b-form-input id="password" size="sm" class="mr-sm-2" placeholder="Password" name="password" v-model="password" type="password"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Login</b-button>
        </b-nav-form>
 
      </b-navbar-nav>
    </b-collapse>
  </b-navbar> 
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios' 
export default {
  name: 'Header',
  components: {
  },
  data(){
      return {
          username: '',
          password: '',
          token: localStorage.getItem('user-token') || null,
      }
  },
  methods: {
      login(){
          axios.post('http://127.0.0.1:8000/auth/', {
             username: this.username,
             password: this.password
          }
          )
          .then(res => {
              this.token = res.data.token,
              console.log(this.token),
              localStorage.setItem('user-token', res.data.token)
          })
          .catch(err => {
              localStorage.removeItem('user-token')
          })    
      }
  }
}
</script> 
