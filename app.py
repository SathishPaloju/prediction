import flask
import pandas as pd
import werkzeug
from flask import Flask, render_template, url_for, request
# fit scaler on training data
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import VotingClassifier

from flask import send_file
# load models at top of app to load into memory only one time
# Loading the dataset onto running environment

# Load from file
import os

# app is an object of home page using Flask package
app = flask.Flask(__name__, template_folder='templates')


# route for home page
@app.route('/')
def main():
    return (flask.render_template('index.html'))


# route for EDA_show page
@app.route('/EDA_show')
def report():
    return (flask.render_template('EDA_show.html'))


# route for predict page
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    # flask.render_template('predict.html',title="predict ")
    if flask.request.method == 'GET':
        return (flask.render_template('agree_disagree.html'))
    if flask.request.method == 'POST':
        col = []

        pred = ensemble_model_new.predict(temp)

        return flask.render_template(r'predict.html', result=res)

@app.route("/slider", methods=['GET', 'POST'])
def slider():
    # flask.render_template('predict.html',title="predict ")
    if flask.request.method == 'GET':
        return (flask.render_template('slider.html'))
    if flask.request.method == 'POST':
        col = []
        return flask.render_template(r'slider.html', result=res)


@app.route('/return-files/')
def return_files():
    return send_file(
        r'C:/Users/Administrator/PycharmProjects/Major_cse/static/- Manhattan GRE_ Algebra GRE Strategy Guide.pdf',
        attachment_filename='a.pdf')


@app.route('/file_downloads/')
def file_downloads():
    return flask.render_template('download.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
