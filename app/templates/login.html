@app.route('/login', methods=['GET', 'POST'])
def pagina_login():
    if request.method == 'POST':
        cpf_digitado = request.form['cpf']
        senha_digitada = request.form['senha']

        banco = conectar_banco()
        banco.row_factory = sqlite3.Row
        usuario = banco.execute(
            'SELECT * FROM usuarios WHERE cpf = ? AND senha = ?',
            (cpf_digitado, senha_digitada)
        ).fetchone()
        banco.close()

        if usuario:
            session['id_usuario'] = usuario['id']
            flash('Login feito com sucesso!')
            return redirect(url_for('pagina_index'))
        else:
            flash('CPF ou senha incorretos. Tente novamente.')

    return render_template('login.html')