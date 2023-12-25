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



if __name__ == '__main__':
    app.run(debug=True)
