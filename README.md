# 💰 Expense Manager

A simple Django-based web application for managing daily expenses.  
It allows users to **create, read, update, and delete (CRUD)** expense records easily.

---

## 🚀 Features
- Add, view, edit, and delete expenses  
- View all expenses in a clean table  
- Store data using **SQLite (default Django database)**  
- Simple and responsive UI (HTML + CSS)  
- Organized folder structure for maintainability  

---

## 🧠 Technologies Used
- **Python 3.10+**
- **Django 5.x**
- **HTML5, CSS3**
- **SQLite (default DB)**

---

## ⚙️ Setup Instructions

### 1️⃣ Create and Activate Virtual Environment
```bash
python -m venv myenv
myenv\Scripts\activate

📦 2️⃣ Install Dependencies

pip install django

🛠️ 3️⃣ Run Migrations

python manage.py makemigrations
python manage.py migrate

💻 4️⃣ Run the Development Server

python manage.py runserver

Then open your browser and go to 👉
http://127.0.0.1:8000/