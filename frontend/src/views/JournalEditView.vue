<script setup>
import { 
  NButton, 
  NSpace, 
  NCard, 
  NText, 
  NForm,
  NFormItem,
  NInput,
  NDatePicker,
  NSelect,
  NCheckbox,
  NUpload,
  NIcon,
  NTag,
  useMessage,
  useDialog
} from 'naive-ui'
import { 
  ArrowBackOutline,
  CheckmarkOutline,
  PencilOutline, 
  MicOutline, 
  CameraOutline, 
  VideocamOutline
} from '@vicons/ionicons5'
import { useRouter, useRoute } from 'vue-router'
import { onMounted, ref, computed } from 'vue'
import { useJournalStore } from '@/stores/journal'
import AppLayout from '@/components/AppLayout.vue'
import dayjs from 'dayjs'

const router = useRouter()
const route = useRoute()
const message = useMessage()
const dialog = useDialog()
const journalStore = useJournalStore()

const formRef = ref(null)
const loading = ref(false)
const entry = ref(null)

const formModel = ref({
  date: null,
  entry_type: 'text',
  content: '',
  media: [],
  irl_mode: false
})

const entryTypeOptions = [
  { label: 'Text', value: 'text' },
  { label: 'Voice', value: 'voice' },
  { label: 'Photo', value: 'photo' },
  { label: 'Video', value: 'video' }
]

const rules = {
  date: {
    required: true,
    message: 'Please select a date',
    trigger: 'blur'
  },
  entry_type: {
    required: true,
    message: 'Please select an entry type',
    trigger: 'change'
  }
}

const goBack = () => {
  router.push('/journal')
}

const handleSave = async () => {
  try {
    await formRef.value?.validate()
    loading.value = true
    
    const formData = new FormData()
    formData.append('date', dayjs(formModel.value.date).format('YYYY-MM-DD'))
    formData.append('entry_type', formModel.value.entry_type)
    formData.append('content', formModel.value.content)
    formData.append('irl_mode', formModel.value.irl_mode)
    
    // Handle file upload
    if (formModel.value.media && formModel.value.media.length > 0) {
      const file = formModel.value.media[0].file || formModel.value.media[0]
      formData.append('media', file)
    }
    
    if (route.params.id) {
      await journalStore.updateEntry(route.params.id, formData)
      message.success('Entry updated successfully')
    } else {
      await journalStore.createEntry(formData)
      message.success('Entry created successfully')
    }
    
    router.push('/journal')
  } catch (error) {
    if (error.message) {
      message.error(error.message)
    } else {
      message.error('Failed to save entry')
    }
  } finally {
    loading.value = false
  }
}

const handleFileChange = (event) => {
  const file = event.file
  if (file.status === 'done') {
    message.success(`${file.name} uploaded successfully`)
  } else if (file.status === 'error') {
    message.error(`${file.name} upload failed.`)
  }
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
      return PencilOutline
  }
}

const formatDate = (date) => {
  return dayjs(date).format('MMMM D, YYYY')
}

onMounted(async () => {
  if (route.params.id) {
    try {
      loading.value = true
      entry.value = await journalStore.fetchEntry(route.params.id)
      
      // Populate form with existing data
      formModel.value = {
        date: dayjs(entry.value.date).toDate(),
        entry_type: entry.value.entry_type,
        content: entry.value.content || '',
        media: null,
        irl_mode: entry.value.irl_mode || false
      }
    } catch (error) {
      message.error('Failed to load entry')
      router.push('/journal')
    } finally {
      loading.value = false
    }
  }
})
</script>

<template>
  <AppLayout>
    <n-space vertical size="large">
      <!-- Edit Form -->
      <n-card title="Entry Details">
        <n-form
          ref="formRef"
          :model="formModel"
          :rules="rules"
          label-placement="left"
          label-width="auto"
          require-mark-placement="right-hanging"
        >
          <n-form-item label="Date" path="date">
            <n-date-picker
              v-model:value="formModel.date"
              type="date"
              clearable
              style="width: 100%"
            />
          </n-form-item>

          <n-form-item label="Entry Type" path="entry_type">
            <n-select
              v-model:value="formModel.entry_type"
              :options="entryTypeOptions"
              style="width: 100%"
            />
          </n-form-item>

          <n-form-item label="Content" path="content">
            <n-input
              v-model:value="formModel.content"
              type="textarea"
              placeholder="Write your thoughts..."
              :rows="6"
              style="width: 100%"
            />
          </n-form-item>

          <n-form-item label="Media" path="media">
            <n-upload
              v-model:file-list="formModel.media"
              :max="1"
              :show-file-list="true"
              accept="image/*,video/*,audio/*"
              @change="handleFileChange"
            >
              <n-button>Upload File</n-button>
            </n-upload>
            <n-text depth="3" size="small">
              Upload an image, video, or audio file (optional)
            </n-text>
          </n-form-item>

          <n-form-item label="IRL Mode" path="irl_mode">
            <n-checkbox v-model:checked="formModel.irl_mode">
              Enable IRL Mode
            </n-checkbox>
          </n-form-item>

          <n-form-item>
            <n-space>
              <n-button @click="goBack">Cancel</n-button>
              <n-button 
                @click="handleSave" 
                type="primary" 
                :loading="loading"
              >
                <template #icon>
                  <n-icon><CheckmarkOutline /></n-icon>
                </template>
                {{ route.params.id ? 'Update Entry' : 'Create Entry' }}
              </n-button>
            </n-space>
          </n-form-item>
        </n-form>
      </n-card>

      <!-- Entry Preview -->
      <n-card v-if="entry" title="Current Entry Preview">
        <n-space vertical size="medium">
          <n-space align="center">
            <n-icon :component="getEntryIcon(entry.entry_type)" size="24" />
            <div>
              <n-text strong>{{ entry.entry_type.charAt(0).toUpperCase() + entry.entry_type.slice(1) }} Entry</n-text>
              <br>
              <n-text depth="3">{{ formatDate(entry.date) }}</n-text>
            </div>
            <n-tag v-if="entry.irl_mode" type="error" size="small">IRL Mode</n-tag>
          </n-space>
          
          <div v-if="entry.content">
            <n-text>{{ entry.content }}</n-text>
          </div>
          
          <div v-if="entry.media">
            <img v-if="entry.entry_type === 'photo'" :src="entry.media" alt="Journal photo" style="max-width: 100%; max-height: 200px; border-radius: 8px;" />
            <video v-else-if="entry.entry_type === 'video'" controls style="max-width: 100%; max-height: 200px; border-radius: 8px;">
              <source :src="entry.media" type="video/mp4">
            </video>
            <audio v-else-if="entry.entry_type === 'voice'" controls style="width: 100%;">
              <source :src="entry.media" type="audio/mpeg">
            </audio>
          </div>
        </n-space>
      </n-card>
    </n-space>
  </AppLayout>
</template>

<style scoped>
/* Component-specific styles can go here */
</style> 