## Architecture

DevProfile is a Django REST Framework based backend system that manages developer profiles, skills, and projects.

### Components

* **Django** → Core web framework
* **Django REST Framework (DRF)** → API layer for CRUD operations
* **SQLite** → Default database for development
* **HTML + JavaScript UI** → Minimal frontend to interact with APIs

### Data Flow

1. User interacts with the HTML dashboard.
2. Dashboard sends HTTP requests to DRF APIs.
3. APIs process data using Django models and serializers.
4. JSON response is returned and rendered on the UI.


## Local Setup

Follow these steps to run the project locally:

```bash
git clone https://github.com/<your-username>/devprofile-api.git
cd devprofile-api

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

## Production Setup (Basic)

For production deployment:

* Use **PostgreSQL** instead of SQLite
* Serve Django with **Gunicorn / Uvicorn**
* Use **Nginx** as reverse proxy
* Configure **environment variables** for secrets
* Set `DEBUG = False` and allowed hosts

Example command:

```bash
gunicorn config.wsgi:application
```

## Database Schema

### Profile

* name
* email
* education
* bio
* skills (Many-to-Many)
* created_at
* updated_at

### Skill

* name (unique)

### Project

* profile (ForeignKey)
* title
* description
* tech_stack (Many-to-Many → Skill)
* github_link
* live_link
* created_at


  ## Sample API Requests

### Create Skill

```bash
curl -X POST http://127.0.0.1:8000/api/skills/create/ \
-H "Content-Type: application/json" \
-d '{"name": "python"}'
```

### List Projects

```bash
curl http://127.0.0.1:8000/api/projects/
```

### Search Profiles

```bash
curl "http://127.0.0.1:8000/api/search/?q=python"
```

## Known Limitations

* No authentication or user login system
* Minimal frontend UI (not production ready)
* Uses SQLite in development
* No pagination or rate limiting in APIs
* No file/image upload support

## Resume

You can view my resume here:

**[View Resume]([https://your-resume-link.com](https://drive.google.com/file/d/1XH0Ecy3gv9NkU6POF4_X_-Y5Iq5DL55Y/view?usp=drive_link))**

