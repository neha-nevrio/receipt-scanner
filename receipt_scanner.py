from docquery import document, pipeline

def receipt_scanner(image_path):
    p = pipeline('document-question-answering')
    doc = document.load_document(image_path)
    for q in ["What is the invoice number?", "What is the invoice total?"]:

        result = (p(question=q, **doc.context))
        print(result)

    return result



