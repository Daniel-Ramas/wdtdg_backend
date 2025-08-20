export default defineNuxtConfig({
  modules: [
    '@nuxt/ui'
  ],
  
  // UI configuration
  ui: {},
  css: ['~/assets/css/main.css'],
  // Color mode
  colorMode: {
    preference: 'dark',
    fallback: 'dark',
    classSuffix: ''
  }
})