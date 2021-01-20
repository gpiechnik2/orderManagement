<template>
  <div class="container">
    <h3>Orders:</h3>
    <div class="row justify-content-center">
      <div class="col-md-10 order-md-1">
        <div class="table-responsive">
          <table id="example" class="table table-hover">
            <thead class="thead-light">
              <tr class="align-middle">
                <th class="align-middle" scope="col">Nr</th>
                <th class="align-middle" scope="col">Contractor NIP</th>
                <th class="align-middle" scope="col">Implementation date</th>
                <th class="align-middle" scope="col">Data of placing the order</th>
                <th class="align-middle" scope="col">Status</th>
                <th class="align-middle" scope="col">Order value</th>
                <th class="align-middle no-sort" scope="col"></th>
                <th class="align-middle no-sort" scope="col"></th>
                <th class="align-middle no-sort" scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="order in orders" v-bind:key="order.id">
                <td class="align-middle" scope="row">{{order.id}}</td>
                <td class="align-middle">{{order.contractor_id.nip}}</td>
                <td class="align-middle">{{order.implementation_date}}</td>
                <td class="align-middle">{{order.data_of_placing_the_order}}</td>
                <td class="align-middle">{{order.status}}</td>
                <td class="align-middle">{{order.order_value}}</td>
                <td class="align-middle">
                  <button @click="seeOrder(order.id)">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M16 12C16 14.2091 14.2091 16 12 16C9.79086 16 8 14.2091 8 12C8 9.79086 9.79086 8 12 8C14.2091 8 16 9.79086 16 12ZM14 12C14 13.1046 13.1046 14 12 14C10.8954 14 10 13.1046 10 12C10 10.8954 10.8954 10 12 10C13.1046 10 14 10.8954 14 12Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3C17.5915 3 22.2898 6.82432 23.6219 12C22.2898 17.1757 17.5915 21 12 21C6.40848 21 1.71018 17.1757 0.378052 12C1.71018 6.82432 6.40848 3 12 3ZM12 19C7.52443 19 3.73132 16.0581 2.45723 12C3.73132 7.94186 7.52443 5 12 5C16.4756 5 20.2687 7.94186 21.5428 12C20.2687 16.0581 16.4756 19 12 19Z" fill="currentColor" />
                    </svg>
                  </button>
                </td>
                <td class="align-middle">
                  <button @click="editOrder(order.id)">
                    <svg id="i-edit" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="18" height="18" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
                      <path d="M30 7 L25 2 5 22 3 29 10 27 Z M21 6 L26 11 Z M5 22 L10 27 Z" />
                    </svg>
                  </button>
                </td>
                <td class="align-middle">
                  <button @click="deleteData(order.id)">
                    <svg id="i-trash" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="18" height="18" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
                      <path d="M28 6 L6 6 8 30 24 30 26 6 4 6 M16 12 L16 24 M21 12 L20 24 M11 12 L12 24 M12 6 L13 2 19 2 20 6" />
                    </svg>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>



    <footer class="my-5 pt-5 text-muted text-center text-small">
      <p class="mb-1">Orders management</p>
    </footer>

  </div>
</template>

