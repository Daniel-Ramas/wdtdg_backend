# Where Did The Day Go? (WDTDG)

A personal journaling application built with Django REST API backend and Vue 3 SPA frontend.

## Architecture

This project uses a modern full-stack architecture:

- **Backend**: Django REST API with PostgreSQL
- **Frontend**: Vue 3 SPA with Naive UI components
- **Authentication**: Token-based authentication
- **Database**: PostgreSQL
- **Development**: Docker Compose for easy setup

## Features

- 📝 **Text Entries**: Write your thoughts and reflections
- 🎤 **Voice Entries**: Record audio journal entries
- 📸 **Photo Entries**: Upload and store photos
- 🎥 **Video Entries**: Upload and store videos
- 🔒 **Secure**: Private, user-authenticated entries
- 📊 **Statistics**: Track your journaling habits
- 🎨 **Modern UI**: Clean, responsive interface with Naive UI

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js 20+ (for frontend development)
- Python 3.12+ (for backend development)

### Backend Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd wdtdg_backend
```

2. Set up environment variables:
```bash
cp .envs/.local .env
```

3. Start the backend services:
```bash
docker-compose -f docker-compose.local.yml up -d
```

4. Run migrations:
```bash
docker-compose -f docker-compose.local.yml exec django python manage.py migrate
```

5. Create a superuser:
```bash
docker-compose -f docker-compose.local.yml exec django python manage.py createsuperuser
```

The Django API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The Vue frontend will be available at `http://localhost:3000`

## Development

### Backend Development

The Django backend provides a REST API with the following endpoints:

- `GET /api/journal-entries/` - List journal entries
- `POST /api/journal-entries/` - Create new entry
- `GET /api/journal-entries/{id}/` - Get specific entry
- `PUT /api/journal-entries/{id}/` - Update entry
- `DELETE /api/journal-entries/{id}/` - Delete entry
- `POST /api/auth-token/` - Login and get token

### Frontend Development

The Vue frontend includes:

- **Home Page**: Welcome and feature overview
- **Journal List**: View all entries with statistics
- **Entry Editor**: Create and edit journal entries
- **Login Page**: User authentication

### API Documentation

Access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/api/docs/`
- API Schema: `http://localhost:8000/api/schema/`

## Project Structure

```
wdtdg_backend/
├── config/                 # Django settings and configuration
├── journal/                # Journal app with models and API views
├── wdtdg_backend/          # Main Django project
├── frontend/               # Vue 3 frontend application
│   ├── src/
│   │   ├── views/          # Page components
│   │   ├── stores/         # Pinia state management
│   │   ├── services/       # API services
│   │   └── router/         # Vue Router configuration
│   └── package.json
├── docker-compose.local.yml
└── README.md
```

## Deployment

### Production

For production deployment:

1. Build the frontend:
```bash
cd frontend
npm run build
```

2. Deploy the Django backend with the built frontend static files.

3. Configure environment variables for production settings.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
