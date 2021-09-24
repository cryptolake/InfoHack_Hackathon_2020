from flask import Flask, render_template, request
from random import choice, randrange
from flask.helpers import url_for
from datetime import datetime
from os import listdir

app = Flask(__name__)


global discoveries
global des
global supplies
supplies = [100,100,100]
discoveries = []

def gen_des():
    """TODO: Docstring for gen_des.

    :function: TODO
    :returns: TODO

    """
    places = ['Cave','Mountain','Volcano', 'slope','Dust Devil track', 'Sand Dune', 'Guille', 'Yarndang', 'Glassier' ,'Halo Crator', 'Delta']
    enc = "You have encountered a "+choice(places)
    return enc

def fill(cc):
    discoveries.append([ cc,datetime.now() ])
def dim(a=0,b=0,c=0):
    supplies[0] += a
    supplies[1] += b
    supplies[2] += c




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mars',methods= ['POST','GET'])
def mars():
    return render_template("mars.html")

@app.route('/mars/explore',methods= ['POST','GET'])
def explore():
    return render_template("thejourney.html")

@app.route('/mars/land',methods=['POST'])
def land():
    x = randrange(1,101,1)
    if x >= 50:
        return render_template("success.html")
    else:
        imgs = listdir('./static/exp')
        pathi = choice(imgs)
        return render_template("failure.html", img = pathi)
@app.route('/mars/build',methods=['POST','GET'])
def build():
    if request.method == 'POST':
        if 'advance' in request.form:
            desc = gen_des()
            fill(desc)
            imgs = listdir('./static/surfaces')
            pathi = choice(imgs)
            i = randrange(-3,6)
            vv = randrange(-20,20)
            ot = randrange(-10,0)
            dim(ot,vv,i)
            if supplies[0] <= 0 or supplies[2] <= 0:
                supplies[0] = 100
                supplies[1] = 100
                supplies[1] = 100
                discoveries.clear()
                return render_template("end.html")
            elif len(discoveries) > 20:
                supplies[0] = 100
                supplies[1] = 100
                supplies[1] = 100
                discoveries.clear()
                return render_template("win.html")
            else:
                return render_template("build.html", surface = pathi, desc = desc,des=discoveries, s=supplies)
        else:
                i = randrange(-10,0)
                oo = randrange(1,20)
                dim(oo,i,i)
                imgs = listdir('./static/surfaces')
                pathi = choice(imgs)
                if supplies[0] <= 0 or supplies[2] <= 0:
                    supplies[0] = 100
                    supplies[1] = 100
                    supplies[1] = 100
                    discoveries.clear()
                    return render_template("end.html")
                elif len(discoveries) > 20:
                    supplies[0] = 100
                    supplies[1] = 100
                    supplies[1] = 100
                    discoveries.clear()
                    return render_template("win.html")
                else:
                    return render_template("build.html", surface = pathi, desc = gen_des(),des=discoveries, s=supplies)
    else:
        imgs = listdir('./static/surfaces')
        pathi = choice(imgs)
        return render_template("build.html", surface = pathi, desc = gen_des(), s=supplies)
if __name__ == "__main__":
    app.run(debug=True)
