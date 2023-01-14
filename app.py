import pandas as pd
from flask import Flask, request
from flask_cors import CORS

import search as search

app = Flask(__name__)
CORS(app)


@app.route('/searchbytitle', methods=['GET'])
def animeSearch():
    argList = request.args.to_dict(flat=False)
    query_term = argList['query'][0]
    result = search.searchByTitle(query_term)
    if isinstance(result, pd.DataFrame):
        resultTranpose = result.T
        jsonResult = resultTranpose.to_json()
        return jsonResult
    else:
        json_object = {'response': '404 not found', 'similar word': result}
        return json_object


# jsonResult = result.to_json()
# response = make_response(jsonResult)
# response.headers['Access-Control-Allow-Origin'] = '*'
# response.headers['Access-Control-Allow-Credentials'] = 'true'
# return response

@app.route('/searchbydescription', methods=['GET'])
def animedesSearch():
    argList = request.args.to_dict(flat=False)
    query_term = argList['query'][0]
    result = search.searchByDescription(query_term)
    # check whether if result is a dataframe
    if isinstance(result, pd.DataFrame):
        resultTranpose = result.T
        jsonResult = resultTranpose.to_json()
        return jsonResult
    else:
        json_object = {'response': '404 not found', 'similar word': result}
        return json_object
    # jsonResult = result.to_json()
    # response = make_response(jsonResult)
    # return response


if __name__ == '__main__':
    app.run(debug=True)
