<script setup>
import { 
  NTag, 
  NSpace, 
  NCard, 
  NText, 
  NButton,
  NIcon,
  NGrid,
  NGridItem,
  NH1,
  NH2,
  NH3,
  NDivider,
  NStatistic,
  NRow,
  NCol,
  NImage,
  NAvatar,
  NBadge
} from 'naive-ui'
import { 
  SparklesOutline,
  BookOutline, 
  HeartOutline, 
  TrendingUpOutline,
  ShieldCheckmarkOutline,
  TimeOutline,
  PersonOutline,
  PlayOutline,
  StarOutline,
  CheckmarkCircleOutline,
  GlobeOutline,
  LockClosedOutline
} from '@vicons/ionicons5'
import { useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

// Navigation functions
const goToDashboard = () => router.push('/dashboard')
const goToLogin = () => router.push('/login')
const goToDemo = () => {
  // Demo functionality - could open a modal or navigate to demo page
  console.log('Demo clicked')
}

// Stats data
const stats = [
  { label: 'Active Users', value: '10K+', icon: PersonOutline },
  { label: 'Journal Entries', value: '1M+', icon: BookOutline },
  { label: 'Uptime', value: '99.9%', icon: CheckmarkCircleOutline },
  { label: 'Support', value: '24/7', icon: GlobeOutline }
]

// Features data
const features = [
  {
    icon: BookOutline,
    title: 'Multi-Format Journaling',
    description: 'Write, record, or capture your thoughts in text, voice, photos, and videos. Express yourself naturally.',
    color: 'success'
  },
  {
    icon: ShieldCheckmarkOutline,
    title: 'Privacy First',
    description: 'Your personal thoughts are encrypted and secure. We protect your privacy above all else.',
    color: 'info'
  },
  {
    icon: TrendingUpOutline,
    title: 'Insightful Analytics',
    description: 'Discover patterns in your thoughts and emotions over time. Track your personal growth journey.',
    color: 'warning'
  }
]

// Testimonials data
const testimonials = [
  {
    name: 'Sarah Chen',
    role: 'Product Manager',
    content: 'This platform has transformed how I reflect on my daily experiences. The insights are incredible.',
    avatar: 'https://07akioni.icu/28'
  },
  {
    name: 'Marcus Rodriguez',
    role: 'Software Engineer',
    content: 'Finally, a journaling app that understands the importance of privacy and user experience.',
    avatar: 'https://07akioni.icu/29'
  },
  {
    name: 'Emma Thompson',
    role: 'Life Coach',
    content: 'I recommend this to all my clients. The analytics help them see patterns they never noticed.',
    avatar: 'https://07akioni.icu/30'
  }
]
</script>

<template>
  <div>
    <!-- Hero Section -->
    <section style="padding: 80px 0; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);">
      <div style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
        <n-grid :cols="2" :x-gap="80" align-items="center">
          <n-grid-item>
            <n-space vertical size="large">
              <!-- Badge -->
              <n-tag type="success" size="large" :bordered="false">
                <template #icon>
                  <n-icon><SparklesOutline /></n-icon>
                </template>
                Transform Your Daily Reflection
              </n-tag>
              
              <!-- Main Title -->
              <n-h1 style="font-size: 3.5rem; font-weight: 800; line-height: 1.1; margin: 0;">
                Capture Life's Moments
                <br>
                <span style="color: #18a058;">One Day at a Time</span>
              </n-h1>
              
              <!-- Subtitle -->
              <n-text depth="3" style="font-size: 1.25rem; line-height: 1.6; max-width: 500px;">
                Transform your daily experiences into meaningful insights with our intelligent journaling platform. 
                Whether it's a fleeting thought or a life-changing moment, preserve it in the way that feels most natural to you.
              </n-text>
              
              <!-- CTA Buttons -->
              <n-space size="large">
                <n-button 
                  @click="authStore.isAuthenticated ? goToDashboard() : goToLogin()" 
                  type="primary" 
                  size="large"
                  style="padding: 16px 32px; font-size: 1.125rem;"
                >
                  <template #icon>
                    <n-icon><BookOutline /></n-icon>
                  </template>
                  {{ authStore.isAuthenticated ? 'Go to Dashboard' : 'Get Started Free' }}
                </n-button>
                
                <n-button 
                  @click="goToDemo" 
                  quaternary 
                  size="large"
                  style="padding: 16px 32px; font-size: 1.125rem;"
                >
                  <template #icon>
                    <n-icon><PlayOutline /></n-icon>
                  </template>
                  Watch Demo
                </n-button>
              </n-space>
            </n-space>
          </n-grid-item>
          
          <n-grid-item>
            <!-- Hero Visual Cards -->
            <n-space vertical size="medium" style="position: relative;">
              <n-card size="small" style="width: 200px; margin-left: auto;">
                <n-space align="center" size="small">
                  <n-icon size="24" color="#18a058"><BookOutline /></n-icon>
                  <n-text>Daily thoughts</n-text>
                </n-space>
              </n-card>
              
              <n-card size="small" style="width: 200px;">
                <n-space align="center" size="small">
                  <n-icon size="24" color="#2080f0"><HeartOutline /></n-icon>
                  <n-text>Memories</n-text>
                </n-space>
              </n-card>
              
              <n-card size="small" style="width: 200px; margin-left: auto;">
                <n-space align="center" size="small">
                  <n-icon size="24" color="#f0a020"><TrendingUpOutline /></n-icon>
                  <n-text>Growth</n-text>
                </n-space>
              </n-card>
            </n-space>
          </n-grid-item>
        </n-grid>
      </div>
    </section>

    <!-- Stats Section -->
    <section style="padding: 60px 0; background: #ffffff;">
      <div style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
        <n-grid :cols="4" :x-gap="24">
          <n-grid-item v-for="stat in stats" :key="stat.label">
            <n-card size="small" style="text-align: center;">
              <n-space vertical align="center" size="small">
                <n-icon size="48" color="#18a058">
                  <component :is="stat.icon" />
                </n-icon>
                <n-statistic :value="stat.value" :label="stat.label" />
              </n-space>
            </n-card>
          </n-grid-item>
        </n-grid>
      </div>
    </section>

    <!-- Features Section -->
    <section style="padding: 80px 0; background: #f8fafc;">
      <div style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
        <n-space vertical align="center" size="large" style="text-align: center; margin-bottom: 60px;">
          <n-h2 style="font-size: 2.5rem; font-weight: 700; margin: 0;">
            Why Choose Our Platform?
          </n-h2>
          <n-text depth="3" style="font-size: 1.125rem; max-width: 600px;">
            Built with modern technology and user experience in mind
          </n-text>
        </n-space>
        
        <n-grid :cols="3" :x-gap="24" :y-gap="24">
          <n-grid-item v-for="feature in features" :key="feature.title">
            <n-card size="large" style="height: 100%; text-align: center;">
              <n-space vertical align="center" size="large">
                <n-avatar 
                  round 
                  size="large" 
                  :color="feature.color"
                  style="font-size: 2rem;"
                >
                  <n-icon size="32">
                    <component :is="feature.icon" />
                  </n-icon>
                </n-avatar>
                
                <n-h3 style="font-size: 1.5rem; font-weight: 600; margin: 0;">
                  {{ feature.title }}
                </n-h3>
                
                <n-text depth="3" style="line-height: 1.6;">
                  {{ feature.description }}
                </n-text>
              </n-space>
            </n-card>
          </n-grid-item>
        </n-grid>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section style="padding: 80px 0; background: #ffffff;">
      <div style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
        <n-space vertical align="center" size="large" style="text-align: center; margin-bottom: 60px;">
          <n-h2 style="font-size: 2.5rem; font-weight: 700; margin: 0;">
            What Our Users Say
          </n-h2>
          <n-text depth="3" style="font-size: 1.125rem; max-width: 600px;">
            Join thousands of satisfied users who are already transforming their daily reflections
          </n-text>
        </n-space>
        
        <n-grid :cols="3" :x-gap="24">
          <n-grid-item v-for="testimonial in testimonials" :key="testimonial.name">
            <n-card size="large">
              <n-space vertical size="medium">
                <n-space align="center" size="medium">
                  <n-avatar round size="medium" :src="testimonial.avatar" />
                  <div>
                    <n-text strong>{{ testimonial.name }}</n-text>
                    <br>
                    <n-text depth="3" size="small">{{ testimonial.role }}</n-text>
                  </div>
                </n-space>
                
                <n-text depth="3" style="line-height: 1.6; font-style: italic;">
                  "{{ testimonial.content }}"
                </n-text>
                
                <n-space>
                  <n-icon color="#f0a020" v-for="i in 5" :key="i">
                    <StarOutline />
                  </n-icon>
                </n-space>
              </n-space>
            </n-card>
          </n-grid-item>
        </n-grid>
      </div>
    </section>

    <!-- CTA Section -->
    <section style="padding: 80px 0; background: linear-gradient(135deg, #18a058 0%, #36ad6a 100%);">
      <div style="max-width: 800px; margin: 0 auto; padding: 0 24px; text-align: center;">
        <n-card size="large" :bordered="false" style="background: transparent; color: white;">
          <n-space vertical size="large">
            <n-h2 style="font-size: 2.5rem; font-weight: 700; margin: 0; color: white;">
              Ready to Start Your Journey?
            </n-h2>
            
            <n-text style="font-size: 1.25rem; opacity: 0.9; color: white;">
              Join thousands of users who are already transforming their daily reflections into meaningful insights.
            </n-text>
            
            <n-space size="large" justify="center">
              <n-button 
                @click="authStore.isAuthenticated ? goToDashboard() : goToLogin()" 
                size="large"
                style="padding: 16px 32px; font-size: 1.125rem; background: white; color: #18a058;"
              >
                <template #icon>
                  <n-icon><BookOutline /></n-icon>
                </template>
                {{ authStore.isAuthenticated ? 'Go to Dashboard' : 'Get Started Free' }}
              </n-button>
            </n-space>
          </n-space>
        </n-card>
      </div>
    </section>

    <!-- Footer -->
    <section style="padding: 40px 0; background: #1a1a1a; color: white;">
      <div style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
        <n-grid :cols="4" :x-gap="24">
          <n-grid-item>
            <n-space vertical size="medium">
              <n-h3 style="color: white; margin: 0;">Journal Pro</n-h3>
              <n-text style="color: #999;">
                Transform your daily experiences into meaningful insights.
              </n-text>
            </n-space>
          </n-grid-item>
          
          <n-grid-item>
            <n-space vertical size="small">
              <n-text strong style="color: white;">Product</n-text>
              <n-text style="color: #999;">Features</n-text>
              <n-text style="color: #999;">Pricing</n-text>
              <n-text style="color: #999;">API</n-text>
            </n-space>
          </n-grid-item>
          
          <n-grid-item>
            <n-space vertical size="small">
              <n-text strong style="color: white;">Company</n-text>
              <n-text style="color: #999;">About</n-text>
              <n-text style="color: #999;">Blog</n-text>
              <n-text style="color: #999;">Careers</n-text>
            </n-space>
          </n-grid-item>
          
          <n-grid-item>
            <n-space vertical size="small">
              <n-text strong style="color: white;">Support</n-text>
              <n-text style="color: #999;">Help Center</n-text>
              <n-text style="color: #999;">Contact</n-text>
              <n-text style="color: #999;">Status</n-text>
            </n-space>
          </n-grid-item>
        </n-grid>
        
        <n-divider style="margin: 40px 0; border-color: #333;" />
        
        <n-space justify="space-between" align="center">
          <n-text style="color: #999;">
            © 2024 Journal Pro. All rights reserved.
          </n-text>
          
          <n-space size="medium">
            <n-text style="color: #999;">Privacy Policy</n-text>
            <n-text style="color: #999;">Terms of Service</n-text>
          </n-space>
        </n-space>
      </div>
    </section>
  </div>
</template> 