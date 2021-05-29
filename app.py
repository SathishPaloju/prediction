import flask
import pandas as pd
import werkzeug
from flask import (Blueprint,Flask, flash, g, redirect, render_template, request, session, url_for)
# fit scalar on training data
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import VotingClassifier

from flask import send_file
# load models at top of app to load into memory only one time
# Loading the dataset onto running environment

# Load from file
import os

# gGLOBAL vVARIABLES

COL = ['EXT1', 'EXT2', 'EXT3', 'EXT4', 'EXT5', 'EXT6', 'EXT7', 'EXT8', 'EXT9', 'EXT10',
       'EST1', 'EST2', 'EST3', 'EST4', 'EST5', 'EST6', 'EST7', 'EST8', 'EST9', 'EST10',
       'AGR1', 'AGR2', 'AGR3', 'AGR4', 'AGR5', 'AGR6', 'AGR7', 'AGR8', 'AGR9', 'AGR10',
       'CSN1', 'CSN2', 'CSN3', 'CSN4', 'CSN5', 'CSN6', 'CSN7', 'CSN8', 'CSN9', 'CSN10',
       'OPN1', 'OPN2', 'OPN3', 'OPN4', 'OPN5', 'OPN6', 'OPN7', 'OPN8', 'OPN9', 'OPN10']
EXT1 = 0
EXT2 = 0
EXT3 = 0
EXT4 = 0
EXT5 = 0
EXT6 = 0
EXT7 = 0
EXT8 = 0
EXT9 = 0
EXT10 = 0
EST1 = 0
EST2 = 0
EST3 = 0
EST4 = 0
EST5 = 0
EST6 = 0
EST7 = 0
EST8 = 0
EST9 = 0
EST10 = 0
AGR1 = 0
AGR2 = 0
AGR3 = 0
AGR4 = 0
AGR5 = 0
AGR6 = 0
AGR7 = 0
AGR8 = 0
AGR9 = 0
AGR10 = 0
CNS1 = 0
CNS2 = 0
CNS3 = 0
CNS4 = 0
CNS5 = 0
CNS6 = 0
CNS7 = 0
CNS8 = 0
CNS9 = 0
CNS10 = 0
OPN1 =0
OPN2 =0
OPN3 =0
OPN4 =0
OPN5 =0
OPN6 =0
OPN7 =0
OPN8 =0
OPN9 =0
OPN10 =0


# app is an object of home page using Flask package
app = flask.Flask(__name__, template_folder='templates')


# route for home page
@app.route('/')
def main():
    return flask.render_template('index.html')


# route for EDA_show page
@app.route('/EDA_show')
def report():
    return flask.render_template('EDA_show.html')


# route for predict page
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    # flask.render_template('predict.html',title="predict ")
    if flask.request.method == 'GET':
        return flask.render_template('EXT.html')
    if flask.request.method == 'POST':
        return flask.render_template('EXT.html')


@app.route('/return-files/')
def return_files():
    return send_file(
        r'C:/Users/Administrator/PycharmProjects/Major_cse/static/- Manhattan GRE_ Algebra GRE Strategy Guide.pdf',
        attachment_filename='a.pdf')

@app.route('/EXT',methods=['GET', 'POST'])
def EXT():
    global EXT1 , EXT2 , EXT3 , EXT4 , EXT5 , EXT6 , EXT7 , EXT8 , EXT9 , EXT10
    # flask.render_template('predict.html',title="predict ")
    if flask.request.method == 'GET':
        return flask.render_template('EXT.html')
    if flask.request.method == 'POST':
        EXT1 = float(flask.request.form['EXT1'])
        print("rexc")
        print(EXT1)
        EXT2 = float(flask.request.form['EXT2'])
        EXT3 = float(flask.request.form['EXT3'])
        EXT4 = float(flask.request.form['EXT4'])
        EXT5 = float(flask.request.form['EXT5'])
        EXT6 = float(flask.request.form['EXT6'])
        EXT7 = float(flask.request.form['EXT7'])
        EXT8 = float(flask.request.form['EXT8'])
        EXT9 = float(flask.request.form['EXT9'])
        EXT10 = float(flask.request.form['EXT10'])
        print(EXT1,EXT2,EXT3)
        return flask.render_template('EST.html')


