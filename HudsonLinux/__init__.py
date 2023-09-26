import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, 
        static_url_path='', 
        instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY="I no tell you",
            DATABASE=os.path.join(app.instance_path, 'hudsonlinux.db3'),
        )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/classes/')
    def classes():
        return render_template('classes.html')

    @app.route('/services/')
    def services():
        return render_template('services.html')

    @app.route('/instructors/')
    def instructors():
        return render_template('instructors.html')

    @app.route('/contact/')
    def contact():
        return render_template('contact.html')



    return app
