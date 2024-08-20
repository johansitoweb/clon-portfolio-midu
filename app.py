from flask import Flask, render_template  

app = Flask(__name__)  

@app.route("/")  # Corrige aquí  
def index():  
    return render_template("sitio/index.html")  

if __name__ == "__main__":  
    app.run(debug=True)