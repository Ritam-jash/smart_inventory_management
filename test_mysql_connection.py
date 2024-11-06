from flask import Flask
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = '_inventory_'

mysql = MySQL(app)

with app.app_context():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        print("Successfully connected to the database:", db_name[0])
    except MySQLdb.Error as e:
        print("Database connection error:", e)
    finally:
        cursor.close()
