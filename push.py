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


from git import Repo
import os

dirfile = os.path.abspath('C:/xampp/htdocs/for_lightening/uploads') # code的文件位置，我默认将其存放在根目录下
repo = Repo(dirfile, search_parent_directories=True)

g = repo.git
g.add("--all")
g.commit("-m auto update")
g.push()
print("Successful push!")
