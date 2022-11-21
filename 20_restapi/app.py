from flask import Flask, render_template, request

@app.route('/')
def main():
    
    return render_template('main.html')