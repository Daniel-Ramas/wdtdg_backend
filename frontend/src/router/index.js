import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DashboardView from '../views/DashboardView.vue'
import JournalListView from '../views/JournalListView.vue'
import JournalEditView from '../views/JournalEditView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { 
        title: 'Home',
        description: 'Welcome to your personal journaling platform'
      }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      meta: { 
        requiresAuth: true,
        title: 'Dashboard',
        description: 'Overview of your journaling activity and progress'
      }
    },
    {
      path: '/journal',
      name: 'journal-list',
      component: JournalListView,
      meta: { 
        requiresAuth: true,
        title: 'Journal Entries',
        description: 'View and manage your journal entries'
      }
    },
    {
      path: '/journal/new',
      name: 'journal-new',
      component: JournalEditView,
      meta: { 
        requiresAuth: true,
        title: 'New Journal Entry',
        description: 'Create a new journal entry'
      }
    },
    {
      path: '/journal/edit/:id',
      name: 'journal-edit',
      component: JournalEditView,
      meta: { 
        requiresAuth: true,
        title: 'Edit Journal Entry',
        description: 'Edit your journal entry'
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: { 
        title: 'Login',
        description: 'Sign in to your account'
      }
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
    next('/dashboard')
  } else {
    next()
  }
})

export default router
