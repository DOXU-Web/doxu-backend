# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django REST API backend for a character management system, designed to work with a Next.js frontend. The project manages RPG-style characters with images, descriptions, and class information.

## Development Commands

### Environment Setup
```bash
# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Database Operations
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### Development Server
```bash
# Start development server
python manage.py runserver

# Server runs on http://localhost:8000/
# API endpoints available at http://localhost:8000/api/
# Admin interface at http://localhost:8000/admin/
```

### Testing API Endpoints
```bash
# List all active characters
curl http://localhost:8000/api/characters/

# Get specific character details
curl http://localhost:8000/api/characters/1/
```

## Architecture Overview

### Project Structure
- `backend/` - Django project configuration and settings
- `characters/` - Main Django app handling character management
- `media/characters/` - User-uploaded character images
- `db.sqlite3` - SQLite database (development)

### Key Components

#### Models (`characters/models.py`)
- **Character Model**: Core entity with fields for name, class, descriptions, image, and management fields
- **Character Classes**: Guerrier, Mage, Assassin, Archer, Paladin
- **Management Fields**: `is_active`, `order` for display control

#### API Views (`characters/views.py`)
- **CharacterListAPIView**: Returns all active characters with basic info
- **CharacterDetailAPIView**: Returns detailed character information
- Both views filter by `is_active=True` and order by `order` field, then `name`

#### Serializers (`characters/serializers.py`)
- **CharacterSerializer**: Full character data for detail view
- **CharacterListSerializer**: Optimized for list view, includes `detailed_description`
- Both include computed `image_url` field with absolute URLs

#### URL Configuration
- **Root URLs**: `/api/` prefix for all API endpoints
- **Character List**: `GET /api/characters/`
- **Character Detail**: `GET /api/characters/{id}/`
- **Media URLs**: `/media/characters/` for character images

### Database Schema
- Uses SQLite for development
- Character table with image uploads to `media/characters/`
- Two migrations: initial creation and detailed_description field addition

## Frontend Integration

### CORS Configuration
- Configured for Next.js frontend on `localhost:3000` and `127.0.0.1:3000`
- CORS middleware properly positioned in middleware stack

### Image Handling
- Images uploaded to `media/characters/` directory
- Absolute URLs computed in serializers using `request.build_absolute_uri()`
- Media files served in development via Django's static file serving

### API Design
- RESTful endpoints using Django REST Framework
- JSON responses with computed fields for frontend consumption
- Open permissions for development (`AllowAny`)

## Development Notes

### Settings Configuration
- **DEBUG**: Enabled (development mode)
- **SECRET_KEY**: Development key (change for production)
- **Database**: SQLite (suitable for development)
- **Language**: English (en-us), UTC timezone

### Content Management
- Use Django Admin interface for character management
- Characters can be activated/deactivated via `is_active` field
- Custom ordering via `order` field
- Rich text descriptions (short for cards, detailed for full pages)

### Common Development Tasks
- Add new characters via Django admin
- Modify character model in `characters/models.py`
- Update API responses by modifying serializers
- Add new endpoints in `characters/views.py` and `characters/urls.py`

### Production Considerations
- Current configuration is development-focused
- For production: update SECRET_KEY, disable DEBUG, configure proper database, add authentication
- Media files would need proper static file serving (e.g., nginx, CDN)