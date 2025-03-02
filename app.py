from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def greeter():
    return "<h1>Hello World</h1>"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Handling POST request (form data submission)
        user_name = request.form["username"]
        password = request.form["password"]
        res = f'Username: {user_name}, Password: {password}'
        return f'<h1>Registration Successful</h1><p>{res}</p>'
    
    # Return the registration form on GET request
    return """
    <form action="/register" method="POST">
        <input type="text" name="username" placeholder="Username"><br><br>
        <input type="password" name="password" placeholder="Password"><br><br>
        <input type="submit" value="Register">
    </form>
    """
@app.route("/sum",methods=["GET","POST"])
def sum():
    if request.method=="POST":
        num1=int(request.form["num1"])
        num2=int(request.form["num2"])
        sum=num1+num2
        return f"<h1>sum of two numbers {num1}+{num2} ={sum}</h1>"
    return """
    <form action="/sum" method="POST">
    <input type="number" name="num1" placeholder="Enter Num1 : "><br><br>
    <input type="number" name="num2" placeholder="Enter Num2 : "><br><br>
    <input type="submit" value="+">
    </form>
    """

@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]
            
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    return "<h1>Division by zero is not allowed.</h1>"
                result = num1 / num2
            else:
                return "<h1>Invalid operation selected.</h1>"
            
            return f"<h1>Result: {num1} {operation} {num2} = {result}</h1>"
        except ValueError:
            return "<h1>Invalid input. Please enter numbers only.</h1>"
    
    return '''
    <form action="/calculate" method="POST">
        <input type="number" name="num1" placeholder="Enter Num1" required><br><br>
        <input type="number" name="num2" placeholder="Enter Num2" required><br><br>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select><br><br>
        <input type="submit" value="Calculate">
    </form>
    '''


if __name__ == "__main__":
        app.run("0.0.0.0")
