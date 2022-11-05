#Luigi (he/they):: Yat Long Chan, Brian Wang
#SoftDev pd 8
#K19: Give me all your login info pwease
#2022-11-03
#time spent:  hours

from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
#hard-coded login
user = "frodo"
passwd = "baggins"
app.secret_key="HI"

@app.route('/', methods=['GET'])
def disp_login():
    
    if 'username' in session:
        return redirect('/auth')
    return render_template('login.html')
    


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    if request.method == 'GET':
        return render_template('auth.html')

    if request.method == 'POST':
        if request.form['username'] == user and request.form['password'] == passwd:
            session['username']=request.form['username']
            return render_template('auth.html')
        elif request.form['username'] != user and request.form['password'] != passwd:
            return render_template('login.html', status="Incorrect Username and Password")
        elif request.form['username'] != user:
            return render_template('login.html', status="Incorrect Username")
        elif request.form['password'] != passwd:
            return render_template('login.html', status="Incorrect Password")

@app.route("/logout", methods=['POST'])
def logout():
    #wipe login info cookies
    session.pop('username', None)
    return redirect('/')

if __name__ == "__main__":
    app.debug = True
    app.run()