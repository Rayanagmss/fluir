@app.route('/cadastro', methods=['GET', 'POST'])
def pagina_cadastro():
    if request.method == 'POST':
        nome_completo = request.form['nome']
        cpf_novo = request.form['cpf']
        senha_nova = request.form['senha']

        banco = conectar_banco()
        try:
            banco.execute(
                'INSERT INTO usuarios (nome, cpf, senha, tipo) VALUES (?, ?, ?, ?)',
                (nome_completo, cpf_novo, senha_nova, 'usuario')
            )
            banco.commit()
            flash('Cadastro realizado com sucesso! Agora faça login.')
            return redirect(url_for('pagina_login'))
        except sqlite3.IntegrityError:
            flash('Esse CPF já está cadastrado.')
        finally:
            banco.close()

    return render_template('cadastro.html')