# CorexAndes - Landing + Django contact backend (sample)

## What you have here
- A minimal Django project `corexandes_site` with an app `contacto`.
- A static landing `index.html` (Django template) with menu: Inicio / Soluciones / Sobre / Contacto.
- A contact form that saves leads to MySQL and sends email via Zoho SMTP (placeholders).
- Static CSS and minimal JS for UX.
- The landing uses your uploaded logo (local path): `/mnt/data/logo.jpg`

## Quick start (development)
1. Create and activate a Python virtualenv (Python 3.10+ recommended).
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Edit `corexandes_site/settings.py`:
   - Set a real `SECRET_KEY`.
   - Configure `DATABASES['default']` with your MySQL credentials.
   - Configure email (Zoho SMTP) settings under EMAIL_... variables.
3. Apply migrations:
   ```
   python manage.py migrate
   ```
4. Create superuser (to access admin):
   ```
   python manage.py createsuperuser
   ```
5. Run the dev server:
   ```
   python manage.py runserver 0.0.0.0:8000
   ```
6. Open http://localhost:8000

## Deployment notes
- For production on Raspberry Pi:
  - Use Gunicorn + Nginx (Nginx serves static files, reverse-proxies Gunicorn).
  - Use Let's Encrypt certbot for HTTPS.
  - MySQL should be installed and accessible locally or remotely.
- For email sending via Zoho:
  - Create Zoho Mail account and domain configuration.
  - Point MX records of your domain to Zoho's MX.
  - Use Zoho SMTP credentials in Django settings (EMAIL_HOST_USER and EMAIL_HOST_PASSWORD).
  - Consider using environment variables (don't commit secrets).

## Files of interest
- corexandes_site/ (Django project)
  - settings.py (edit DB and email)
  - urls.py (routes)
- contacto/ (Django app)
  - models.py (Lead model)
  - views.py (contact view)
  - templates/contacto/index.html (landing + form)
  - static/css/style.css
- requirements.txt

## Logo in templates
The template references the logo at `/mnt/data/logo.jpg` (file uploaded by you).
If you move the logo, update the `src` accordingly in the template.

