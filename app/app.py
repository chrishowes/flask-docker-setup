from flask import Flask
from flask_assets import Environment, Bundle
from webassets.loaders import YAMLLoader

from flask import render_template

app = Flask(__name__)
assets = Environment(app)

assets.register('app-js',
    Bundle('js/lib/vue.min.js',
           'js/app.js',
           filters='rjsmin',
           output='dist/app.js'))

assets.register('app-css',
    Bundle('scss/lib/bootstrap.scss',
           'scss/app.scss',
           filters='scss',
           output='dist/app.css'))

@app.route('/')
def hello():
    return render_template("index.html")

app.config.update(
    TEMPLATES_AUTO_RELOAD=True
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
