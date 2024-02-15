import os

logs = os.listdir("C:\Program Files (x86)\Cobian Backup 11\Logs")

files = []

x = 0
for i in logs:  
    if "log" in logs[x]:
       print(logs[x])
    x =+ 1

print(files)

print("Digite o nome do arquivo: ")
fileName = input()

file = open("C:\Program Files (x86)\Cobian Backup 11\logs\{}.txt".format(fileName), "r")
content = file.read()
print(content)
file.close()