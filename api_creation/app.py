from flask import Flask,request,url_for,render_template,redirect

app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "SERVER UP AND RUNNING"

@app.route("/index",methods=["GET"])
def index():
    return "Welcome To The Index Page"

#variable rule 


if __name__=="__main__":
    app.run(debug=True)