<script>
  import axios from 'axios';

  // Include jquery
  const jQuery = require('jquery')
  // Make it available globally
  // DT editor seems to need this, so does the .vue component
  window.jQuery = jQuery

  // Include datatables and plugins
  require('datatables.net-bs4')

  export default {
    name: 'OrdersList',
    data() {
      return {
        orders: null,
      };
    },
    mounted: function() {

      //get orders
      axios
        .get('http://127.0.0.1:8000/api/orders/')
        .then(res => {
          this.orders = res.data;

          //update datatable
          setTimeout(this.updateJquery(), 4000);
        })
    },
    created: function() {

      //get orders
      axios
        .get('http://127.0.0.1:8000/api/orders/')
        .then(res => {
          this.orders = res.data;
        })
    },
    methods: {
        deleteData(id) {

          //delete order with specified id
          axios
            .delete('http://127.0.0.1:8000/api/orders/' + id)
            .then(res => {
              console.log(res)
              this.updateData()
            })
        },
        updateData() {

          //get data
          axios
            .get('http://127.0.0.1:8000/api/orders/')
            .then(res => {
              this.orders = res.data;
            })
        },
        seeOrder(id) {

          //store order id
          localStorage.setItem('orderId', JSON.parse(id))

          //move to the edit view
          window.location = 'http://127.0.0.1:8081/order/'

        },
        editOrder(id) {

          //store order id
          localStorage.setItem('orderId', JSON.parse(id))

          //move to the edit view
          window.location = 'http://127.0.0.1:8081/editorder/'

        },
        updateJquery() {

          //remove unwanted fields
          jQuery('#example').DataTable({
            "language": {
            "lengthMenu": "_MENU_"
            },
            "columnDefs": [{
            "targets": 'no-sort',
            "orderable": false
            }]
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
  div#example_length.dataTables_length {
    float: left;
    position: absolute;
    bottom: 0;
  }
  #example_length > label > select {
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    --blue: #007bff;
    --indigo: #6610f2;
    --purple: #6f42c1;
    --pink: #e83e8c;
    --red: #dc3545;
    --orange: #fd7e14;
    --yellow: #ffc107;
    --green: #28a745;
    --teal: #20c997;
    --cyan: #17a2b8;
    --white: #fff;
    --gray: #6c757d;
    --gray-dark: #343a40;
    --primary: #007bff;
    --secondary: #6c757d;
    --success: #28a745;
    --info: #17a2b8;
    --warning: #ffc107;
    --danger: #dc3545;
    --light: #f8f9fa;
    --dark: #343a40;
    --breakpoint-xs: 0;
    --breakpoint-sm: 576px;
    --breakpoint-md: 768px;
    --breakpoint-lg: 992px;
    --breakpoint-xl: 1200px;
    --font-family-sans-serif: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    --font-family-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    -webkit-font-smoothing: antialiased;
    box-sizing: border-box;
    margin: 0;
    font-family: inherit;
    text-transform: none;
    height: calc(1.5em + 0.75rem + 2px);
    padding: 0.375rem 1.75rem 0.375rem 0.75rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #495057;
    vertical-align: middle;
    background: #fff url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='4' height='5' viewBox='0 0 4 5'%3e%3cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") no-repeat right 0.75rem center/8px 10px;
    border: 1px solid #ced4da;
    border-radius: 0.25rem;
    appearance: none;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    display: block !important;
    width: 100% !important;
  }
  div#example_info.dataTables_info {
    float: left;
    align: middle;
    padding-top: 8px;
  }
  #example_filter > label > input {
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    --blue: #007bff;
    --indigo: #6610f2;
    --purple: #6f42c1;
    --pink: #e83e8c;
    --red: #dc3545;
    --orange: #fd7e14;
    --yellow: #ffc107;
    --green: #28a745;
    --teal: #20c997;
    --cyan: #17a2b8;
    --white: #fff;
    --gray: #6c757d;
    --gray-dark: #343a40;
    --primary: #007bff;
    --secondary: #6c757d;
    --success: #28a745;
    --info: #17a2b8;
    --warning: #ffc107;
    --danger: #dc3545;
    --light: #f8f9fa;
    --dark: #343a40;
    --breakpoint-xs: 0;
    --breakpoint-sm: 576px;
    --breakpoint-md: 768px;
    --breakpoint-lg: 992px;
    --breakpoint-xl: 1200px;
    --font-family-sans-serif: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    --font-family-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    -webkit-font-smoothing: antialiased;
    border-collapse: collapse;
    box-sizing: border-box;
    margin: 0;
    font-family: inherit;
    overflow: visible;
    display: block;
    width: 100%;
    height: calc(1.5em + 0.75rem + 2px);
    padding: 0.375rem 0.75rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #495057;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ced4da;
    border-radius: 0.25rem;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  }
  #example_wrapper > div:nth-child(1) > div:nth-child(2) {
  }
  #label#text {
    visibility: none;
  }
</style>
