module.exports = {
  pages: {
    index: {
      entry: 'src/pages/Orders/main.js',
      template: 'public/index.html',
      title: 'Orders',
      chunks: ['chunk-vendors', 'chunk-common', 'index']
    },
    neworder: {
      entry: 'src/pages/NewOrder/main.js',
      template: 'public/index.html',
      title: 'New order',
      chunks: ['chunk-vendors', 'chunk-common', 'neworder']
    },
    order: {
      entry: 'src/pages/Order/main.js',
      template: 'public/index.html',
      title: 'Order',
      chunks: ['chunk-vendors', 'chunk-common', 'order']
    },
    editorder: {
      entry: 'src/pages/EditOrder/main.js',
      template: 'public/index.html',
      title: 'Edit order',
      chunks: ['chunk-vendors', 'chunk-common', 'editorder']
    }
  }
}
