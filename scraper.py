import webbrowser
from string import digits
import os
import platform
import time
from pyfiglet import Figlet
from pyfiglet import figlet_format
from termcolor import colored
from random import randint
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
import time
from geopy.geocoders import Nominatim

#3x5
font = ['slant', "3-d", "3x5", "5lineoblique",
        "alphabet", "banner3-D", "doh", "isometric1", "letters",
        "alligator", "dotmatrix", "bubble", "bulbhead", "digital", "standard"]

fontpref = font[0]
valid_color = ('red', 'green', 'yellow', 'cyan', 'white')

def initData(inp, zipcode, county, town, cordF, njid):
    dataAttr = [
        "Google Search",
        "Manhattan Directions",
        "Google Maps",
        "Zillow",
        "FEMA", 
        "Great Schools", 
        "City-Data", 
        "Bergen GIS",
        "Google GIS",
        "NJMLS More Info"
        "ARCGIS Coordinates"
        ]
            
    links = [
        f"https://www.google.com/search?q={inp}", #google search
        f"https://www.google.com/maps/dir/manhattan ny/{inp}", #manhattan to property direction
        f"https://www.google.com/maps?q={inp}", #google maps
        f"https://www.zillow.com/homes/{inp}_rb/", #zillow
        f"https://msc.fema.gov/portal/search?AddressQuery={inp}", #fema
        f"https://www.greatschools.org/search/search.zipcode?sort=rating&zip={zipcode}", # great schools
        f"http://www.city-data.com/zips/{zipcode}.html", #city-data
        f"https://bchapeweb.co.bergen.nj.us/parcelviewer/", #bergen gis
        f"https://www.google.com/search?q=arcgis+{county}+county", # backup for arcgis checker
        f"http://www.njmls.com/NJ/{county}/{town}-community-information", #njmls MORE INFO town info
        f"https://hub.arcgis.com/datasets/NJTPA::bergen-county-parcels-2015?geometry={cordF[0]}%2C{cordF[1]}%2C{cordF[2]}%2C{cordF[3]}"

    ]

    dataAttr2 = ["Spotcrime", "Moving", "PropertyShark", "NJMLS - Search by ZIP", "NJMLS - Search by INPUT"]

    data2 =[
        f"https://spotcrime.com/map?address={zipcode}", #spotcrime recent data
        f"https://www.moving.com/real-estate/city-profile/results.asp?Zip={zipcode}", #area information
        f"https://www.propertyshark.com/mason/Lookup/resolve4.html?location={county} county&search_token={inp}", # propertyshark
        f"https://www.njmls.com/m/results.cfm?searchvalue={zipcode}&radius=10&Submit=Search&proptype=1%2C3&status=A&minprice=&maxprice=&beds=0&baths=0&sortby=newest&daysSince=15&yearbuilt=&latitude=&longitude=&searchType=default",
        f"https://www.njmls.com/m/results.cfm?searchvalue={njid}&radius=10&Submit=Search&proptype=1%2C3&status=A&minprice=&maxprice=&beds=0&baths=0&sortby=newest&daysSince=15&yearbuilt=&latitude=&longitude=&searchType=default",
    ]
    return [dataAttr, links, dataAttr2, data2]
    
#width = os.get_terminal_size().columns
#operating = str(os.name())
#autorecognize platofrm name

if platform.system()=='Windows':
    oMobileToggle = False
else:
    oMobileToggle = True
#print(os.name)
#replace code for automated and vice versa for def update_width() method
#if str(os.name)=="posix"

# %%

def display(msg,style, color):
    if oMobileToggle == True:
        g=msg
        print(g)
    else:
        f = figlet_format(msg, font=fontpref)
        g = colored(f, color)
        print(g)

def googleSearch(query):
    g_clean = [ ]
    url = 'https://www.google.com/search?q={}'.format(query)
        
    try:
        html = requests.get(url)
        if html.status_code==200:
            soup = BeautifulSoup(html.content, 'html.parser')
            a = soup.find_all('a')
            for i in a:
                k = i.get('href')
                try:
                    m = re.search("(?P<url>https?://[^\s]+)", k)
                    n = m.group(0)
                    rul = n.split('&')[0]
                    domain = urlparse(rul)
                    if(re.search('google.com', domain.netloc)):
                        continue
                    else:
                        g_clean.append(rul)
                except:
                    continue
    except Exception as ex:
            print(str(ex))

    finally:
        return (g_clean)

