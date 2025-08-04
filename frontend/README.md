# WDTDG Frontend

Vue 3 SPA frontend for the "Where Did The Day Go?" journal application.

## Features

- **Vue 3** with Composition API
- **Naive UI** component library
- **Vue Router** for navigation
- **Pinia** for state management
- **Axios** for API communication
- **Day.js** for date formatting
- **Vite** for fast development and building

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Development

- **Development server**: `npm run dev`
- **Build for production**: `npm run build`
- **Preview production build**: `npm run preview`

## Project Structure

```
src/
├── components/          # Reusable Vue components
├── views/              # Page components
│   ├── HomeView.vue    # Home page
│   ├── JournalListView.vue  # Journal entries list
│   ├── JournalEditView.vue  # Create/edit journal entry
│   └── LoginView.vue   # Login page
├── stores/             # Pinia stores
│   └── journal.js      # Journal state management
├── services/           # API services
│   └── api.js          # API client and endpoints
├── router/             # Vue Router configuration
│   └── index.js        # Route definitions
├── App.vue             # Root component
└── main.js             # Application entry point
```

## API Integration

The frontend communicates with the Django backend API at `http://localhost:8000/api/`. The Vite dev server is configured to proxy API requests to the backend.

## Authentication

The app uses token-based authentication. Users log in through the `/login` page, and the token is stored in localStorage. Protected routes automatically redirect to login if no token is present.

## Styling

The app uses Naive UI components with a clean, modern design. The theme can be easily customized by modifying the theme configuration in `App.vue`.
