from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import json
import MySQLdb


app = Flask(__name__)


conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="rs1234",
                  db="namelist")
cur = conn.cursor()


@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']

    query="SELECT * FROM User WHERE firstn LIKE '%s' LIMIT 1,5 " % ("%" + text + "%",)
    #query="SELECT * FROM User"
    #processed_text = text.upper()
    #cur query here
    cur.execute(query)
    #data=cur.fetchall()
    #print data
    """
    namesret=[]
    for person in data:
    	namedict = {
    	'First Name': data[0],
    	'Last Name' : data[1]
    	}
    	nameret.append(namedict)
    """
    return jsonify(data=cur.fetchall())

if __name__ == '__main__':
    app.run()
