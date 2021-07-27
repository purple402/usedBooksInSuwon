from flask import Flask, render_template, request
from aladdin import get_books as get_books_aladdin
from lib import get_books as get_books_lib


app = Flask(__name__)
library = {
    "ALL": "전체", "MA": "선경", "MB": "중앙", "MC": "영통", "MD": "슬기샘", "ME": "바른샘", "MF": "지혜샘", "MG": "서수원", "MH": "북수원", "MI": "태장마루", "MK": "한아름", "MM": "반달어린이", "MN": "사랑샘", "MO": "희망샘", "MP": "화홍어린이", "MT": "대추골", "MU": "한림", "MV": "창룡", "MW": "버드내", "MX": "광교홍재", "MY": "호매실", "MZ": "일월", "SB": "화서다산", "SC": "광교푸른숲", "SD": "매여울", "SE": "망포글빛" }

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/report')
def report():
    lib = request.args.get('lib')
    lib_name = library[lib]
    searchword = request.args.get('searchword')
    books = []
    aladdin_books = get_books_aladdin(searchword)
    lib_books = get_books_lib(searchword, lib)
    books = aladdin_books + lib_books
    return render_template('report.html', searchword = searchword, lib = lib_name, books = books)

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)