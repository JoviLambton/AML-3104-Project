import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from flask import Flask,request,jsonify,render_template
from keras.models import load_model

application=Flask(__name__)
app=application


ann_model=pickle.load(open('ann_model.pkl', 'rb'))
standard_scaler=pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['Get', 'Post'])
def predict_datapoint():
    if request.method=='POST':
        age=float(request.form.get('age'))
        job=float(request.form.get('job'))
        marital=float(request.form.get('marital'))
        education=float(request.form.get('education'))
        month=float(request.form.get('month'))
        day_of_week=float(request.form.get('day_of_week'))
        default=float(request.form.get('default'))
        housing=float(request.form.get('housing'))
        loan=float(request.form.get('loan'))
        contact=float(request.form.get('contact'))
        duration=float(request.form.get('duration'))
        campaign=float(request.form.get('campaign'))
        pdays=float(request.form.get('pdays'))
        previous=float(request.form.get('previous'))
        poutcome=float(request.form.get('poutcome'))
        empvarrate=float(request.form.get('empvarrate'))
        consconfidx=float(request.form.get('consconfidx'))

        new_data_sc=standard_scaler.transform([[age,job,marital,education,month,day_of_week,default,housing,loan,contact,duration,campaign,pdays,previous,poutcome,empvarrate,consconfidx]])

        result=ann_model.predict(new_data_sc)        
        return render_template('index.html', result=result[0])
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(host="127.0.0.1", port=7000)