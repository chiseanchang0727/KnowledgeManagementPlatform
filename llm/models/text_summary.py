from llm.config.llm_config import LLMConfig
from llm.bots.summary_bot import SummaryBot
from ..prompts.prompts import TEXT_SUMMARY_PROMPT, WEBSITE_SUMMARY_PROMPT


#TODO: combine with summary bot
def get_text_summary(text, prompt=TEXT_SUMMARY_PROMPT):
    
    bot = SummaryBot(config=LLMConfig())
    
    response = bot.summarize(text, prompt)
    
    return response




# Here will be two jobs: Summary the user-provided files and daily highlight summary


def get_web_summary(url, prompt=WEBSITE_SUMMARY_PROMPT):

    bot = SummaryBot(config=LLMConfig())

    response = bot.web_summary(url, prompt)

    return response