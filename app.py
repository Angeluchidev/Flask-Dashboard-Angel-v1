from flask import Flask, render_template


app = Flask(__name__)


proyecto = {"titulo": "Angel Template", "intro": "PLantilla Basada en Flask / jinja 2", "logo": "logo.png"}

#menu_items = ['Principal', 'item1', 'item2', 'item3']


@app.route('/')
def home():
    return render_template('index.html', proyecto=proyecto, active_route='/')

@app.route('/about')
def about():
    return render_template('test.html', proyecto=proyecto, active_route='/about')

@app.route('/contact')
def contact():
    return render_template('index.html', proyecto=proyecto, active_route='/contact')


if __name__ == '__main__':
    app.run(debug=True)

