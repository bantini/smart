__author__ = 'nilayan'

import re

def pattern_matcher(items):
    hash_pattern = re.compile('[#][a-zA-Z0-9]+')
    user_pattern = re.compile('[@][a-zA-Z0-9]+')
    url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    cleaned_items = []
    for item in items:
        if re.match(hash_pattern,item):
            cleaned_items.append(item[1:])
        elif re.match(user_pattern,item):
            pass
        elif re.match(url_pattern,item):
            pass
        else:
            cleaned_items.append(item)
    return cleaned_items

