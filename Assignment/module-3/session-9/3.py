import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags
caption = "Loving this vibe #sunset #nature #PythonCoding #riya"

result = extract_hashtags(caption)
print(result)