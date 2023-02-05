from flask import *

def createapp(testing:bool = True):
      app = Flask(__name__)  
      
      @app.route('/')  
      def index():  
            return render_template('index.html')  
      return app
