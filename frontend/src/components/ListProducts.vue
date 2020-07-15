<template>
  <div class="">
    <div class="col-md-12 mb-5" v-if="createNew"> 
      <CreateProduct v-on:createdProduct="updateProduct"/>
    </div> 
    <div class="row">
        <div class="col-md-5 text-center product-view">
            <h4>Welcome to Jiji</h4>
            <form @submit="createdNew()">
              <input class="btn-sm btn-primary mb-3 btn-center" id="createdNew" type="submit" value="Add Product"> 
            </form>
            <br>
            <p v-bind:key="product.id" v-for= "product in products">
              {{product.description}}
              <button class="btn sm btn-primary mt-2 mb-3" v-on:click="productDetail(product)">
                products list
              </button>
              <br> 
            </p>
        </div> 

        <div class="col-md-6">
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

  }
</style>