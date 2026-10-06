# 🌍 Translator App

A simple and user-friendly **Translator Web Application** built using Django and Googletrans.

This application allows users to enter text, select the source and target languages, and instantly translate the text into the selected language.

## ✨ Features

- 🌐 Translate text between multiple languages
- 📝 Simple and clean user interface
- 🔄 Select source and target languages
- ⚡ Fast translation using Googletrans
- 📱 Responsive design
- 🎨 Modern gradient-based UI
- 🔐 Django CSRF protection

## 🛠️ Technologies Used

- Python
- Django
- Googletrans
- HTML
- CSS

## 🌎 Supported Languages

- English
- Hindi
- French
- Spanish
- German
- Italian
- Japanese
- Korean
- Chinese

## 📂 Project Structure

```text
translator_app/
│
├── translator/
│   ├── migrations/
│   ├── templates/
│   │   └── translator/
│   │       └── index.html
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── admin.py
│
├── translator_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md