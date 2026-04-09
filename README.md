# 📚 Comic Dataset Processing Application

## 📖 Overview

This project is a Python-based dataset processing application developed to analyze and manage a large comic book dataset.  
The system allows users to filter, search, group, sort, and analyse comic records efficiently.

It demonstrates the use of **Object-Oriented Programming (OOP)**, **SOLID principles**, and clean architecture design.

---

## 🚀 Features

- 📥 Load large dataset (47,000+ records)
- 🔎 Filter comics by genre
- 🔍 Search functionality:
  - Simple search (by title)
  - Advanced search (author, year, genre)
- 📊 Group comics:
  - By Author
  - By Year of Publication
- 🔃 Sort results:
  - Alphabetically (A–Z / Z–A)
- 🧹 Data cleaning:
  - Handles missing ISBN values
  - Cleans special characters
  - Processes multi-value fields
- 🔗 Merge duplicate records into single entries
- 💾 Save selected results temporarily
- 📈 Analytics:
  - Top search queries
  - Most viewed results

---

## 🧠 Technologies Used

- Python
- Object-Oriented Programming (OOP)
- SOLID Principles
- CSV Data Processing
- Pytest (for testing)

---

## 📂 Project Structure

project/  
├── controller/  
│   └── app_controller.py  
├── data/  
│   └── names.csv  
├── models/  
│   └── comic.py  
├── services/  
│   ├── data_loader.py  
│   ├── filter_service.py  
│   ├── search_service.py  
│   ├── sort_service.py  
│   └── group_service.py  
├── main.py  
└── tests/  
    └── test_services.py

---

## ▶️ How to Run

```bash
python main.py
```

### 🧪 Testing

pytest

### 📸 Sample Output

📚 Loading dataset...
Total Records Loaded: 47626

🔎 Filtering by genre: Fiction
🔍 Search Results: 923

📂 Group: 2020

1. Zombie Tramp | Nicole D'Andria | 2020 | Horror
