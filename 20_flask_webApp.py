from flask import Flask,jsonify,request,render_template
app=Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/name',methods=['POST'])
def res1():
    if request.method=='POST':
        first_name=request.json['firstName']
        last_name=request.json['lastName']
    return jsonify(first_name+last_name)
@app.route('/math',methods=['POST'])
def add():
    ##if request.method=='POST':
        a=request.json['x']
        b=request.json['y']
        return jsonify(int(a)+int(b))

@app.route('/math/web',methods=['POST'])
def add_web():
    ##if request.method=='POST':
        a=request.form['x']
        b=request.form['y']
        return render_template(result.html)

if __name__=="__main__":
    app.run(host="0.0.0.0")