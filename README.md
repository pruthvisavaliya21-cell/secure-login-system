# 🔐 Secure Login System with Role-Based Access (Flask)

## 📌 Project Overview
This project is a secure web-based login system developed using Flask (Python). It implements user authentication, authorization, and role-based access control (RBAC) with a modern user interface and CAPTCHA verification for basic security.

---

## 🚀 Features

- User Registration and Login
- Role-Based Access Control (Admin/User)
- CAPTCHA Verification (Bot protection)
- Session Management
- Modern UI using HTML and CSS
- Input validation and duplicate user prevention

---

## 🛠️ Technologies Used

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS
- **Security Concepts:** Authentication, Authorization, CAPTCHA

---

## 📁 Project Structure

secure-login/
│
├── app.py
├── requirements.txt
│
├── templates/
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── admin.html
│
├── static/
│ └── style.css

---

## ▶️ How to Run the Project

### 1. Clone the Repository

git clone https://github.com/your-username/Secure_Login_System.git

cd Secure_Login_System


### 2. Install Dependencies

pip install -r requirements.txt


### 3. Run the Application

python app.py


### 4. Open in Browser

http://127.0.0.1:5000


---

## 🔐 How It Works

1. User registers with username, email, password, and role.
2. User logs in with credentials.
3. CAPTCHA verification is required during login.
4. Based on role:
   - Admin → redirected to Admin Dashboard
   - User → redirected to User Dashboard

---

## 📸 Screenshots

- Login Page  
- Register Page  
- Admin Dashboard  
- User Dashboard  

---

## ⚠️ Limitations

- No database used (data stored in memory)
- Passwords are stored in plain text (not secure for production)

---

## 🔮 Future Improvements

- Add MySQL or MongoDB database
- Implement password hashing (bcrypt)
- Add JWT authentication
- Add account lock after multiple failed attempts
- Improve UI with advanced components

---

## 👨‍💻 Author

Pruthvi Savaliya  
GitHub: https://github.com/pruthvisavaliya21-cell

---

## 📌 Conclusion

This project demonstrates the implementation of authentication and role-based access control using Flask. It is designed for learning and academic purposes and can be extended into a production-level system with additional security features.

---
✅ WHY THIS VERSION IS BEST

✔ Clean and professional
✔ Easy to read
✔ Perfect for college submission
✔ Covers all required points
✔ Not over-designed (teachers prefer this)

🚀 FINAL STEP

Run:

git add README.md
git commit -m "Added final README"
git push
