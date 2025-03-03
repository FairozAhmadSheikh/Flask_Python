from flask import Flask,request,url_for,render_template,redirect,jsonify

app=Flask(__name__)

# Default or Home Route
@app.route("/",methods=["GET"])
def welcome():
    return "SERVER UP AND RUNNING"

# Index Route
@app.route("/index",methods=["GET"])
def index():
    return "Welcome To The Index Page"

#variable rule 

# Route for Pass
@app.route("/success/<int:score>")
def success(score):
    return f'Congratulations You Passed With Score :{score} 🎉'
# Route for fail
@app.route('/fail/<int:score>')
def fail(score):
    return f'You Failed With Score :{score} 😢'


# calculating result page
@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    else:
        math=float(request.form["math"])
        science=float(request.form["science"])
        history=float(request.form["history"])
        average=(math+science+history)/3
        # return render_template('form.html',score=average)

        # if you want to redirect it to success or failure page
        res=""
        if average>50:
            res="success"
        else:
            res="fail"
        return redirect(url_for(res,score=average))
    
# API Creation  we will do it using JSON 
"""
Use Postman 
"""
@app.route('/api',methods=['POST'])
def calculate_sum():
    data=request.get_json()
    value_a=float(dict(data)['first'])
    value_b=float(dict(data)['second'])
    return jsonify(value_a+value_b)

if __name__=="__main__":
    app.run(debug=True)