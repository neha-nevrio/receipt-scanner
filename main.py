from flask import *
import receipt_scanner

app = Flask(__name__)

@app.route('/response', methods=['POST', 'GET'])
def request_page():
    result = receipt_scanner.receipt_scanner(image_path=url)

    return result

if __name__ == '__main__':
    app.run(port=7777, debug=True)
