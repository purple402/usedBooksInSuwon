from flask import Flask, render_template, request
from aladdin import get_books as get_books_aladdin
from lib import get_books as get_books_lib


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/report')
def report():
    lib = request.args.get('lib')
    searchword = request.args.get('searchword')
    books = []
    aladdin_books = get_books_aladdin(searchword)
    lib_books = get_books_lib(searchword, lib)
    books = aladdin_books + lib_books
    return render_template('report.html', searchword = searchword, lib = lib, books = books)

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)