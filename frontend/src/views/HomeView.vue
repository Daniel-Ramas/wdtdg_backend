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
  NGrid,
  NGridItem,
  NDivider,
  NTag,
  useMessage
} from 'naive-ui'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { ref, computed, h, onMounted } from 'vue'
import { 
  MenuOutline, 
  PersonOutline, 
  LogOutOutline, 
  SettingsOutline, 
  BookOutline,
  SparklesOutline,
  ShieldCheckmarkOutline,
  TimeOutline,
  HeartOutline,
  TrendingUpOutline
} from '@vicons/ionicons5'

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
      message.info('Profile feature coming soon')
      break
    case 'settings':
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

// Animation states
const animatedElements = ref([])

onMounted(() => {
  // Trigger animations on mount
  setTimeout(() => {
    animatedElements.value = ['hero', 'features', 'stats', 'cta']
  }, 100)
})
</script>

<template>
  <n-layout class="landing-page">
    <!-- Header -->
    <n-layout-header class="header">
      <div class="header-content">
        <div class="logo-section">
          <n-icon size="32" class="logo-icon">
            <SparklesOutline />
          </n-icon>
          <n-h1 class="logo-text">Where Did The Day Go?</n-h1>
        </div>
        
        <n-space class="header-actions">
          <n-button @click="goToJournal" type="primary" v-if="authStore.isAuthenticated" class="journal-btn">
            <template #icon>
              <n-icon><BookOutline /></n-icon>
            </template>
            My Journal
          </n-button>
          
          <!-- Menu dropdown -->
          <n-dropdown 
            :options="menuOptions" 
            @select="handleMenuSelect"
            trigger="click"
            placement="bottom-end"
          >
            <n-button quaternary class="menu-btn">
              <template #icon>
                <n-icon>
                  <MenuOutline />
                </n-icon>
              </template>
              {{ authStore.isAuthenticated ? 'Menu' : 'Account' }}
            </n-button>
          </n-dropdown>
        </n-space>
      </div>
    </n-layout-header>
    
    <n-layout-content class="main-content">
      <!-- Hero Section -->
      <section class="hero-section" :class="{ 'animate-in': animatedElements.includes('hero') }">
        <div class="hero-content">
          <div class="hero-text">
            <n-tag type="success" size="large" class="hero-badge">
              <template #icon>
                <n-icon><TrendingUpOutline /></n-icon>
              </template>
              Transform Your Daily Reflection
            </n-tag>
            
            <n-h1 class="hero-title">
              Capture Life's Moments
              <span class="highlight">One Day at a Time</span>
            </n-h1>
            
            <n-p class="hero-subtitle">
              Transform your daily experiences into meaningful insights with our intelligent journaling platform. 
              Whether it's a fleeting thought or a life-changing moment, preserve it in the way that feels most natural to you.
            </n-p>
            
            <n-space class="hero-actions">
              <n-button @click="goToJournal" type="primary" size="large" v-if="authStore.isAuthenticated" class="cta-button">
                <template #icon>
                  <n-icon><BookOutline /></n-icon>
                </template>
                Start Journaling
              </n-button>
              <n-button @click="goToLogin" type="primary" size="large" v-else class="cta-button">
                <template #icon>
                  <n-icon><PersonOutline /></n-icon>
                </template>
                Get Started Free
              </n-button>
              
              <n-button quaternary size="large" class="demo-button">
                <template #icon>
                  <n-icon><TimeOutline /></n-icon>
                </template>
                Watch Demo
              </n-button>
            </n-space>
          </div>
          
          <div class="hero-visual">
            <div class="floating-card card-1">
              <n-icon size="24"><BookOutline /></n-icon>
              <span>Daily thoughts</span>
            </div>
            <div class="floating-card card-2">
              <n-icon size="24"><HeartOutline /></n-icon>
              <span>Memories</span>
            </div>
            <div class="floating-card card-3">
              <n-icon size="24"><TrendingUpOutline /></n-icon>
              <span>Growth</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Features Section -->
      <section class="features-section" :class="{ 'animate-in': animatedElements.includes('features') }">
        <div class="section-header">
          <n-h2 class="section-title">Why Choose Our Platform?</n-h2>
          <n-p class="section-subtitle">
            Built with modern technology and user experience in mind
          </n-p>
        </div>
        
        <n-grid :cols="3" :x-gap="24" :y-gap="24" class="features-grid">
          <n-grid-item>
            <n-card class="feature-card">
              <div class="feature-icon">
                <n-icon size="48"><BookOutline /></n-icon>
              </div>
              <n-h3 class="feature-title">Multi-Format Journaling</n-h3>
              <n-p class="feature-description">
                Write, record, or capture your thoughts in text, voice, photos, and videos. 
                Express yourself in the way that feels most natural.
              </n-p>
            </n-card>
          </n-grid-item>
          
          <n-grid-item>
            <n-card class="feature-card">
              <div class="feature-icon">
                <n-icon size="48"><ShieldCheckmarkOutline /></n-icon>
              </div>
              <n-h3 class="feature-title">Privacy First</n-h3>
              <n-p class="feature-description">
                Your personal thoughts and memories are encrypted and secure. 
                We believe in protecting your privacy above all else.
              </n-p>
            </n-card>
          </n-grid-item>
          
          <n-grid-item>
            <n-card class="feature-card">
              <div class="feature-icon">
                <n-icon size="48"><TrendingUpOutline /></n-icon>
              </div>
              <n-h3 class="feature-title">Insightful Analytics</n-h3>
              <n-p class="feature-description">
                Discover patterns in your thoughts and emotions over time. 
                Gain deeper insights into your personal growth journey.
              </n-p>
            </n-card>
          </n-grid-item>
        </n-grid>
      </section>

      <!-- Stats Section -->
      <section class="stats-section" :class="{ 'animate-in': animatedElements.includes('stats') }">
        <n-grid :cols="4" :x-gap="24" class="stats-grid">
          <n-grid-item>
            <div class="stat-item">
              <n-h2 class="stat-number">10K+</n-h2>
              <n-text class="stat-label">Active Users</n-text>
            </div>
          </n-grid-item>
          
          <n-grid-item>
            <div class="stat-item">
              <n-h2 class="stat-number">1M+</n-h2>
              <n-text class="stat-label">Journal Entries</n-text>
            </div>
          </n-grid-item>
          
          <n-grid-item>
            <div class="stat-item">
              <n-h2 class="stat-number">99.9%</n-h2>
              <n-text class="stat-label">Uptime</n-text>
            </div>
          </n-grid-item>
          
          <n-grid-item>
            <div class="stat-item">
              <n-h2 class="stat-number">24/7</n-h2>
              <n-text class="stat-label">Support</n-text>
            </div>
          </n-grid-item>
        </n-grid>
      </section>

      <!-- CTA Section -->
      <section class="cta-section" :class="{ 'animate-in': animatedElements.includes('cta') }">
        <n-card class="cta-card">
          <div class="cta-content">
            <n-h2 class="cta-title">Ready to Start Your Journey?</n-h2>
            <n-p class="cta-subtitle">
              Join thousands of users who are already transforming their daily reflections into meaningful insights.
            </n-p>
            
            <n-space class="cta-actions">
              <n-button @click="goToLogin" type="primary" size="large" v-if="!authStore.isAuthenticated" class="cta-button">
                <template #icon>
                  <n-icon><PersonOutline /></n-icon>
                </template>
                Create Free Account
              </n-button>
              <n-button @click="goToJournal" type="primary" size="large" v-else class="cta-button">
                <template #icon>
                  <n-icon><BookOutline /></n-icon>
                </template>
                Continue Journaling
              </n-button>
            </n-space>
          </div>
        </n-card>
      </section>
    </n-layout-content>
  </n-layout>
