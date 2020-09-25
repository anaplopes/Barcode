# -*- coding: utf-8 -*-
from core.app import create_app as app


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']
    
    # executa o servidor web do flask
    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )
