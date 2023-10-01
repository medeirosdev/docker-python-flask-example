from flask import Flask, request, jsonify
from APIME2Check import APInstagram

app = Flask(__name__)

publicList = ["8c848e5fc392204f1c85f0e5d0b57f6a7dbd5941e4e1646df014c34d0b0172d8587c5dc4f3bf84475a58497f25b665effec56dd0778fb6b51584132cccfdfd91",
            "13d83467c8e942927b2a4e4b64607930828fe334d1ba40c6dfad9ddb75f3515ef7fe598b5f9d2c3d8e558773f8c169855a9ac55323b0275333e4b59f398a2180",
            "683cd4656571ca9a619e7b51cb8be1ba6c3412012aede21c9c45468b1d2ab52ecda7fc27f323dd0eb10071367fafa1e0d7d2202cf7081af32b3cbbd1c33d691c",
               ]
privateKeyOriginal = "f03ddd814defc74c96f2b087f49440e620b698d2028209f969e28e3137be049e1227cbf4ab00f41eb7888d28476c3e662854eccb9d6c6a6de20bc924a0b5d241"
#==================================
def verifica_string_em_lista(string_a_verificar, lista_de_strings):
    return string_a_verificar in lista_de_strings
#=================================

@app.route('/apime2check',methods=['GET'])
def getData():
    data = request.get_json()

    # Verifique se os campos token, chave e username estão presentes no JSON
    if 'token' not in data or 'privateKey' not in data or 'username' not in data:
        return jsonify({'message': 'Campos incompletos'}), 400

    token = data['token']
    publicKey = data['publicKey']
    privateKey = data['privateKey']
    username = data['username']

    statusCheckPublic = verifica_string_em_lista(publicKey, publicList)
    statusCheckPrivate = verifica_string_em_lista(privateKey, privateKeyOriginal)
    if statusCheckPrivate == False:
        return jsonify({'message': 'Chave publica errada'}), 400
    #if statusCheckPrivate == False:
    #    return jsonify({'message': 'Chave privada errada'}), 400

    data = APInstagram(username, token)

    return jsonify(data, 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
