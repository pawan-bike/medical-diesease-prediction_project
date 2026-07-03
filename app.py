from flask import Flask, render_template,url_for,request
app =Flask(__name__)

import joblib
model=joblib.load(r"C:\Users\abc\OneDrive\Desktop\anand collage 45 days traning\project\medical\model\RandomForestClassifier.lb")

@app.route('/')
def index():
    return render_template('index.html') 
@app.route('/contact')
def contact():
    return render_template('contact.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/project',methods=['GET','POST'])

def predict():
    prediction=None
    if request.method=="POST":
        Gender=1 if request.form['Gender']=='Male' else 0
        Smoking =1 if request.form['Smoking']=='Yes' else 0
        BMI=float(request.form['BMI'])
        Age=int(request.form['Age'])
        BloodPressure=int(request.form['BloodPressure'])
        HeartRate=int(request.form['HeartRate'])
        
        data=[[Gender,Smoking,Age,BMI,BloodPressure,HeartRate]]
        
        result=model.predict(data)
        print(result)
        
        
        if result[0]==1:
            prediction="disease:healthy"
        elif result[0]==2:
            prediction="disease:pre-dibates"
        elif result[0]==3:
            prediction="disease:Hypertension"
        elif result[0]==4:
            prediction="disease:Heart Disease"     
        elif result[0]==5:
            prediction="disease:Diabetes"   
            
    return render_template('project.html',prediction=prediction)
    
if __name__ == "__main__":
    app.run(debug=True)