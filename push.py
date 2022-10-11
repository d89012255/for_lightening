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
import time
import os




dirfile = os.path.abspath('C:/xampp/htdocs/for_lightening/uploads') # code的文件位置，我默认将其存放在根目录下
repo = Repo(dirfile, search_parent_directories=True)

g = repo.git

g.add("--all",shell=True)
g.commit("-m auto update",shell=True)
g.push(shell=True)
print("Successful push!")


# f = open('news.txt','a')
# f.write('今年iT邦幫忙鐵人賽不僅延續傳統鋼鐵般的精神，更把組別一口氣增加到7組：【MIS 技術】、【開發技術】、【其他技術】、【IT 人生】、【Cloud、Big Data】、【App 開發】及【學生組】等7組\n')
# f.close()