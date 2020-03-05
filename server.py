from flask import Flask, render_template, request, redirect
app = Flask(__name__)  
from datetime import datetime

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    total_items = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f"Charging {request.form['first_name']} for {total_items} fruits")
    return render_template("checkout.html", strawberries=request.form['strawberry'],raspberries=request.form['raspberry'],apples=request.form['apple'],first_name=request.form['first_name'],last_name=request.form['last_name'],student_id=request.form['student_id'],total_items=total_items,date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    