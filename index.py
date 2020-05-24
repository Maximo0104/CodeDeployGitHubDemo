from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def home ():
    return render_template('home.html')
@app.route ('/about')
def about ():
    return render_template('about.html')
@app.route('/comidas')
def comidas():
    return render_template('comidas.html')
@app.route ('/contacto')
def contacto():
    return render_template ('contacto.html')
@app.route ('/tips')
def tips():
    return render_template('tips.html')
@app.route('/pecho')
def pecho():
    return render_template('pecho.html')
@app.route('/brazos')
def brazos():
    return render_template('brazos.html')
@app.route('/abs')
def abs():
    return render_template('abs.html')
@app.route('/hombros')
def hombros():
    return render_template('hombros.html')
@app.route('/espalda')
def espalda():
    return render_template('espalda.html')
@app.route('/piernas')
def piernas():
    return render_template('piernas.html')







if __name__ == '__main__':
    app.run(debug = True)
