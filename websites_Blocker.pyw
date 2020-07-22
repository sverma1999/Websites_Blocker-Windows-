import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.movie4k.movie/", "movie4k.movie/", "www.edx.org", "edx.org"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 13):
        print("Working Hours...")
        with open(hosts_temp, 'r+') as inputFile:
            content=inputFile.read()
            for eachWebsite in website_list:
                if eachWebsite in content:
                    pass
                else:
                    inputFile.write(redirect + "    " + eachWebsite + "\n")
    else:
        with open(hosts_temp, 'r+') as inputFile2:
            content2 = inputFile2.readlines()
            inputFile2.seek(0)
            for eachLine in content2:
                if not any(website in eachLine for website in website_list):
                    inputFile2.write(eachLine)
            inputFile2.truncate()

        print("Free Hours...")
    time.sleep(5)
