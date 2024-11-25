from flask import Flask, request, jsonify
import json

app=Flask(__name__)
listaCarti=[]

def load_books():
    global listaCarti
    try:
        with open('books.json', 'r') as f:
            listaCarti = json.load(f)
    except Exception as e:
        print(f"Eroare la incarcarea cărților: {str(e)}")
load_books()

#Create
@app.route('/library', methods=['POST'])
def createLibrary():
    dateCarti=request.json
    try:
        if not dateCarti :
            return jsonify({"mesaj":"tb sa existe nume si autor, ambele!!!"}), 400
        if 'nume' not in dateCarti or 'autor' not in dateCarti:
            return jsonify({"mesaj": "Request-ul trebuie să conțină cheile 'nume' și 'autor'!"}), 400
        if not dateCarti['nume'] or not dateCarti['autor']: 
            return jsonify({"mesaj": "Valorile pentru 'nume' și 'autor' nu trebuie să fie goale!"}), 400
        listaCarti.append(dateCarti)
        return jsonify({"mesaj": "adaugarea s a fct cu succes"}), 201
    except Exception as e:
        return jsonify({"mesaj": f"ceva nu a mers cum trebuie, {str(e)}"}), 500
    
#read
@app.route('/library', methods=['GET'])
def getBook():
    try:
        return jsonify(listaCarti), 200
    except Exception as e:
        return jsonify ({"eroare":f"ceva nu a mers cum trb, {str(e)}"}), 500
    
@app.route('/library/<nume>', methods=['GET'])
def getBookbyName(nume):
    try:
        for carte in listaCarti:
            if carte['nume']==nume:
                return jsonify(carte), 200#200-confirmare,
        return jsonify({"error":"cartea nu a fost citita"}), 404
    except Exception as e:
        return jsonify({"eroare":f"ceva nu a mers,{str(e)}"}), 500


    
#update
@app.route('/library/<nume>', methods=['PUT'])
def updateBooks(nume): #am astfel pt ca updatez numele cartilor in fct de nume 
    try:
        dateCarti=request.json
        carteNoua=dateCarti.get('nume')
        autorNou=dateCarti.get('autor')
        if 'nume' not in listaCarti and 'autor' not in listaCarti:
            return jsonify({"eroare":"carte inexistenta"}), 400
        for carte in listaCarti:
            if carte['nume']==nume:
                if carteNoua:
                    carte['nume']=carteNoua
                    if autorNou:
                        carte['autor']=autorNou
                    return jsonify({"mesaj":"inlocuirea a fsot realizata"}),200
        return jsonify({"eroare": "carte inexistenta"}), 400
    except ValueError as e:
        return jsonify({"eroare": "ceva nu a mers corespunzator"}), 500
    
#delete
@app.route('/library/<nume>', methods=['DELETE'])
def removeBook(nume):
    try:
        for carte in listaCarti:
            if carte['nume']==nume:
                listaCarti.remove(carte)
                return jsonify({"mesaj":"cartea a fost scoasa din biblioteca"}), 200
        return jsonify({"mesaj": "cartea nu exista"}), 400
    except ValueError as e:
        return jsonify({"eroare": "ceva nu a mers coresupnzator"}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
