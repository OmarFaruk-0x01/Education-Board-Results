from flask import Flask, json, request, send_from_directory, send_file
from flask.typing import StatusCode
from Lib import ResultTracker, HTMLGenaretion
import requests as req
import os
from random import choice
from Lib.UserAgents import UserAgents
app = Flask(__name__)
app.config['PDF_DIR'] = os.path.join(os.path.abspath('.'), 'PDF_DIR')

if (not os.path.exists(app.config['PDF_DIR'])):
    os.mkdir(app.config['PDF_DIR'])


@app.route('/')
def root():
    try:
        isActive = req.get(
            'http://www.educationboardresults.gov.bd/index.php', timeout=1, headers={"User-Agent": choice(UserAgents)})
        return json.jsonify(StatusCode=200, message="ok")
    except:
        return json.jsonify(StatusCode=404, message="fail")


@app.route('/getPDF/<roll>')
def getPDF(roll):
    try:
        return send_file(path_or_file=os.path.join(app.config['PDF_DIR'], f"{roll}.pdf"), mimetype='application/pdf', download_name=f"{roll}.pdf")
    except Exception as e:
        return json.jsonify(StatusCode=500, message="file not found", arg=e.args)


@app.route('/genPDF', methods=['POST'])
def genPDF():
    getData = request.get_json()
    print(getData)
    genHTML = HTMLGenaretion.GenarateHtml(getData)

    isError = ResultTracker.convert_html_to_pdf(
        genHTML, os.path.join(app.config['PDF_DIR'], f'{getData["roll"]}.pdf'))
    if (not isError):
        try:
            return json.jsonify(StatusCode=200, message="PDF Genaration Complete", downLink="https://educationboardresult-bd.herokuapp.com/getPDF/"+getData["roll"])
        except Exception as e:
            return json.jsonify(StatusCode=500, message="Somting went wrong", arg=e.args)
    else:
        return json.jsonify(StatusCode=500, message="Somting went wrong", arg=isError)


@app.route('/getresult', methods=["POST"])
def getresult():
    getData = request.get_json()
    try:
        result = ResultTracker.GetResult(**getData)
        return json.jsonify(**result)
    except Exception as e:
        print(e)
        return json.jsonify(StatusCode=500, status="Error!", message="Someting wrong is heppening", arg=e.args)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=os.environ.get('PORT'))
