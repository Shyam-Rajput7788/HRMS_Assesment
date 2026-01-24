# Quick Setup Guide - Development & Production

## ⚡ Super Simple Setup

**Same code works for BOTH development and production - just change ONE variable!**

### 1️⃣ Local Development Setup (5 minutes)

```bash
# Create .env file
cp .env.example .env

# Keep this in .env:
DEBUG=True
SECRET_KEY=anything-you-want

# Install dependencies (one time)
pip install -r requirements.txt

# Run migrations (one time)
python manage.py migrate

# Start server
python manage.py runserver
```

✅ Done! Server running at `http://localhost:8000`

---

### 2️⃣ Production Deployment (Render/Railway)

**Same code, just different environment variables!**

On Render/Railway dashboard, set these environment variables:

```
DEBUG=False
SECRET_KEY=<generate-secure-key>
ALLOWED_HOSTS=yourapp.onrender.com,yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.com

# PostgreSQL credentials (from Render/Railway)
DB_NAME=<from-platform>
DB_USER=<from-platform>
DB_PASSWORD=<from-platform>
DB_HOST=<from-platform>
DB_PORT=5432
```

**That's it!** Platform auto-deploys your code with new environment variables.

---

## 🎯 How It Works (Magic!)

The same `settings.py` code detects `DEBUG` setting and automatically:

| Setting | When `DEBUG=True` | When `DEBUG=False` |
|---------|-------------------|-------------------|
| **Database** | SQLite (local file) | PostgreSQL (production) |
| **Static Files** | Django serves them | WhiteNoise serves them |
| **CORS** | Allow all origins | Restrict to specific domains |
| **Security** | Disabled | Enabled (HTTPS, HSTS, etc.) |

---

## 📋 Minimal Changes Required

### For Development:
- ✅ Nothing! Keep `DEBUG=True` locally

### For Production:
- Change `DEBUG=False`
- Add PostgreSQL credentials
- That's all!

---

## 🔧 Single Code File Structure

```
HRMS_Backend/
├── config/
│   └── settings.py ← ONE file controls everything!
├── Procfile ← Render/Railway reads this
├── requirements.txt ← Same for dev & prod
├── .env.example ← Copy this to .env
└── ... apps
```

---

## 💡 Pro Tips

1. **Generate Secure SECRET_KEY:**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **To test production settings locally:**
   ```bash
   DEBUG=False python manage.py runserver
   ```
   (Requires PostgreSQL running locally)

3. **View current settings:**
   ```bash
   python manage.py shell
   >>> from django.conf import settings
   >>> print(settings.DEBUG)
   ```

---

## ✨ No More Separate Config Files!

❌ **Old approach:** `settings.py`, `settings-prod.py`, `settings-dev.py` (confusing!)
✅ **New approach:** ONE `settings.py` that works everywhere!

