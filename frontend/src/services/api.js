import axios from 'axios'

const API_BASE_URL = '/api'

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken')
    if (token) {
      config.headers.Authorization = `Token ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor to handle errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('authToken')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

// Auth API
export const authAPI = {
  login: (credentials) => api.post('/auth-token/', credentials),
  logout: () => {
    localStorage.removeItem('authToken')
  },
}

// Journal API
export const journalAPI = {
  getEntries: () => api.get('/journal-entries/'),
  getEntry: (id) => api.get(`/journal-entries/${id}/`),
  createEntry: (data) => api.post('/journal-entries/', data),
  updateEntry: (id, data) => api.put(`/journal-entries/${id}/`, data),
  deleteEntry: (id) => api.delete(`/journal-entries/${id}/`),
}

// User API
export const userAPI = {
  getProfile: () => api.get('/users/me/'),
  updateProfile: (data) => api.put('/users/me/', data),
}

export default api 