#Luigi (he/they):: Yat Long Chan, Brian Wang
#SoftDev pd 8
#K12: Form(s) Take and Give
#2022-10-17
#time spent: 0.5 hours

from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET'])
def disp_loginpage():
    return render_template( 'login.html' ) #run website with template


@app.route("/response", methods=['POST'])
def authenticate():
    return render_template('response.html', user=request.form['username'], method=request.method)  #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
