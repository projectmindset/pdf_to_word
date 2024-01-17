# from flask import Flask, render_template, request, send_file

# import tempfile
# import pdf2docx

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/convert', methods=['POST'])
# def convert_pdf_to_docx():
#     try:
#         pdf_file = request.files['pdfFile']
#         if pdf_file:
#             # Create a temporary directory to store the converted .docx file
#             with tempfile.TemporaryDirectory() as tmpdirname:
#                 pdf_path = f"{tmpdirname}/input.pdf"
#                 docx_path = f"{tmpdirname}/output.docx"

#                 # Save the uploaded PDF to a temporary file
#                 pdf_file.save(pdf_path)

#                 # Convert PDF to .docx
#                 pdf2docx.Converter(pdf_path).convert(docx_path)

#                 # Send the converted .docx file as a response
#                 return send_file(docx_path, as_attachment=True, download_name="converted_document.docx")

#     except Exception as e:
#         return str(e)

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, send_file, jsonify
# import tempfile
# import pdf2docx

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/convert', methods=['POST'])
# def convert_pdf_to_docx():
#     try:
#         pdf_file = request.files['pdfFile']
#         if pdf_file:
#             # Create a temporary directory to store the converted .docx file
#             with tempfile.TemporaryDirectory() as tmpdirname:
#                 pdf_path = f"{tmpdirname}/input.pdf"
#                 docx_path = f"{tmpdirname}/output.docx"

#                 # Save the uploaded PDF to a temporary file
#                 pdf_file.save(pdf_path)

#                 # Convert PDF to .docx
#                 pdf2docx.Converter(pdf_path).convert(docx_path)

#                 # Return a JSON response with the download URL
#                 response = {
#                     'url': docx_path
#                 }
#                 return jsonify(response)

#     except Exception as e:
#         return str(e)

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, send_file, jsonify
# import tempfile
# import pdf2docx

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/convert', methods=['POST'])
# def convert_pdf_to_docx():
#     try:
#         pdf_file = request.files['pdfFile']
#         if pdf_file:
#             # Creating a temporary directory to store the converted .docx file
#             with tempfile.TemporaryDirectory() as tmpdirname:
#                 pdf_path = f"{tmpdirname}/input.pdf"
#                 docx_path = f"{tmpdirname}/output.docx"

#                 # Save the uploaded PDF to a temporary file
#                 pdf_file.save(pdf_path)

#                 # Log a message to confirm file creation
#                 print(f"Saved PDF file to: {pdf_path}")

#                 # Convert PDF to .docx
#                 pdf2docx.Converter(pdf_path).convert(docx_path)

#                 # Log a message to confirm .docx file creation
#                 print(f"Converted file saved to: {docx_path}")

#                 # Return a JSON response with the download URL
#                 response = {
#                     'url': docx_path
#                 }
#                 return jsonify(response)

#     except Exception as e:
#         return str(e)

# if __name__ == '__main__':
#     app.run(debug=True)


'''TRIAL 4'''


# # Defining the custom file path (destination) for the .docx file on the desktop
# desktop_path = os.path.expanduser("~/Desktop")
# docx_path = os.path.join(desktop_path, "docs", "output.docx")

#importing necessary libraries
from flask import Flask, render_template, request, send_file, jsonify
#importing Flask specifically for its ability to generate http responses such as rendering html templates, returning JSON data and sending files.
import tempfile
import pdf2docx
import os

app = Flask(__name__)

#defining a route for the homepage
'''
A route is a URL pattern that your web application responds to.
It defines how  an application should handle incoming http requests 
''' 

@app.route('/')
def home():
    return render_template('index.html')

#defining a route for handling the conversion request
#this part of the code is responsible for 
@app.route('/convert', methods=['POST'])
def convert_pdf_to_docx():
    try:
        pdf_file = request.files['pdfFile']
        if pdf_file:
            # Define the custom file path for the .docx file on the desktop
            desktop_path = os.path.expanduser("~/Desktop")
            docx_path = os.path.join(desktop_path, "docs", "output.docx")

            # Save the uploaded PDF to a temporary file
            pdf_path = f"{tempfile.gettempdir()}/input.pdf"
            pdf_file.save(pdf_path)

            # Convert PDF to .docx using pdf2docx library function
            pdf2docx.Converter(pdf_path).convert(docx_path)

            # Return a JSON response with the download URL
            response = {
                'url': docx_path
            }
            return jsonify(response)

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)