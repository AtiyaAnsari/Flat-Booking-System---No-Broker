from flask import Flask, render_template, request, redirect
from flask.globals import request
from dbm import delHomeById, getAllHome, addHome, getHomeById, updateHomeById
from model import Home

app = Flask(__name__)

@app.route('/', methods=['get'])
def index():
    return render_template('index.html', username='Atiya')


@app.route('/gethome', methods=['get'])
def showhome():
    data = getAllHome()
    return render_template('homelist.html', homes=data)


@app.route('/addhome')
def showAddHomeForm():
    return render_template('addhome.html')


@app.route('/savehome', methods=['post'])
def savehome():
    name = request.form['name']
    email = request.form['email']
    numb = request.form['number']
    number=int(numb)
    tower = request.form['tower']
    bhk = request.form['bhk']
    types = request.form['types']
    home = Home(name,email,number,tower,bhk,types)
    addHome(home)
    return redirect('/gethome')


@app.route('/deletehome/<int:i>')
def deletehome(i):
    delHomeById(i)
    return redirect('/gethome')


@app.route('/gethome/<int:i>')
def gethome(i):
    h = getHomeById(i)
    return render_template('updatehome.html', home=h)


@app.route('/updatehome', methods=['post'])
def updatehome():
    i = request.form['bid']
    bid = int(i)
    name = request.form['name']
    email = request.form['email']
    n = request.form['number']
    numbr=int(n)
    tower = request.form['tower']
    bhk = request.form['bhk']
    types = request.form['types']
    h = Home(name,email,numbr,tower,bhk,types,bid)
    updateHomeById(h)
    return redirect('/gethome')



if __name__ == '__main__':
    app.run(debug=True)
