from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
import json

app = Flask(__name__)
app.secret_key = 'LOGIN-FORM'

AUTH_SERVICE_URL = 'http://localhost:5000'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        response = requests.post(f'{AUTH_SERVICE_URL}/login', json={
            'username': username,
            'password': password
        })

        if response.status_code == 200:
            token = response.json().get('token')
            session['token'] = token
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        response = requests.post(f'{AUTH_SERVICE_URL}/register', json={
            'username': username,
            'password': password
        })

        if response.status_code == 201:
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        
        else:
            flash('Registration failed. Try different credentials.', 'danger')

    return render_template('register.html')

@app.route('/logout', methods=['POST'])
def logout():
    # Perform the logout action
    if 'token' in session:
        response = requests.post(f'{AUTH_SERVICE_URL}/logout')
        session.pop('token', None)
        flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'token' not in session:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