</template>

<style scoped>
.landing-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

/* Header Styles */
.header {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 16px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-icon {
  color: #18a058;
}

.logo-text {
  margin: 0;
  font-size: 24px;
  font-weight: 700;
  background: linear-gradient(135deg, #18a058 0%, #36ad6a 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.header-actions {
  gap: 16px;
}

.journal-btn {
  background: linear-gradient(135deg, #18a058 0%, #36ad6a 100%);
  border: none;
  box-shadow: 0 4px 15px rgba(24, 160, 88, 0.3);
}

.menu-btn {
  border: 1px solid rgba(0, 0, 0, 0.1);
  background: rgba(255, 255, 255, 0.8);
}

/* Main Content */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

/* Hero Section */
.hero-section {
  padding: 80px 0;
  text-align: center;
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s ease;
}

.hero-section.animate-in {
  opacity: 1;
  transform: translateY(0);
}

.hero-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.hero-text {
  text-align: left;
}

.hero-badge {
  margin-bottom: 24px;
  font-weight: 600;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  line-height: 1.1;
  margin: 24px 0;
  color: #1a1a1a;
}

.highlight {
  background: linear-gradient(135deg, #18a058 0%, #36ad6a 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 1.25rem;
  line-height: 1.6;
  color: #666;
  margin: 24px 0 40px 0;
  max-width: 500px;
}

.hero-actions {
  gap: 16px;
}

.cta-button {
  background: linear-gradient(135deg, #18a058 0%, #36ad6a 100%);
  border: none;
  box-shadow: 0 4px 20px rgba(24, 160, 88, 0.4);
  font-weight: 600;
  padding: 16px 32px;
}

.demo-button {
  border: 2px solid #18a058;
  color: #18a058;
  font-weight: 600;
  padding: 16px 32px;
}

/* Hero Visual */
.hero-visual {
  position: relative;
  height: 400px;
}

.floating-card {
  position: absolute;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 16px;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  animation: float 6s ease-in-out infinite;
}

.floating-card:nth-child(1) {
  top: 20%;
  left: 10%;
  animation-delay: 0s;
}

.floating-card:nth-child(2) {
  top: 50%;
  right: 20%;
  animation-delay: 2s;
}

.floating-card:nth-child(3) {
  bottom: 20%;
  left: 30%;
  animation-delay: 4s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}

/* Features Section */
.features-section {
  padding: 80px 0;
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s ease 0.2s;
}

.features-section.animate-in {
  opacity: 1;
  transform: translateY(0);
}

.section-header {
  text-align: center;
  margin-bottom: 60px;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 16px 0;
}

.section-subtitle {
  font-size: 1.125rem;
  color: #666;
  margin: 0;
}

.features-grid {
  margin-top: 40px;
}

.feature-card {
  height: 100%;
  text-align: center;
  border: none;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.15);
}

.feature-icon {
  margin-bottom: 24px;
  color: #18a058;
}

.feature-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 16px 0;
}

.feature-description {
  color: #666;
  line-height: 1.6;
  margin: 0;
}

/* Stats Section */
.stats-section {
  padding: 80px 0;
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s ease 0.4s;
}

.stats-section.animate-in {
  opacity: 1;
  transform: translateY(0);
}

.stats-grid {
  text-align: center;
}

.stat-item {
  padding: 32px 16px;
}

.stat-number {
  font-size: 3rem;
  font-weight: 800;
  color: #18a058;
  margin: 0 0 8px 0;
  background: linear-gradient(135deg, #18a058 0%, #36ad6a 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-label {
  font-size: 1.125rem;
  color: #666;
  font-weight: 500;
}

/* CTA Section */
.cta-section {
  padding: 80px 0;
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s ease 0.6s;
}

.cta-section.animate-in {
  opacity: 1;
  transform: translateY(0);
}

.cta-card {
  background: linear-gradient(135deg, #18a058 0%, #36ad6a 100%);
  border: none;
  border-radius: 24px;
  box-shadow: 0 16px 48px rgba(24, 160, 88, 0.3);
}

.cta-content {
  text-align: center;
  color: white;
}

.cta-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0 0 16px 0;
  color: white;
}

.cta-subtitle {
  font-size: 1.25rem;
  margin: 0 0 40px 0;
  opacity: 0.9;
  color: white;
}

.cta-actions {
  justify-content: center;
}

.cta-button {
  background: white;
  color: #18a058;
  border: none;
  font-weight: 600;
  padding: 16px 32px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-content {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .header-content {
    flex-direction: column;
    gap: 16px;
  }
  
  .hero-actions {
    flex-direction: column;
    align-items: center;
  }
}
</style> 