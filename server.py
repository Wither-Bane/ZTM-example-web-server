from flask import Flask, render_template, request

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home_default():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return 'form submitted'
    else:
        return 'something went wrong. Try again'
    
    return 'form submitted hooorayyy!'