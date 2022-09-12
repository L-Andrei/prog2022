from config import *
from modelo import *


@app.route('/')
def iniciar_backend():
    a = 'Backend iniciado!!!'
    return a

@app.route('/listar')
def listar_registros():
    select =  db.session.query(Compania).offset(5000).limit(100)
    resposta = [ x.json() for x in select ]
    resposta = jsonify(resposta)
    resposta.headers.add("Access-Control-Allow-Origin", '*')
    return resposta

@app.route('/quantos_registros')  
def retorna_quantidade():
    resultado = len(db.session.query(Compania.id).all())
    return str(resultado)

app.run(host='0.0.0.0',debug=True)