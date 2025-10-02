from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hola_Mundo():
    return """
    <h1>!Hola Mundo desde Flask y Docker Juan Camilo Vargas!</h1>
    <p>Esta es una aplicación web sencilla ejecutándose en Docker</p>
    <p>Puerto: 5000</p>
    """


@app.route('/api/saludo')
def api_saludo():
    return {
        'Mensaje': 'Hola Mundo',
        'Tecnologia': ['Python', 'Flask', 'Docker','Docker Compose'],
        'Estado': 'Funcionando'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)