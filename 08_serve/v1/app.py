# Young Lions Crying At War:: Ameer Alnasser, Yat Long Chan, Wilson Mach
# SoftDev pd 8
# K08: Flask stuff
# 2022-10-6

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()
 
# We noticed there was no print statement printing out the instance of Flask, which was named __main__
