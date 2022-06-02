#!/usr/bin/python2 
 #coding=utf-8 
 #The Credit For This Code Goes To lovehacker 
 #If You Wanna Take Credits For This Code, Please Look Yourself Again... 
 #Reserved2020 
  
  
 import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize 
 from multiprocessing.pool import ThreadPool 
 from requests.exceptions import ConnectionError 
 from mechanize import Browser 
  
  
 reload(sys) 
 sys.setdefaultencoding('utf8') 
 br = mechanize.Browser() 
 br.set_handle_robots(False) 
 br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1) 
 br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')] 
  
  
 def keluar(): 
         print "\x1b[1;91mExit" 
         os.sys.exit() 
  
  
 def acak(b): 
     w = 'ahtdzjc' 
     d = '' 
     for i in x: 
         d += '!'+w[random.randint(0,len(w)-1)]+i 
     return cetak(d) 
  
  
 def cetak(b): 
     w = 'ahtdzjc' 
     for i in w: 
         j = w.index(i) 
         x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j)) 
     x += '\033[0m' 
     x = x.replace('!0','\033[0m') 
     sys.stdout.write(x+'\n') 
  
  
 def jalan(z): 
         for e in z + '\n': 
                 sys.stdout.write(e) 
                 sys.stdout.flush() 
                 time.sleep(0.07) 
  
 #Dev:love_hacker 
 ##### LOGO ##### 
 logo = """ 
        \033[1;91m:▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒: 
       \033[1;92m▒▒▒▒▒▒▒▒█▒█▒█▒▒▒█▒█▒█▒▒▒▒▒▒▒▒▒▒::      
      \033[1;93m:▒▒▒▒▒▒███▒█▒█▒███▒█▒█▒▒▒▒▒▒▒▒▒▒:::       
     \033[1;94m::▒▒▒▒▒▒█▒▒▒█▒█▒█▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒::::       
    \033[1;95m:::▒▒▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:::::          
   \033[1;96m::♧♧♧♧♧♧♧♧♧♧\033[1;91mWhatsapp\033[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒::::         
   \033[1;91m:》》》\033[1;93m+93745464155\033[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒::::: 
 \033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96m-shfeeullah.zahir-\033[1;95m♡╭──────────•◈•──────────╮♡ 
 \033[1;92m..........................shfeeullah.zahir...................... 
 \033[1;93m╔╗ ╔╗╔═╦╦╦═╗ ╔╗╔╦═╦╦╗ 
 \033[1;93m║║ ║╚╣║║║║╩╣ ╚╗╔╣║║║║   afghanistan
 \033[1;93m╚╝ ╚═╩═╩═╩═╝═ ╚╝╚═╩═╝  
 \033[1;95m♡╰──────────•◈•──────────╯♡\033[1;96mshfeeullah.zahir\033[1;95m♡╰──────────•◈•──────────╯♡""" 
  
 def tik(): 
         titik = ['.   ','..  ','... '] 
         for o in titik: 
                 print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1) 
  
  
 back = 0 
 berhasil = [] 
 cekpoint = [] 
 oks = [] 
 id = [] 
 listgrup = [] 
 vulnot = "\033[31mNot Vuln" 
 vuln = "\033[32mVuln" 
  
 os.system("clear") 
 print  """ 
   \033[1;96m-┈┈┈┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈          
   \033[1;96m┈┈┈┈┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈         
   \033[1;96m┈┈┈┈┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈    
  \033[1;96m ┈┈┈┈┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈    
  \033[1;96m ┈┈┈┈┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈ 
  \033[1;96m ┈┈┈┈┈┈┈┈╱▔▔▔▔┊┊┊┊▔▔▔▔╲┈┈┈┈ 
   \033[1;96m ─────────────•◈•──────────   
    \033[1;92m███████▒▒Welcome To shfeeullah.zahir▒▒████████ 
 \033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96mshfeeullah.zahir\033[1;95m♡╭──────────•◈•──────────╮♡ 
 \033[1;94mAuthor\033[1;91m: \033[1;91mNloveS 
 \033[1;94mshfeeullah.zahir\033[1;91m: \033[1;91▒▓██████████████]99.9 
 \033[1;94mFacebook\033[1;91m: \033[1;91mNloveS 
 \033[1;94mWhatsapp\033[1;91m: \033[1;91m+93745464155 
 \033[1;95m♡╰──────────•◈•──────────╯♡\033[1;96mshfeeullah.zahir\033[1;95m♡╰──────────•◈•──────────╯♡""" 
 jalan('              \033[1;96m....................shfeeullah.zahir.....................:') 
 jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈   ") 
 jalan('\033[1;93m   ┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈   ') 
 jalan('\033[1;93m   ┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈   ') 
 jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈ ") 
 jalan("\033[1;93m   ┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈") 
 print "\033[1;93m♡─────╱▔▔▔▔┊┊┊┊▔▔▔▔╲───────♡\033[1;96mLogin shfeeullah.zahir\033[1;95m♡╰──────────•◈•──────────╯♡" 
  
 CorrectUsername = "shfeeullah" 
 CorrectPassword = "N.love.S" 
  
 loop = 'true' 
 while (loop == 'true'): 
     username = raw_input("\033[1;91m🔐 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;93m") 
     if (username == CorrectUsername): 
             password = raw_input("\033[1;94m🔐 \x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;92m") 
         if (password == CorrectPassword): 
             print "Logged in successfully as " + username #Dev:love_hacker 
             time.sleep(2) 
             loop = 'false' 
         else: 
             print "\033[1;91mWrong Password" 
             os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw') 
     else: 
         print "\033[1;94mWrong Username" 
         os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw') 
  
 def login(): 
         os.system('clear') 
         try: 
                 toket = open('login.txt','r') 
                 menu()  
         except (KeyError,IOError): 
                 os.system('clear') 
                 print logo 
                 jalan(' \033[1;92mWarning: \033[1;97mDo Not Use Your Personal Account' )
