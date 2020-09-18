# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'you-will-never-guess')
    
    UPLOAD_FOLDER = os.path.join(os.path, 'uploads')
    if not os.path.isdir(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
        
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    # blueprint
    from core.routes import bp
    app.register_blueprint(bp)

    return app
