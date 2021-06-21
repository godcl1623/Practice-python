# html 내용 반환
def get_web(url):
	import urllib.request
	response = urllib.request.urlopen(url)
	data = response.read()
	decoded = data.decode('utf-8')
	return decoded

url = input('주소를 입력하세요 >')
content = get_web(url)
print(content)