import requests
import urllib.parse
import os
# os.path.abspath("mydir/myfile.txt")
# 'C:/example/cwd/mydir/myfile.txt'
# query = 'Hellö Wörld@Python'
# urllib.parse.quote(query)


output_file_path = 'DE.txt'

def get_upload_link(output_file_path):
	"""	 ? path=<путь, по которому следует загрузить файл>
		 & [overwrite=<признак перезаписи>]
		 & [fields=<свойства, которые нужно включить в ответ>]"""

	TOKEN = 'AgAAAAAd7LCoAADLW7cgFmFB3Uqtuquv3tektMM'

	PREPARE_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

	headers = {'Accept': 'application/json', 'Authorization': TOKEN}

	params = {'path': output_file_path, 'overwrite': True}


	response = requests.get(PREPARE_UPLOAD_URL, params=params, headers=headers)
	json_ = response.json()

	return ''.join(json_['href'])




def upload_file(upload_link):

	params = {'path': os.path.abspath(output_file_path)}

	response = requests.put(upload_link, params=params)

	json_ = response.json()

	return ''.join(json_['href'])


if __name__ == '__main__':
	output_file_path = 'DE.txt'
	upload_link = 'https://uploader6o.disk.yandex.net:443/upload-target/20200605T120802.468.utd.4uh53oz90wwm93osp31xxkuws-k6o.16669441'

	# print(upload_file(upload_link))
	#
	upload_link = get_upload_link('FR.txt')
	#
	print(upload_link)

