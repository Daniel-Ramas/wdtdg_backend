import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import JournalListView from '../views/JournalListView.vue'
import JournalEditView from '../views/JournalEditView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/journal',
      name: 'journal-list',
      component: JournalListView,
      meta: { requiresAuth: true }
    },
    {
      path: '/journal/edit/:id',
      name: 'journal-edit',
      component: JournalEditView,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    }
  ]
})

// Navigation guard for authentication
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('authToken')
  
  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else if (to.path === '/login' && token) {
    // Redirect authenticated users away from login page
    next('/journal')
  } else {
    next()
  }
})

export default router
