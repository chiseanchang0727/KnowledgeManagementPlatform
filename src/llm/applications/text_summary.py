import os
from configs import Configs
from ..bots.summary_bot import SummaryBot

from ...utils import read_txt

def get_text_summary(text):
    
    bot = SummaryBot()
    
    response = bot.summarize(text)
    
    return response