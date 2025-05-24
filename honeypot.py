from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

# HTML for fake login
login_page = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login</title>
  <style>
    body {
      background-color: #51e2f5;
      font-family: Times New Roman, sans-serif;
      display: flex;
      height: 100vh;
      justify-content: center;
      align-items: center;
    }

    .login-box {
      background-color: #9df9ef;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      width: 300px;
    }

    h2 {
      text-align: center;
      margin-bottom: 20px;
    }

    input[type="text"], input[type="password"] {
      width: 100%;
      padding: 10px;
      margin: 8px 0;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    input[type="submit"] {
      width: 100%;
      background-color: #4CAF50;
      color: white;
      padding: 10px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-weight: bold;
    }

    input[type="submit"]:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <div class="login-box">
    <h2>LOGIN</h2>
    <form method="POST">
      <label>Username:</label>
      <input type="text" name="username" required /><br />
      <label>Password:</label>
      <input type="password" name="password" required /><br />
      <input type="submit" value="Submit" />
    </form>
  </div>
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def login():
    ip = request.remote_addr
    now = datetime.datetime.now()
    with open("honeypot_log.txt", "a") as log:
        log.write(f"[{now}] IP: {ip}, Method: {request.method}, Path: {request.path}\n")
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            log.write(f"    Username: {username}, Password: {password}\n")
    return render_template_string(login_page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