repeat = True

def get_linkTitle(url):
    import requests
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'zguid=23|%2403435e76-0699-4a32-b86d-77d033c907ef; _ga=GA1.2.1271511001.1575011821; zjs_user_id=null; zjs_anonymous_id=%2203435e76-0699-4a32-b86d-77d033c907ef%22; _gcl_au=1.1.1333357279.1575011822; _pxvid=3cfcc163-1278-11ea-bff8-0242ac12000b; ki_r=; __gads=ID=84d8013cfac6df96:T=1575012041:S=ALNI_MaSvVNZsir2JXJ17pv54bjsPuyfcw; ki_s=199442%3A0.0.0.0.0%3B199444%3A0.0.0.0.2; zgsession=1|c0999376-b167-4a47-a1cd-0e456d882d4e; _gid=GA1.2.55965867.1578668946; JSESSIONID=87D0662A6BC141A73F0D12620788519C; KruxPixel=true; DoubleClickSession=true; KruxAddition=true; ki_t=1575011869563%3B1578669044158%3B1578669044158%3B2%3B10; _pxff_tm=1; _px3=2e6809e35ce7e076934ff998c2bdb8140e8b793b53e08a27c5da11f1b4760755:DFItCmrETuS2OQcztcFmt0FYPUn00ihAAue2ynQgbfSq6H+p2yP3Rl3aeyls3Unr1VRJSgcNue8Rr1SUq4P1jA==:1000:9ueZvAJ6v5y4ny7psGF25dK+d3GlytY2Bh+Xj9UUhC4DaioIZ+FMXPU0mOX+Qnghqut0jIT61gLecN4fyu6qXaPDlBX6YsZVbIry1YyBN/37l0Ri3JP+E0h+m+QEBB+bqb6MbE2HtgGBJRJAry8dgOKGM5JtBGdX+X/nuQX1xaw=; AWSALB=E6JYC43gXQRlE2jPT9e2vAQOYPvdHnccBlqi0mcXevYExTaHro0M+uo/Qxahi6JyLz9LpotY9eLtEbYrAOeQXcCm6UhjWnTopQHernmjlR/ibE6JmE8F6tReiBn4; search=6|1581261153229%7Crect%3D40.96202658306895%252C-73.55498286718745%252C40.4487909557045%252C-74.40093013281245%26rid%3D6181%26disp%3Dmap%26mdm%3Dauto%26p%3D3%26z%3D0%26lt%3Dfsbo%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%09%01%096181%09%09%09%090%09US_%09',
            'pragma': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/75.0.3770.142 Chrome/75.0.3770.142 Safari/537.36'
        }
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.select('title')
    val = title[0].getText()
    return val

def parse(msg):
        display(msg,fontpref, valid_color[colorChoice])

def update_width():
    if oMobileToggle != True:
        width = os.get_terminal_size().columns

def printIndex(inpList):
    for x in range(len(inpList)):
        print(f"{x+1}. {inpList[x]}")
    
def fullTown():
    # init
    zipcode = 00000
    address = []
    que = "[~]"
    # ask prop       ------------------------------------------------------------------------------------------
    print('\n'*5)
    parse("     ------------- Full Address ------------- ")
    inp = input(f"{que}")
    inpList = inp.replace(",","").split()
    return [inp, que, inpList]

def verifyTown(inpList, que):
    #verify town    -------------------------------------------------------------------------------------------
    print('\n'*5)
    parse("     ------------- Town Name ------------- ")
    printIndex(inpList) #Print menu index
    town = str(input(f"Town: Enter Index Below {que}"))
    if "+" in town:
        nt = town.replace("+", " ").split()
        for t in range(len(nt)):
            town+=nt[t]
    else:
        if (town.isnumeric() is True and len(town) <= len(inpList)):
            town = inpList[int(town)-1]
        else:
            while(town.isnumeric() is True):
                town = input(f"Enter Valid Town Name{que}")

    print(town)
    return town

