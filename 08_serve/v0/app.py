# Young Lions Crying At War:: Ameer Alnasser, Yat Long Chan, Wilson Mach
# SoftDev pd 8
# K08: Flask stuff
# 2022-10-6

from flask import Flask
app = Flask(__name__) # constructs an "instance" of Flask called app

@app.route("/") # finds directory for app
def hello_world():
    print(__name__) # unsure why
    return "No hablo queso!"  # would be returned on the webpage of 127.0.0.1

app.run()  # runs the webpage


#we got this line 127.0.0.1 - - [06/Oct/2022 13:43:47] "GET /favicon.ico HTTP/1.1" 404 - in a certain instance, and dont know how to replicate
