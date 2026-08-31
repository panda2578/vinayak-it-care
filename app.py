from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
app.secret_key = "vinayak7008541544"
@app.route('/')
def home():
    return "<h1>Vinayak IT Care</h1><h2>7008541544</h2><p>150+ Boards | 800+ BIOS | 15000+ Parts</p><a href='/motherboards'>Motherboards</a>"
@app.route('/motherboards')
def mb():
    return "<h1>All Boards</h1><p>LA-9981P - Lenovo</p><p>LA-K101P - Dell</p><p>DA0G7CMB6D0 - HP</p><a href='/'>Back</a>"
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
