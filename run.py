import subprocess  
import time  

def run_script(script_path):  
    process = subprocess.Popen(["python", script_path])  
    return process  

# print("Starting create.py...")  
# main_process = run_script("create.py")  
# main_process.wait()  
# print("Creating finished.")  

# time.sleep(50)
s = set()
while True:
    if time.strftime('%H',time.localtime(time.time()))=='02' and not time.strftime('%Y-%m-%d',time.localtime(time.time())) in s:
        update_process = run_script("get_data.py")  
        s.add(time.strftime('%Y-%m-%d',time.localtime(time.time())))