from bs4 import BeautifulSoup
import os
from subprocess import Popen
import requests as req

p = Popen("config.bat", cwd=r".\\")
stdout, stderr = p.communicate()

HTMLfile = open('battery-report.html', 'r')

index = HTMLfile.read()

S = BeautifulSoup(index, 'html.parser')
divs = S.find_all("td")
mwh = "mWh"
count = 0
l1 = []

for i in divs:

    if "mWh" in i.text:
        count += 1
        l1.append(i.text)
        if count == 2:
            break

HTMLfile.close()
os.remove('battery-report.html')

one = int(l1[0].replace(",", "").replace(" mWh", "").strip())
two = int(l1[1].replace(",", "").replace(" mWh", "").strip())
print(f'Design Capacity: {one}')
print(f'Full Charge Capacity: {two}')

total = int((two/one)*100)

cmd = "echo '{}%'".format(total)
os.system(cmd)
os.system('pause')


#pattern = r'(\d*,\d* mWH)'
