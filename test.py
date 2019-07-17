from flask import Flask ,render_template,request
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydata"]
mycol1 = mydb["customers"]

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')


@app.route("/about")
def hello3():
    return render_template('about.html')


@app.route("/login",methods=["GET","POST"])
def login():
    username=""
    if request.method == "POST":
        username=request.form.get("username")
        password=request.form.get("password")
        f=0
        for x in mycol1.find():
            if x['username']==username and x['password']== password:
                f=1
                break
            else:
                return render_template('login.html')
        if f==1:
            return render_template('about.html')







    return render_template('login.html')


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method =="POST":
        name=request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        print(name,username,password,confirm)
        if password == confirm:
            d={}
            d['name']=name
            d['username']=username
            d['password']=password
            d['confirm']=confirm
            x = mycol1.insert_one(d)
            return render_template('login.html')
        else:
            return "Error"
    return render_template('register.html')



app.run(debug=True)