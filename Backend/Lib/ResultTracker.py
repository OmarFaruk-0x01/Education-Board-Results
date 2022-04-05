import requests as req
from os.path import join as pathJoin, abspath
from bs4 import BeautifulSoup as bs
from xhtml2pdf import pisa
from random import choice
from .UserAgents import UserAgents
EXAM = {
    "JSC/JDC": "jsc",
    "SSC(Vocational)": "ssc_voc",
    "SSC/Dakhil": "ssc",
    "HSC/Alim/Equivalent": "hsc",
    "HSC()": 'hsc_voc',
    "HSC(BM)": 'hsc_hbm',
    "Diploma in Commerce": 'hsc_dic',
    "Diploma in Business Studies": "hsc"
}

BOARD = {
    "Dhaka": 'dhaka',
    "Barisal": "barisal",
    "Chittagong": "chittagong",
    "Comilla": "comilla",
    "Dinajpur": "dinajpur",
    "Jessore": "jessore",
    "Mymensingh": "mymensingh",
    "Rajshahi": "rajshahi",
    "Shylet": "shylet",
    "Madrasah": "madrasah",
    "Technical": "tec",
    "DIBS(Dhaka)": "dibs",
}


def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF

    pisa_status = pisa.CreatePDF(
        source_html,                # the HTML to convert
        dest=result_file, raise_exception=True)           # file handle to recieve result
    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err


def GetResult(exam, year, board, roll, reg):
    ss = req.Session()
    indexPage = ss.get("http://www.educationboardresults.gov.bd/index.php")
    soup = bs(indexPage.content, 'html.parser')
    captcha_string = soup.select_one(
        "body fieldset > table > tr:nth-child(7) > td:nth-child(2)").text
    captcha_solved = eval(captcha_string)
    headers = {
        "User-Agent": choice(UserAgents),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "sr": '3',  # f"{random.randint(1,5)}",
        "et": '2',  # f"{random.randint(1,5)}",
        "exam": f"{EXAM[exam]}",
        'year': f"{year}",
        "board": f'{BOARD[board]}',
        'roll': roll,
        "reg": reg,
        'value_s': captcha_solved,
        'button2': 'Submit'
    }
    resultPage = ss.post(
        'http://www.educationboardresults.gov.bd/result.php', data=data, headers=headers)
    # resultPage = ss.get(
    #     'https://stainedfinefirewall.haxzsadik.repl.co/')
    resultSoup = bs(resultPage.content, 'html.parser')
    html = resultPage.text.replace(
        "src=\"", "src=\"http://www.educationboardresults.gov.bd/")
    html = html.replace(
        "href=\"", "href=\"http://www.educationboardresults.gov.bd/")
    html = html.replace(
        "background=\"", "background=\"http://www.educationboardresults.gov.bd/")

    AllinfoTable = resultSoup.find_all('table', {"class": 'black12'})
    if (AllinfoTable):
        infoTable = AllinfoTable[0]
        gradeSheet = AllinfoTable[-1]
        allSubjectGreades = []
        name = infoTable.select_one(
            "tr:nth-child(1) > td:nth-child(4)").text.strip()
        fathersName = infoTable.select_one(
            "tr:nth-child(2) > td:nth-child(4)").text.strip()
        mothersName = infoTable.select_one(
            "tr:nth-child(3) > td:nth-child(4)").text.strip()
        group = infoTable.select_one(
            "tr:nth-child(3) > td:nth-child(2)").text.strip()
        _type = infoTable.select_one(
            "tr:nth-child(4) > td:nth-child(2)").text.strip()
        Dob = infoTable.select_one(
            "tr:nth-child(4) > td:nth-child(4)").text.strip()
        result = infoTable.select_one(
            "tr:nth-child(5) > td:nth-child(2)").text.strip()
        institute = infoTable.select_one(
            "tr:nth-child(5) > td:nth-child(4)").text.strip()
        gpa = infoTable.select_one(
            "tr:nth-child(6) > td:nth-child(2)").text.strip()
        exam = exam.replace('/', "_")

        for row in gradeSheet.select("tr")[1:]:
            allSubjectGreades.append({
                'subjectName': row.select_one('td:nth-child(2)').text.strip(),
                'subjectCode': row.select_one('td:nth-child(1)').text.strip(),
                'subjectGPA': row.select_one('td:nth-child(3)').text.strip()
            })

        return {
            "StatusCode": 200,
            "name": name,
            "father_name": fathersName,
            "mother_name": mothersName,
            "board": board.title(),
            "group": group,
            "dob": Dob,
            "type": _type,
            "roll": roll,
            "result": result,
            "institute": institute,
            'gpa': gpa,
            "year": year,
            'subject_grades': allSubjectGreades
        }
    else:
        return {
            "StatusCode": 404,
            "message": 'Wrong Information. Check Clearly!!',
            "status": 'Error',
        }
