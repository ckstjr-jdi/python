import requests
import os

path = f'{os.getcwd()}/data'

if not os.path.exists(path):
    os.makedirs(path)
# print(path)

name = input('이름>')
url=f'https://www.google.com/search?sca_esv=5d812c3a7137edf1&udm=2&fbs=AIIjpHyDg0Pef0CibV20xjIa-FRejxCuOmkq074km2sZXr7uqz9_8tiStZcoMiP-q5iAtTYSp3Dd1cIVIUmn-SwXY53VwkLRk5i722Kr7JNKVL-YykKvLRBg19pGtlzqtJyrpaYYMSFajpJRp-840XCdFXvFIsZ841pwu7M8UQ8rqzfZEc9i_b4XMW1zpYchCE-5CvO6B9Sp5_NOG2ObNyiqwHSXcv0Y4Q&q={name}&sa=X&ved=2ahUKEwjl7q_p7riPAxXth1YBHeP6Ne4QtKgLegQIFhAB&biw=1536&bih=730&dpr=1.25'
res = requests.get(url)

# print(res.text)

file_name = path + f'data/{name}.html'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(res.text)

