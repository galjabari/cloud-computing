from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

productsDB=[
 {
 'id':'101',
 'name':'Smart Watch',
 'price':'500.0'
 },
 {
 'id':'102',
 'name':'WiFi Router',
 'price':'200.0'
 }
 ]

@app.route('/api/product',methods=['GET'])
def getAllProducts():
    return jsonify({'products':productsDB})

@app.route('/api/product/<productId>',methods=['GET'])
def getProduct(productId):
    prod = [ p for p in productsDB if (p['id'] == productId) ] 
    return jsonify({'product':prod})


@app.route('/api/product/<productId>',methods=['PUT'])
def updateProduct(productId):

    prod = [ p for p in productsDB if (p['id'] == productId) ]

    if 'name' in request.json : 
        prod[0]['name'] = request.json['name']

    if 'price' in request.json:
        prod[0]['price'] = request.json['price']

    return jsonify({'product':prod[0]})


@app.route('/api/product',methods=['POST'])
def createProdcut():

    rec = {
    'id':request.json['id'],
    'name':request.json['name'],
    'price':request.json['price']
    }
    productsDB.append(rec)
    return jsonify(rec)

@app.route('/api/product/<productId>',methods=['DELETE'])
def deleteProdcut(productId):
    prod = [ p for p in productsDB if (p['id'] == productId) ]

    if len(prod) == 0:
       abort(404)

    productsDB.remove(prod[0])
    return jsonify({'response':'Success'})

if __name__ == '__main__':
 app.run()
