import requests


def get_upload_link(path):
	"""	 ? path=<путь, по которому следует загрузить файл>
		 & [overwrite=<признак перезаписи>]
		 & [fields=<свойства, которые нужно включить в ответ>]"""

	TOKEN = 'AgAAAAAd7LCoAADLW7cgFmFB3Uqtuquv3tektMM'

	PREPARE_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

	headers = {'Accept': 'application/json', 'Authorization': TOKEN}

	params = {'path': path, 'overwrite': True}


	response = requests.get(PREPARE_UPLOAD_URL, params=params, headers=headers)
	json_ = response.json()

	return ''.join(json_['href'])


path = 'C:\Users\79055\PycharmProjects\homework_http\DE.txt'

def upload_file(path):


	upload_link = get_upload_link(path)

	params = {'path': path}


	response = requests.put(upload_link, params=params)
	json_ = response.json()

	return ''.join(json_['href'])

print(upload_file(path))


if __name__ == '__main__':

	upload_link = get_upload_link('DE.txt')

	print(upload_link)