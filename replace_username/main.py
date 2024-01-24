import re
from .replace import replace_words

class Replace_username:

    async def replace_words(string):
        prohibitedWords = REPLACE_WORDS
        big_regex = re.compile(r'(\s?(' + '|'.join(map(re.escape, prohibitedWords)) + r')\b\s?)|(\s?\b(' + '|'.join(map(re.escape, prohibitedWords)) + r')\s?)')
        formatted = big_regex.sub(lambda match: match.group().replace(match.group(2) or match.group(4), ""), string)
        return formatted.replace('salar', 'salaar').replace('Salar', 'salaar').replace('s1', 's01').replace('s2', 's02').replace('s3', 's03').replace('s4', 's04').replace('s5', 's05').replace('s6', 's06')#.replace("-"," ")
