<script setup>
import { 
  NCard, 
  NText, 
  NH2, 
  NH3,
  NStatistic,
  NGrid,
  NGridItem,
  NProgress,
  NTag,
  NIcon,
  NSpace,
  NButton,
  NTimeline,
  NTimelineItem
} from 'naive-ui'
import { 
  BookOutline, 
  TrendingUpOutline,
  CalendarOutline,
  HeartOutline,
  TimeOutline,
  CheckmarkCircleOutline,
  AlertCircleOutline
} from '@vicons/ionicons5'
import { useRouter } from 'vue-router'
import { computed } from 'vue'
import { useJournalStore } from '@/stores/journal'
import AppLayout from '@/components/AppLayout.vue'

const router = useRouter()
const journalStore = useJournalStore()

const goToJournal = () => {
  router.push('/journal')
}

const goToNewEntry = () => {
  router.push('/journal/new')
}

// Mock data for demonstration
const recentActivity = [
  {
    type: 'text',
    content: 'Had an amazing conversation with Sarah today about future plans',
    time: '2 hours ago',
    icon: BookOutline,
    color: 'success'
  },
  {
    type: 'voice',
    content: 'Recorded thoughts about the new project idea',
    time: '5 hours ago',
    icon: BookOutline,
    color: 'info'
  },
  {
    type: 'photo',
    content: 'Captured the beautiful sunset during evening walk',
    time: '1 day ago',
    icon: BookOutline,
    color: 'warning'
  }
]

const weeklyProgress = 75
const monthlyGoal = 20
const currentStreak = 7
</script>

<template>
  <AppLayout>
    <!-- Welcome Section -->
    <n-card style="background: var(--n-color); border: 1px solid var(--n-border-color);">
      <n-space vertical size="medium" style="padding: 32px;">
        <n-h2 style="margin: 0; color: var(--n-primary-color);">
          Welcome back! 👋
        </n-h2>
        <n-text depth="3" size="large">
          Ready to capture today's thoughts and experiences?
        </n-text>
        <n-space>
          <n-button @click="goToNewEntry" type="primary" size="large">
            <template #icon>
              <n-icon><BookOutline /></n-icon>
            </template>
            New Entry
          </n-button>
          <n-button @click="goToJournal" quaternary size="large">
            <template #icon>
              <n-icon><BookOutline /></n-icon>
            </template>
            View Journal
          </n-button>
        </n-space>
      </n-space>
    </n-card>

    <!-- Stats Overview -->
    <n-grid :cols="4" :x-gap="16" :y-gap="16" style="margin-top: 24px;">
      <n-grid-item>
        <n-card>
          <n-statistic 
            label="Total Entries" 
            :value="journalStore.totalEntries || 0"
            :value-style="{ color: 'var(--n-primary-color)' }"
          />
        </n-card>
      </n-grid-item>
      
      <n-grid-item>
        <n-card>
          <n-statistic 
            label="Current Streak" 
            :value="currentStreak"
            :value-style="{ color: 'var(--n-warning-color)' }"
          />
          <n-text depth="3" size="small">days</n-text>
        </n-card>
      </n-grid-item>
      
      <n-grid-item>
        <n-card>
          <n-statistic 
            label="Weekly Progress" 
            :value="weeklyProgress"
            :value-style="{ color: 'var(--n-info-color)' }"
          />
          <n-text depth="3" size="small">%</n-text>
        </n-card>
      </n-grid-item>
      
      <n-grid-item>
        <n-card>
          <n-statistic 
            label="Monthly Goal" 
            :value="monthlyGoal"
            :value-style="{ color: 'var(--n-error-color)' }"
          />
          <n-text depth="3" size="small">entries</n-text>
        </n-card>
      </n-grid-item>
    </n-grid>

    <!-- Progress and Goals -->
    <n-grid :cols="2" :x-gap="16" :y-gap="16" style="margin-top: 24px;">
      <n-grid-item>
        <n-card title="Weekly Progress">
          <n-space vertical size="medium">
            <n-text>You're {{ weeklyProgress }}% through your weekly goal</n-text>
            <n-progress 
              type="line" 
              :percentage="weeklyProgress" 
              :color="weeklyProgress >= 80 ? 'var(--n-success-color)' : weeklyProgress >= 60 ? 'var(--n-warning-color)' : 'var(--n-error-color)'"
            />
            <n-text depth="3" size="small">
              {{ 7 - Math.floor(weeklyProgress / 14.28) }} days remaining this week
            </n-text>
          </n-space>
        </n-card>
      </n-grid-item>
      
      <n-grid-item>
        <n-card title="Monthly Goal">
          <n-space vertical size="medium">
            <n-text>Monthly target: {{ monthlyGoal }} entries</n-text>
            <n-progress 
              type="line" 
              :percentage="Math.min((journalStore.totalEntries || 0) / monthlyGoal * 100, 100)" 
              :color="(journalStore.totalEntries || 0) >= monthlyGoal ? 'var(--n-success-color)' : 'var(--n-warning-color)'"
            />
            <n-text depth="3" size="small">
              {{ Math.max(monthlyGoal - (journalStore.totalEntries || 0), 0) }} more entries needed
            </n-text>
          </n-space>
        </n-card>
      </n-grid-item>
    </n-grid>

    <!-- Recent Activity -->
    <n-card title="Recent Activity" style="margin-top: 24px;">
      <n-timeline>
        <n-timeline-item 
          v-for="(activity, index) in recentActivity" 
          :key="index"
          :type="activity.color"
          :title="activity.content"
          :time="activity.time"
        >
          <template #icon>
            <n-icon :component="activity.icon" />
          </template>
          <n-tag :type="activity.color" size="small">
            {{ activity.type.charAt(0).toUpperCase() + activity.type.slice(1) }}
          </n-tag>
        </n-timeline-item>
      </n-timeline>
    </n-card>

    <!-- Quick Actions -->
    <n-card title="Quick Actions" style="margin-top: 24px;">
      <n-grid :cols="3" :x-gap="16">
        <n-grid-item>
          <n-button quaternary block size="large" @click="goToNewEntry">
            <template #icon>
              <n-icon><BookOutline /></n-icon>
            </template>
            Text Entry
          </n-button>
        </n-grid-item>
        
        <n-grid-item>
          <n-button quaternary block size="large">
            <template #icon>
              <n-icon><TimeOutline /></n-icon>
            </template>
            Voice Note
          </n-button>
        </n-grid-item>
        
        <n-grid-item>
          <n-button quaternary block size="large">
            <template #icon>
              <n-icon><HeartOutline /></n-icon>
            </template>
            Photo Entry
          </n-button>
        </n-grid-item>
      </n-grid>
    </n-card>
  </AppLayout>
</template>


