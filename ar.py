# encoding=utf8
import sys, requests, os
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
global tag, email, password
tag = sys.argv[3]
email = sys.argv[4]
password = sys.argv[5]
def report(id_target, s):
    buka = s.get("https://free.facebook.com/profile.php?id=" + id_target)
    if "Lainnya" in buka.text or "Tambah Jadi Teman" in buka.text:
        soup = BeautifulSoup(buka.text, features='html5lib')
    else:
        print ("\033[34m|-----\033[31mID Target Tidak Ditemukan!")
        sys.exit()
    for a in soup.find_all('a', href=True):
        if '/rapid_report/?' in a["href"]:
            global url_r
            url_r = ("https://free.facebook.com" + a["href"])
            print ("\033[34m|-----\033[36mBerhasil Mendapatkan Link Report Target!")
            pass
        else:
            continue
    hah = s.get(url_r)
    soup = BeautifulSoup(hah.text, features='html5lib')
    for a in soup('form'):
        urlReport_A = "https://free.facebook.com" + a['action']
    for i in soup('input'):
        if 'fb_dtsg' in i["name"]:
            fb_dtsg = i["value"]
        if 'jazoest' in i["name"]:
            jazoest = i["value"]
        else:
            continue
    data_r = {
	'fb_dtsg': (fb_dtsg),
	'jazoest': (jazoest),
	'tag': (tag),
	'action': 'Kirim'
    }
    report = s.post(urlReport_A, data=data_r)
    soup = BeautifulSoup(report.text, features='html5lib')
    for a in soup('form'):
        urlReport_end = "https://free.facebook.com" + a['action']
    for i in soup('input'):
       if 'fb_dtsg' in i["name"]:
           fb_dtsg = i["value"]
       if 'jazoest' in i["name"]:
           jazoest = i["value"]
       else:
           continue
    data_end = {
	  'fb_dtsg': (fb_dtsg),
	  'jazoest': (jazoest),
  	'action': 'Kirim'}
    report_end = s.post(urlReport_end, data=data_end)
    if 'Dikirimkan ke Facebook untuk Ditinjau' in report_end.text:
        print ("\033[34m|-----\033[35mReport \033[32mBerhasil!")
    else:
        print ("\033[34m|-----\033[39mReport \033[31mGagal!") 
def login(id_target, lis):
    print ("\033[39m[ \033[32mINFO \033[39m] \033[39mLogin Dengan Akun "+email+"|"+password)
    s = requests.Session()
    url = ("https://free.facebook.com/login/?ref=dbl&fl&refid=8")
    key = {
	'email': (email),
	'pass': (password),
	'login': 'Masuk'}
    login = s.post(url, data=key)
    soup = BeautifulSoup(login.text, features='html5lib')
    if soup.title.text =='Facebook':
        print ("\033[34m|-----\033[36mLogin Berhasil!")
        report(id_target, s)
    if "verify" in login.url or "challange" in login.url or "checkpoint" in login.url:
        print ("\033[34m|-----\033[33mAkun Kena Cekpoin! \033[36m(Skip)")
    else:
        print ("\033[34m|-----\033[39mLogin \033[31mGagal! \033[36m(Skip)")

if __name__=='__main__':
login(sys.argv[1], sys.argv[2])
