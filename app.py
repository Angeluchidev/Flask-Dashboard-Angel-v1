from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', active_route='/')

@app.route('/about')
def about():
    return render_template('index.html', active_route='/about')

@app.route('/contact')
def contact():
    return render_template('index.html', active_route='/contact')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html', active_route='/dashboard')

@app.route('/settings')
def settings():
    return render_template('test.html', active_route='/settings')

@app.route('/profile')
def profile():
    return render_template('index.html', active_route='/profile')

if __name__ == '__main__':
    app.run(debug=True)

