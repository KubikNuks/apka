# Importing Flask and necessary functions
from flask import Flask, render_template, request

# Creating a new Flask app instance
app = Flask(__name__)

# Defining the route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    name = []
    email = []
    message = []
    if request.method == 'POST':
        # Getting form data when form is submitted
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
    
        
    # Rendering the index.html template for GET requests
    return render_template('index.html', name=name, email=email, message=message)

# Running the app when this file is executed
if __name__ == '__main__':
    app.run(host = '0.0.0.0' , debug=True)
