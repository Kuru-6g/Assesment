from flask import Flask, request, render_template
import openai
from llamaindex import process_pdf  # Import the Llama Index processing function

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query-pdf', methods=['POST'])
def query_pdf():
    if 'pdf_file' not in request.files:
        return 'No file part'

    file = request.files['pdf_file']
    question = request.form['question']

    # Process the PDF file using Llama Index
    pdf_text = process_pdf(file.read())  # Use the function from llamaindex.py

    # Query using OpenAI
    response = openai.Answer.create(
        documents=[pdf_text],  # Processed text from PDF
        question=question,
        search_model="davinci",  # Choose the model
        model="curie",  # Choose the model for answers
        examples_context="In 2017, U.S. life expectancy was 78.6 years.",
        examples=[["What is human life expectancy in the United States?", "78 years."]]
    )

    return response['answers'][0]


if __name__ == '__main__':
    app.run(debug=True)