def verifyZip(inpList, que):
    #verify zip    -------------------------------------------------------------------------------------------
    print('\n'*5)
    parse("     ------------- Zip Code ------------- ")
    printIndex(inpList) #Print menu index
    zipcode = str(input(f"ZipCode: Enter Index Below {que}"))
    
    if (zipcode.isnumeric() is True and len(zipcode) <= len(inpList)) and len(zipcode)==1:
        zipcode = inpList[int(zipcode)-1]
    else:
        while(zipcode.isnumeric() is False or len(zipcode)!= 5):
            zipcode = input(f"Enter Valid Zipcode {que}")

    return zipcode

def zillowNjParcels(inp):
    print(inp)
    #get link title of Zillow and njparcel
    getTitles = ["zillow.com", "njparcels.com"]
    spTitleStrings = []
    for g in range(len(getTitles)):
        gLink = googleSearch(f"{inp} site:{getTitles[g]}")
        print(f"did {g}")
        print(gLink)
        spTitleStrings.append(gLink)
        

    print(spTitleStrings)
    gLinkTextL= str(get_linkTitle(spTitleStrings[0][0])).split() #zillow title list
    # njparcelLinkTextL = str(f"{spTitleStrings[1][1]}").replace("_"," ").replace ("/", " ").split() # njparcel title list
    # print(njparcelLinkTextL)
    return gLinkTextL

def getCounty(zipcode):
    #get county info from link address njmls.com
    search = googleSearch(f"{zipcode} community information site:njmls.com")
    ogCountyL = str(f"{search[0]}").replace("/", " ").split() # njparcel title list
    bestCountyL = []
    for cc in range(len(ogCountyL)):
        if ('-' not in ogCountyL[cc] and '-' not in ogCountyL[cc] and ".com" not in ogCountyL[cc]):
            bestCountyL.append(ogCountyL[cc])
    
    #Verify county     -------------------------------------------------------------------------------------------
    print('\n'*5)
    parse("     ------------- County ------------- ")
    printIndex(bestCountyL)
    county= input(f"Country: Enter Index Below {que}")
    print('\n'*5)
    return county

def verifyNJMLID(inp, gLinkTextL, inpList):
    #arcgis parser
    geolocator = Nominatim(user_agent="my_user_agent")

    parse("     ------------- LAT, LONG INFO  ------------- ")
    loc = geolocator.geocode(inp)
    try:
        print("latitude is :" ,loc.latitude,"\nlongtitude is:" ,loc.longitude)
    except:
        loc = geolocator.geocode(inp)
        inp = []
        for i in range(len(inpList)):
            print(f"{i} {inpList[i]}")
        while True: 
            index = input("Please choose the long-lat keywords (enter 99 to exit)")
            if int(index)== 99:
                break
            else:
                inp.append(inpList[int(index)])
                print("current: ", inp)
        print(inp[-1])
        new = " ".join(inp)
        loc = geolocator.geocode(new)
        print("latitude is :" ,loc.latitude,"\nlongtitude is:" ,loc.longitude)
        
    lat = loc.latitude
    lon = loc.longitude

    variant = 0.001
    latF = lat+variant
    lonF = lon+variant
    latS = lat-variant
    lonS = lon-variant

    #format to 3 decimal place
    cord = [lonS, latF, lonF, latS]
    cordF = []
    for cim in range(len(cord)):
        cordF.append("{:.3f}".format(cord[cim]))

    #verify NJMLS ID  
    print('\n'*5)
    parse("     ------------- NJMLS ID ------------- ")
    ogLinkTextL = []
    for a in range(len(gLinkTextL)):
        if "#" in gLinkTextL[a]: 
            ogLinkTextL.append(gLinkTextL[a].replace("#",""))
    printIndex(ogLinkTextL) #Print menu index for title index
    print(ogLinkTextL)
    njid = str(input(f"NJMLSID: Enter Index Below {que}"))
    
    os.system('cls')


    if (njid.isnumeric() is True and len(njid) <= len(ogLinkTextL)):
        njid = ogLinkTextL[int(njid)-1]
    else:
        while(njid.isnumeric() is False):
            njid = input(f"Please Verify correctly {que}")

    return [cordF, njid]

