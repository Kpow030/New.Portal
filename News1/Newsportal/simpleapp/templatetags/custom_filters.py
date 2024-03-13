import re

from django import template




register = template.Library()


@register.filter()
def censor(text):
    forbidden_letters = ['ец', 'уй', 'ван', 'ина', 'ен', 'еб']

    def censor_word(match):
        word = match.group()
        if match.group(1) in forbidden_letters:
            return word[:-len(match.group(1))] + '*' * len(match.group(1))
        return word

    pattern = r'\b\w*(' + '|'.join(forbidden_letters) + r')\b'

    return re.sub(pattern, censor_word, text, flags=re.IGNORECASE)