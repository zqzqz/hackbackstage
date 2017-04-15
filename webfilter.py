import requests
import base64

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
url = 'http://ctf5.shiyanbar.com/web/10/10.php'
my_headers = {'User-Agent': user_agent}
a = (base64.b64decode(requests.get(url, headers=my_headers).headers['FLAG'])[25:])
print(a)
print(requests.post(url,data={'key': a}).content)
#.split(':')[1]}).content)