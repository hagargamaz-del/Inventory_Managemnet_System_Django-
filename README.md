# Invento

<div align="center">


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Django Version](https://img.shields.io/badge/Django-5.1.1-green.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

A modern inventory management system built with Django
</div>

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## 🎯 Overview

Invento is a robust inventory management system designed to help businesses efficiently track and manage their inventory, orders, and staff. Built with Django and modern web technologies, it provides a user-friendly interface for managing products, processing orders, and maintaining staff records.

## ✨ Features

### User Management
- Secure authentication system
- Role-based access control
- Staff profile management
- Password reset functionality via email

### Product Management
- Add, update, and delete products
- Product categorization (Stationary, Electronics, Food)
- Real-time quantity tracking
- Product search and filtering

### Order Management
- Create and process orders
- Order status tracking
- Order history
- Basic analytics and reporting

### Dashboard
- Intuitive admin interface
- Real-time inventory updates
- Staff activity monitoring
- Responsive design for all devices

## 📋 Requirements

- Python 3.x
- Django 5.1.1
- Other dependencies listed in `requirements.txt`

## 💻 Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/invento.git
cd invento
```


2. Install dependencies
```bash
pip install -r requirements.txt
```


3. Run migrations
```bash
python manage.py migrate
```

4. Create superuser
```bash
python manage.py createsuperuser
```

5. Start development server
```bash
python manage.py runserver
```

## 📱 Usage

1. **Admin Dashboard**
   - Access at `/admin/`
   - Manage all system aspects
   - View analytics and reports

2. **Staff Management**
   - Register new staff members
   - Manage staff profiles
   - Set permissions and roles

3. **Inventory Management**
   - Add/Edit products
   - Track stock levels
   - Manage categories

4. **Order Processing**
   - Create new orders
   - Update order status
   - View order history

## 📖 API Documentation

API endpoints are available at `/api/v1/`:

- `/api/v1/products/` - Product management
- `/api/v1/orders/` - Order management
- `/api/v1/users/` - User management


---