@app.route('/EST' ,methods=['GET', 'POST'])
def EST():
    global EST1 , EST2 , EST3 , EST4 , EST5 , EST6 , EST7 , EST8 , EST9 , EST10
    if flask.request.method == 'GET':
        return flask.render_template('EST.html')
    if flask.request.method == 'POST':
        EST1 = float(flask.request.form['EST1'])
        EST2 = float(flask.request.form['EST2'])
        EST3 = float(flask.request.form['EST3'])
        EST4 = float(flask.request.form['EST4'])
        EST5 = float(flask.request.form['EST5'])
        EST6 = float(flask.request.form['EST6'])
        EST7 = float(flask.request.form['EST7'])
        EST8 = float(flask.request.form['EST8'])
        EST9 = float(flask.request.form['EST9'])
        EST10 = float(flask.request.form['EST10'])
        print(EST10,EST1)
        print("fdghsb")
        print(EXT1,EXT2,EXT3)
        return flask.render_template('AGR.html')


@app.route('/AGR',methods=['GET', 'POST'])
def AGR():
    global AGR1 ,AGR2 ,AGR3 ,AGR4 ,AGR5 ,AGR6 ,AGR7 ,AGR8 ,AGR9 ,AGR10
    # flask.render_template('predict.html',title="predict ")
    if flask.request.method == 'GET':
        return flask.render_template('AGR.html')
    if flask.request.method == 'POST':
        AGR1 = float(flask.request.form['AGR1'])
        AGR2 = float(flask.request.form['AGR2'])
        AGR3 = float(flask.request.form['AGR3'])
        AGR4 = float(flask.request.form['AGR4'])
        AGR5 = float(flask.request.form['AGR5'])
        AGR6 = float(flask.request.form['AGR6'])
        AGR7 = float(flask.request.form['AGR7'])
        AGR8 = float(flask.request.form['AGR8'])
        AGR9 = float(flask.request.form['AGR9'])
        AGR10 = float(flask.request.form['AGR10'])
        return flask.render_template(r'CSN.html')
@app.route('/CSN',methods=['GET', 'POST'])
def CSN():
    global CSN1 , CSN2 , CSN3 , CSN4 , CSN5 , CSN6 , CSN7 , CSN8 , CSN9 , CSN10
    # flask.render_template('predict.html',title="predict ")
    if flask.request.method == 'GET':
        return flask.render_template('CSN.html')
    if flask.request.method == 'POST':
        CSN1 = float(flask.request.form['CNS1'])
        CSN2 = float(flask.request.form['CNS2'])
        CSN3 = float(flask.request.form['CNS3'])
        CSN4 = float(flask.request.form['CNS4'])
        CSN5 = float(flask.request.form['CNS5'])
        CSN6 = float(flask.request.form['CNS6'])
        CSN7 = float(flask.request.form['CNS7'])
        CSN8 = float(flask.request.form['CNS8'])
        CSN9 = float(flask.request.form['CNS9'])
        CSN10 = float(flask.request.form['CNS10'])
        return flask.render_template(r'OPN.html')

@app.route('/OPN',methods=['GET', 'POST'])
def OPN():
    global OPN1 , OPN2 , OPN3 , OPN4 , OPN5 , OPN6 , OPN7 , OPN8 , OPN9 , OPN10
    if flask.request.method == 'GET':
        return flask.render_template('OPN.html')
    if flask.request.method == 'POST':
        OPN1 = float(flask.request.form['OPN1'])
        OPN2 = float(flask.request.form['OPN2'])
        OPN3 = float(flask.request.form['OPN3'])
        OPN4 = float(flask.request.form['OPN4'])
        OPN5 = float(flask.request.form['OPN5'])
        OPN6 = float(flask.request.form['OPN6'])
        OPN7 = float(flask.request.form['OPN7'])
        OPN8 = float(flask.request.form['OPN8'])
        OPN9 = float(flask.request.form['OPN9'])
        OPN10 = float(flask.request.form['OPN10'])
        print(OPN1,OPN2,OPN3,OPN4,OPN5,OPN6)
        print(EST10,EST1)
        return flask.render_template(r'OPN.html')


@app.route('/result',methods=['GET', 'POST'])
def result():

        print(OPN10)
        return flask.render_template(r'result.html')


@app.route('/file_downloads/')
def file_downloads():
    return flask.render_template('download.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
