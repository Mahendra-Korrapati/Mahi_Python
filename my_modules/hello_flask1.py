from flask import Flask
from vsearch import search4letters
app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'hello world from flask'

@app.route('/search4')
def do_search() -> str:
    return str(search4letters("helllo woerld actualyy", "aeiou"))
app.run()
