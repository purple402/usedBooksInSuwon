from flask import Flask

app = Flask("Used Books in Suwon")

@app.route('/')
def home():
    return 'hello world'

app.run(host="127.0.0.1", debug=True)