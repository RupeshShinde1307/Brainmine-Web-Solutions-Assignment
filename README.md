🧠 Brainmine Web Solutions Assignment

This project is a simple Flask-based web application designed for Brainmine Web Solutions' assignment. It allows users to submit a form with their details (Name, Email, Phone Number, and Message), which are then stored in an SQLite database. Additionally, users can view the stored data through a separate page.



🌟 Features:

📋 Form Submission: Users can submit their details via a form.

💾 Database: All form submissions are stored in an SQLite database for later retrieval.

📊 View Data: A separate page that displays all the submitted user data in a tabular format.

✅ Validation: The form ensures all fields are filled out before submission.



🔧 Technologies Used:

🐍 Flask: A Python-based micro-framework to build the web application.

📦 SQLite: A lightweight database to store user data.

🌐 HTML/CSS/JavaScript: For creating the form and frontend interaction.

🔲 Bootstrap (optional): For simple styling of the form and data table.



📥 Requirements:

To run this project locally, make sure you have the following installed:

Python 3.x

Flask

SQLite3 (should be included with Python)



🚀 Installation:

Clone the repository:

bash

Copy code

git clone https://github.com/username/repository-name.git

cd repository-name

Run the Flask app:

bash

Copy code

python app.py

Navigate to http://127.0.0.1:5000/ in your browser to see the form and start interacting with the application.



🔍 How It Works:

Form Page (/): Users can input their name, email, phone number, and a message. Upon submission, the data is sent to the server and stored in an SQLite database.

View Data Page (/view-data): Displays a table with all the form submissions stored in the database.



🚀 Future Improvements:

Implement advanced form validation 🛠️.

Add authentication for viewing the data 🔐.

Use a more robust database for production (e.g., PostgreSQL, MySQL) 🗄️.

Add error handling and logging 📜.

📝 License:

This project is open-source and available under the MIT License. See the LICENSE file for more information.
