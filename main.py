from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Bem-vindo. Use /telefone?telefone=11999998888'

@app.route('/telefone', methods=['GET', 'POST'])
def telefone():
    fone = request.values.get('telefone', '')
    fone = ''.join(filter(str.isdigit, fone))
    
    if len(fone) == 11:  # Celular: (11)99999-8888
        resultado = f'({fone[:2]}){fone[2:7]}-{fone[7:]}'
        return resultado
    
    elif len(fone) == 10:  # Fixo: (11)9999-8888
        resultado = f'({fone[:2]}){fone[2:6]}-{fone[6:]}'
        return resultado
        
    else:
        return 'Erro: telefone precisa ter 10 ou 11 dígitos', 400

if __name__ == '__main__':
    app.run(debug=True)
