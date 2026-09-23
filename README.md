# 🛒 SmartCart

SmartCart is a responsive Flask and MySQL based E-Commerce Web Application designed to provide a simple, secure, and user-friendly online shopping experience.

The application provides separate User and Admin modules with product management, shopping cart operations, order management, Razorpay payment integration, and invoice generation.

---

## 📌 Project Overview

SmartCart is a full-stack E-Commerce web application developed using Python Flask and MySQL.

Users can create an account, browse products, search and filter products, add products to their cart, manage quantities, provide a delivery address, make online payments, view their orders, and download invoices.

Administrators can manage products and product images through a dedicated Admin Dashboard.

The application follows a responsive design approach so that the interface can be used across desktop, tablet, and mobile devices.

---

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

---

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

---

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