from flask import *
import json, time
import receipt_scanner

app = Flask(__name__)

@app.route('/response', methods=['POST', 'GET'])
def request_page():
    result = receipt_scanner.receipt_scanner(image_path="receipt1.jpg")
    # data_set = {'Name':'XYX', 'Date':'23-07-2023', 'Total': '78', 'Time':time.time()}
    response = json.dumps(result, time.time())

    return response

if __name__ == '__main__':
    app.run(port=7777, debug=True)
