from flask import Flask, session

from routes.index import index
from routes.app   import r_app


if __name__ == '__main__':
    app = Flask(__name__)

    # Register these routes
    app.register_blueprint(index)
    app.register_blueprint(r_app)
    

    app.secret_key = "123456"

    
    app.run(debug=True, host='0.0.0.0')



