# encoding=utf8
import sys, requests, os
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")
def main(id):
    lis = raw_input("\033[31m[\033[39mACCOUNT\033[31m] \033[39mList Akun: ")
    try:
      bul = open(lis, "r").read().split()
      akin = open(lis, "r")
    except:
      print ("\033[39m[\033[31mWARNING\033[39m] File Tidak Ditemukan!")
      sys.exit()
    print ("\033[39m" + 50*"_" + "\n\033[34m[\033[39m1\033[34m] \033[39mAkun Palsu\n\033[34m[\033[39m2\033[34m] \033[39mNama Palsu\n\033[34m[\033[39m3\033[34m] \033[39mMengirim Hal yang Tidak Pantas\n" + 50*"_")

    while True:
        report_type = input("\033[31m[\033[39mREPORT\033[31m] \033[39mTipe Report: ")
        if report_type ==1:
            tag = ("profile_fake_account")
            break
        elif report_type ==2:
            tag = ("profile_fake_name")
            break
        elif report_type ==3:
            tag = ("profile_posting_inappropriate_things")
            break
        else:
            print ("\033[33m[\033[31mWARNING\033[33m] \033[39mPilih Nomornya!")
            continue

    for a in range(len(bul)):
        if a == len(bul):
            break
        akn = akin.readline().strip()
        akun = akn.split("|")
        email = akun[0]
        password = akun[1]
        os.system("python2 ar.py "+id+" "+lis+" "+tag+" "+email+" "+password)
print ("\033[34m[\033[39m1\033[34m] \033[39mSingle Report")
print ("\033[34m[\033[39m2\033[34m] \033[39mList Report")

while True:
    try:
        yaya = input("\033[32m..\033[31m/\033[33mPilih\033[35m> \033[36m")
    except:
        print ("\033[39m[\033[31m!\033[39m] Pilih Gayn /_-")
        continue
    if yaya==1:
        break
    elif yaya==2:
        id = raw_input("\033[31m[\033[39mTARGET\033[31m]\033[39m ID Target: ")
        main(id)
        break
    else:
        print ("\033[39m[\033[31m!\033[39m] Pilih Gayn /_-")
        continue
def pura(s, report, id_target):
    soup = BeautifulSoup(report, features='html.parser')
    for a in soup('form'):
        urlReport_pura = "https://free.facebook.com" + a['action']
    for i in soup('input'):
        if 'fb_dtsg' in i["name"]:
            fb_dtsg = i["value"]
        if 'jazoest' in i["name"]:
            jazoest = i["value"]
        else:
            continue
    key = {'fb_dtsg': (fb_dtsg),
    	'jazoest': (jazoest),
    	'tag': 'profile_impersonation_me',
    	'action': 'Kirim'}
    rep = s.post(urlReport_pura, data=key)
    soup = BeautifulSoup(rep.text, features='html.parser')
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
    report = s.post(urlReport_end, data=data_end)
    if 'Dikirimkan ke Facebook untuk Ditinjau' in report.text:
        print ("\033[39m[ \033[32mINFO \033[39m] \033[39mReport Berhasil!")
        bukti = raw_input("\033[39m[ \033[32mINFO \033[39m] \033[39mIngin Mendapatkan Bukti? [Y/N]: ")
        if bukti=="Y" or bukti =="y":
            nama_file = raw_input("\033[39m[ \033[32mFILE \033[39m] \033[39mNama File (ex: report.html): ")
            cok = open((nama_file), "a")
            cok.write(report.text)
            cok.close()
            try:
                os.system("mv " + nama_file + " /storage/emulated/0")
                print ("\033[39m[ \033[32mINFO \033[39m] \033[39mBukti File Di:\033[32m /storage/emulated/0/" + nama_file)
            except:
                os.system("mv " + nama_file + " /sdcard")
                print ("\033[39m[ \033[32mINFO \033[39m] \033[39mBukti File Di:\033[32m /sdcard/" + nama_file)
        else:
            pass
        while True:
            lagi = raw_input("\033[31m[\033[39mREPORT\033[31m] \033[39mReport Lagi? [Y/n]: ")
            if lagi =="Y" or lagi =="y":
                print (50*"\033[36m_")
                return login(id_target)
            elif lagi =="N" or lagi =="n":
                sys.exit()
            else:
                print ("\033[33m[\033[31mWARNING\033[33m] \033[39mPilih \033[39m(\033[33mY \033[31m/ \033[33mN\033[39m)")
    else:
        print ("\033[33m[\033[31mWARNING\033[33m] \033[39mReport \033[31mGagal!") 
