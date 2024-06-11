from flask import Flask, render_template, request, redirect, url_for
from google.cloud import firestore
import google.auth

app = Flask(__name__)

# Initialize Firestore DB
db = firestore.Client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        db.collection('users').add(user_data)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db.collection('users').where('email', '==', email).where('password', '==', password).get()
        if user:
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/set_alert', methods=['POST'])
def set_alert():
    alert_data = {
        'user_email': request.form['email'],
        'stock_symbol': request.form['stock_symbol'],
        'threshold': float(request.form['threshold'])
    }
    db.collection('alerts').add(alert_data)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
