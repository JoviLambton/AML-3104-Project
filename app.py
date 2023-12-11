import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from flask import Flask,request,jsonify,render_template

application=Flask(__name__)
app=application


model_dtree = pickle.load(open('model_dtree.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
outlier_limits = pickle.load(open('outlier_limits.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['Get', 'Post'])
def predict_datapoint():
    if request.method=='POST':

        # Get user input
        age = float(request.form.get('age'))
        balance = float(request.form.get('balance'))
        pdays = float(request.form.get('pdays'))
        previous = float(request.form.get('previous'))
        job = request.form.get('job')
        marital = request.form.get('marital')
        education = request.form.get('education')
        housing = request.form.get('housing')
        loan = request.form.get('loan')
        contact = request.form.get('contact')
        month = request.form.get('month')
        poutcome = request.form.get('poutcome')
        
        # Create dataframe with all the data
        model_data = pd.DataFrame({
                'age' : [age],
                'balance' : [balance],
                'pdays' : [pdays],
                'previous' : [previous],
                'job' : [job],
                'marital' : [marital],
                'education' : [education],
                'housing' : [housing],
                'loan' : [loan],
                'contact' : [contact],
                'month' : [month],
                'poutcome' : [poutcome],
                'default' : ['x'] # Added dummy value, this feature is not used in prediction
                })

        # Encode categorical data to numeric
        model_data['job_retired_student'] = model_data['job'].apply(lambda value: 1 if value.lower() in ['retired', 'student'] else 0)
        model_data['marital_single'] = model_data['marital'].apply(lambda value: 1 if value.lower() == 'single' else 0)
        model_data['education_primary_secondary'] = model_data['education'].apply(lambda value: 1 if value.lower() in ['primary','secondary'] else 0)
        model_data['default_yes'] = model_data['default'].apply(lambda value: 1 if value.lower() == 'yes' else 0)
        model_data['housing_yes'] = model_data['housing'].apply(lambda value: 1 if value.lower() == 'yes' else 0)
        model_data['loan_yes'] = model_data['loan'].apply(lambda value: 1 if value.lower() == 'yes' else 0)
        model_data['contact_cellular_telephone'] = model_data['contact'].apply(lambda value: 1 if value.lower() in ['cellular','telephone'] else 0)
        model_data['month_feb_mar_apr_sep_oct_dec'] = model_data['month'].apply(lambda value: 1 if value.lower() in ['feb', 'mar', 'apr', 'oct', 'sep', 'dec'] else 0)
        model_data['poutcome_success'] = model_data['poutcome'].apply(lambda value: 1 if value.lower() == 'success' else 0)
    
        # Create dataframe for encoded features
        x_test = model_data[['age',
                        'balance',
                        'pdays',
                        'previous',
                        'job_retired_student',
                        'marital_single',
                        'education_primary_secondary',
                        'default_yes', # Added
                        'housing_yes',
                        'loan_yes',
                        'contact_cellular_telephone',
                        'month_feb_mar_apr_sep_oct_dec',
                        'poutcome_success'
                        ]]
    
        # Function to check for outliers and cap values of outliers
        def RemoveOutliers(inData,inOutliers):
            
            # Initialize blank dataframes
            outData = inData
            
            # Loop through all features
            for colName in inData.columns:
                
                if colName in list(inOutliers.keys()):
                    
                    min_val = inOutliers.get(colName)[0]  # Lower limit
                    max_val = inOutliers.get(colName)[1]  # Upper limit
                    
                    # If the value is lower/greater than the min/max limits, it is an outlier
                    outliers = inData[(inData[colName] < min_val) | (inData[colName] > max_val)]
                    
                    # For outliers, apply capping -- replace the value with either the lower or upper limit
                    outData[colName] = np.where( inData[colName] > max_val, max_val, np.where( inData[colName] < min_val, min_val, inData[colName] ) )
                    
                    # Summary per feature
                    # print(f'No. of outliers for {colName}: {outliers.shape[0]} \t\tLimits: {round(min_val,4)} , {round(max_val,4)}')
                    
                else:
                    outData[colName] = inData[colName].values
            
            return outData

        # Check and handle outliers of the data. For the test set, the lower/upper limits will be the same as the training set.
        x_test_no_outliers = RemoveOutliers(x_test,outlier_limits)
   
        # Scale features
        x_test_sc = scaler.transform(x_test_no_outliers)
        
        # Predict target variable
        y_pred_test_dtree = model_dtree.predict(x_test_sc)
        
        # Class prediction    
        if [y_pred_test_dtree][0][0] == 1:
            result = 'YES'
        else:
            result = 'NO'
            
        # return render_template('index.html', result=result[0])
        # age = float(request.form.get('age'))
        return render_template('index.html', result=result)
    
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
# if __name__ == "__main__":
#     app.run(debug=True)