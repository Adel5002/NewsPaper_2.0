from django import template

register = template.Library()

bad_words = ['редиска', 'банан', 'тапок', 'муха', 'сгущенка', 'орешки', 'стручек']

@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise TypeError(f"unresolved type '{type(value)}' expected  type 'str'")

    for word in value.split():
        if word.lower() in bad_words:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return value


