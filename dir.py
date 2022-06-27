import glob
import json

from github import Github
import os

json_obj = {}

urls = glob.glob('*assets/**/*.*', recursive = True)

for url in urls:
 url = url.replace('\\', '/')
 arr = url.split('/')
 name = arr[-1]
 dir = arr[-2]
 data = {"name": name}
 try:
  json_obj[dir]. append(data)
 except:
  json_obj. update({dir:[]})
  json_obj[dir]. append(data)

str=json.dumps(json_obj)
print(str)

f = open('dir.json','w')
f.write(str)
f.close()

########################

token=os.environ['GITHUB_TOKEN']
rep_name=os.environ['REPOSITORY'].split('/')[-1]
filename='assets/test.txt'
data='blabla'
#print([token, rep_name, filename, data])

g = Github(token)
rep = g.get_user().get_repo(rep_name)
files = rep.get_contents(filename);

rep.update_file(filename,'json commit',data,files.sha)
