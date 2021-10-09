import pandas as pd
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("bigmart.pkl")

@app.route('/')
def hi():
    return render_template('html code.html')

@app.route('/hello')
def hello():
    return "Hello how are you"

@app.route('/predict', methods=['POST'])
def predict():
    print(request.form.values())
    inp = [i for i in request.form.values()]
    
    try:
        if not isinstance(int(inp[1]), int):
            mess = "Please enter valid input"
            return render_template('html code.html', prediction = mess)
    except:
        mess = "Please enter valid input"
        return render_template('html code.html', prediction = mess)
    
    try:
        if not isinstance(int(inp[2]), int):
            mess = "Please enter valid input"
            return render_template('html code.html', prediction = mess)
    except:
        mess = "Please enter valid input"
        return render_template('html code.html', prediction = mess)

    test = {"Item_MRP":inp[0],"Outlet_Size":int(inp[1]),"Outlet_Establishment_Year":int(inp[2]), "Item_Visibility":int(inp[3]), "Item_Weight":int(inp[4])}
    print(test)
    test_df = pd.DataFrame([test])
    print(test_df)
    res = model.predict(test_df)
    print(res[0])
    #return str(res[0])
    if isinstance(res[0], float):
        mess = "Item Outlet Sales is {} ".format(str(res[0]))
    else:
        mess = "Please enter valid input"
    return render_template('html code.html', prediction = mess)


if __name__ == "__main__":
    app.run(port = 5000, debug = True)
