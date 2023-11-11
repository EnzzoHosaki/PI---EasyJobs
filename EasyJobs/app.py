from flask import Flask, render_template, send_from_directory, request
import os
import logica as lg

app = Flask(__name__)
app.template_folder = os.path.abspath('templates')

@app.route('/')
def index():
    return render_template('perfil_candidato.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('templates', filename)

if __name__ == '__main__':
    app.run(debug=True)
