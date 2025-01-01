from flask import Flask, request, render_template, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Function to initialize the database
def init_db():
    # Establish connection to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create the users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Initialize the database when the app starts
init_db()

# Route to render the user input form
@app.route('/')
def form():
    return render_template('form.html')

# API to handle form submissions
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get data from the form submission
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    message = data.get('message')

    # Ensure all required fields are provided
    if not name or not email or not phone_number or not message:
        return jsonify({'error': 'All fields are required!'}), 400

    # Insert data into the users table
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, email, phone_number, message)
        VALUES (?, ?, ?, ?)
    ''', (name, email, phone_number, message))
    
    # Commit and close the connection
    conn.commit()
    conn.close()

    return jsonify({'success': 'Form submitted successfully!'})

# Route to view the stored data
@app.route('/view-data')
def view_data():
    try:
        # Fetch all user data from the database
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        users = []

    # Render the view_data template with the retrieved user data
    return render_template('view_data.html', users=users)

# Start the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
