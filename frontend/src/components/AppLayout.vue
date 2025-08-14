<script setup>
import { 
  NLayout, 
  NLayoutHeader, 
  NLayoutSider, 
  NLayoutContent, 
  NLayoutFooter,
  NDivider,
  NBreadcrumb,
  NBreadcrumbItem,
  NSpace,
  NButton,
  NIcon,
  NText,
  NMenu,
  NAvatar,
  NDropdown,
  NBadge,
  NH1,
  NPopover
} from 'naive-ui'
import { 
  SparklesOutline,
  SearchOutline,
  NotificationsOutline,
  AddOutline,
  BookOutline,
  GridOutline,
  TrendingUpOutline,
  CalendarOutline,
  PersonOutline,
  LogOutOutline,
  SunnyOutline,
  MoonOutline
} from '@vicons/ionicons5'
import { useRouter, useRoute } from 'vue-router'
import { computed, ref, h, inject } from 'vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

// Inject theme from parent component
const theme = inject('theme', { isDark: ref(false), toggleTheme: () => {} })

const collapsed = ref(false)
const activeKey = ref('dashboard')

// Menu options using Naive UI's built-in structure
const menuOptions = [
  {
    label: 'Dashboard',
    key: 'dashboard',
    icon: () => h(GridOutline),
    path: '/dashboard'
  },
  {
    label: 'Journal',
    key: 'journal',
    icon: () => h(BookOutline),
    children: [
      {
        label: 'View Journal',
        key: 'journal-list',
        icon: () => h(BookOutline),
        path: '/journal'
      },
      {
        label: 'New Entry',
        key: 'journal-new',
        icon: () => h(AddOutline),
        path: '/journal/new'
      }
    ]
  },
  {
    label: 'Analytics',
    key: 'analytics',
    icon: () => h(TrendingUpOutline),
    path: '/analytics'
  },
  {
    label: 'Calendar',
    key: 'calendar',
    icon: () => h(CalendarOutline),
    path: '/calendar'
  },
  {
    label: 'Help & Support',
    key: 'help',
    icon: () => h(PersonOutline),
    href: 'https://help.wdtdg.com',
    children: [
      {
        label: 'Documentation',
        key: 'docs',
        icon: () => h(BookOutline),
        href: 'https://docs.wdtdg.com'
      },
      {
        label: 'Contact Support',
        key: 'contact',
        icon: () => h(PersonOutline),
        href: 'mailto:support@wdtdg.com'
      }
    ]
  }
]

// User menu options
const userMenuOptions = [
  {
    label: 'Profile',
    key: 'profile',
    icon: () => h(PersonOutline)
  },
  {
    label: 'Logout',
    key: 'logout',
    icon: () => h(LogOutOutline)
  }
]

// Breadcrumb items
const breadcrumbItems = computed(() => {
  const items = [
    { label: 'Home', path: '/' }
  ]
  
  if (route.path === '/dashboard') {
    items.push({ label: 'Dashboard', path: '/dashboard' })
  } else if (route.path.startsWith('/journal')) {
    items.push({ label: 'Journal', path: '/journal' })
    if (route.path === '/journal/new') {
      items.push({ label: 'New', path: '/journal/new' })
    } else if (route.path.includes('/edit/')) {
      items.push({ label: 'Edit', path: route.path })
    }
  }
  
  return items
})

// Get current page title
const currentPageTitle = computed(() => {
  if (route.path === '/') return 'Home'
  if (route.path === '/journal') return 'Journal Entries'
  if (route.path === '/journal/new') return 'New Journal Entry'
  if (route.path.includes('/journal/edit/')) return 'Edit Journal Entry'
  
  const pathSegments = route.path.split('/').filter(Boolean)
  return pathSegments[pathSegments.length - 1]
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ')
})

// Notifications count (mock data)
const notificationsCount = ref(3)

// Navigation functions
const goHome = () => router.push('/')
const createNewEntry = () => router.push('/journal/new')

const handleMenuSelect = (key) => {
  activeKey.value = key
  const menuItem = findMenuItemByKey(menuOptions, key)
  if (menuItem?.path) {
    router.push(menuItem.path)
  }
}

const handleUserMenuSelect = (key) => {
  if (key === 'logout') {
    authStore.logout()
    router.push('/')
  }
}

// Handle sidebar collapse/expand
const handleSidebarCollapse = (collapsedState) => {
  collapsed.value = collapsedState
}

// Helper function to find menu item by key
const findMenuItemByKey = (items, key) => {
  for (const item of items) {
    if (item.key === key) return item
    if (item.children) {
      const found = findMenuItemByKey(item.children, key)
      if (found) return found
    }
  }
  return null
}

// Render functions for menu
const renderLabel = (option) => {
  return option.label;
}

