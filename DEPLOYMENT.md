# HRMS Backend - Production Deployment Guide

## ✅ What's Fixed:

1. **Security**: Removed hardcoded `SECRET_KEY`, set `DEBUG=False` for production
2. **Database**: Switched from SQLite to PostgreSQL (production-ready)
3. **Environment Variables**: Added `python-decouple` for secure configuration
4. **Static Files**: Added WhiteNoise middleware for serving static files
5. **CORS**: Restricted CORS to specific origins instead of allowing all
6. **Procfile**: Created for Render/Railway deployment
7. **Runtime**: Specified Python version (3.11.7)

---

## 📋 Deployment Checklist:

### For Render:

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Production ready configuration"
   git push origin main
   ```

2. **Create Render Service**
   - Go to render.com and create new Web Service
   - Connect your GitHub repository
   - Select the HRMS_Backend directory

3. **Environment Variables** (set in Render dashboard):
   ```
   DEBUG=False
   SECRET_KEY=<generate-secure-key>
   ALLOWED_HOSTS=your-app.onrender.com
   CORS_ALLOWED_ORIGINS=https://your-frontend.com
   
   # Database (if using Render PostgreSQL)
   DB_NAME=<db_name>
   DB_USER=<db_user>
   DB_PASSWORD=<db_password>
   DB_HOST=<db_host>
   DB_PORT=5432
   ```

4. **Build Settings**
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn config.wsgi:application`

---

### For Railway:

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Production ready configuration"
   git push origin main
   ```

2. **Create Railway Project**
   - Go to railway.app and create new project
   - Deploy from GitHub repository

3. **Environment Variables** (Railway dashboard):
   ```
   DEBUG=False
   SECRET_KEY=<generate-secure-key>
   ALLOWED_HOSTS=your-app.railway.app
   CORS_ALLOWED_ORIGINS=https://your-frontend.com
   
   # Database (PostgreSQL)
   DB_NAME=<db_name>
   DB_USER=<db_user>
   DB_PASSWORD=<db_password>
   DB_HOST=<db_host>
   DB_PORT=5432
   ```

4. **Procfile Configuration**
   - Railway automatically reads Procfile
   - Services: Web & Release tasks configured

---

## 🔧 Local Development Setup:

1. **Create .env file** (copy from .env.example):
   ```bash
   cp .env.example .env
   ```

2. **Update .env with local settings**:
   ```
   DEBUG=True
   SECRET_KEY=your-dev-secret-key
   ALLOWED_HOSTS=localhost,127.0.0.1
   CORS_ALLOWED_ORIGINS=http://localhost:3000
   
   # Local SQLite (keep as is)
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**:
   ```bash
   python manage.py runserver
   ```

---

## 🗄️ Database Setup (PostgreSQL):

### Option 1: Railway PostgreSQL
1. Create Railway project
2. Add PostgreSQL service
3. Copy connection credentials to environment variables

### Option 2: Render PostgreSQL
1. Create Render database
2. Copy connection details
3. Set environment variables

### Option 3: External PostgreSQL (AWS RDS, Supabase, etc.)
1. Create PostgreSQL instance
2. Copy credentials
3. Set environment variables

---

## 🚀 Deployment Steps:

### First Deploy (Initial Setup):

1. Set all environment variables on platform (Render/Railway)
2. Platform will run: `python manage.py migrate`
3. Create superuser via shell:
   ```bash
   # Via SSH on platform
   python manage.py createsuperuser
   ```
4. Service will be live!

### Subsequent Deploys:

1. Make code changes locally
2. Commit and push to GitHub
3. Platform auto-deploys
4. Migrations run automatically (release command in Procfile)

---

## 🔐 Security Checklist:

- ✅ `DEBUG=False` in production
- ✅ `SECRET_KEY` stored in environment variables
- ✅ `ALLOWED_HOSTS` restricted to your domains
- ✅ `CORS_ALLOWED_ORIGINS` restricted
- ✅ `SECURE_SSL_REDIRECT=True` in production
- ✅ `SESSION_COOKIE_SECURE=True`
- ✅ `CSRF_COOKIE_SECURE=True`
- ✅ `SECURE_HSTS_SECONDS=31536000`

---

## 📝 Important Notes:

1. **SQLite → PostgreSQL**: Local uses SQLite, production uses PostgreSQL
2. **Environment Variables**: Always use .env files, never hardcode secrets
3. **Static Files**: WhiteNoise handles static file serving in production
4. **Migrations**: Automatic via Procfile release command
5. **Logs**: Check platform dashboard for error logs

---

## 🆘 Troubleshooting:

### Static files not loading?
```bash
python manage.py collectstatic --noinput
```

### Database connection issues?
- Verify environment variables are set correctly
- Check database credentials
- Ensure firewall allows connections

### 404 on API endpoints?
- Check ALLOWED_HOSTS includes your domain
- Verify DNS points to platform

---

## 📚 Useful Resources:

- [Render Django Deployment](https://render.com/docs/deploy-django)
- [Railway Django Deployment](https://docs.railway.app)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
