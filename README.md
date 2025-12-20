### BudgetFlow – Personal Finance & Expense Tracking API

BudgetFlow is a RESTful backend API for managing personal finances. It allows authenticated users to track their incomes and expenses, create custom expense categories, view their financial analytics, and monthly summaries, making financial insights easy. This project is built using Django and Django REST Framework, with MySQL as the database.

## Features:

# Authentication
Token-based authentication
Secure user registration & login
Protected endpoints

# Expense Management
Create expenses
View expenses
Update & delete expenses

# Income Management
Create income records
List incomes
Update & delete incomes

# Category Management
Create categories (e.g., Food, Housing, Transport)
List categories
Update & delete categories

# Analytics
Overall analytics
Monthly financial summary
Balance calculations
Top 3 spending categories

# Tech Stack
Backend: Django, Django REST Framework
Database: MySQL
Authentication: Token Authentication
Environment: Python 3+

## Project Structure (Key Apps)
budgetflow_project/
│
├── accounts/      -> Authentication & User Management
├── income/        -> Income APIs
├── expense/       -> Expense APIs
├── category/      -> Category APIs
├── analytics/     -> Analytics & Summary APIs
└── budgetflow_db  -> MySQL Database


## Installation & Setup

# Clone Repository
mkdir budgetflow_project
cd budgetflow_project
git clone https://github.com/DannyTechStudio/ALX_BE_Capstone_Project.git

# Create Virtual Environment
python -m venv env
source env/bin/activate     # macOS/Linux
env\Scripts\activate        # Windows

## Install Dependencies
pip install -r requirements.txt

## Configure Database (MySQL)
Update your settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'budgetflow_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

## Run Migrations
python manage.py migrate

## Run Server
python manage.py runserver

API now runs at:
http://127.0.0.1:8000/

# Authentication
All endpoints require authenticated users.
Send your token as:
Authorization: Token <your-token>

Base Path: /api/auth/

Method:	    Endpoint:	    Description:
POST	    /register/	    Register a new user
POST	    /login/	        Login a user
GET	        /profile/	    Authenticated user profile
PATCH	    /profile/       Edit user profile - username and default currency only
POST	    /login/	        Login user

# Category Endpoints
Base Path: /api/

Method:	    Endpoint:               Description:
POST	    /categories/            Create category
GET	        /categories/            List all categories
GET	        /categories/<id>/       Get a single category
PATCH	    /categories/<id>/       Edit a category
DELETE	    /categories/<id>/       Delete a category


# Income Endpoints
Base Path: /api/

Method:	    Endpoint:	        Description:
POST	    /income/	        Create an income instance
GET	        /income/	        List user incomes
GET	        /income/<id>/	    Get an income instance
PUT/PATCH	/income/<id>/	    Update an income
DELETE	    /income/<id>/	    Delete an income

# Expense Endpoints
Base Path: /api/

Method:	    Endpoint:	        Description:
POST	    /expense/	        Create an expense
GET	        /expense/	        List all user's expenses
GET	        /expense/<id>/	    Get a single expense
PUT/PATCH	/expense/<id>/	    Update
DELETE	    /expense/<id>/	    Delete

# Analytics Endpoints
Base Path: /api/analytics/

# Overall Analytics
GET /api/analytics/overall/

Returns:
total income
total expense
balance
top 3 spending categories

# Monthly Summary
GET /api/analytics/summary/

Optional Query Params:
Param:	        Meaning:
month	        specific month
year	        specific year

# Examples
Current month summary:
GET /api/analytics/summary/

Specific month summary:
GET /api/analytics/summary/?month=2&year=2025