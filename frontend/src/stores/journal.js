import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { journalAPI } from '@/services/api'

export const useJournalStore = defineStore('journal', () => {
  const entries = ref([])
  const loading = ref(false)
  const error = ref(null)

  // Computed properties
  const totalEntries = computed(() => entries.value.length)
  const textEntries = computed(() => entries.value.filter(entry => entry.entry_type === 'text').length)
  const voiceEntries = computed(() => entries.value.filter(entry => entry.entry_type === 'voice').length)
  const mediaEntries = computed(() => entries.value.filter(entry => ['photo', 'video'].includes(entry.entry_type)).length)

  // Actions
  const fetchEntries = async () => {
    loading.value = true
    error.value = null
    try {
      const response = await journalAPI.getEntries()
      entries.value = response.data
    } catch (err) {
      error.value = err.response?.data?.message || 'Failed to fetch entries'
      throw err
    } finally {
      loading.value = false
    }
  }

  const fetchEntry = async (id) => {
    loading.value = true
    error.value = null
    try {
      const response = await journalAPI.getEntry(id)
      return response.data
    } catch (err) {
      error.value = err.response?.data?.message || 'Failed to fetch entry'
      throw err
    } finally {
      loading.value = false
    }
  }

  const createEntry = async (entryData) => {
    loading.value = true
    error.value = null
    try {
      const response = await journalAPI.createEntry(entryData)
      entries.value.unshift(response.data)
      return response.data
    } catch (err) {
      error.value = err.response?.data?.message || 'Failed to create entry'
      throw err
    } finally {
      loading.value = false
    }
  }

  const updateEntry = async (id, entryData) => {
    loading.value = true
    error.value = null
    try {
      const response = await journalAPI.updateEntry(id, entryData)
      const index = entries.value.findIndex(entry => entry.id === id)
      if (index !== -1) {
        entries.value[index] = response.data
      }
      return response.data
    } catch (err) {
      error.value = err.response?.data?.message || 'Failed to update entry'
      throw err
    } finally {
      loading.value = false
    }
  }

  const deleteEntry = async (id) => {
    loading.value = true
    error.value = null
    try {
      await journalAPI.deleteEntry(id)
      const index = entries.value.findIndex(entry => entry.id === id)
      if (index !== -1) {
        entries.value.splice(index, 1)
      }
    } catch (err) {
      error.value = err.response?.data?.message || 'Failed to delete entry'
      throw err
    } finally {
      loading.value = false
    }
  }

  const clearError = () => {
    error.value = null
  }

  return {
    // State
    entries,
    loading,
    error,
    
    // Computed
    totalEntries,
    textEntries,
    voiceEntries,
    mediaEntries,
    
    // Actions
    fetchEntries,
    fetchEntry,
    createEntry,
    updateEntry,
    deleteEntry,
    clearError,
  }
}) 