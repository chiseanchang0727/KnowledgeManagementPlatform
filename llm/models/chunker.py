from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class FileChunker:


    @staticmethod
    def split_pdf_to_chunks(file_path, chunk_size, chunk_overlap):

        loader = PyPDFLoader(file_path)
        pages = loader.load() 


        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False,
        )
        chunked_documents = splitter.transform_documents(pages)

        last_page = chunked_documents[-1].metadata.get('page', None)

        return chunked_documents, last_page
