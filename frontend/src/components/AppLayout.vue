<script setup>
import { 
  NLayout, 
  NLayoutHeader, 
  NLayoutSider, 
  NLayoutContent, 
  NLayoutFooter,
  NButton, 
  NSpace, 
  NText, 
  NH1, 
  NMenu,
  NDropdown,
  NIcon,
  NAvatar,
  NBreadcrumb,
  NBreadcrumbItem,
  NDivider,
  NBadge,
  useMessage,
  useDialog
} from 'naive-ui'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { ref, computed, h, onMounted } from 'vue'
import { 
  MenuOutline, 
  PersonOutline, 
  LogOutOutline, 
  SettingsOutline, 
  BookOutline,
  HomeOutline,
  SparklesOutline,
  NotificationsOutline,
  SearchOutline,
  AddOutline,
  CalendarOutline,
  StatsChartOutline,
  HelpCircleOutline
} from '@vicons/ionicons5'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()
const message = useMessage()
const dialog = useDialog()

// Sidebar collapsed state
const collapsed = ref(false)
const sidebarWidth = computed(() => collapsed.value ? 64 : 240)

// Navigation menu items
const menuItems = [
  {
    label: 'Dashboard',
    key: 'dashboard',
    icon: () => h(HomeOutline),
    path: '/dashboard'
  },
  {
    label: 'Journal',
    key: 'journal',
    icon: () => h(BookOutline),
    children: [
      {
        label: 'All Entries',
        key: 'journal-list',
        path: '/journal'
      },
      {
        label: 'New Entry',
        key: 'journal-new',
        path: '/journal/new'
      },
      {
        label: 'Categories',
        key: 'journal-categories',
        path: '/journal/categories'
      }
    ]
  },
  {
    label: 'Analytics',
    key: 'analytics',
    icon: () => h(StatsChartOutline),
    path: '/analytics'
  },
  {
    label: 'Calendar',
    key: 'calendar',
    icon: () => h(CalendarOutline),
    path: '/calendar'
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
    label: 'Settings',
    key: 'settings',
    icon: () => h(SettingsOutline)
  },
  {
    label: 'Help & Support',
    key: 'help',
    icon: () => h(HelpCircleOutline)
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

// Breadcrumb items
const breadcrumbItems = computed(() => {
  const items = [
    { label: 'Home', path: '/' }
  ]
  
  if (route.path !== '/') {
    const pathSegments = route.path.split('/').filter(Boolean)
    let currentPath = ''
    
    pathSegments.forEach((segment, index) => {
      currentPath += `/${segment}`
      const label = segment.charAt(0).toUpperCase() + segment.slice(1)
      items.push({ label, path: currentPath })
    })
  }
  
  return items
})

// Navigation handlers
const handleMenuSelect = (key) => {
  const menuItem = findMenuItemByKey(menuItems, key)
  if (menuItem && menuItem.path) {
    router.push(menuItem.path)
  }
}

const handleUserMenuSelect = (key) => {
  switch (key) {
    case 'profile':
      message.info('Profile feature coming soon')
      break
    case 'settings':
      message.info('Settings feature coming soon')
      break
    case 'help':
      message.info('Help & Support feature coming soon')
      break
    case 'logout':
      handleLogout()
      break
  }
}

const handleLogout = () => {
  dialog.warning({
    title: 'Confirm Logout',
    content: 'Are you sure you want to logout?',
    positiveText: 'Logout',
    negativeText: 'Cancel',
    onPositiveClick: () => {
      authStore.logout()
      message.success('Logged out successfully')
      router.push('/')
    }
  })
}

const goHome = () => {
  router.push('/')
}

const goToJournal = () => {
  router.push('/journal')
}

const createNewEntry = () => {
  router.push('/journal/new')
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
</script>

<template>
  <n-layout class="app-layout">
    <!-- Header -->
    <n-layout-header class="header">
      <div class="header-content">
        <!-- Left side: Logo and breadcrumb -->
        <div class="header-left">
          <div class="logo-section" @click="goHome">
            <n-icon size="24" class="logo-icon">
              <SparklesOutline />
            </n-icon>
            <n-text class="logo-text" v-if="!collapsed">WDTDG</n-text>
          </div>
          
          <n-divider vertical />
          
          <n-breadcrumb class="breadcrumb">
            <n-breadcrumb-item 
              v-for="(item, index) in breadcrumbItems" 
              :key="index"
              @click="router.push(item.path)"
              :class="{ 'clickable': index < breadcrumbItems.length - 1 }"
            >
              {{ item.label }}
            </n-breadcrumb-item>
          </n-breadcrumb>
        </div>
        
        <!-- Right side: Actions and user menu -->
        <div class="header-right">
          <n-space gap="16">
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
            <n-button @click="createNewEntry" type="primary" class="new-entry-btn">
              <template #icon>
                <n-icon><AddOutline /></n-icon>
              </template>
              New Entry
            </n-button>
            
            <!-- User menu -->
            <n-dropdown 
              :options="userMenuOptions" 
              @select="handleUserMenuSelect"
              trigger="click"
              placement="bottom-end"
            >
              <div class="user-avatar">
                <n-avatar 
                  round 
                  size="medium"
                  :src="authStore.user?.avatar"
                  fallback-src="https://07akioni.icu/28"
                />
                <n-text class="user-name" v-if="!collapsed">
                  {{ authStore.user?.username || 'User' }}
                </n-text>
              </div>
            </n-dropdown>
          </n-space>
        </div>
      </div>
    </n-layout-header>
    
    <n-layout has-sider>
      <!-- Sidebar -->
      <n-layout-sider 
        :width="sidebarWidth" 
        :collapsed="collapsed"
        :collapsed-width="64"
        :show-trigger="true"
        collapse-mode="width"
        class="sidebar"
        @collapse="collapsed = true"
        @expand="collapsed = false"
      >
        <div class="sidebar-content">
          <!-- Navigation menu -->
          <n-menu
            :options="menuItems"
            :collapsed="collapsed"
            :collapsed-width="64"
            :collapsed-icon-size="22"
            mode="vertical"
            @update:value="handleMenuSelect"
            class="sidebar-menu"
          />
          
          <!-- Quick actions -->
          <div class="sidebar-actions" v-if="!collapsed">
            <n-divider />
            <n-space vertical size="small">
              <n-button 
                @click="goToJournal" 
                quaternary 
                block
                class="quick-action-btn"
              >
                <template #icon>
                  <n-icon><BookOutline /></n-icon>
                </template>
                View Journal
              </n-button>
              
              <n-button 
                @click="createNewEntry" 
                type="primary" 
                block
                class="quick-action-btn"
              >
                <template #icon>
                  <n-icon><AddOutline /></n-icon>
                </template>
                New Entry
              </n-button>
            </n-space>
          </div>
        </div>
      </n-layout-sider>
      
      <!-- Main content -->
      <n-layout-content class="main-content">
        <div class="content-wrapper">
          <!-- Page header -->
          <div class="page-header">
            <n-h1 class="page-title">{{ currentPageTitle }}</n-h1>
            <n-text class="page-subtitle" depth="3">
              {{ route.meta?.description || 'Manage your personal journal and reflections' }}
            </n-text>
          </div>
          
          <!-- Page content -->
          <div class="page-content">
            <slot />
          </div>
        </div>
      </n-layout-content>
    </n-layout>
    
    <!-- Footer -->
    <n-layout-footer class="footer">
      <div class="footer-content">
        <n-text depth="3" size="small">
          © 2024 Where Did The Day Go? All rights reserved.
        </n-text>
        <n-space size="small">
          <n-text depth="3" size="small" class="footer-link">Privacy Policy</n-text>
          <n-text depth="3" size="small" class="footer-link">Terms of Service</n-text>
          <n-text depth="3" size="small" class="footer-link">Support</n-text>
        </n-space>
      </div>
    </n-layout-footer>
  </n-layout>
</template>

<style scoped>
.app-layout {
  height: 100vh;
  background: #f8f9fa;
}

/* Header Styles */
.header {
  background: #ffffff;
  border-bottom: 1px solid #e9ecef;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.header-content {
  height: 64px;
  padding: 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 16px;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  padding: 8px;
  border-radius: 8px;
  transition: background-color 0.2s ease;
}

.logo-section:hover {
  background-color: #f8f9fa;
}

.logo-icon {
  color: #18a058;
}

.logo-text {
  font-weight: 700;
  font-size: 18px;
  color: #18a058;
}

.breadcrumb {
  font-size: 14px;
}

.breadcrumb .clickable {
  cursor: pointer;
  color: #6c757d;
}

.breadcrumb .clickable:hover {
  color: #18a058;
}

.header-right {
  display: flex;
  align-items: center;
}

.new-entry-btn {
  background: linear-gradient(135deg, #18a058 0%, #36ad6a 100%);
  border: none;
  box-shadow: 0 2px 8px rgba(24, 160, 88, 0.2);
}

.user-avatar {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  padding: 8px;
  border-radius: 8px;
  transition: background-color 0.2s ease;
}

.user-avatar:hover {
  background-color: #f8f9fa;
}

.user-name {
  font-weight: 500;
  color: #495057;
}

/* Sidebar Styles */
.sidebar {
  background: #ffffff;
  border-right: 1px solid #e9ecef;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.06);
}

.sidebar-content {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.sidebar-menu {
  flex: 1;
  border-right: none;
}

.sidebar-actions {
  padding: 16px;
}

.quick-action-btn {
  justify-content: flex-start;
  height: 40px;
}

/* Main Content Styles */
.main-content {
  background: #f8f9fa;
  padding: 24px;
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  margin-bottom: 32px;
  padding-bottom: 24px;
  border-bottom: 1px solid #e9ecef;
}

.page-title {
  font-size: 2rem;
  font-weight: 700;
  color: #212529;
  margin: 0 0 8px 0;
}

.page-subtitle {
  font-size: 1rem;
  margin: 0;
}

.page-content {
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  overflow: hidden;
}

/* Footer Styles */
.footer {
  background: #ffffff;
  border-top: 1px solid #e9ecef;
  padding: 16px 0;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-link {
  cursor: pointer;
  transition: color 0.2s ease;
}

.footer-link:hover {
  color: #18a058;
}

/* Responsive Design */
@media (max-width: 768px) {
  .header-content {
    padding: 0 16px;
  }
  
  .main-content {
    padding: 16px;
  }
  
  .footer-content {
    padding: 0 16px;
    flex-direction: column;
    gap: 8px;
    text-align: center;
  }
  
  .breadcrumb {
    display: none;
  }
  
  .user-name {
    display: none;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .app-layout {
    background: #1a1a1a;
  }
  
  .header,
  .sidebar,
  .page-content,
  .footer {
    background: #2d2d2d;
    border-color: #404040;
  }
  
  .page-title {
    color: #ffffff;
  }
  
  .user-name {
    color: #e9ecef;
  }
}
</style>
