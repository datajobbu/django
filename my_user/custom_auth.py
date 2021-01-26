import requests
import urllib.request


def check_if_user(user_id, user_pw):
#    payload = {
#        'user_id': str(user_id),
#        'user_pw': str(user_pw)
#    }
    encText = urllib.parse.quote("Hello")
    data = "source=en&target=ko&text=" + encText
    
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", user_id)
    request.add_header("X-Naver-Client-Secret", user_pw)
    
    res_ssl = ssl._create_unverified_context()
    response = urllib.request.urlopen(request, data=data.encode("utf-8"), context=res_ssl)
    rescode = response.getcode()
    print(rescode)
    if(rescode==200):
        return True

    else:
        return False


#    with requests.Session() as s:
#        s.post('https://community-dummy.com/login', data=payload)
#        auth = s.get('https://community-dummy.com/login_requited_page')
#        if auth.status_code == 200: # 성공적으로 가져올 때
#            return True
#        else: # 로그인이 실패시
#            return False