<template>
  <div id="app">
    <NewOrder />
  </div>
</template>

<script>
import NewOrder from '@/components/NewOrder.vue'

export default {
  name: 'app',
  components: {
    NewOrder
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
