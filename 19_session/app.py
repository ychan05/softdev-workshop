#Luigi (he/they):: Yat Long Chan, Brian Wang
#SoftDev pd 8
#K19: Give me all your login info pwease
#2022-11-03
#time spent: 1.5 hours

from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
ex_user = "mykolyk"
ex_pass = "foofoo"
app.secret_key="HI" #dummy key

@app.route('/', methods=['GET'])
def disp_login():
    if 'username' in session:
        return redirect('/auth')
    return render_template('login.html')
    
@app.route("/auth", methods=['POST'])
def authenticate():
    if request.method == 'GET':
        return render_template('response.html')

    if request.method == 'POST':
        #print(request.form)
        if request.form['username'] == ex_user and request.form["password"] == ex_pass:
            session['username']=request.form['username']
            return render_template('response.html')
        return render_template('login.html', status="Incorrect login info")

@app.route("/logout", methods=['GET'])
def logout():
    #wipe login info cookies
    session.pop('username')
    return redirect('/')

if __name__ == "__main__":
    app.debug = True
    app.run()