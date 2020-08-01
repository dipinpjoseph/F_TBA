from app import app
from flask import render_template, flash
from flask import Response,request
import os 
from models import E_List, db
from modules import utils

@app.route('/')
def index():
    return render_template('Index.html', data=utils.pre_load("The Beginner's Arsenal","Home Page of The Beginner's Arsenal",""))

@app.route("/robots.txt")
def robots_dot_txt():
    return app.send_static_file("robots.txt")

@app.route('/ads.txt')
def ads_google():
    return app.send_static_file("ads.txt")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',data=utils.pre_load("Page not found | TheBeArsenal","he requested page is not present in the application","Page Not Found")), 404

@app.route("/sitemap")
@app.route("/sitemap/")
@app.route("/sitemap.xml")
def sitemap():
    from flask import make_response
    xml_sitemap = render_template("sitemap.xml")
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/QR-Code-Generator')
def qr_code_gen():
    return render_template("QR_Code.html", data=utils.pre_load("Generate QR Code Online","Generate and download QR code","QR Code Generator"))

@app.route('/Bar-Code-Generator')
def bar_code_gen():
    return render_template("Bar_Code.html", data=utils.pre_load("Generate Bar Code Online for Free","Online Bar Code Generator","Bar Code Generator"))

@app.route('/Extract-Emails-From-Text')
def extract_email():
    return render_template('Extract_Emails.html', data=utils.pre_load("Extract Emails from Text Online","Extract emails from text - Online","Emails from Text"))

@app.route('/Find-Permutation-and-Combination-Online')
def perm_comb():
    return render_template('Perm_Comb.html', data=utils.pre_load("Find Permutation and Combination Online","Calculate Permutations and Combinations of two numbers online","Permutation & Combination Finder"))

@app.route('/Morse-Code-Generator')
def morse_code_gen():
    return render_template('Morse_Code_Generator.html', data=utils.pre_load("Text to Morse Code Converter Online","Generate Morse Code Online","Text to Morse Code Online"))

@app.route('/NZ-PostCode-Finder')
def nz_postcode_finder():
    return render_template('NZ_PostCode_Finder.html', data=utils.pre_load("Find New Zealand Post Codes Online","Find Postal Codes in New Zealand Suburbs","Post Code Finder - New Zealand"))

@app.route('/Online-BMI-Calculator')
def bmi_cal():
    return render_template('Online_BMI_Calculator.html', data=utils.pre_load("Online-BMI-Calculator","BMI calculator online from height and weight","BMI Calculator"))

@app.route('/The-Elite-List-Home')
def el_home():
    return render_template('EL_Home.html', data=utils.pre_load("The Elite List Home","Homepage for all technical handbooks","The Elite List | Home"))

@app.route('/EL/<list_cat>')
def el_gen(list_cat):
    con = E_List.query.filter_by(cat=list_cat)
    return render_template('EL_Template.html', data=utils.pre_load(list_cat, list_cat+" Tips, Errors and Solutions", list_cat+" - The Elite List"), con=con)

@app.route('/Update-Elite-List', methods=['GET','POST'])
def update_elite_list():
    cat = ['R','Linux', 'SQL', 'Python', 'VIM','Spark','Raspberry-Pi']
    data = utils.pre_load("Elite List Updation","Portal to update Elite List","Elite List Update")
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

@app.route('/find-determinant-of-matrix', methods=['GET','POST'])
def det_mat():
    from modules import DetMat
    gen_form = DetMat.GenForm()
    data = utils.pre_load("Online Matrix Determinant Calculator","Perform matrix operation - determinant","Determinant of Matrix")
    data["n_val"] = 0
    data["det"] = -1
    if request.method == "POST":
        if gen_form.validate_on_submit():
            try:
                data["n_val"] = gen_form.n_val.data
                if "ip_0" in request.form:
                    mat =[]
                    for i in range(data["n_val"]):
                        e_row = request.form.get('ip_'+str(i))
                        e_row = [float(s) for s in e_row.split(',')]
                        mat.append(e_row)
                    import numpy as np
                    data["det"] = round(np.linalg.det(mat),2)
            except:
                data["det"] = "Error, please check the input."        
        return render_template('Det_Matrix.html', data=data, gen_form=gen_form)
    return render_template('Det_Matrix.html', data=data, gen_form=gen_form)

@app.route('/Fiber-Optic-Color-Code-Finder')
def focc_finder():
    return render_template('Fiber-Optic-Color-Coder-Finder.html')
    
@app.route('/Online-Video-Splitter', methods=['GET','POST'])
def vid_splitter():
    from modules import VideoEditor
    from werkzeug.utils import secure_filename
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    
    data = utils.pre_load("Online-Video-Editor","Online Video Splitter in Python","Online Video Splitter")
    data['result'] = ""
    data["file_download"] = ""
    data["intervals"] = ""
    vid_form = VideoEditor.VidForm()
    if request.method == "POST":
        if vid_form.file_download.data != "":
            from flask import send_file
            return send_file(os.path.join('../', str(vid_form.file_download.data)), as_attachment=True)
            #os.remove(str(vid_form.file_download.data))

        try:            
            file = request.files['target_file']
            data["intervals"] = vid_form.intervals.data
            intervals = vid_form.intervals.data.split(",")
            
            filename = secure_filename(file.filename)
            file.save(filename)
                  
            splits_files = []
            
            for interval in intervals:
                start, end = interval.split(":")
                file_path_op = filename.split(".")[0]+start+"-"+end+".mp4"
                ffmpeg_extract_subclip(filename, int(start), int(end), targetname=file_path_op)
                splits_files.append(file_path_op)
                
            file_path_zip =  filename.split(".")[0]+".zip"
            import zipfile
            with zipfile.ZipFile(file_path_zip, 'a') as myzip:
                for each_path in splits_files:
                    myzip.write(each_path)
                    os.remove(each_path)
            os.remove(filename)
            data['result'] = "Split operation completed successfully. Please click the below button to download."
            data["file_download"] = file_path_zip
            return render_template('Video-Splitter.html', data=data, vid_form = vid_form)
            
        except  Exception as e:
            print(e)
            data["result"] = "Exception: "+str(e)
            return render_template('Video-Splitter.html', data=data, vid_form = vid_form)

    return render_template('Video-Splitter.html', data=data, vid_form = vid_form)

    
