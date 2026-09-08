# TapTapTyping

A full-featured Django-powered typing tutor website — structured lessons for every row
of the keyboard, typing tests/games, plus a blog and a small jobs board built into the
same platform.

## Features

- **Lesson curriculum** — dedicated lessons for the home row, top row, and bottom row,
  down to individual key-pair drills (e.g. `S` `L`, `Z` `N`, `Q` `U`, `F` `K`)
- **Typing tests & games** — `start_test` and `taptap` typing-speed practice modes
- **Blog** — create, edit, and delete blog posts (`BlogPost` model)
- **Job board** — post and browse job listings (`JobPost` model)
- **Accounts** — user registration/login
- **FAQ, About, Policy** pages

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** Django templates, HTML/CSS/JS

## Project Structure

```
TapTapTyping/    Django project settings, root urls
typingApp/       Lessons, typing tests/games, blog, jobs, static pages
accounts/        Authentication
```

## Running Locally

```bash
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate on Windows
pip install -r requirement.txt
python manage.py migrate
python manage.py runserver
```

## Author

**Md. Asaduzzaman** — Software Developer & Trainer
[Portfolio](https://asad6426.github.io/AsadProfile/) · [LinkedIn](https://www.linkedin.com/in/asad1038/)
