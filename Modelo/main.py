from flask import Flask, render_template
from controller.blueprint import pagina

app = Flask(__name__)
app.register_blueprint(pagina)

if __name__ == "__main__":
   app.run(debug=True)