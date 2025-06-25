
# 🧰 django-goodies

A collection of reusable Django utilities and plug-and-play apps — designed to save you time and make your projects cleaner, faster, and more maintainable.

Includes:
- 🔍 HTMX integration helpers
- 🔠 Autocomplete widgets for Django forms
- 📝 Markdown renderer + editor widget
- 🔐 Lightweight extended authentication tools

---

## 🚀 Installation

Install directly from PyPI (or your local setup):

```bash
pip install django-goodies
````

No extras needed — everything is bundled and ready to go.

---

## 📦 Included Apps

| App            | Description                                                                          |
| -------------- | ------------------------------------------------------------------------------------ |
| `htmx`         | Middleware, decorators, and helpers for HTMX detection, partial responses, etc.      |
| `autocomplete` | Form widgets + HTMX views for async model lookups and field autocompletion           |
| `djmarkit`     | Markdown rendering utilities + a beautiful JS markdown editor widget (HTMX-enhanced) |
| `xauth`        | Lightweight "extended auth" system (token views, utils) with optional OAuth hooks    |

---

## ⚙️ Usage

### Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "django_goodies.autocomplete",
    "django_goodies.djmarkit",
    "django_goodies.htmx",
    "django_goodies.xauth",
]
```

### Include static files:

```bash
python manage.py collectstatic
```

---

## 📚 Documentation

Documentation coming soon!

For now, check out the individual modules inside `django_goodies/`.

---

## 🧪 Development

To run locally:

```bash
git clone https://github.com/yourusername/django-goodies.git
cd django-goodies
python -m venv venv
source venv/bin/activate
pip install -e .
```

To run tests:

```bash
pytest
```

---
