import requests

url='https://s.pstatic.net/static/www/mobile/edit/20250828_1095/upload_1756382437711LLaD4.png'
res = requests.get(url)

file_name='data/naver.png'
with open(file_name, 'wb') as file:
    file.write(res.content)