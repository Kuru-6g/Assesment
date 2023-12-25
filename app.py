from flask import Flask, request, render_template
import openai
import llamaindex

app = Flask(__name__)


def process_pdf(file):

    processed_text = llamaindex.process_pdf(file)
    return processed_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query-pdf', methods=['POST'])
def query_pdf():
    if 'pdf_file' not in request.files:
        return 'No file part'

    file = request.files['pdf_file']
    question = request.form['question']


    pdf_text = process_pdf(file)


if __name__ == '__main__':
    app.run(debug=True)
