
from flask import *
import receipt_scanner
from docquery import document, pipeline


app = Flask(__name__)
p = pipeline('document-question-answering')


@app.route('/scan', methods=['POST', 'GET'])
def request_page():

    try:
        args = request.args
        doc = document.load_document(args.get('file'))
        result = receipt_scanner.receipt_scanner(p, doc)

    except Exception as e:
        result = str(e)

    return result

if __name__ == '__main__':
    app.run(port=7777, debug=True)
