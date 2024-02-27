from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("./index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# @app.route("/components.html")
# def my_component():
#     return render_template("components.html")

# @app.route("/contact.html")
# def my_components():
#     return render_template("contact.html")

# @app.route("/thankyou.html")
# def my_thankyou():
#     return render_template("thankyou.html")

# @app.route("/work.html")
# def my_work():
#     return render_template("work.html")

# @app.route("/works.html")
# def my_works():
#     return render_template("works.html") 

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject},{message}")

@app.route('/submit_form', methods=['POST', 'GET']) #get means the browser wants us to send info, post to save info.
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
        except:
            return "did not save to database"
        return redirect("/thankyou.html")
    else:
        return "something went wrong try again"
    
def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])