<template>
  <div id="app">
    <EditOrder />
  </div>
</template>

<script>
import EditOrder from '@/components/EditOrder.vue'

export default {
  name: 'app',
  components: {
    EditOrder
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
