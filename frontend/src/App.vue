<script setup>
import { NConfigProvider, NMessageProvider, NNotificationProvider, NDialogProvider, NLoadingBarProvider, NButton, NIcon, NSpace, darkTheme, lightTheme } from 'naive-ui'
import { ref, onMounted, computed } from 'vue'
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
            <div id="app" :class="{ 'dark-mode': isDark }">
              <!-- Theme Toggle Button -->
              <div class="theme-toggle">
                <n-button 
                  quaternary 
                  circle 
                  size="small"
                  @click="toggleTheme"
                  :title="isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode'"
                >
                  <template #icon>
                    <n-icon>
                      <SunnyOutline v-if="isDark" />
                      <MoonOutline v-else />
                    </n-icon>
                  </template>
                </n-button>
              </div>
              
              <router-view />
            </div>
          </n-message-provider>
        </n-notification-provider>
      </n-dialog-provider>
    </n-loading-bar-provider>
  </n-config-provider>
</template>

<style>
#app {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100vh;
}

.theme-toggle {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 9999;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  transition: background-color 0.3s ease;
  background-color: #ffffff;
}

/* Dark mode body background */
body.dark-mode {
  background-color: #1a1a1a;
}


</style>
