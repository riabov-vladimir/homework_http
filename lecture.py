import requests
import urllib.parse
import os
# os.path.abspath("mydir/myfile.txt")
# 'C:/example/cwd/mydir/myfile.txt'
# query = 'Hellö Wörld@Python'
# urllib.parse.quote(query)

#
output_file_path = 'DE.txt'
#
# TOKEN = 'AgAAAAAd7LCoAADLW7cgFmFB3Uqtuquv3tektMM'
#
# PREPARE_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
#
# headers = {'Accept': 'application/json', 'Authorization': TOKEN}
#
# params = {'path': output_file_path, 'overwrite': True}
#
#
# response = requests.get(PREPARE_UPLOAD_URL, params=params, headers=headers)
# json_ = response.json()
#
# upload_link = ''.join(json_['href'])

upload_link = 'https://uploader12o.disk.yandex.net:443/upload-target/20200605T135027.543.utd.7ssx4lulfac2ncezb3k6idtc7-k12o.16637024'
# put _______________________________________________________________

files={'file': open(output_file_path,'rb')}
response = requests.put(upload_link, files=files)
