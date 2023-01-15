import pandas as pd
from flask import Flask, request, make_response
from flask_cors import CORS

import search as search
import suggest as suggest

app = Flask(__name__)
CORS(app)

pd.options.display.max_columns = 100
@app.route('/searchbytitle', methods=['GET'])
def animeSearch():
    argList = request.args.to_dict(flat=False)
    query_term = argList['query'][0]
    result = search.searchByTitle(query_term)
    if isinstance(result, pd.DataFrame):
        resultTranpose = result.T
        jsonResult = resultTranpose.to_json()
        response = make_response(jsonResult)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    else:
        jsonResult = {'response': '404', 'similar_word': result}
        response = make_response(jsonResult)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response


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
        response = make_response(jsonResult)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    else:
        jsonResult = {'response': '404', 'similar_word': result}
        response = make_response(jsonResult)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

@app.route('/suggestion', methods=['GET'])
def Suggestion():
    argList = request.args.to_dict(flat=False)
    query_term = int(argList['query'][0])
    users_list = argList['list'][0]
    lookup_user_score_df = pd.DataFrame(eval(users_list))
    anime = suggest.anime
    suggest.user_anime_lookup_rating = lookup_user_score_df
    suggest.user1000_rating["user_id"] = suggest.user1000_rating["user_id"].apply(suggest.generate_new_id)
    rating = pd.concat([suggest.user_anime_lookup_rating, suggest.user1000_rating], join="outer", ignore_index=True)
    rating.reset_index(inplace=True)
    rating.drop(columns=["index"], inplace=True)
    print(rating)
    user_df = rating.copy().loc[rating['user_id'] == query_term]
    user_df = user_df.rename(columns={'rating': 'rating_y'})
    user_df = suggest.make_user_feature(user_df)
    recommend_df = suggest.predict(user_df, 40, anime, rating)
    resultTranpose = recommend_df[['mal_id', 'title', 'main_picture']].T
    jsonResult = resultTranpose.to_json()
    response = make_response(jsonResult)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

if __name__ == '__main__':
    app.run(debug=True)
