# Young Lions Crying At War:: Ameer Alnasser, Yat Long Chan, Wilson Mach
# SoftDev pd 8
# K08: Flask stuff
# 2022-10-6


from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? this will go to the terminal for every refresh of the webpage
    return "No hablo queso!"

app.run()

