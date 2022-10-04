'''
TLOTFP1 Henry Bach, Donald Bi, Yat Long Chan
SoftDev
K07 -- something about flask
2022-10-3
time spent: 0.2 hour(s)
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
-__NAME__ is an object in regular python
-"No hablo queso!" is put into the body of the html script.
QCC:
0. This looks like initializing an object in java.
1. / is usually used for separating directories. '/' on its own is also referring to the current directory.
2. It prints to the terminal.
3. It prints '__main__' but we're not sure why.
4. This will print on the live server. We know because we ran it.
5. .run() is similar to netlogo/processing run.
...

INVESTIGATIVE APPROACH:
We thought about the languages we've learned collaboratively.
We also ran the code and visited the live server demo to see what's on it.
We inspected the web server to see what's on the html.
'''
