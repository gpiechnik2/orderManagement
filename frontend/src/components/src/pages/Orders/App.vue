<template>
  <div id="app">
    <OrdersList />
  </div>
</template>

<script>
import OrdersList from '@/components/OrdersList.vue'

export default {
  name: 'app',
  components: {
    OrdersList
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
