from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def home():
  try:
    data = DB.get_all_inputs()0
  except Exception as e:
    print e
    data = None
  return render_template("home.html,data=data)

@app.route 
