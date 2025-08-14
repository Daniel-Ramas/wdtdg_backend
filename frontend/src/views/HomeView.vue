<script setup>
import { 
  NLayout, 
  NLayoutHeader, 
  NLayoutContent, 
  NButton, 
  NSpace, 
  NCard, 
  NText, 
  NH1, 
  NP,
  NDropdown,
  NIcon,
  NAvatar,
  NMenu,
  useMessage
} from 'naive-ui'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { ref, computed, h } from 'vue'
import { MenuOutline, PersonOutline, LogOutOutline, SettingsOutline, BookOutline } from '@vicons/ionicons5'

const router = useRouter()
const authStore = useAuthStore()
const message = useMessage()

const goToJournal = () => {
  router.push('/journal')
}

const goToLogin = () => {
  router.push('/login')
}

const handleLogout = () => {
  authStore.logout()
  message.success('Logged out successfully')
  router.push('/')
}

const handleMenuSelect = (key) => {
  switch (key) {
    case 'profile':
      // TODO: Navigate to profile page
      message.info('Profile feature coming soon')
      break
    case 'settings':
      // TODO: Navigate to settings page
      message.info('Settings feature coming soon')
      break
    case 'journal':
      goToJournal()
      break
    case 'logout':
      handleLogout()
      break
  }
}

// Menu options for authenticated users
const authenticatedMenuOptions = [
  {
    label: 'Profile',
    key: 'profile',
    icon: () => h(PersonOutline)
  },
  {
    label: 'Settings',
    key: 'settings',
    icon: () => h(SettingsOutline)
  },
  {
    label: 'My Journal',
    key: 'journal',
    icon: () => h(BookOutline)
  },
  {
    type: 'divider'
  },
  {
    label: 'Logout',
    key: 'logout',
    icon: () => h(LogOutOutline)
  }
]

// Menu options for unauthenticated users
const unauthenticatedMenuOptions = [
  {
    label: 'Login',
    key: 'login',
    icon: () => h(PersonOutline)
  }
]

const menuOptions = computed(() => {
  return authStore.isAuthenticated ? authenticatedMenuOptions : unauthenticatedMenuOptions
})


</script>

<template>
  <n-layout>
    <n-layout-header style="height: 64px; padding: 16px; background: #fff; border-bottom: 1px solid #eee;">
      <n-space justify="space-between" align="center">
        <n-h1 style="margin: 0; font-size: 24px;">Where Did The Day Go?</n-h1>
        <n-space>
          <n-button @click="goToJournal" type="primary" v-if="authStore.isAuthenticated">
            My Journal
          </n-button>
          
          <!-- Menu dropdown -->
          <n-dropdown 
            :options="menuOptions" 
            @select="handleMenuSelect"
            trigger="click"
            placement="bottom-end"
          >
            <n-button quaternary>
              <template #icon>
                <n-icon>
                  <MenuOutline />
                </n-icon>
              </template>
              {{ authStore.isAuthenticated ? 'Menu' : 'Account' }}
            </n-button>
          </n-dropdown>
        </n-space>
      </n-space>
    </n-layout-header>
    
    <n-layout-content style="padding: 24px;">
      <n-card style="max-width: 800px; margin: 0 auto;">
        <n-space vertical size="large">
          <div>
            <n-h1>Welcome to Your Personal Journal</n-h1>
            <n-p>
              Track your daily thoughts, memories, and experiences with our intuitive journaling platform.
              Whether it's text, voice, photos, or videos, capture your moments in the way that feels most natural to you.
            </n-p>
          </div>
          
          <n-space vertical>
            <n-text strong>Features:</n-text>
            <n-space vertical>
              <n-text>📝 Text entries for your thoughts and reflections</n-text>
              <n-text>🎤 Voice recordings for spontaneous moments</n-text>
              <n-text>📸 Photo uploads to capture visual memories</n-text>
              <n-text>🎥 Video uploads for dynamic content</n-text>
              <n-text>🔒 Secure and private - your data stays yours</n-text>
            </n-space>
          </n-space>
          
          <n-space>
            <n-button @click="goToJournal" type="primary" size="large" v-if="authStore.isAuthenticated">
              Start Journaling
            </n-button>
            <n-button @click="goToLogin" type="primary" size="large" v-else>
              Get Started
            </n-button>
          </n-space>
        </n-space>
      </n-card>
    </n-layout-content>
  </n-layout>
</template>

<style scoped>
.n-layout-header {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
</style> 