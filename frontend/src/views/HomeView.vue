<script setup>
import { NLayout, NLayoutHeader, NLayoutContent, NButton, NSpace, NCard, NText, NH1, NP } from 'naive-ui'
import { useRouter } from 'vue-router'

const router = useRouter()

const goToJournal = () => {
  router.push('/journal')
}
</script>

<template>
  <n-layout>
    <n-layout-header style="height: 64px; padding: 16px; background: #fff; border-bottom: 1px solid #eee;">
      <n-space justify="space-between" align="center">
        <n-h1 style="margin: 0; font-size: 24px;">Where Did The Day Go?</n-h1>
        <n-space>
          <n-button @click="goToJournal" type="primary">
            My Journal
          </n-button>
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
          
          <n-button @click="goToJournal" type="primary" size="large">
            Start Journaling
          </n-button>
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