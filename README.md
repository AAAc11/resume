# Portfolio Website

A personal portfolio website built with Django and styled with Tailwind CSS. Projects are managed through Django's admin panel and stored in a database.

The included SQLite database already contains my actual content.

## Features

- Responsive navigation with mobile menu
- Projects loaded dynamically from the database via Django admin
- Copy-to-clipboard email contact
- Custom SVG favicon and icons

## Tech Stack

- **Backend:** Python, Django
- **Styling:** Tailwind CSS
- **Database:** SQLite

## Setup / Running Locally

1. Clone the repository:

```git clone https://github.com/AAAc11/resume.git```

```cd resume```

2. Install dependencies:

```pip install -r requirements.txt```

3. Create a `.env` file in the project root with your own secret key:

```SECRET_KEY=your-generated-key-here```

(Generate one with: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)

4. Run migrations:

```python manage.py migrate```

5. Start the server:

```python manage.py runserver```

6. To rebuild Tailwind CSS after making style changes:

```npx @tailwindcss/cli -i ./cv/static/cv/src/input.css -o ./cv/static/cv/home_page.css --watch```
