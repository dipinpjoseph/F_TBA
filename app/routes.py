from app import app
from flask import render_template
from flask import Response,request
import os

@app.route('/')
def index():
    print(os.getcwd())
    data = {}
    data["title"] = "The Beginner's Arsenal"
    data["desc"] = "Home Page of The Beginner's Arsenal"

    return render_template('index.html', data=data)

@app.route('/find-determinant-of-matrix', methods=['GET','POST'])
def det_mat():
    from modules import DetMat
    gen_form = DetMat.GenForm()
    data = {}
    data["title"] = "Online Matrix Determinant Calculator"
    data["desc"] = "Perform matrix operation - determinant"
    data["app"] = "Determinant of Matrix"
    data["n_val"] = 0
    data["det"] = -1
    if request.method == "POST":
        if gen_form.validate_on_submit():
            data["n_val"] = gen_form.n_val.data
            if "ip_0" in request.form:
                mat =[]
                for i in range(data["n_val"]):
                    e_row = request.form.get('ip_'+str(i))
                    e_row = [int(s) for s in e_row.split(',')]
                    mat.append(e_row)
                import numpy as np
                data["det"] = np.linalg.det(mat)
        return render_template('det_matrix.html', data=data, gen_form=gen_form)
    return render_template('det_matrix.html', data=data, gen_form=gen_form)

@app.route('/ads.txt')
def ads_google():
    with open("app/ads.txt", "r") as f:
        con = f.read()
    return(Response(con, mimetype='text/plain'))

@app.route('/QR-Code-Generator')
def qr_code_gen():
    return render_template("QR-Code-Generator.html")

@app.route('/Bar-Code-Generator')
def bar_code_gen():
    return render_template("Bar-Code-Generator.html")

@app.route('/Extract-Emails-From-Text')
def extract_email():
    return render_template('Extract-Emails-From-Text.html')

@app.route('/Find-Permutation-and-Combination-Online')
def perm_comb():
    return render_template('Find-Permutation-and-Combination-Online.html')

@app.route('/Frequent-Linux-Commands-List')
def freq_linux_cmds():
    return render_template('Frequent-Linux-Commands-List.html')

@app.route('/Morse-Code-Generator')
def morse_code_gen():
    return render_template('Morse-Code-Generator.html')

@app.route('/NZ-PostCode-Finder')
def nz_postcode_finder():
    return render_template('NZ-PostCode-Finder.html')

@app.route('/Online-BMI-Calculator')
def bmi_cal():
    return render_template('Online-BMI-Calculator.html')

@app.route('/python-tips-and-tricks')
def python_tips():
    return render_template('python-tips-and-tricks.html')

@app.route('/SQL-Commands-List')
def sql_cmds():
    return render_template('SQL-Commands-List.html')

@app.route('/vim-useful-shortcuts')
def vim_shortcuts():
    return render_template('vim-useful-shortcuts.html')

@app.route('/The-Elite-List-Home')
def elite_list_home():
    return render_template('The-Elite-List-Home.html')
