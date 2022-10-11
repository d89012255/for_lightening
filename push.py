# from git import Repo
# import time
# from datetime import datetime
# dirfile= "C:/xampp/htdocs/for_lightening/uploads"
# repo=Repo(dirfile)
# print(repo)
# g=repo.git
# g.add("--all")
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print(current_time)
# g.commit('-m', current_time)
# g.push()
# print("Successful push!") 



import os





os.environ["GIT_PYTHON_REFRESH"] = "quiet"
from git import Repo
dirfile = os.path.abspath('C:/xampp/htdocs/for_lightening/uploads') # code的文件位置，我默认将其存放在根目录下
repo = Repo(dirfile, search_parent_directories=True)

g = repo.git

g.add("--all",shell=True)
g.commit("-m auto update",shell=True)
g.push(shell=True)
print("Successful push!")
