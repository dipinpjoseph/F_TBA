from app import app
from flask import render_template
from flask import Response,request
import os 
from models import E_List, db
from modules import utils

@app.route('/')
def index():
    print(os.getcwd())
    data = {}
    data["title"] = "The Beginner's Arsenal"
    data["desc"] = "Home Page of The Beginner's Arsenal"

    return render_template('Index.html', data=data)

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

@app.route('/Update_Elite_List', methods=['GET','POST'])
def update_elite_list():
    cat = ['Linux', 'SQL', 'Python', 'VIM','Spark','Raspberry-Pi']
    data = {}
    data["title"] = "Elite List Updation"
    data["desc"] = "Portal to update Elite List"
    data["app"] = "Elite List Update"
    if request.method == "POST":
        cat = request.form.get('cat')
        topic = request.form.get('topic')
        sol = request.form.get('sol')
        comment = request.form.get('comment')
        
        new_entry = E_List(topic, sol, comment, cat)
        db.session.add(new_entry)
        db.session.commit()
        
        return render_template('Update_E_List.html', data=data)

    return render_template('Update_E_List.html', data=data, cat=cat)

@app.route("/robots.txt")
def robots_dot_txt():
    return app.send_static_file("robots.txt")

@app.route('/ads.txt')
def ads_google():
    return app.send_static_file("ads.txt")

@app.errorhandler(404)
def page_not_found(e):
    data = {}
    data["title"] = "Page not found | TheBeArsenal"
    data["desc"] = "The requested page is not present in the application"
    data["app"] = "Page Not Found"
    return render_template('404.html',data=data), 404

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

@app.route('/The-Elite-List-Home')
def el_home():
    data = {}
    data["title"] = "The Elite List Home"
    data["desc"] = "Homepage for all technical handbooks"
    data["app"] = "The Elite List | Home"
    return render_template('EL_Home.html', data=data)

@app.route('/EL/<list_cat>')
def el_gen(list_cat):
    con = E_List.query.filter_by(cat=list_cat)
    return render_template('EL_Template.html', data=utils.pre_load(list_cat, list_cat+" Tips, Errors and Solutions", list_cat+" - The Elite List"), con=con)


@app.route('/Morse-Code-Generator')
def morse_code_gen():
    return render_template('Morse-Code-Generator.html')

@app.route('/NZ-PostCode-Finder')
def nz_postcode_finder():
    return render_template('NZ-PostCode-Finder.html')

@app.route('/Online-BMI-Calculator')
def bmi_cal():
    return render_template('Online-BMI-Calculator.html')

@app.route('/The-Elite-List-Home')
def elite_list_home():
    return render_template('The-Elite-List-Home.html')


@app.route("/sitemap")
@app.route("/sitemap/")
@app.route("/sitemap.xml")
def sitemap():
    
    from flask import make_response, request, render_template
    import datetime
    from urllib.parse import urlparse

    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc

    # Static routes with static content
    static_urls = list()
    for rule in app.url_map.iter_rules():
        if not str(rule).startswith("/admin") and not str(rule).startswith("/user"):
            if "GET" in rule.methods and len(rule.arguments) == 0:
                url = {
                    "loc": f"{host_base}{str(rule)}"
                }
                static_urls.append(url)

    xml_sitemap = render_template("sitemap.xml", static_urls=static_urls, host_base=host_base)
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response
