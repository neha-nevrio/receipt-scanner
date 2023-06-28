
def receipt_scanner(p, doc):

    resultArr = []
    for q in ["name", "date", "What is the invoice number?", "What is the invoice total?"]:
        result = (p(question=q, **doc.context))

        resultArr.append(result[0]['answer'])

    resultJson = {
        "Seller name": resultArr[0],
        "Date": resultArr[1],
        "Invoice number": resultArr[2],
        "Total amount": resultArr[3]
    }

    return resultJson
