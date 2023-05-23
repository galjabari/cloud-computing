from flask import Flask, request, jsonify

app = Flask(__name__)

users=[
 {
 'id':'101',
 'name':'Bob',
 'password':'123456'
 },
 {
 'id':'102',
 'name':'Alice',
 'password':'123456'
 }
 ]

# curl -i -X GET http://localhost/api/users
@app.route('/api/users',methods=['GET'])
def getAllusers():
    return jsonify({'users':users})

# curl -i -X GET http://localhost/api/users/101
@app.route('/api/users/<userId>',methods=['GET'])
def getuser(userId):
    user = [ p for p in users if (p['id'] == userId) ] 
    return jsonify({'user':user})

# curl -i -X PUT -H 'Content-Type: application/json' -d '{"password":400}' http://localhost/api/users/101
@app.route('/api/users/<userId>',methods=['PUT'])
def updateuser(userId):
    user = [ p for p in users if (p['id'] == userId) ]
  
    if 'name' in request.json: 
        user[0]['name'] = request.json['name']

    if 'password' in request.json:
        user[0]['password'] = request.json['password']

    return jsonify({'user':user[0]})

# curl -i -X POST -H 'Content-Type: application/json' -d '{"id":"103","name":"Tom","password":'123456'}' http://localhost/api/users
@app.route('/api/users',methods=['POST'])
def createProdcut():
    user = {
    'id':request.json['id'],
    'name':request.json['name'],
    'password':request.json['password']
    }
    users.append(user)
    return jsonify(user)

# curl -i -X DELETE http://localhost/api/users/103
@app.route('/api/users/<userId>',methods=['DELETE'])
def deleteProdcut(userId):
    user = [ p for p in users if (p['id'] == userId) ]

    if len(user) == 0:
       abort(404)

    users.remove(user[0])
    return jsonify({'response':'Success'})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
