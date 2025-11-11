from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

# Lista de pratos com nome, descrição, preço e imagem
PRATOS = [
    {
        "nome": "Baião de Dois",
        "preco": 25.00,
        "descricao": "Arroz, feijão verde, queijo coalho e temperos da casa.",
        "img": "baiao.jpg"
    },
    {
        "nome": "Carne de Sol com Nata",
        "preco": 32.00,
        "descricao": "Suculenta carne de sol com nata cremosa e macaxeira.",
        "img": "carne.jpg"
    },
    {
        "nome": "Munguzá Cremoso",
        "preco": 15.00,
        "descricao": "Delicioso munguzá doce com leite de coco e canela.",
        "img": "munguza.jpg"
    },
    {
        "nome": "Tapioca Recheada",
        "preco": 10.00,
        "descricao": "Tapioca crocante com coco e queijo coalho.",
        "img": "tapioca.jpg"
    },
    {
        "nome": "Cuscuz Nordestino",
        "preco": 12.00,
        "descricao": "Cuscuz com ovo, queijo e manteiga da terra.",
        "img": "cuscuz.jpg"
    }
]

@app.route('/')
def index():
    return render_template('index.html', pratos=PRATOS)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        mensagem = request.form['mensagem']

        texto = f"""*Novo contato - Bom Sabor Delivery*
*Nome:* {nome}
*Telefone:* {telefone}
*Mensagem:* {mensagem}"""

        msg_encoded = urllib.parse.quote(texto)
        whatsapp_url = f"https://wa.me/5588921494170?text={msg_encoded}"
        return redirect(whatsapp_url)

    return render_template('contato.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
