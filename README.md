# Inventory Management System

This is an Inventory Management System built with Flask and MySQL. It allows users to manage products, suppliers, and orders through a web-based interface.

## Features

- **Product Management**: Add, edit, and delete products with details such as name, quantity, price, and supplier.
- **Supplier Management**: Manage supplier details including name and contact information.
- **Order Management**: Track orders with information such as product ID, order date, and quantity.

## Project Structure

/smart_inventory_management
├── app/
│   ├── __init__.py          # Initialize the Flask app
│   ├── routes.py            # Define all the routes (e.g., add item, delete item)
│   ├── models.py            # Define the database models (e.g., Product, Supplier)
│
├── static/
│   ├── css/
│   │   └── styles.css       # Custom styles
│   └── js/
│       └── scripts.js       # Optional JS for interactivity
│
├── templates/
│   ├── base.html            # Base layout template
│   ├── dashboard.html       # Inventory dashboard template
│   ├── add_item.html        # Add new item form template
│   ├── edit_item.html       # Edit item form template
│
├── config.py                # Configuration for database and secret keys
├── test_mysql_connection.py           
├── run.py 
├── run.py                   # Main entry point to run the Flask app
├── requirements.txt         # List of dependencies for the project
└── README.md                # Project documentation




## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/inventory_management_app.git
   cd inventory_management_app


2. **Create a virtual environment (optional but recommended)**:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3. **Install dependencies**:
pip install -r requirements.txt


4. **Set up MySQL Database**:

Create a database (e.g., inventory_db) in MySQL.

Update your database configuration in app/__init__.py or in a separate config file.

Initialize the database tables using the **SQL script**:

CREATE TABLE Suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255)
);

CREATE TABLE Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INT DEFAULT 0,
    price DECIMAL(10, 2),
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(id)
);

CREATE TABLE Orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES Products(id)
);

5. **Run the application**:
flask run


**Usage**
Dashboard: View all products, suppliers, and orders.
Edit Item: Click on an item to edit its details.
Delete Item: Delete an item from the dashboard.
