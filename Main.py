import flask  
from flask import  Flask, redirect, url_for ,render_template , request
#from flask import 
#from flask_restful import Resource, Api
app = flask.Flask(__name__)
app.config["DEBUG"] = True




@app.route('/')
def home():
    return render_template("home.html")
    # return redirect(url_for('square', side='10'))
        # Also pass an optional URL variable

@app.route('/squareinput')
def squareinput():
    return render_template("square.html")

@app.route('/square', methods = ['POST'])
def square():
    if (not request.form['side'] == ''):
        side = request.form['side']
        perimeter = 4 * int(side)
        area = pow( int(side) , 2)
        return render_template("result.html", type ="square", area=area ,perimeter=perimeter)
    else:
        return render_template("error.html")

@app.route('/rectangleinput')
def rectangleinput():
    return render_template("rectangle.html")

@app.route('/rectangle', methods = ['POST'])
def rectangle():
    if (not(request.form['hight'] == '' or request.form['weight'] == '')):
        weight = request.form['weight']
        hight = request.form['hight']
        perimeter = 2 * ( int(weight) + int(hight) )
        area = int(weight) * int(hight)
        return render_template("result.html", type ="rectangle", area=area ,perimeter=perimeter)
    else:
        return render_template("error.html")


@app.route('/parallelograminput')
def parallelograminput():
    return render_template("parallelogram.html")

@app.route('/parallelogram', methods = ['POST'])
def parallelogram():
    if (not(request.form['hight'] == '' or request.form['base'] == '')):
        base = request.form['base']
        hight = request.form['hight']
        perimeter = 2 * (int(base) + int(hight) )
        area = int(base) * int(hight)
        return render_template("result.html", type ="parallelogram", area=area ,perimeter=perimeter)
    else:
        return render_template("error.html")

@app.route('/triangleinput')
def triangleinput():
    return render_template("triangle.html")

@app.route('/triangle', methods = ['POST'])
def triangle():
    if (not(request.form['side'] == '' or request.form['side2'] == '' or request.form['base'] == '')):
        side = request.form['side']
        side2 = request.form['side2']
        base = request.form['base']
        hight = request.form['base']
        perimeter = int(side) + int(side2) + int(base)
        area = ( int(base) * int(hight)/2)
        return render_template("result.html", type ="triangle", area=area ,perimeter=perimeter)
    else:
        return render_template("error.html")


@app.route('/circleinput')
def circleinput():
    return render_template("circle.html")

@app.route('/circle', methods = ['POST'])
def circle():
    if (not request.form['radius'] == ''):
        radius = request.form['radius']
        PI = 3.14
        perimeter = 2 * PI * int(radius)
        area = PI * pow( int(radius)  , 2)
        return render_template("result.html", type ="circle", area=area ,perimeter=perimeter)
    else:
        return render_template("error.html")
        
app.run()



