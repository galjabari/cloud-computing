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
    product = [ p for p in productsDB if (p['id'] == productId) ] 
    return jsonify({'product':product})

@app.route('/api/product/<productId>',methods=['PUT'])
def updateProduct(productId):
    product = [ p for p in productsDB if (p['id'] == productId) ]
  
    if 'name' in request.json: 
        product[0]['name'] = request.json['name']

    if 'price' in request.json:
        product[0]['price'] = request.json['price']

    return jsonify({'product':product[0]})

@app.route('/api/product',methods=['POST'])
def createProdcut():
    p = {
    'id':request.json['id'],
    'name':request.json['name'],
    'price':request.json['price']
    }
    productsDB.append(p)
    return jsonify(p)

@app.route('/api/product/<productId>',methods=['DELETE'])
def deleteProdcut(productId):
    product = [ p for p in productsDB if (p['id'] == productId) ]

    if len(product) == 0:
       abort(404)

    productsDB.remove(product[0])
    return jsonify({'response':'Success'})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
