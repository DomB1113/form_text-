from flask import Flask, render_template, request, redirect,session
import os
app = Flask(__name__)
app.secret_key = os.urandom(16)
b'_5#y2L"F4Q8z\n\xec]/'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     # Never render a template on a POST request.
#     # Instead we will redirect to our index route.
#     return redirect('/')


# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     name = request.form['name']
#     email = request.form['email']
#     return redirect("/show")	 

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')


    
# adding this method
# @app.route("/show")
# def show_user():
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return render_template("show.html")


# Previously in our show_user function, we didn't have access to the name and email from the form submission. 
# Now, because of session, we have a way to access the name and email in a different function!

# Let's modify our show_user function:
@app.route('/show')
def show_user():
    print(app.secret_key)
    return render_template('show.html', name_on_template=session['username'],
    email_on_template=session['useremail'])



if __name__ == "__main__":
    app.run(debug=True)

