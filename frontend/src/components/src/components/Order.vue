<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8 order-md-1">
        <h3>Order number {{order.id}}</h3>
        <br/>
        <br/>
        <table class="table table-hover">
          <thead class="thead-light">
            <tr>
              <th scope="col">Contractor name</th>
              <th scope="col">Contractor NIP</th>
              <th scope="col">Contractor Address</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="align-middle">
                {{order.contractor_id.name}}
              </td>

              <td class="align-middle">
                {{order.contractor_id.nip}}
              </td>

              <td class="align-middle">
                {{order.contractor_id.address}}
              </td>
            </tr>
          </tbody>
        </table>

        <table class="table table-hover">
          <thead class="thead-light">
            <tr>
              <th scope="col">Implementation date</th>
              <th scope="col">Data of placing the order</th>
              <th scope="col">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="align-middle">
                {{order.implementation_date}}
              </td>

              <td class="align-middle">
                {{order.data_of_placing_the_order}}
              </td>

              <td class="align-middle">
                {{order.status}}
              </td>
            </tr>
          </tbody>
        </table>

        <table class="table table-hover">
          <thead class="thead-light">
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Quantity</th>
              <th scope="col">Price</th>
              <th scope="col">Full price</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="product in products" v-bind:key="product.name">
              <td class="align-middle">
                {{product.name}}
              </td>

              <td class="align-middle">
                {{product.quantity}}
              </td>

              <td class="align-middle">
                {{product.price}}
              </td>

              <td class="align-middle">
                {{product.full_price}}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <footer class="my-5 pt-5 text-muted text-center text-small">
      <p class="mb-1">Orders management</p>
    </footer>

  </div>
</template>


<script>

  // Import required dependencies
  import 'bootstrap/dist/css/bootstrap.css';
  import axios from 'axios';

  export default {
    name: 'Order',
    data() {
      return {
        order: null,
        products: null
      };
    },
    components: {
    },
    created: function() {

      //get orderId
      var id = localStorage.getItem('orderId')

      //update data
      this.updateOrderData(id)

    },
    methods: {
      updateOrderData(id) {
        axios
          .get('http://127.0.0.1:8000/api/orders/' + id)
          .then(res => {

            var response = res.data

            //get basic info
            this.order = {
              "contractor_id": {
                "name": response.contractor_id.name,
                "nip": response.contractor_id.nip,
                "address": response.contractor_id.address,
              },
              "id": response.id,
              "implementation_date": response.implementation_date,
              "data_of_placing_the_order": response.data_of_placing_the_order,
              "status": response.status,
            }


            //iterate through products
            var products = []
            var i

            for (i = 0; i < response.products.length; i++) {
              var product = {
                "name": response.products[i].name,
                "quantity": response.products[i].quantity,
                "price": response.products[i].price,
                "full_price": response.products[i].full_price
              }
              products.push(product)
            }

            //update products
            this.products = products

          });
      }
    }
  }
</script>

<style>
  h3 {
    margin-bottom: 5%;
  }
  td {
    font-size: 14px;
  }
  th {
    font-size: 14px;
  }
  button {
    border: none;
    background: none;
  }
  div {
    border-top: none;
  }
</style>
