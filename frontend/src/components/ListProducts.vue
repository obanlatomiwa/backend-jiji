<template>
  <div class="container-fluid">
    <div class="col-md-12 mb-5" v-if="createNew"> 
      <CreateProduct v-on:createdProduct="updateProduct"/>
    </div> 
    <div class="row">
        <div class="col-md-3 text-center product-view card">
            <form @submit="createdNew()" class ="">
              <input class="btn-sm btn-primary mb-3 btn-center" id="createdNew" type="submit" value="Add Product"> 
            </form> 
            <h5>Products</h5>
            <ul class ="product-view">
              <div v-bind:key="product.id" v-for= "product in products">
              <button class="btn sm btn-light mt-2 mb-3" v-on:click="productDetail(product)">
                {{product.description}}
              </button>               
            </div>
            </ul>
        </div> 

        <div class="col-md-9">
          <ProductDetails v-bind:productdetailitem="productDetailItem" v-on:deleted="updateProduct"/>
        </div>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import ProductDetails from "./ProductDetails";
import CreateProduct from "./CreateProduct";


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
</style>

