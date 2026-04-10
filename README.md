# LifeVault

A centralized personal information management system. Store, organize, and quickly retrieve important life data — health records, insurance, home maintenance, finances, pets, and more — in one secure place.

**Stack:** Django · PostgreSQL · Python

---

## Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/LifeVault.git
cd LifeVault
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your database credentials and secret key
```

### 5. Create the PostgreSQL database
```sql
CREATE DATABASE lifevault;
```

### 6. Run migrations
```bash
python manage.py migrate
```

### 7. (Optional) Create a superuser
```bash
python manage.py createsuperuser
```

### 8. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## Project Structure

```
lifevault/
├── lifevault/          # Project config (settings, urls, wsgi)
├── accounts/           # Auth: register, login, logout
├── core/               # Dashboard, landing page
├── templates/          # HTML templates
│   ├── base.html
│   ├── app_shell.html
│   ├── accounts/
│   └── core/
├── static/
│   ├── css/main.css
│   └── js/main.js
├── manage.py
├── requirements.txt
└── .env.example
```

