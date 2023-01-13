from flask import Flask, request, jsonify, make_response
import search
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/searchbytitle', methods=['GET'])
def animeSearch():
    argList = request.args.to_dict(flat=False)
    query_term = argList['query'][0]
    result = search.searchByTitle(query_term).T
    jsonResult = result.to_json()
    response = make_response(jsonResult)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@app.route('/searchbydescription', methods=['GET'])
def animedesSearch():
    argList = request.args.to_dict(flat=False)
    query_term = argList['query'][0]
    result = search.searchByDescription(query_term).T
    jsonResult = result.to_json()
    response = make_response(jsonResult)
    return response


if __name__ == '__main__':
    app.run(debug=True)
