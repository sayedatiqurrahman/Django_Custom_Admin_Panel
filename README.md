# 🚀 Django Unfold Integration Guide

**Unfold** is a beautiful and modern admin UI replacement for Django's default admin. It provides a customizable sidebar, enhanced layouts, theme support, and much more.

This guide will help you:
- ✅ Integrate Unfold into your Django project
- 🎨 Customize the admin layout, sidebar, and theme
- 🧩 Use Unfold components like collapsible nav, badges, and custom logos

---

## 📦 Installation

1. **Install via pip:**

```bash
pip install django-unfold
````

2. **Add to `INSTALLED_APPS` (before `django.contrib.admin`)**:

```python
INSTALLED_APPS = [
    "unfold",  # Must come before admin
    "django.contrib.admin",
    ...
]
```

3. **Update your `settings.py`:**

```python
UNFOLD = {
    "SITE_TITLE": "Custom Admin",
    "SITE_HEADER": "Your Brand",
    "SITE_SUBHEADER": "Welcome to the dashboard",
    "SITE_URL": "/",
    "THEME": "dark",  # or "light"
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_HISTORY": True,

    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Dashboard",
                        "icon": "dashboard",
                        "link": "/admin/",
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": "Comments",
                        "icon": "mark_unread_chat_alt",
                        "link": "/admin/core/comments/",
                        "permission": lambda request: request.user.is_authenticated,
                    },
                ],
            },
        ],
    },
}
```

---

## 🧩 Customizing Admin Panel with Unfold

### 1. **Replace `ModelAdmin` with `UnfoldModelAdmin`**

```python
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from django.contrib import admin
from .models import Comments

@admin.register(Comments)
class CommentAdmin(UnfoldModelAdmin):
    list_display = ('id', 'message')
```

You can also use it with Django’s built-in `UserAdmin` or `GroupAdmin`.

---

### 2. **Customize the Login Page**

To modify Unfold's built-in login page:

#### ✅ Create: `templates/admin/login.html`

```html
{% extends "unfold/admin/login.html" %}

{% block content %}
  {{ block.super }}
  <div style="text-align: center; margin-top: 20px;">
    <a href="{% url 'register' %}" class="text-primary-400 hover:underline">
      Don't have an account? Register here.
    </a>
  </div>
{% endblock %}
```

This adds a register link to the existing Unfold-styled login page.

---

### 3. **Use Your Own Logo and Colors**

```python
from django.templatetags.static import static

UNFOLD["SITE_LOGO"] = {
    "light": lambda request: static("logo/my-logo-light.png"),
    "dark": lambda request: static("logo/my-logo-dark.png"),
}
```

Also customize colors and radius:

```python
UNFOLD["BORDER_RADIUS"] = "8px"
UNFOLD["COLORS"] = {
    "primary": {
        "500": "168, 85, 247",  # purple
        "700": "126, 34, 206",
    },
    ...
}
```

---

## 🗂️ Sidebar Features

### ✅ Features you can use:

* `separator`: Draws a line above the group
* `collapsible`: Group of links can be collapsed
* `badge`: Optional dynamic badge (e.g., for notifications)
* `icon`: Google Material Symbols icon name

Example:

```python
"items": [
    {
        "title": "Users",
        "icon": "group",
        "link": "/admin/auth/user/",
    },
    {
        "title": "Settings",
        "icon": "settings",
        "link": "/admin/config/",
        "badge": lambda request: "New",
    },
],
```

> For supported icons: [https://fonts.google.com/icons](https://fonts.google.com/icons)

---

## 🧪 Extras

### ✅ Add Registration Page

If you're adding a custom registration page:

```python
# urls.py
from .views import register_view

urlpatterns = [
    path("register/", register_view, name="register"),
]
```

Then link it from the login template as shown earlier.

---

## 🎉 Done!

You're now ready to use Unfold as a powerful modern admin dashboard!

### 🔗 Useful Links

* Unfold GitHub: [https://github.com/unfoldadmin/unfold](https://github.com/unfoldadmin/unfold)
* Django Docs: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)

---

## 🧑‍💻 Contribution Tips

* Keep templates in `templates/admin/` to override Unfold easily
* Use Tailwind utility classes if you're doing frontend tweaks
* Use `UnfoldModelAdmin` everywhere to get full benefits


