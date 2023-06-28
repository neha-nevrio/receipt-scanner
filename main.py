
from flask import *
import receipt_scanner


app = Flask(__name__)


@app.route('/scan', methods=['POST', 'GET'])
def request_page():
    args = request.args
    result = receipt_scanner.receipt_scanner(image_path=args.get('file'))

    return result

if __name__ == '__main__':
    app.run(port=7777, debug=True)
