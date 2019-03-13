from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # get today dates
    x = datetime.datetime.now()
    x = x.strftime('%B %d, %Y %X %p')

    # get the number of items order
    items = 0
    for key, value in request.form.items():
        if key == 'strawberry' or key == 'raspberry' or key == 'apple':
            items += int(value)

    return render_template("checkout.html", items=items, today=x)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

# if __name__=="__main__":   
#     app.run(debug=True)    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=true)