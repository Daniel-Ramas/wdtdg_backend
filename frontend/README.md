# Frontend - Where Did The Day Go?

A Vue.js frontend for the personal journaling application.

## Features

- **Authentication System**: Login/logout functionality with secure token management
- **Responsive Design**: Built with Naive UI components for a modern, accessible interface
- **Journal Management**: Create, edit, and manage journal entries
- **User Menu**: Dropdown menu with profile, settings, and other features (coming soon)

## New Features Added

### Authentication & Menu System
- **Login/Logout**: Full authentication flow with the backend API
- **User Menu**: Dropdown menu button that adapts based on authentication status
- **Protected Routes**: Journal pages require authentication
- **State Management**: Centralized auth state using Pinia store

### Menu Options
- **Authenticated Users**:
  - Profile (coming soon)
  - Settings (coming soon)
  - My Journal
  - Logout
- **Unauthenticated Users**:
  - Login

## Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## Project Structure

```
src/
├── stores/
│   ├── auth.js          # Authentication state management
│   └── counter.js       # Example store
├── views/
│   ├── HomeView.vue     # Home page with menu
│   ├── LoginView.vue    # Login form
│   └── Journal*.vue     # Journal management views
├── services/
│   └── api.js          # API communication
└── router/
    └── index.js        # Route configuration with auth guards
```

## Authentication Flow

1. User visits home page
2. If not authenticated, sees "Get Started" button and "Account" menu
3. Clicking "Get Started" or "Account" → Login takes them to login page
4. After successful login, redirected to journal page
5. Menu changes to show full options including logout
6. Protected routes automatically redirect to login if not authenticated

## Technologies Used

- **Vue 3** with Composition API
- **Naive UI** for components
- **Pinia** for state management
- **Vue Router** with authentication guards
- **Axios** for API communication
- **Vite** for build tooling
