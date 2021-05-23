import flask
import pickle
import pandas as pd
import werkzeug
from flask import Flask, render_template, url_for, request
# fit scaler on training data
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import  VotingClassifier
#load models at top of app to load into memory only one time
#Loading the dataset onto running environment 

# Load from file
import os
os.chdir(r"C:\Users\Administrator\Downloads\loan-default-prediction-master")
pkl_filename = r'models\pickle_model.pkl'
with open(pkl_filename, "rb") as file:
    ensemble_model_new= pickle.load(file)
df_train = pd.read_csv(r'data\data.csv')

#app is an object of home page using Flask package
app = flask.Flask(__name__,template_folder='templates')

#route for home page
@app.route('/')
def main():
    return (flask.render_template('index.html'))

#route for EDA_show page
@app.route('/EDA_show')
def report():
    return (flask.render_template('EDA_show.html'))

#route for predict page
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    
        #flask.render_template('predict.html',title="predict ")
    if flask.request.method == 'GET':
        return (flask.render_template('predict.html'))
    if flask.request.method == 'POST':
        col = []
        
        pred = ensemble_model_new.predict(temp)
        
        
        return flask.render_template(r'predict.html', result=res)
from flask import send_from_directory, current_app as app

@app.route('/show/PDFs/')
def send_pdf():
    return send_from_directory(app.config[r'C:\Users\Administrator\OneDrive\Desktop\Manhattan GRE_ Algebra GRE Strategy Guide.pdf'], 'file.pdf')
if __name__ == '__main__':
    app.run(debug=True,port=5000)
