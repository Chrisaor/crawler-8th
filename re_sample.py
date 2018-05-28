import re

# re.weekday_item_title.html 파일을 불러와서 html 변수에 할당

# with open('re_weekday_item_title.html', 'rt') as f:
#     html = f.read()
#
# print(html)

html = open('re_weekday_item_title.html', 'rt').read()
print(html)

a_tag = re.findall('<a.*?class="title".*?>([\w\s]*?)</a>' , html)
print(a_tag)

html1 = open('weekday.html', 'rt').read()
a_tag1 = re.findall('<a.*?class="title".*?>([\w\s]*?)</a>' , html1)
print(a_tag1)

img_tag = re.findall('<img onerror.*?src="(.*?)".*?>',html1)
print(img_tag)