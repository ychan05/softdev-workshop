#Luigi (he/they):: Yat Long Chan, Brian Wang
#SoftDev pd 8
#K12: Form(s) Take and Give
#2022-10-17
#time spent: 0.5 hours

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not.
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/", methods=['GET'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) #prints the app running the request (Flask)
    print("***DIAG: request obj ***")
    print(request) #prints the server that app.py is running on
    print("***DIAG: request.form ***")
    #print(request.args) #returns the dictionary in which the args are stored
    print(request.form)
    #print("***DIAG: request.form['username']  ***")
    #print(request.form['username']) #code returns an error when ran because arg
                                      #argument requested doesn't exist
    print("***DIAG: request.headers ***")
    print(request.headers) # returns data about the webpage (operating system, web browser, etc.)
    return render_template( 'login.html' ) #run website with template


@app.route("/auth", methods=['POST'])
def authenticate():
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.form ***")
    #print(request.args)
    #print(request.form)
    #print("***DIAG: request.form['username']  ***")
    name=request.form['username'] #returns username entered
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template('response.html')  #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