def report(id_target, s):
    buka = s.get("https://free.facebook.com/profile.php?id=" + id_target)
    if "Lainnya" in buka.text or "Tambah Jadi Teman" in buka.text:
        soup = BeautifulSoup(buka.text, features='html.parser')
    else:
        print ("\033[33m[\033[31mWARNING\033[33m] \033[39mID Target Tidak Ditemukan!")
        sys.exit()
    for a in soup.find_all('a', href=True):
        if '/rapid_report/?' in a["href"]:
            global url_r
            url_r = ("https://free.facebook.com" + a["href"])
            print ("\033[39m[ \033[32mINFO \033[39m] Berhasil Mendapatkan Link Report Target!")
            break
        else:
            continue
    print ("\033[39m" + 50*"_" + "\n\033[34m[\033[39m1\033[34m] \033[39mBerpura Pura Menjadi Saya\n\033[34m[\033[39m2\033[34m] \033[39mAkun Palsu\n\033[34m[\033[39m3\033[34m] \033[39mNama Palsu\n\033[34m[\033[39m4\033[34m] \033[39mMengirim Hal yang Tidak Pantas\n" + 50*"_")
    while True:
        report_type = input("\033[31m[\033[39mREPORT\033[31m] \033[39mTipe Report: ")
        if report_type ==1:
            tag = ("profile_impersonation")
            hah = s.get(url_r)
            soup = BeautifulSoup(hah.text, features='html.parser')
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
  	'action': 'Kirim'}
            report = s.post(urlReport_A, data=data_r)
            pura(s, report.text, id_target)
        elif report_type ==2:
            tag = ("profile_fake_account")
            break
        elif report_type ==3:
            tag = ("profile_fake_name")
            break
        elif report_type ==4:
            tag = ("profile_posting_inappropriate_things")
            break
        else:
            print ("\033[33m[\033[31mWARNING\033[33m] \033[39mPilih Nomornya!")
            continue
    hah = s.get(url_r)
    soup = BeautifulSoup(hah.text, features='html.parser')
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
    soup = BeautifulSoup(report.text, features='html.parser')
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
        print ("\033[39m[ \033[32mINFO \033[39m] \033[39mReport Berhasil!")
        bukti = raw_input("\033[39m[ \033[32mINFO \033[39m] \033[39mIngin Mendapatkan Bukti? [Y/N]: ")
        if bukti=="Y" or bukti =="y":
            nama_file = raw_input("\033[39m[ \033[32mFILE \033[39m] \033[39mNama File (ex: report.html): ")
            cok = open((nama_file), "a")
            cok.write(report.text)
            cok.close()
            try:
                os.system("mv " + nama_file + " /storage/emulated/0")
                print ("\033[39m[ \033[32mINFO \033[39m] \033[39mBukti File Di:\033[32m /storage/emulated/0/" + nama_file)
            except:
                os.system("mv " + nama_file + " /sdcard")
                print ("\033[39m[ \033[32mINFO \033[39m] \033[39mBukti File Di:\033[32m /sdcard/" + nama_file)
        else:
            pass
        while True:
            lagi = raw_input("\033[31m[\033[39mREPORT\033[31m] \033[39mReport Lagi? [Y/n]: ")
            if lagi =="Y" or lagi =="y":
                print (50*"\033[36m_")
                return login(id_target)
            elif lagi =="N" or lagi =="n":
                sys.exit()
            else:
                print ("\033[33m[\033[31mWARNING\033[33m] \033[39mPilih \033[39m(\033[33mY \033[31m/ \033[33mN\033[39m)")
    else:
        print ("\033[33m[\033[31mWARNING\033[33m] \033[39mReport \033[31mGagal!") 
def login(id_target):
    print ("\033[39m[ \033[32mINFO \033[39m] \033[39mAkun Yang Akan MeReport (\033[34m" + id_target + "\033[39m)")
    email = raw_input("\033[39m[\033[31m EMAIL\033[39m]: \033[39m")
    password = raw_input("\033[39m[ \033[31mPASS \033[39m]: \033[39m")
    print ("\033[39m[ \033[32mINFO \033[39m] \033[39mSedang Login...")
    s = requests.Session()
    url = ("https://free.facebook.com/login/?ref=dbl&fl&refid=8")
    key = {
	'email': (email),
	'pass': (password),
	'login': 'Masuk'}
    login = s.post(url, data=key)
    soup = BeautifulSoup(login.text, features='html.parser')
    if soup.title.text =='Facebook':
        print ("\033[39m[ \033[32mINFO \033[39m] Login Berhasil!")
        report(id_target, s)
    if "verify" in login.url or "challange" in login.url or "checkpoint" in login.url:
        print ("\033[33m[\033[31mWARNING\033[33m] \033[39mAkun Kena Cekpoin! Coba Login Ke \033[35mwww.facebook.com")
    else:
        print ("\033[33m[\033[31mWARNING\033[33m] \033[39mLogin \033[31mGagal!")
        sys.exit()
def what_id():
    id_target = raw_input("\033[39m[\033[31mTARGET\033[39m] ID Target: \033[36m")
    login(id_target)
if __name__=='__main__':
    os.system("clear")
what_id()
