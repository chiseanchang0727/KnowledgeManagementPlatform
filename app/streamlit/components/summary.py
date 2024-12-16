from llm.utils import count_tokens
from llm.models.text_summary import get_text_summary


def text_summary(file):
    tokens = count_tokens(file)


    if tokens > 8192:
        "cunker"

    #TODO: call chunker for long file and double summary
    summary = get_text_summary(file)

    return summary
    