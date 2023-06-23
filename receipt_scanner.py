from docquery import document, pipeline

def receipt_scanner(image_path):
    p = pipeline('document-question-answering')
    doc = document.load_document(image_path)
    resultArr = []
    for q in ["name","date","What is the invoice number?", "What is the invoice total?"]:

        result = (p(question=q, **doc.context))

        resultArr.append(result[0]['answer'])

    resultJson = {
        "Seller name": resultArr[0],
        "Date": resultArr[1],
        "Invoice number": resultArr[2],
        "Total amount": resultArr[3]
    }



    return resultJson



