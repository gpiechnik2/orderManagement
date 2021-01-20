<template>
  <div class="container">
    <div class="row justify-content-center">

      <div class="col-md-8 order-md-1">
        <h3>New order</h3>

        <notifications group="alertSuccess" position="top right" max="3" classes="alert alert-success"/>
        <notifications group="alertDanger" position="top right" max="3" classes="alert alert-danger"/>

        <form v-if="validation === 0" class="needs-validation" novalidate>
          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="contractor">Contractor NIP</label>
              <select class="custom-select d-block w-100" id="contractor" v-model="contractor" required>
                <option :value="null">Choose...</option>
                <option v-for="contractor in contractors" :value="contractor" :key="contractor.id">
                  <option>{{contractor.nip}}</option>
                </option>
              </select>
            </div>

            <div class="col-md-6 mb-3">
              <label for="status">Status</label>
              <select class="custom-select d-block w-100" id="status" v-model="status" required>
                <option :value="null">Choose...</option>
                <option v-for="status in statuses" :value="status" :key="status.name">
                  <option>{{status.status}}</option>
                </option>
              </select>
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="status">implementation date</label>
              <date-picker v-model="implementationDate" @dp-change="changeImplementationDate(implementationDate)" :config="{format: 'DD-MM-YYYY hh:mm'}"></date-picker>

            </div>
            <div class="col-md-6 mb-3">
              <label for="status">Date of placing the order</label>
              <date-picker v-model="dateOfPlacingTheOrder" @dp-change="changeDateOfPlacingTheOrder(dateOfPlacingTheOrder)" :config="{format: 'DD-MM-YYYY hh:mm'}"></date-picker>
            </div>
          </div>
        </form>

        <form v-if="validation === 1" class="was-validated" novalidate>
          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="contractor">Contractor NIP</label>
              <select class="custom-select d-block w-100" id="contractor" v-model="contractor" required>
                <option :value="null">Choose...</option>
                <option v-for="contractor in contractors" :value="contractor" :key="contractor.id">
                  <option>{{contractor.nip}}</option>
                </option>
              </select>
              <div class="invalid-feedback">
                Please choose a contractor.
              </div>
            </div>

            <div class="col-md-6 mb-3">
              <label for="status">Status</label>
              <select class="custom-select d-block w-100" id="status" v-model="status" required>
                <option :value="null">Choose...</option>
                <option v-for="status in statuses" :value="status" :key="status.name">
                  <option>{{status.status}}</option>
                </option>
              </select>
              <div class="invalid-feedback">
                Please choose a status.
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="status">implementation date</label>
              <date-picker v-model="implementationDate" @dp-change="changeImplementationDate(implementationDate)" :config="{format: 'DD-MM-YYYY hh:mm'}"></date-picker>
            </div>
            <div class="col-md-6 mb-3">
              <label for="status">Date of placing the order</label>
              <date-picker v-model="dateOfPlacingTheOrder" @dp-change="changeDateOfPlacingTheOrder(dateOfPlacingTheOrder)" :config="{format: 'DD-MM-YYYY hh:mm'}"></date-picker>
            </div>
          </div>
        </form>

        <div class="mb-5 float-right">
          <button @click=addRow() class="btn btn-primary">Add new product</button>
        </div>

        <form v-if="validation === 0" class="needs-validation" novalidate>
          <table class="table table-hover">
            <thead class="thead-light">
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Quantity</th>
                <th scope="col">Price</th>
                <th scope="col">Total price</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, index) in rows" v-bind:key="row.id">
                <td class="align-middle">
                  <select class="custom-select d-block w-100" id="" v-model="row.id" @change="updateProduct(row.id, index)" required>
                    <option v-for="product in products" :value="product" :key="product.id">
                      <option>{{product.name}}</option>
                    </option>
                  </select>
                </td>

                <td>
                  <input type="number" min="1" oninput="this.value = !!this.value && Math.abs(this.value) >= 1 ? Math.abs(this.value) : null" class="form-control" id="quantityid" placeholder="" v-model="row.quantity" required>
                </td>

                <td class="align-middle">
                  {{row.price}}
                </td>

                <td class="align-middle" v-if="row.price">
                  {{(row.price * row.quantity).toFixed(2)}}
                </td>
                <td v-else>
                </td>

                <td class="align-middle">
                  <button @click=removeRow(index)>
                    <svg id="i-trash" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="18" height="18" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
                      <path d="M28 6 L6 6 8 30 24 30 26 6 4 6 M16 12 L16 24 M21 12 L20 24 M11 12 L12 24 M12 6 L13 2 19 2 20 6" />
                    </svg>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </form>

        <form v-if="validation === 1" class="was-validated" novalidate>
          <table class="table table-hover">
            <thead class="thead-light">
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Quantity</th>
                <th scope="col">Price</th>
                <th scope="col">Total price</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, index) in rows" v-bind:key="row.id">
                <td class="align-middle">
                  <select class="custom-select d-block w-100" id="" v-model="row.id" @change="updateProduct(row.id, index)" required>
                    <option v-for="product in products" :value="product" :key="product.id">
                      <option>{{product.name}}</option>
                    </option>
                  </select>
                </td>

                <td>
                  <input type="number" min="1" oninput="this.value = !!this.value && Math.abs(this.value) >= 1 ? Math.abs(this.value) : null" class="form-control" id="quantityid" placeholder="" v-model="row.quantity" required>
                </td>

                <td class="align-middle">
                  {{row.price}}
                </td>

                <td class="align-middle" v-if="row.price">
                  {{(row.price * row.quantity).toFixed(2)}}
                </td>
                <td v-else>
                </td>

                <td class="align-middle">
                  <button @click=removeRow(index)>
                    <svg id="i-trash" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="18" height="18" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
                      <path d="M28 6 L6 6 8 30 24 30 26 6 4 6 M16 12 L16 24 M21 12 L20 24 M11 12 L12 24 M12 6 L13 2 19 2 20 6" />
                    </svg>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </form>

        <div class="mb-5 float-right">
          <button @click=postOrder() class="btn btn-primary">Save the order</button>
        </div>
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

  // Import this component
  import datePicker from 'vue-bootstrap-datetimepicker';

  // Import date picker css
  import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css';
  import moment from 'moment';
  import axios from 'axios';

  export default {
    name: 'NewOrder',
    data() {
      return {
        validation: 0,
        contractor: null,
        status: null,
        rows: [
          {
            "name": null,
            "quantity": null,
            "price": null,
            "product_id": null
          }
        ],
        implementationDate: moment().format('DD-MM-YYYY hh:mm'),
        dateOfPlacingTheOrder: moment().format('DD-MM-YYYY hh:mm'),
        configs: {
          basic: {
            // https://momentjs.com/docs/#/displaying/format/
            format: 'DD-MM-YYYY hh:mm'
          }
        },
        options: {
          format: 'DD-MM-YYYY hh:mm'
        },
        contractors: [
          {
            "name": "Johnny",
            "nip": "3829473912",
            "address": "3528  Hampton Meadows"
          },
          {
            "name": "Joe",
            "nip": "3927438104",
            "address": "4780  Meadow Lane"
          },
          {
            "name": "Alice",
            "nip": "9378194273",
            "address": "1708  Henry Ford Avenue"
          }
        ],
        statuses: [
          {
            "status": "Submitted"
          },
          {
            "status": "Not submitted"
          }
        ],
        products: [
          {
            "name": "Banana",
            "price": "1.93",
            "product_id": 0
          },
          {
            "name": "Apple",
            "price": "4.43",
            "product_id": 1
          },
          {
            "name": "Carrot",
            "price": "3",
            "product_id": 2
          }
        ]
      };
    },
    components: {
      datePicker
    },
    created: function() {
    },
    methods: {
      addRow() {
        this.rows.push({
          "name": null,
          "quantity": null,
          "price": null,
          "product_id": null
        });
      },
      removeRow: function(index){
        this.rows.splice(index, 1)
      },
      changeDateOfPlacingTheOrder(date) {
        this.dateOfPlacingTheOrder = date;
      },
      changeImplementationDate(date) {
        this.implementationDate = date;
      },
      updateProduct(product, index) {
        this.rows[index].name = JSON.parse(JSON.stringify(product.name))
        this.rows[index].price = JSON.parse(JSON.stringify(product.price))
        this.rows[index].product_id = JSON.parse(JSON.stringify(product.product_id))
      },
      postOrder() {

        this.validation = 1

        var products = []
        var i

        for (i = 0; i < this.rows.length; i++) {
          var product = {
            "name": this.rows[i].name,
            "quantity": this.rows[i].quantity,
            "price": this.rows[i].price,
            "product_id": this.rows[i].product_id
          }
          products.push(product)
        }

        axios
        .post('http://127.0.0.1:8000/api/orders/', {
            'contractor_id': {
              "name": this.contractor.name,
              "nip": this.contractor.nip,
              "address": this.contractor.address
            },
            "number": 23,
            "implementation_date": this.implementationDate,
            "data_of_placing_the_order": this.dateOfPlacingTheOrder,
            "status": this.status.status,
            "products": products
        })
        .then(res => {
          var data = res.data
          console.log(res)
          this.$notify({
            group: 'alertSuccess',
            type: 'success',
            title: 'New order.',
            text: 'New order has been added succesfully.'
          });

          //store order id
          localStorage.setItem('orderId', JSON.parse(data.id))

          //move to the edit view
          window.location = 'http://127.0.0.1:8081/editorder/'
        })
        .catch(error => {
          console.log(error.response.data);
          this.$notify({
            group: 'alertDanger',
            type: 'error',
            title: 'New order.',
            text: 'Adding new order failed.'
          });
        })
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
  /* remove validation icons */
  .was-validated .custom-select:valid {
    background-image: none;
  }
  .was-validated .custom-select:invalid {
    background-image: none;
  }
  .form-control.is-invalid, .was-validated .form-control:invalid {
      background-image: none;
  }
  .form-control.is-valid, .was-validated .form-control:valid {
      background-image: none;
  }
</style>
