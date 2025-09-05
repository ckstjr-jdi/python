#할리스 서울 매장정보
import json
import requests

#할리스매장 정보(매장이름, 주소, 전화번호)
def getAddress():
    with open('data/hollys.json', 'r',encoding='utf-8') as file:
        address = json.load(file)
        list =[]
        for add in address:
            data={'name':add['name'], 'address':add['address'], 'phone':add['phone']}
            list.append(data)
        return list

#주소 입력 위도(y), 경도(x) 출력
def getXY(query):
    headers={'Authorization':'KakaoAK fec12da4ad345a6ee097f819c207fc34'}
    url = f'https://dapi.kakao.com/v2/local/search/address.json?query={query}'
    res= requests.request(method='get', url=url, headers=headers)
    data = res.json()
    documents = data['documents']
    y = documents[0]['y']    
    x = documents[0]['x']
    return y, x

def getAddress2(address):
        address = address.split(' ')[:4]
        address = ' '.join(address)
        return address

if __name__=="__main__":
    list=getAddress()
    list_json = []
    for add in list:
        name = add['name']
        phone = add['phone']
        address=getAddress2(add['address'])
        xy = getXY(address)
        x = xy[1]
        y = xy[0]
        print(f'{address}, ({y},{x})')
        data={'name':name,'phone':phone,'address':address,'x':x,'y':y}
        list_json.append(data)

    with open('data/hollys_location.json', 'w', encoding='utf-8') as file:
        json.dump(list_json, file, indent='\t', ensure_ascii=False)
        