from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

# In-memory storage (no database)
users = []

# ✅ CAPTCHA FUNCTION (FIXED)
def generate_captcha():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    return a, b, a + b


# ✅ LOGIN PAGE
@app.route('/')
def login_page():
    a, b, ans = generate_captcha()
    session['captcha'] = ans
    return render_template('login.html', a=a, b=b)


# ✅ REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')

        # Validation
        if not username or not email or not password:
            return "❌ All fields are required!"

        # Check duplicate
        for user in users:
            if user['email'] == email:
                return "❌ User already exists!"

        # Save user
        users.append({
            "username": username,
            "email": email,
            "password": password,
            "role": role
        })

        return redirect('/')

    return render_template('register.html')


# ✅ LOGIN LOGIC
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    captcha_input = request.form.get('captcha')

    # CAPTCHA check
    if not captcha_input or int(captcha_input) != session.get('captcha'):
        return "❌ CAPTCHA Incorrect"

    # Authentication
    for user in users:
        if user['email'] == email and user['password'] == password:
            session['user'] = user

            if user['role'] == 'admin':
                return redirect('/admin')
            else:
                return redirect('/dashboard')

    return "❌ Invalid Email or Password"


# ✅ USER DASHBOARD
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html', user=session['user'])


# ✅ ADMIN DASHBOARD
@app.route('/admin')
def admin():
    if 'user' not in session or session['user']['role'] != 'admin':
        return redirect('/')
    return render_template('admin.html', users=users)


# ✅ LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# ✅ RUN APP
if __name__ == '__main__':
    app.run(debug=True)