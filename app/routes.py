from flask import Blueprint, request, redirect, url_for, render_template, flash
from app import mysql  # Ensure `mysql` is imported from the initialized instance
import MySQLdb

app_routes = Blueprint('app_routes', __name__)

# Home route, redirecting to the dashboard
@app_routes.route('/')
def index():
    return redirect(url_for('app_routes.dashboard'))


@app_routes.route('/dashboard')
def dashboard():
    try:
        print("Accessing database cursor...")
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Products")
        items = cursor.fetchall()
        cursor.close()
        print("Rendering dashboard template...")
        return render_template('dashboard.html', items=items)
    except Exception as e:
        print("General error loading dashboard:", e)  # More specific error logging
        return "Error loading dashboard", 500




# Route to display the form for adding a new item
@app_routes.route('/add_item', methods=['GET'])
def add_item_form():
    return render_template('add_item.html')

# Route to add a new item to the database
@app_routes.route('/add_item', methods=['POST'])
def add_item():
    try:
        name = request.form['name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        supplier_id = int(request.form['supplier_id'])

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Products (name, quantity, price, supplier_id) VALUES (%s, %s, %s, %s)",
            (name, quantity, price, supplier_id)
        )
        mysql.connection.commit()
        cursor.close()
        # flash("Item added successfully!")
        return redirect(url_for('app_routes.dashboard'))
    except Exception as e:
        print("Error adding item:", e)
        return "Error adding item to the database", 500

# Route to display the form for editing an existing item
@app_routes.route('/edit_item/<int:id>', methods=['GET'])
def edit_item_form(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Products WHERE id = %s", (id,))
        item = cursor.fetchone()
        cursor.close()
        return render_template('edit_item.html', item=item)
    except Exception as e:
        print("Error loading edit form:", e)
        return "Error loading edit form", 500

# Route to update an existing item in the database
@app_routes.route('/edit_item/<int:id>', methods=['POST'])
def edit_item(id):
    try:
        name = request.form['name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])

        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE Products SET name=%s, quantity=%s, price=%s WHERE id=%s",
            (name, quantity, price, id)
        )
        mysql.connection.commit()
        cursor.close()
        flash("Item updated successfully!")
        return redirect(url_for('app_routes.dashboard'))
    except Exception as e:
        print("Error updating item:", e)
        return "Error updating item", 500

# Route to delete an item from the database
@app_routes.route('/delete_item/<int:id>', methods=['POST'])
def delete_item(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM Products WHERE id=%s", (id,))
        mysql.connection.commit()
        cursor.close()
        flash("Item deleted successfully!")
        return redirect(url_for('app_routes.dashboard'))
    except Exception as e:
        print("Error deleting item:", e)
        return "Error deleting item", 500
