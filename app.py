from flask import Flask,render_template,request
from dbfunction import create_post, get_posts
app= Flask(__name__,template_folder='client/template')

@app.route('/',methods=["GET","POST"])
def index():
    if request.method =="GET":
        pass

    else:
        name=request.form.get('name')
        post=request.form.get('post')
        create_post(name,post)

    posts=get_posts()
    return render_template('index.html',posts=posts)



app.run(debug=True)

