from flask import Flask, render_template, request, redirect, url_for

App = Flask(__name__)

@App.route('/')

def register():
    return render_template('register.html')
@App.route('/register', methods=['POST'])
def handle_registration():

    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    print(f"Registered with Username: {username}, Email: {email}, Password: {password}")
    return render_template('success.html', username=username)
if __name__ == "__main__":
    App.run(debug=True)