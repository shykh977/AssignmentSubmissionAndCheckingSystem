import json
import os
from flask import Flask ,request,jsonify
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from DataAccessLayer.ApiMiddleware import Middleware
from DataConnectionLayer.DbConfig import DbConfig
from Controllers import register_blueprints
from PIL import Image
from io import BytesIO
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText



app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
CORS(app, resources={r"/*": {"origins": "*"}})
register_blueprints(app)


# @app.before_request
# def Invoke():	
#     mid = Middleware()
#     res =mid.authenticate_request()
#     return res


@app.route('/Create')
def upload():
	

    
    pdf_target = os.path.join(APP_ROOT, 'static/pdf')

    # Preparing directory
    if not os.path.isdir(pdf_target):
        os.mkdir(pdf_target)

    # Uploading File
    for file in request.files.getlist('file'):
        filename = file.filename
        destination = "/".join([pdf_target,filename])

        file.save(destination)

      
    return jsonify("Message:Application Started")
       
# def convert_pdf_to_images():
#     if 'PDF' not in request.files :
#         return "No file part"

#     pdf_file = request.files['PDF']

#     if pdf_file.filename == '':
#         return "No selected file"

#     if pdf_file:
#         pdf = PyPDF2.PdfReader(pdf_file)

#         image_list = []

#         for page_num in range(len(pdf.pages)):
#             page = pdf.pages[page_num]
#             xObject = page['/Resources']['/XObject'].get_object()

#             for obj in xObject:
#                 if xObject[obj]['/Subtype'] == '/Image':
#                     img = xObject[obj]
#                     img_data = img.get_data()
#                     img_format = img['/Filter'][1:]

#                     if 'JPXDecode' in img_format:
#                         img_format = 'jp2'
#                     elif 'DCTDecode' in img_format:
#                         img_format = 'jpeg'
#                     else:
#                         img_format = 'png'

#                     img_filename = f'page_{page_num + 1}_{obj[1:4]}.{img_format}'
#                     image_list.append(img_filename)

#                     with open(img_filename, 'wb') as img_file:
#                         img_file.write(img_data)




# subject = "Email Subject"
# body = "This is the body of the text message"
# sender = "btgtechnologies2021@gmail.com"
# recipients = ["shaikhnouman96@gmail.com"]
# password = "qsokaccacxqnctsn"


# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ', '.join(recipients)
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#        smtp_server.login(sender, password)
#        smtp_server.sendmail(sender, recipients, msg.as_string())
#     print("Message sent!")


# @app.route('/SendMail')
# def SendMail():
#       result = send_email(subject, body, sender, recipients, password)
      

#       return result


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True,host="0.0.0.0",port=9870)