from bs4 import BeautifulSoup
import os
from subprocess import Popen

#Creating the battery report - using bash in config.bat
# p = Popen("config.bat", cwd=r".\\")
# stdout, stderr = p.communicate()

#reconstructed to not use batch file.
create_report = 'powercfg /batteryreport'
os.system(create_report)

#Opening up the battery report and assigning it to a variable
HTMLfile = open('battery-report.html', 'r')
index = HTMLfile.read()


#Using beautifulsoup to grab information from HTML file
S = BeautifulSoup(index, 'html.parser')
tds = S.find_all("td")
l1 = []

#sticking the first 2 td's with mWh into a list
for i in tds:
    if "mWh" in i.text:
        l1.append(i.text)
        if len(l1) == 2:
            break

#cleaning up and closing files
HTMLfile.close()
os.remove('battery-report.html')

#Taking each integer and making it usable and printing them
one = int(l1[0].replace(",", "").replace(" mWh", "").strip())
two = int(l1[1].replace(",", "").replace(" mWh", "").strip())
print(f'Design Capacity: {one}')
print(f'Full Charge Capacity: {two}')

#math to find the percentage of healthy battery Design Capacity/Full Charge
total = int((two/one)*100)

#printing out the percentage of healthy battery. This time were using bash instead of print
cmd = "echo {}%".format(total)
os.system(cmd)
os.system('pause')


