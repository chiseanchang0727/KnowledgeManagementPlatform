from llm.applications.text_summary import get_text_summary



def text_summary():
    file_path = './data/text_data/paper_price.txt'

    summary = get_text_summary(file_path)


    