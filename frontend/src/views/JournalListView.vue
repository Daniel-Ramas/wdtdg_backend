<script setup>
import { 
  NButton, 
  NSpace, 
  NCard, 
  NText, 
  NH3,
  NStatistic,
  NGrid,
  NGridItem,
  NEmpty,
  NIcon,
  NTag,
  NPopconfirm,
  useMessage,
  useDialog
} from 'naive-ui'
import { 
  BookOutline, 
  PencilOutline, 
  MicOutline, 
  CameraOutline, 
  VideocamOutline,
  AddOutline,
  TrashOutline,
  CreateOutline
} from '@vicons/ionicons5'
import { useRouter } from 'vue-router'
import { onMounted, computed } from 'vue'
import { useJournalStore } from '@/stores/journal'
import AppLayout from '@/components/AppLayout.vue'
import dayjs from 'dayjs'

const router = useRouter()
const message = useMessage()
const dialog = useDialog()
const journalStore = useJournalStore()

const goToCreate = () => {
  router.push('/journal/new')
}

const goToEdit = (id) => {
  router.push(`/journal/edit/${id}`)
}

const handleDelete = async (id) => {
  dialog.warning({
    title: 'Delete Entry',
    content: 'Are you sure you want to delete this journal entry? This action cannot be undone.',
    positiveText: 'Delete',
    negativeText: 'Cancel',
    onPositiveClick: async () => {
      try {
        await journalStore.deleteEntry(id)
        message.success('Entry deleted successfully')
      } catch (error) {
        message.error('Failed to delete entry')
      }
    }
  })
}

const getEntryIcon = (entryType) => {
  switch (entryType) {
    case 'text':
      return PencilOutline
    case 'voice':
      return MicOutline
    case 'photo':
      return CameraOutline
    case 'video':
      return VideocamOutline
    default:
      return BookOutline
  }
}

const getEntryTypeColor = (entryType) => {
  switch (entryType) {
    case 'text':
      return 'primary'
    case 'voice':
      return 'success'
    case 'photo':
      return 'info'
    case 'video':
      return 'warning'
    default:
      return 'default'
  }
}

const formatDate = (date) => {
  return dayjs(date).format('MMMM D, YYYY')
}

const formatTime = (date) => {
  return dayjs(date).format('MMM D, h:mm A')
}

onMounted(async () => {
  try {
    await journalStore.fetchEntries()
  } catch (error) {
    message.error('Failed to load journal entries')
  }
})
</script>

<template>
  <AppLayout>
    <!-- Stats Cards -->
    <n-grid :cols="4" :x-gap="16" :y-gap="16">
      <n-grid-item>
        <n-card>
          <n-statistic label="Total Entries" :value="journalStore.totalEntries" />
        </n-card>
      </n-grid-item>
      <n-grid-item>
        <n-card>
          <n-statistic label="Text Entries" :value="journalStore.textEntries" />
        </n-card>
      </n-grid-item>
      <n-grid-item>
        <n-card>
          <n-statistic label="Voice Entries" :value="journalStore.voiceEntries" />
        </n-card>
      </n-grid-item>
      <n-grid-item>
        <n-card>
          <n-statistic label="Media Entries" :value="journalStore.mediaEntries" />
        </n-card>
      </n-grid-item>
    </n-grid>

    <!-- Entries List -->
    <div v-if="journalStore.loading" style="margin-top: 24px;">
      <n-card>
        <n-space justify="center">
          <n-text>Loading entries...</n-text>
        </n-space>
      </n-card>
    </div>

    <div v-else-if="journalStore.entries.length === 0" style="margin-top: 24px;">
      <n-card>
        <n-empty description="No journal entries yet">
          <template #extra>
            <n-button @click="goToCreate" type="primary">
              Create First Entry
            </n-button>
          </template>
        </n-empty>
      </n-card>
    </div>

    <div v-else style="margin-top: 24px;">
      <n-space vertical size="medium">
        <n-card v-for="entry in journalStore.entries" :key="entry.id">
          <n-space vertical size="medium">
            <!-- Entry Header -->
            <n-space justify="space-between" align="center">
              <n-space align="center">
                <n-icon :component="getEntryIcon(entry.entry_type)" size="24" />
                <div>
                  <n-h3 style="margin: 0;">{{ entry.entry_type.charAt(0).toUpperCase() + entry.entry_type.slice(1) }} Entry</n-h3>
                  <n-text depth="3">{{ formatDate(entry.date) }}</n-text>
                </div>
              </n-space>
              <n-space>
                <n-tag v-if="entry.irl_mode" type="error" size="small">IRL Mode</n-tag>
                <n-text depth="3" size="small">{{ formatTime(entry.created_at) }}</n-text>
              </n-space>
            </n-space>

            <!-- Entry Content -->
            <div v-if="entry.content">
              <n-text>{{ entry.content }}</n-text>
            </div>

            <!-- Media Display -->
            <div v-if="entry.media">
              <img v-if="entry.entry_type === 'photo'" :src="entry.media" alt="Journal photo" style="max-width: 100%; border-radius: 8px;" />
              <video v-else-if="entry.entry_type === 'video'" controls style="max-width: 100%; border-radius: 8px;">
                <source :src="entry.media" type="video/mp4">
              </video>
              <audio v-else-if="entry.entry_type === 'voice'" controls style="width: 100%;">
                <source :src="entry.media" type="audio/mpeg">
              </audio>
            </div>

            <!-- Entry Actions -->
            <n-space justify="space-between" align="center">
              <n-space>
                <n-button @click="goToEdit(entry.id)" size="small">
                  <template #icon>
                    <n-icon><CreateOutline /></n-icon>
                  </template>
                  Edit
                </n-button>
                <n-popconfirm @positive-click="handleDelete(entry.id)">
                  <template #trigger>
                    <n-button size="small" type="error">
                      <template #icon>
                        <n-icon><TrashOutline /></n-icon>
                      </template>
                      Delete
                    </n-button>
                  </template>
                  Are you sure you want to delete this entry?
                </n-popconfirm>
              </n-space>
              <n-text depth="3" size="small">ID: {{ entry.id.slice(0, 8) }}...</n-text>
            </n-space>
          </n-space>
        </n-card>
      </n-space>
    </div>
  </AppLayout>
</template>

<style scoped>
/* Component-specific styles can go here */
</style> 