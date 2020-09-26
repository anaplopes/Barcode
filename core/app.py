# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_cors import CORS
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    CORS(app)
    Bootstrap(app)
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'you-will-never-guess')
    
    # blueprint
    from core.routes import bp
    app.register_blueprint(bp)

    return app
