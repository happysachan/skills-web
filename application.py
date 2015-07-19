from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/app_form")
def app_form():
 	return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application():
	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	salary = request.form.get("salary")
	job = request.form.get("job")

	return render_template("application.html", firstname=firstname, lastname=lastname, salary=salary, job=job)

if __name__ == "__main__":
    app.run(debug=True)