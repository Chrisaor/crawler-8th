# 우리가 웹 브라우저를 통해 보는 HTML문서는 GET요청의 결과
# requests를 사용해 'https://comic.naver.com/webtoon/weekday.nhn'주소에 Get요청을 하고
# 요청 결과를 response변수에 할당해서 status_code속성을 출력

import requests
import re
r = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
print(r.status_code)

# HTTP GET 요청으로 받아온 content를 text데이터로 리턴
# print(r.text)
# response.text에 해당하는 데이터를
# weekday.html이라는 파일에 기록
# 다 기록했으면 close()호출
#
# f = open('weekday.html', 'wt')
# f.write(r.text)
# f.close()
#
# with open('weekday.html', 'wt') as f:
#     f.write(r.text)



source = r.text
col_inner = re.findall('<div class="col_inner">(.*?)</div>', source)
print(col_inner)

