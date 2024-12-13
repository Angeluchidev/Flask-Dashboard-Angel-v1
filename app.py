from flask import Flask, render_template

app = Flask(__name__)

datos = {
  "sistema": "DASA-TEMPLATE",
  "usuario": "Angel Briceño",
  "perfil": "Administrador",
  "imagen":"perfil.jpg"
}

@app.route('/')
def home():
    return render_template('index.html', active_route='/', datos=datos)

@app.route('/about')
def about():
    return render_template('index.html', active_route='/about', datos=datos)

@app.route('/contact')
def contact():
    return render_template('index.html', active_route='/contact', datos=datos)

@app.route('/dashboard')
def dashboard():
    return render_template('index.html', active_route='/dashboard', datos=datos)

@app.route('/settings')
def settings():
    return render_template('test.html', active_route='/settings', datos=datos)

@app.route('/profile')
def profile():
    return render_template('index.html', active_route='/profile', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)

