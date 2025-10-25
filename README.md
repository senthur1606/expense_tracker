## 💰 Expense Manager

A simple Django-based web application for managing daily expenses.
It allows users to create, read, update, and delete (CRUD) expense records, view category-wise summaries, and export reports as Excel or PDF files.
---

## 🚀 Features
- Add, view, edit, and delete expenses

- View all expenses in a clean, responsive table

- Generate category-wise summary reports

- Export expense summary as Excel (.xlsx) or PDF (.pdf)

- Confirmation prompt before deleting any expense

- Store data using SQLite (default Django database, can use PostgreSQL or MongoDB)

- Modern, responsive UI with HTML + CSS

- Organized folder structure for maintainability  

---

## 🧠 Technologies Used
- **Python 3.10+**
- **Django 5.x**
- **HTML5, CSS3**
- **SQLite (default DB)**
- **openpyxl for Excel export**
- **xhtml2pdf for PDF generation**

---

## ⚙️ Setup Instructions

## 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd expense_manager

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv myenv
# Windows
myenv\Scripts\activate

# Mac/Linux
source myenv/bin/activate

📦 3️⃣ Install Dependencies

pip install django

🛠️ 4️⃣ Run Migrations

python manage.py makemigrations
python manage.py migrate

💻 5️⃣ Run the Development Server

python manage.py runserver

Then open your browser and go to 👉
http://127.0.0.1:8000/