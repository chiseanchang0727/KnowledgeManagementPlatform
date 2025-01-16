TEXT_SUMMARY_PROMPT="""
我們是一家專業造紙商，相當關注造紙業界的需求變化、原料價格、同業生態
以這個為目的，理解以下提供資訊後，整理重要的資訊

必須使用繁體中文呈現結果


{input_string}
"""



SUMMARY_TITLE_PROMPT="""
理解以下內容之後，給我最適合的title，只要一句話就好，限縮在20個繁體中文字元內

{input_string}
"""