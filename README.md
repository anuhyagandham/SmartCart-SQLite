# 🛒 SmartCart

SmartCart is a responsive E-Commerce Web Application developed using Python Flask and SQLite. It provides a simple and user-friendly online shopping experience with separate User and Admin modules.

## 📌 Project Overview

SmartCart allows users to:

- Create an account
- Verify their account using OTP
- Login securely
- Browse products
- Search and filter products
- Add products to cart
- Manage product quantities
- Provide delivery address
- Make online payments using Razorpay
- View previous orders
- Download invoices

Administrators can manage products, product images, and their profile through a dedicated Admin Dashboard.

The application is designed to work across desktop, tablet, and mobile devices.

## ✨ Features

### 👤 User Features

- User Registration
- OTP Verification
- User Login
- User Dashboard
- Browse Products
- Search Products
- Filter Products by Category
- View Product Details
- Add Products to Cart
- Increase Product Quantity
- Decrease Product Quantity
- Remove Products from Cart
- Select Products for Checkout
- Delivery Address Management
- Razorpay Payment Integration
- Payment Confirmation
- My Orders
- View Order Details
- Download Invoice
- User Logout

### 👨‍💼 Admin Features

- Admin Registration
- OTP Verification
- Admin Login
- Admin Dashboard
- Add Products
- Upload Product Images
- View Product Details
- Update Products
- Delete Products
- Search Products
- Filter Products by Category
- Admin Profile Management
- Profile Image Upload
- Admin Logout

## 💳 Payment Integration

SmartCart uses Razorpay for online payment processing.

### Payment Flow

```text
Select Products
       ↓
Shopping Cart
       ↓
Delivery Address
       ↓
Razorpay Checkout
       ↓
Payment Verification
       ↓
Order Confirmation
       ↓
My Orders
       ↓
Download Invoice
```

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap

### Backend

- Python
- Flask

### Database

- SQLite

### Payment

- Razorpay

### Security

- Bcrypt Password Hashing
- Session-based Authentication

### Other Tools

- Git
- GitHub
- VS Code

## 📂 Project Structure

```text
SmartCart/
│
├── app.py
├── config.py
├── init_db.py
├── migrate_mysql_to_sqlite.py
├── requirements.txt
├── schema.sql
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── admin_uploads/
│   │
│   └── uploads/
│       └── product_images/
│
├── templates/
│   ├── admin/
│   ├── user/
│   ├── index.html
│   └── welcome.html
│
└── utils/
    └── pdf_generator.py
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/anuhyagandham/SmartCart-SQLite.git
```

### 2. Open the Project

```bash
cd SmartCart-SQLite
```

### 3. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Initialize the SQLite Database

```bash
python init_db.py
```

### 7. Run the Application

```bash
python app.py
```

### 8. Open in Browser

```text
http://127.0.0.1:5000/
```

## 🔐 Security

Sensitive configuration files and local database files are excluded from GitHub using `.gitignore`.

The following files are not committed to the repository:

- `config.py`
- `smartcart.db`
- `*.db`
- `.env`
- Virtual environment files

Passwords are protected using Bcrypt hashing.

## 🌐 Deployment

The SmartCart application is designed to be deployed using PythonAnywhere with SQLite as the database.

The deployment process includes:

- GitHub repository setup
- PythonAnywhere configuration
- Virtual environment setup
- Dependency installation
- SQLite database setup
- Flask WSGI configuration
- Web application deployment

## 👩‍💻 Author

**Anuhya Gandham**

Python Full Stack Trainee

GitHub: https://github.com/anuhyagandham

## 📄 License

This project was developed as an academic/project demonstration.