def similarSites(sites2Check):
    #ask to check other homes on the street on zillow and Realtor?
    print('\n'*5)
    parse("     ------------- Wanna See Similar Homes In Areas? ------------- ")
    desire = input("[Y/N]")

    if (desire == "y"):
        for dz in range(len(sites2Check)):
            webbrowser.open_new("https://") #opens new browser window seperation
            desiree = googleSearch(f"{inp} site:{sites2Check[dz]}")
            for each in range(len(desiree)):
                webbrowser.open_new(desiree[each])
        
# %%
# ------------------------- Search Start Mode -----------------------------

# loop until user interjection
while True:
    os.system('cls')
    colorChoice = randint(0, len(valid_color)-1)
    print(colorChoice)
    print('\n'*5)
    display("     ------------- Property Search ------------- ",fontpref, valid_color[colorChoice])
    print('\n'*5)

    print("Press Enter for another search, or q to exit ")
    ch = input('')

    if ch == '':
    # try:
        os.system('cls')
        print("get town")
        info = fullTown()
        inp = info[0]
        que = info[1]
        inpList = info[2]
        os.system('cls')
        print("verify town")
        town = verifyTown(inpList, que)
        os.system('cls')  
        print("verify zip")
        zipcode = verifyZip(inpList, que)
        os.system('cls')
        print(inp)
        print("verify zillow")
        gLinkTextL = zillowNjParcels(inp)
        print("verify county")
        county = getCounty(zipcode)
        os.system('cls')

        print("verify and get njmlsIDs")
        njmlsdata = verifyNJMLID(inp, gLinkTextL, inpList) 
        cordF = njmlsdata[0]
        njid = njmlsdata[1]
        #data sets inits

        inits = initData(inp, zipcode, county, town, cordF, njid)
        print(inits)
        dataAttr = inits[0]
        links = inits[1]
        dataAttr2 = inits[2]
        data2 = inits[3]

        #adds special site links
        special = ["Realtor Search", "Compass Search", "Redfin Search", "AreaVibes Search"]
        siteURL = ["realtor.com", "compass.com", "redfin.com", "areavibes.com"]
        for s in range(len(special)):
            if siteURL[s]=="areavibes.com": #special condition for area vibes search parameter
                link2Add = googleSearch(f"{zipcode} site:{siteURL[s]}")
            else:
                link2Add = googleSearch(f"{inp} site:{siteURL[s]}")
            
            print(link2Add)
            dataAttr.insert(5,special[s])
            if len(link2Add)>0:
                links.insert(5+s,link2Add[0])
            else:
                # data.insert("about:blank", "about:blank")
                print("error handling inserts!")

            #opens new browser link
            webbrowser.open_new("https://")

            #output and action 1
            for e in range(len(links)):
                print(f"Queued: {dataAttr[e]}")
                url = str(f"{links[e]}").replace(" ","%20")
                webbrowser.open_new(url)

            #ask to load more info?
            print(f"LOAD MORE INFO:? (Y/N) {que}")
            response = input()
            while str(response).lower()!="y" and str(response).lower()!="n":
                print("PLEASE ENTER VALID LETTER (Y/N)")
                response=input()

            print(response)
            #output2 on conditional statement
            if str(response).lower()=="y":
                for e in range(len(dataAttr2)):
                    print(f"Queued: {dataAttr2[e]}")
                    url = str(f"{data2[e]}").replace(" ","%20")
                    webbrowser.open_new(url)

            print(f"{que}".join("/"*2))

            sites2Check = ["realtor.com", "zillow.com", "trulia.com"]
            similarSites(sites2Check)
    # except:
        # proceed = input("failed Query! Proceed [Y/N]?")
        # if proceed.lower() == "y":
            # pass
    elif ch=='q':
        break

# %%