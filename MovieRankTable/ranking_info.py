import requests
from bs4 import BeautifulSoup

def ranking_info():
    ranking=[]
    result = list()
    url=[]
    response = requests.get('https://movie.daum.net/ranking/reservation')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다
    for tag in soup.select('div[class=box_ranking] li strong[class=tit_item] a'):
        result.append(tag.text)
        url.append('https://movie.daum.net'+tag.get('href'))
        ranking.append(result)
        result = []
    RandM=[ranking, url]
    return RandM
def ranking_info2():
    a=ranking_info()
    a=a[0]
    result=[]
    for i in a:
        result.append(i[0])
    return result
if __name__ == '__main__':
    a=ranking_info2()
    print(a)