const renderIcon = (option) => {
  return option.icon();
}
</script>

<template>
<n-space vertical>
  <n-layout>
    <!-- Header -->
    <n-layout-header style="height: 64px; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--n-border-color);">
      <!-- Left side: Logo and breadcrumb -->
      <n-space align="center" size="medium">
        <n-space align="center" size="small" style="cursor: pointer; padding: 8px; border-radius: 8px;" @click="goHome">
          <n-icon size="24" color="#18a058">
            <SparklesOutline />
          </n-icon>
          <n-text strong style="font-size: 18px; color: #18a058;">WDTDG</n-text>
        </n-space>
        
        <n-divider vertical />
        
        <n-breadcrumb>
          <n-breadcrumb-item 
            v-for="(item, index) in breadcrumbItems" 
            :key="index"
            @click="router.push(item.path)"
            style="cursor: pointer;"
            :style="{ color: index < breadcrumbItems.length - 1 ? 'var(--n-primary-color)' : 'inherit' }"
          >
            {{ item.label }}
          </n-breadcrumb-item>
        </n-breadcrumb>
      </n-space>
      
      <!-- Right side: Actions and user menu -->
      <n-space size="medium">
        <!-- Search button -->
        <n-button quaternary circle>
          <template #icon>
            <n-icon><SearchOutline /></n-icon>
          </template>
        </n-button>
        
        <!-- Notifications -->
        <n-button quaternary circle>
          <template #icon>
            <n-badge :value="notificationsCount" :max="99">
              <n-icon><NotificationsOutline /></n-icon>
            </n-badge>
          </template>
        </n-button>
        
        <!-- Quick actions -->
        <n-button @click="createNewEntry" type="primary">
          <template #icon>
            <n-icon><AddOutline /></n-icon>
          </template>
          New Entry
        </n-button>
        
        <!-- Theme toggle -->
        <n-button 
          quaternary 
          circle 
          @click="theme.toggleTheme"
          :title="theme.isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode'"
        >
          <template #icon>
            <n-icon>
              <SunnyOutline v-if="theme.isDark" />
              <MoonOutline v-else />
            </n-icon>
          </template>
        </n-button>
        
        <!-- User menu -->
        <n-dropdown 
          :options="userMenuOptions" 
          @select="handleUserMenuSelect"
          trigger="click"
          placement="bottom-end"
        >
          <n-space align="center" size="small" style="cursor: pointer; padding: 8px; border-radius: 8px;">
            <n-avatar 
              round 
              size="medium"
              :src="authStore.user?.avatar"
              fallback-src="https://07akioni.icu/28"
            />
            <n-text>
              {{ authStore.user?.username || 'User' }}
            </n-text>
          </n-space>
        </n-dropdown>
      </n-space>
    </n-layout-header>

    <n-layout has-sider>
      <!-- Sidebar -->
      <n-layout-sider 
        :collapsed="collapsed"
        show-trigger
        @collapse="handleSidebarCollapse(true)"
        @expand="handleSidebarCollapse(false)"
        style="border-right: 1px solid var(--n-border-color);"
        collapse-mode="width"
      >
          <!-- Navigation Menu -->
          <n-menu
            :collapsed="collapsed"
            :options="menuOptions"
            @update:value="handleMenuSelect"
            :render-label="renderLabel"
            :render-icon="renderIcon"
            :collapsed-icon-size="22"
            :value="activeKey"
          />
      </n-layout-sider>

      <!-- Main content -->
      <n-layout-content>
        <div style="max-width: 1200px; margin: 0 auto; padding: 24px;">
          <n-space vertical size="large">
            <div style="padding-bottom: 24px; border-bottom: 1px solid var(--n-border-color);">
              <n-h1 style="font-size: 2rem; font-weight: 700; margin: 0 0 8px 0;">
                {{ currentPageTitle }}
              </n-h1>
              <n-text depth="3" style="font-size: 1rem; margin: 0;">
                {{ route.meta?.description || 'Manage your personal journal and reflections' }}
              </n-text>
            </div>
            <div>
              <slot />
            </div>
          </n-space>
        </div>
      </n-layout-content>
    </n-layout>

    <!-- Footer -->
    <n-layout-footer style="padding: 24px; border-top: 1px solid var(--n-border-color); background: var(--n-color);">
      <div style="max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center;">
        <n-text depth="3">© 2024 Where Did The Day Go? All rights reserved.</n-text>
        <n-space size="medium">
          <n-text depth="3" style="cursor: pointer;">Privacy Policy</n-text>
          <n-text depth="3" style="cursor: pointer;">Terms of Service</n-text>
          <n-text depth="3" style="cursor: pointer;">Support</n-text>
        </n-space>
      </div>
    </n-layout-footer>
  </n-layout>
</n-space>
</template>
