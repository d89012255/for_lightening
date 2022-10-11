import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

os.environ["GIT_PYTHON_REFRESH"] = "quiet"
from git import Repo
import time
import os






class MyEventHandler(FileSystemEventHandler):
    # 文件移动
    def on_moved(self, event):
        print("文件移动触发")
        print(event)

    def on_created(self, event):
        print("文件创建触发")
        print(event)
        dirfile = os.path.abspath('C:/xampp/htdocs/for_lightening/uploads') # code的文件位置，我默认将其存放在根目录下
        repo = Repo(dirfile, search_parent_directories=True)

        g = repo.git

        g.add("--all",shell=True)
        g.commit("-m auto update",shell=True)
        g.push("-u origin main",shell=True)
        print("Successful push!")

    def on_deleted(self, event):
        print("文件删除触发")
        print(event)

    def on_modified(self, event):
        print("文件编辑触发")
        print(event)

if __name__ == '__main__':

    observer = Observer()  # 创建观察者对象
    file_handler = MyEventHandler()  # 创建事件处理对象
    observer.schedule(file_handler, "./uploads", False)  # 向观察者对象绑定事件和目录
    observer.start() # 启动
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()