from git import Repo
import os 
import time
import glob
import shutil
from datetime import datetime
import yaml
import mysql.connector
import psutil
from threading import Thread

#連結database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="imilab0936200028",
  database="remodeling_platform",
  auth_plugin="mysql_native_password"
)


#nod1 replica 強制改變
def change_yaml():
    a_yaml_file = open("/home/imilab/tang_yun/Predict/charthome2/values.yaml")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    replica=parsed_yaml_file["deployment"]["replicaCount"]      
    with open('/home/imilab/tang_yun/Predict/charthome2/values.yaml') as f:
        doc=yaml.load(f)
        if replica == 1:
            doc['deployment']["replicaCount"]=2
            print("改為2")
        else:
            doc['deployment']["replicaCount"]=1
            print("改為1")
    with open('/home/imilab/tang_yun/Predict/charthome2/values.yaml','w') as f:
        yaml.dump(doc,f)
def change_yaml2():
    a_yaml_file = open("/home/imilab/tang_yun/Predict2/predictchart/values.yaml")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    replica=parsed_yaml_file["deployment"]["replicaCount"]      
    with open('/home/imilab/tang_yun/Predict2/predictchart/values.yaml') as f:
        doc=yaml.load(f)
        if replica == 1:
            doc['deployment']["replicaCount"]=2
            print("改為2")
        else:
            doc['deployment']["replicaCount"]=1
            print("改為1")
    with open('/home/imilab/tang_yun/Predict2/predictchart/values.yaml','w') as f:
        yaml.dump(doc,f)


#計算公司所佔用的資料夾容量
total_size = 0
def file_size(path):
    global total_size 
    path=os.path.abspath(path)
    file_list=os.listdir(path)
    for i in file_list:
        i_path = os.path.join(path, i)
        if os.path.isfile(i_path):
            total_size += os.path.getsize(i_path)
        else:
            try:
                file_size(i_path)
            except RecursionError:
                print("遞迴操作時超出最大界限")
    return total_size
 
#計算cpu使用量
def job_cpu():
    while 1:
        # Calling psutil.cpu_precent() for 4 seconds
        cpu_percent=psutil.cpu_percent(4)
        str_percnet=str(cpu_percent)
        #print('The CPU usage is: '+ str_percnet)
        #上傳至database
        mycursor2 = mydb.cursor()
        mycursor2.execute('''
            INSERT INTO cpu (percent)
            VALUES
            (%s)
            ''',(cpu_percent,))
        ######cpu_percent這個變數後面要加,
        mydb.commit()
        #print(mycursor2.rowcount, "record inserted.")
        #print("Data inserted")
        
        # Calling psutil.cpu_precent() for 4 seconds
        ram_usage=psutil.virtual_memory().percent
   
        #上傳至database
        mycursor3 = mydb.cursor()
        mycursor3.execute('''
            INSERT INTO ram (percent)
            VALUES
            (%s)
            ''',(ram_usage,))
  
        mydb.commit()
        time.sleep(3)  




def lestening():
    global total_size 
          
    DIR="../remodeling_node1_data"
    DIR2="../remodeling_node2_data"
    file_number_past = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    file_number_past2 = len([name for name in os.listdir(DIR2) if os.path.isfile(os.path.join(DIR2, name))])
    while 1:
        file_number_now = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        file_number_now2 = len([name for name in os.listdir(DIR2) if os.path.isfile(os.path.join(DIR2, name))])
        if file_number_now > file_number_past:
            print("node1有新文件")
            change_yaml()
            latest_model=max(glob.glob('/home/imilab/tang_yun/remodeling_node1_data/*.joblib'), key=os.path.getctime)
            print("最新訓練好的模型："+latest_model) 
            os.remove("/home/imilab/tang_yun/Predict/clf_nn.joblib")
            shutil.copyfile(latest_model,r'/home/imilab/tang_yun/Predict/clf_nn.joblib')
            dirfile= "/home/imilab/tang_yun/Predict"
            repo=Repo(dirfile)
            g=repo.git
            g.add("--all")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time)
            g.commit('-m', current_time)
            g.push()
            print("Successful push!") 
        
            #計算companyA資料夾大小
            companya = file_size("../remodeling_node1_data")
            companya= round(companya/1000000 ,2)
            companya=int(companya) 
            print("佔用容量")
            print(companya)
            #參數歸零
            total_size=0 
            #計算companyB資料夾大小
            companyb = file_size("../remodeling_node2_data")
            companyb= round(companyb/1000000 ,2)
            companyb=int(companyb) 
            #參數歸零
            total_size=0


            
            #A公司完成修模（要來寫進資料庫的）
            compan_a=1
            #上傳至database
            mycursor = mydb.cursor()
            mycursor.execute('''
                INSERT INTO status (time_push,company,asize,bsize)
                VALUES
                (%s, %s, %s, %s)
                ''',(current_time,compan_a,companya,companyb))
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            
            #參數更新
            file_number_past = file_number_now
            time.sleep(3)
            
        elif file_number_now2 > file_number_past2:
            print("node2有新文件")
            change_yaml2()
            latest_model2=max(glob.glob('/home/imilab/tang_yun/remodeling_node2_data/*.joblib'), key=os.path.getctime)
            print("最新訓練好的模型："+latest_model2) 
            os.remove("/home/imilab/tang_yun/Predict2/clf_nn.joblib")
            shutil.copyfile(latest_model2,r'/home/imilab/tang_yun/Predict2/clf_nn.joblib')
            dirfile2= "/home/imilab/tang_yun/Predict2"
            repo2=Repo(dirfile2)
            g2=repo2.git
            g2.add("--all")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time)
            g2.commit('-m', current_time)
            g2.push()
            print("Successful push!") 
            
            #計算companyB資料夾大小
            companyb= file_size("../remodeling_node2_data")
            companyb= round(companyb/1000000 ,2)
            companyb=int(companyb) 
            print("佔用容量")
            print(companyb)
            
            #參數歸零
            total_size=0 
            #計算companyA資料夾大小
            companya = file_size("../remodeling_node1_data")
            companya= round(companya /1000000 ,2)
            companya=int(companya) 
            #參數歸零
            total_size=0
            #B公司完成修模（要來寫進資料庫的） 
            compan_b=2
            #上傳至database
            mycursor = mydb.cursor()
            mycursor.execute('''
                INSERT INTO status (time_push,company,asize,bsize)
                VALUES
                (%s, %s, %s, %s)
                ''',(current_time,compan_b,companya,companyb))
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

            file_number_past2 = file_number_now2
            time.sleep(3)           
        else:
            #print("沒有新文件")
            file_number_past = file_number_now 
            file_number_past2 = file_number_now2  
             
if __name__ == '__main__':
    # 建立一個子執行緒
    t1 = Thread(target = job_cpu)
    t1.start()

    #主執行序
    lestening()

