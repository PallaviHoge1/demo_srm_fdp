from flask import Flask, request, render_template
from qna import qna
from summarize import summarize # Assuming summarize.py has this function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        global content
        content = file.read().decode('utf-8')  # Assuming the document is text-based
        summary = summarize(content)  # Call the summarization function
        return render_template('index.html', summary=summary)

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form['question']
    print(question, content)
    # Here you can implement your Q&A logic
    answer = qna(content, question)  # Call the function to get the answer
    print(answer)
    return render_template('index.html', answer=answer)


if __name__ == '__main__':
    app.run(debug=True)
