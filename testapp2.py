from flask import Flask, redirect,render_template,request,g,url_for

app = Flask(__name__, static_folder="./templates/kabegami")

@app.route('/')
def index():
    return render_template('about_test_index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')