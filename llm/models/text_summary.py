from llm.config.llm_config import LLMConfig
from llm.bots.summary_bot import SummaryBot
from ..prompts.prompts import TEXT_SUMMARY_PROMPT, SUMMARY_TITLE_PROMPT


#TODO: combine with summary bot
def get_text_summary(text, prompt=TEXT_SUMMARY_PROMPT):
    
    bot = SummaryBot(config=LLMConfig())
    
    response = bot.summarize(text, prompt)
    
    return response


def get_summary_title(text, prompt=SUMMARY_TITLE_PROMPT):
    
    bot = SummaryBot(config=LLMConfig())
    
    response = bot.summarize(text, prompt)
    
    return response


