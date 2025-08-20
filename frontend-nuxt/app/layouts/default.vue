<template>
  <UApp class="dark">
    <header class="bg-gray-800 border-b border-gray-700">
      <UContainer class="flex items-center justify-between py-4">
        <div class="flex items-center gap-2">
          <span class="text-white font-semibold text-lg">WDTG</span>
        </div>
      </UContainer>
    </header>

    <main class="min-h-screen">
      <UContainer class="py-10">
        <slot />
      </UContainer>
    </main>

    <footer class="bg-gray-800 border-t border-gray-700">
      <UContainer class="py-6 text-sm text-gray-400">
        © {{ new Date().getFullYear() }} WDtdg. All rights reserved.
      </UContainer>
    </footer>
  </UApp>
</template>

<script setup lang="ts">
// Force dark mode
useColorMode().preference = 'dark'
</script>


