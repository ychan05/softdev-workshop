from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def main():
    api_key = open('key_nasa.txt').read() 
    url = 'https://api.nasa.gov/planetary/apod?api_key=' + api_key
    result = requests.get(url).json()
    return render_template('main.html', img_link=result.get('url'), expl=result.get('explanation'))



if __name__ == '__main__':
    app.debug = True
    app.run()