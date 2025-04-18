# 📚 Library Manager - CLI Book Collection Tool

**Library Manager** is a simple command-line application built in Python using Object-Oriented Programming (OOP) principles. It helps you manage your personal book collection — add, update, delete, search books, and track your reading progress!

---

## ✨ Features

- ✅ Add new books to your collection  
- ❌ Delete books by title  
- 🔍 Search books by title or author  
- ✏️ Update book details (title, author, year, read status)  
- 📖 View complete book collection  
- 📊 Track your reading progress  
- 💾 Saves data persistently in a JSON file (`books_data.json`)  

---

## 🚀 How to Use

1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/library-manager.git
   cd library-manager

**Run the program**
python your_script_name.py

**Follow the menu prompts to manage your collection:**
Welcome to Your Book Collection Manager!
1. Add a new book
2. Remove a book
3. Search for books
4. Update book details
5. View all books
6. View reading progress
7. Exit


# How It Works

All book data is stored in books_data.json.
Each book has:
title
author
year
read (boolean: True/False)

Uses simple file I/O and JSON to persist data.

# File Structure
📦 library-manager/
 ┣ 📄 books_data.json
 ┗ 📄 library_manager.py 


🛠️ Built With
Python 3.x
JSON for data storage
OOP (Classes & Methods)
