# load txt
from config import Configs



def read_txt(path):
    with open('file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    return content
