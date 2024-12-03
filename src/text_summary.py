import os
from configs import Configs
from .llm.summary_bot import SummaryBot

from .utils import read_txt



def get_text(file_path):
    text = read_txt(file_path)
    return text


def get_text_summary(file_name):
    
    text = get_text(file_name)
    
    bot = SummaryBot()
    
    response = bot.summarize(text)
    
    return response