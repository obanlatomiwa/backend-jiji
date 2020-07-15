<template>
  <div class="">
    <b-navbar class="col-md-12 fix" toggleable="lg" type="dark" variant="success" >
    <b-navbar-brand href="#">
      <img src="../assets/jiji.svg" class="d-inline-block align-top" alt="logo">
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="./ListProducts.vue">Home</b-nav-item>
        <b-nav-item class="middle"> SELL FASTER, BUY FASTER</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form @submit.prevent="login" v-if="token==null">
            <b-form-input id="username" size="sm" class="mr-sm-2" placeholder="Username" name="username" v-model="username"></b-form-input>
            <b-form-input id="password" size="sm" class="mr-sm-2" placeholder="Password" name="password" v-model="password" type="password"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Login</b-button>
        </b-nav-form>

        <b-nav-form @submit.prevent="logout" v-if="token !== null">
            <b-button size="sm" class="my-2 ml-2" type="submit">Logout</b-button>
        </b-nav-form>

        <b-nav-form @submit.prevent="register" v-if="token === null">
            <b-button :to="{name: 'register'}" size="sm" class="my-2 ml-2 my-sm-0 outline-warning" type="submit">Register</b-button>
        </b-nav-form>       
 
      </b-navbar-nav>
    </b-collapse>
  </b-navbar> 


  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios' 
import { tokenService } from '../storage/service'
export default {
  name: 'Header',
  components: {
  },
  data(){
      return {
        firstname: '',
        lastname: '',
        email: '',
        residence: '',
        username: '',
        password: '',
        token: localStorage.getItem('user-token') || null,
      }
  },
  methods: {
      login(){
          axios.post('http://127.0.0.1:8000/auth/', {
            firstname: this.firstname,
            lastname: this.lastname,
            email: this.email,
            residence: this.residence,
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
      }, 

      logout(){
        localStorage.removeItem('user-token')
        this.token = null
      },
      register(){
        console.log('Router')
      }
  }, 
  created(){
    this.token = tokenService.getToken() || null
  }
}
</script> 

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Varta:wght@300;400;500&display=swap');
  .middle{
    display: flex;
    justify-content: center;
  }



</style>