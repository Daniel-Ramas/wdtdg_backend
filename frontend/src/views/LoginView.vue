<script setup>
import { 
  NLayout, 
  NLayoutContent, 
  NButton, 
  NSpace, 
  NCard, 
  NText, 
  NH1, 
  NForm,
  NFormItem,
  NInput,
  NCheckbox,
  useMessage
} from 'naive-ui'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const message = useMessage()
const authStore = useAuthStore()

const formRef = ref(null)
const loading = ref(false)

const formModel = ref({
  username: '',
  password: '',
  remember: false
})

const rules = {
  username: {
    required: true,
    message: 'Please enter your email',
    trigger: 'blur'
  },
  password: {
    required: true,
    message: 'Please enter your password',
    trigger: 'blur'
  }
}

const handleLogin = async () => {
  try {
    await formRef.value?.validate()
    loading.value = true
    
    const result = await authStore.login(formModel.value)
    
    if (result.success) {
      message.success('Login successful')
      router.push('/journal')
    } else {
      message.error(result.error)
    }
  } catch (error) {
    message.error('Login failed')
  } finally {
    loading.value = false
  }
}

const goToHome = () => {
  router.push('/')
}
</script>

<template>
  <n-layout>
    <n-layout-content style="padding: 24px; display: flex; align-items: center; justify-content: center; min-height: 100vh;">
      <n-card style="width: 400px;">
        <n-space vertical size="large">
          <div style="text-align: center;">
            <n-h1>Sign In</n-h1>
            <n-text depth="3">
              Welcome back to your journal
            </n-text>
          </div>
          
          <n-form
            ref="formRef"
            :model="formModel"
            :rules="rules"
            label-placement="left"
            label-width="auto"
            require-mark-placement="right-hanging"
          >
            <n-form-item label="Email" path="username">
              <n-input
                v-model:value="formModel.username"
                placeholder="Enter your email"
                type="email"
                style="width: 100%"
              />
            </n-form-item>

            <n-form-item label="Password" path="password">
              <n-input
                v-model:value="formModel.password"
                placeholder="Enter your password"
                type="password"
                show-password-on="click"
                style="width: 100%"
              />
            </n-form-item>

            <n-form-item>
              <n-checkbox v-model:checked="formModel.remember">
                Remember me
              </n-checkbox>
            </n-form-item>

            <n-form-item>
              <n-button 
                @click="handleLogin" 
                type="primary" 
                :loading="loading"
                style="width: 100%"
              >
                Sign In
              </n-button>
            </n-form-item>
          </n-form>
          
          <div style="text-align: center;">
            <n-button text @click="goToHome">
              Back to Home
            </n-button>
          </div>
        </n-space>
      </n-card>
    </n-layout-content>
  </n-layout>
</template>

<style scoped>
.n-layout-content {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
</style> 