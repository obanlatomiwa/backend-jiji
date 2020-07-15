<template>
    <div class="row text">
        <div class="text-left text-justify" v-if="createNew"> 
          <CreateProduct v-if="token==null"  v-on:createdProduct="updateProduct"/>
        </div> 
        <div class="col-md-3 text-center product-view card text-left text-justify">
            <form @submit="createdNew()" class ="">
              <input class="btn-sm btn-primary mb-3 btn" id="createdNew" type="submit" value="Add Product"> 
            </form> 
            <h5>Products</h5>
            <b-list-group class ="text-left text-justify">
            <b-list-group-item v-bind:key="product.id" v-for= "product in products">
              <a href="#" class="btn sm btn-light mt-2 mb-3" v-on:click="productDetail(product)">
                {{product.description}}
              </a>               
            </b-list-group-item>
            </b-list-group>
        </div> 
        <div class="col-md-1"></div>
        <div class="col-md-7  ">
          <ProductDetails v-bind:productdetailitem="productDetailItem" v-on:deleted="updateProduct"/>
        </div>

          <!-- Site footer -->
    <footer class="site-footer" type="dark" variant="success">
      <div class="container">
        <div class="row">
          <div class="col-sm-12 col-md-6">
            <h6>About</h6>
            <p class="text-justify"> Jiji is the best place to sell anything to real people.
It is the biggest free online classified with an advanced security system. We provide a simple hassle-free solution to sell and buy almost anything.</p>
          <p>We are highly focused on the security and can solve any issues in short-terms.</p>
          </div>


          <div class="col-xs-6 col-md-6">
            <h6>Quick Links</h6>
            <ul class="footer-links">
              <li><a href="https://jiji.ng/about.html">About Us</a></li>
              <li><a href="https://jiji.ng/contacts.html">Contact Us</a></li>
              <li><a href="https://jiji.ng/rules.html">Terms and Conditions</a></li>
              <li><a href="https://jiji.ng/privacy.html">Privacy Policy</a></li>
              <li><a href="https://jiji.ng/faq">FAQ</a></li>
            </ul>
          </div>
        </div>
        <hr>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-md-12 col-sm-6 col-xs-12">
            <p class="copyright-text">Copyright &copy; 2020 Jiji.ng 
            </p>
          </div>
        </div>
      </div>
</footer>


      </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import ProductDetails from "./ProductDetails";
import CreateProduct from "./CreateProduct";
import Header from "./Header";


export default {
  name: 'ListProducts',
  components: {
    ProductDetails,
    CreateProduct
  },
  data() {
    return { 
      products: [],
      productDetailItem: Object,
      createNew: "",
      token: Header.data.token,
    }
  },
  methods: {
    getProducts(){
      axios.get('http://127.0.0.1:8000/api/products/')
      .then(res => (this.products = res.data))
      .catch(err =>console.log(err))
      console.log(this.products)
    },
    productDetail(product){
      this.productDetailItem = product; 
      console.log(this.productDetailItem)
    },
    createdNew(){
      this.createNew = !this.createNew;
    },
    updateProduct(){
      this.timer = setTimeout(() => {
        axios.get('http://127.0.0.1:8000/api/products/')
        .then(res => (this.products = res.data))
        .catch(err => console.log(err))
      }, 500);
    }
  },
  created(){
    this.getProducts();
    createNew: false;
  }
}
</script>

<style scoped>
  .product-view {
    @import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;0,900;1,300&display=swap');
    font-size: 26px;
    font-family: 'Lato', sans-serif;
    align-items: center;
    display: flex;
    padding: 1.5rem 3rem;
    transition: all .3s;
    text-decoration: none;


  }
.fix {
position:absolute;
min-width:100%;
min-height:100%;
}

footer{
    position: 'absolute';
    left: 0;
    bottom: 0;
    width: 100%;
    padding: 20px;
    margin-top: 20px;
    background: green;
    text-align: center;
  }

  .site-footer
{
  padding:45px 0 20px;
  font-size:15px;
  line-height:24px;
}
.site-footer hr
{
  border-top-color:#bbb;
  opacity:0.5
}
.site-footer hr.small
{
  margin:20px 0
}
.site-footer h6
{
  color:#fff;
  font-size:16px;
  text-transform:uppercase;
  margin-top:5px;
  letter-spacing:2px
}
.site-footer a
{
  color:#737373;
}
.site-footer a:hover
{
  color:#3366cc;
  text-decoration:none;
}
.footer-links
{
  padding-left:0;
  list-style:none
}
.footer-links li
{
  display:block
}
.footer-links a
{
  color:#737373
}
.footer-links a:active,.footer-links a:focus,.footer-links a:hover
{
  color:#3366cc;
  text-decoration:none;
}
.footer-links.inline li
{
  display:inline-block
}
.site-footer .social-icons
{
  text-align:right
}
.site-footer .social-icons a
{
  width:40px;
  height:40px;
  line-height:40px;
  margin-left:6px;
  margin-right:0;
  border-radius:100%;
  background-color:#33353d
}
.copyright-text
{
  margin:0
}
@media (max-width:991px)
{
  .site-footer [class^=col-]
  {
    margin-bottom:30px
  }
}
@media (max-width:767px)
{
  .site-footer
  {
    padding-bottom:0
  }
  .site-footer .copyright-text,.site-footer .social-icons
  {
    text-align:center
  }
}
</style>

