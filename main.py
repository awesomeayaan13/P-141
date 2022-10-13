from flask import Flask,jsonify, request
import csv

liked_articles=[]
disliked_articles=[]
all_articles=[]

with open('articles.csv',encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]
app=Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/liked-article",methods=['POST'])
def liked_article():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_articles.append(movie)
    return jsonify({
        "data":all_articles[0],
        
    }),201

@app.route("/disliked-article",methods=['POST'])
def disliked_article():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    disliked_article.append(movie)
    return jsonify({
        "data":all_articles[0],
        
    }),201
if __name__=="__main__":
    app.run()