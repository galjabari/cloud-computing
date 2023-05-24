from flask import Flask, request, jsonify

app = Flask(__name__)

products=[
 {
 'id':'101',
 'name':'Smart Watch',
 'price':500
 },
 {
 'id':'102',
 'name':'WiFi Router',
 'price':200
 }
 ]

# curl -i -X GET http://localhost/api/products
@app.route('/api/products',methods=['GET'])
def getAllProducts():
    return jsonify({'products':products})

# curl -i -X GET http://localhost/api/products/101
@app.route('/api/products/<productId>',methods=['GET'])
def getProduct(productId):
    product = [ p for p in products if (p['id'] == productId) ] 
    return jsonify({'product':product})

# curl -i -X PUT -H 'Content-Type: application/json' -d '{"price":400}' http://localhost/api/products/101
@app.route('/api/products/<productId>',methods=['PUT'])
def updateProduct(productId):
    product = [ p for p in products if (p['id'] == productId) ]
  
    if 'name' in request.json: 
        product[0]['name'] = request.json['name']

    if 'price' in request.json:
        product[0]['price'] = request.json['price']

    return jsonify({'product':product[0]})

# curl -i -X POST -H 'Content-Type: application/json' -d '{"id":"103","name":"LED","price":100}' http://localhost/api/products
@app.route('/api/products',methods=['POST'])
def createProdcut():
    product = {
    'id':request.json['id'],
    'name':request.json['name'],
    'price':request.json['price']
    }
    products.append(product)
    return jsonify(product)

# curl -i -X DELETE http://localhost/api/products/103
@app.route('/api/products/<productId>',methods=['DELETE'])
def deleteProdcut(productId):
    product = [ p for p in products if (p['id'] == productId) ]

    if len(product) == 0:
       abort(404)

    products.remove(product[0])
    return jsonify({'response':'Success'})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
