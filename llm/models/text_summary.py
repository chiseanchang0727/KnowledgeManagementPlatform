import os
from configs import Configs
from .llm.bots.summary_bot import SummaryBot

from .utils import read_txt


#TODO: combine with summary bot
def get_text_summary(text):
    
    bot = SummaryBot()
    
    response = bot.summarize(text)
    
    return response