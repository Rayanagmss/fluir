from flask import Flask, render_template, request
from datetime import datetime
import database  # Importa o arquivo database.py criado acima

app = Flask(__name__)

# Cria a tabela de pedidos no banco, caso ainda não exista
database.criar_tabela()

@app.route('/')
def formulario():
    """
    Rota principal que mostra o formulário de pedido.
    """
    return render_template('formulario.html')

@app.route('/enviar_pedido', methods=['POST'])
def enviar_pedido():
    """
    Recebe os dados do formulário via POST,
    cria um pedido e salva no banco com status 'Pendente'.
    """
    dados = request.form  # Dados do formulário

    # Monta um dicionário com os dados recebidos
    pedido = {
        'cpf': dados.get('cpf'),
        'bairro': dados.get('bairro'),
        'rua': dados.get('rua'),
        'cidade': dados.get('cidade'),
        'estado': dados.get('estado'),
        'numero': dados.get('numero'),
        'complemento': dados.get('complemento'),
        'status': 'Pendente',  # Status inicial do pedido
        'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Data atual formatada
    }

    # Validação simples: CPF é obrigatório
    if not pedido['cpf']:
        return "CPF é obrigatório!", 400

    # Insere no banco
    database.inserir_pedido(pedido)

    # Retorna página de resposta com mensagem de sucesso
    return render_template('resposta.html', mensagem="Pedido enviado com sucesso!")

@app.route('/acompanhar')
def acompanhar():
    """
    Página para usuário informar CPF e consultar status do pedido.
    """
    return render_template('acompanhar.html')

@app.route('/consultar_status', methods=['POST'])
def consultar_status():
    """
    Recebe CPF via POST, consulta pedido no banco,
    e mostra status ou mensagem de erro.
    """
    cpf = request.form.get('cpf')
    if not cpf:
        return render_template('resposta.html', mensagem="Por favor, informe o CPF para consulta.")

    pedido = database.buscar_pedido_por_cpf(cpf)
    if pedido:
        return render_template('resposta.html', mensagem=f"Status do pedido: {pedido['status']}")
    else:
        return render_template('resposta.html', mensagem="Pedido não encontrado para o CPF informado.")

if __name__ == '__main__':
    # Roda o app em modo debug (para desenvolvimento)
    app.run(debug=True)
