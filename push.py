from git import Repo
import time
from datetime import datetime
dirfile= "C:/xampp/htdocs/for_lightening/uploads"
repo=Repo(dirfile)
g=repo.git
g.add("--all")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)
g.commit('-m', current_time)
g.push()
print("Successful push!") 