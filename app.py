from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pets= [{'id': 0, 'nome': 'Rex', 'raca': 'Pitbull', 'idade': 2}]
id = 0

@app.route('/')
def home():
    print(pets)
    return  render_template("home.html", pets = pets)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    return  render_template("cadastrar.html")


@app.route('/cadastrar_pet', methods=['POST'])
def cadastrar_pet():
    global id
    nome = request.form['nome']
    raca = request.form['raca']
    idade = request.form['idade']
    pets.append({'id':id, 'nome': nome, 'raca': raca,'idade': idade})
    id+=1
    return redirect(url_for('home'))


@app.route('/editar/<int:index>', methods=['GET', 'POST'])
def editar_pet(index):
    print(index)
    pet = pets[index-1]

    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        idade = request.form['idade']
        pets[index-1]['nome'] = nome
        pets[index-1]['raca'] = raca
        pets[index-1]['idade'] = idade
        return redirect(url_for('home'))
    return render_template('editar.html', pet=pet, index=index)

@app.route('/excluir/<int:index>')
def excluir_pet(index):
    if index-1 < len(pets):
        del pets[index-1]

    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)