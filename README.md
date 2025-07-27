# Pustak_Project_DRF
 DRF_JWT
 ## Pustak Management API with Frontend

### 🔧 Setup Instructions

#### Backend
1. Create virtualenv and install packages:
    ```
    pip install django djangorestframework djangorestframework-simplejwt
    ```
2. Run migrations:
    ```
    python manage.py migrate
    ```
3. Start server:
    ```
    python manage.py runserver
    ```

#### Frontend
- Templates auto-rendered by Django views.
- Login to get JWT, then use it for book operations.

### 🧪 Test Instructions
1. Register: `POST /api/register/`
2. Login: `POST /api/token/` → get access token
3. Use token to:
   - View books
   - Add book
   - Update/Delete book
