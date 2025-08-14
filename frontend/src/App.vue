<script setup>
import { NConfigProvider, NMessageProvider, NNotificationProvider, NDialogProvider, NLoadingBarProvider, NButton, NIcon, NSpace, darkTheme, lightTheme } from 'naive-ui'
import { ref, onMounted, computed, provide } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { SunnyOutline, MoonOutline } from '@vicons/ionicons5'

const router = useRouter()
const authStore = useAuthStore()
const isDark = ref(false)

// Theme computed property
const theme = computed(() => isDark.value ? darkTheme : lightTheme)

// Toggle theme function
const toggleTheme = () => {
  isDark.value = !isDark.value
  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
}

// Provide theme toggle function to child components
provide('theme', {
  isDark,
  toggleTheme
})

onMounted(async () => {
  // Check authentication status when app starts
  await authStore.checkAuth()
  
  // Load saved theme preference
  const savedTheme = localStorage.getItem('theme')
  if (savedTheme) {
    isDark.value = savedTheme === 'dark'
  } else {
    // Check system preference
    isDark.value = window.matchMedia('(prefers-color-scheme: dark)').matches
  }
})
</script>

<template>
  <n-config-provider :theme="theme">
    <n-loading-bar-provider>
      <n-dialog-provider>
        <n-notification-provider>
          <n-message-provider>
            <div id="app" style="font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; height: 100vh;">
              <router-view />
            </div>
          </n-message-provider>
        </n-notification-provider>
      </n-dialog-provider>
    </n-loading-bar-provider>
  </n-config-provider>
</template>
