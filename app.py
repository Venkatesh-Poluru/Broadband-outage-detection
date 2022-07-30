from flask import Flask, request, jsonify, render_template
import auto_ml as ml
import pickle
import os
import json
#Init Flask 
app = Flask(__name__)


@app.route("/",methods=["Get"])
def welcome():
    num1 = request.args["num1"]
    num2 = request.args["num2"]
    result = float(num1) + float(num2)
    return f"The output is {result}"

@app.route("/test",methods=["POST"])
def test():
    print(request.get_data())
    return "Text"


#deploy_model
@app.route('/deploy_model',methods=['POST'])
def deploy_model():
    data=request.get_data()
    model=pickle.loads(data)
    email_id=model.model_id
    password=model.password
    model_id=email_id.split("@")[0]
    u_data=json.dumps({"model_id":model_id,"password":password})
    try:
        os.mkdir("Models-flask/"+model_id+"/")
    except:
        pass
    with open("Models-flask/"+model_id+"/model.pkl",'wb') as f:
        pickle.dump(model,f)
    with open("Models-flask/"+model_id+"/meta_data.json",'w') as f:
        f.write(json.dumps(u_data, indent = 4) )
    print(request.url)
    return "Success!"

@app.route('/predict/<model_id>',methods=['POST',"GET"])
def predict(model_id):
    new_data = request.json["new_data"]
    clf = ml.load("Models-flask/"+model_id+"/model.pkl")
    prediction = clf.predict(new_data)
    for each_key in prediction:
        prediction[each_key] = str(prediction[each_key])
    return json.dumps(prediction)
	
if __name__ == "__main__":
    app.run(debug=True)