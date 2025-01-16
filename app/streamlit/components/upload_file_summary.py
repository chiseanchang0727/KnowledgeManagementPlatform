from llm.utils import count_tokens
from llm.models.text_summary import get_text_summary, get_summary_title
from llm.models.chunker import FileChunker
import PyPDF2



def file_summary(file):


    # tokens = count_tokens(file, model_name='gpt-4o')


    # if tokens > 8190:

    splitted_doc, max_page =  FileChunker.split_pdf_to_chunks(file, chunk_size=2000, chunk_overlap=0)

    page_content = {}
    for page in range(max_page+1):
        temp = [item for item in splitted_doc if item.metadata['page'] == page]
        page_content[page] = "".join(temp[i].page_content for i in range(len(temp)))

    page_summary = {}
    for page, content in page_content.items():
        page_summary[page] = get_text_summary(content)

    summary_all = "".join(page_summary[page] for page, _ in page_summary.items())

    doc_summary = get_text_summary(summary_all)
    summary_title = get_summary_title(doc_summary)
    
    # else:
    #     doc_summary = get_text_summary(file)

    return doc_summary, summary_title
    

