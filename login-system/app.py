import sqlite3 as sql
import time
import webbrowser
giris = """######################################
\t\tOZD ŞİRKETLER GRUBU
\tÜYE GİRİŞ/KAYIT İŞLEMLERİ
1.KAYIT
2.GİRİŞ
3.ÇIKIŞ
######################################"""
con = sql.connect("systemlog.db")
im = con.cursor()
im.execute("CREATE TABLE IF NOT EXISTS bilgiler (usernames,emails,passwords)")

while True:
    key = input(giris + "\nLütfen yapacağınız işlemin numarasını girin : ")

    if key == "1":
        kullanıcıAdı = input("lütfen bir kullanıcı adı girin : ")
        email1 = input("Lütfen bir email girin : ")
        pass1 = input("Şifre : ")
        if ".com" not in email1:
            print("Lütfen emailinizi düzgün girin ..")
            break
        elif len(pass1) <= 6:
            print("Lütfen daha uzun bir şifre girin ..")
            break
        else:
            print("Kaydınız yapılıyor ....")
            im.execute("INSERT INTO bilgiler VALUES (? ,? ,?)",(kullanıcıAdı,email1,pass1))
            con.commit()
            print("Kaydınız başarıyla tamamlandı.Giriş ekranına yönlendiriliyorsunuz ...")
            time.sleep(2)
    elif key == "2":
            email2 = input("Lütfen emailinizi girin : ")
            pass2  = input("Lütfen şifrenizi girin : ")
            find_user = ("SELECT * FROM bilgiler WHERE emails = ? AND passwords = ?")
            im.execute(find_user,[(email2),(pass2)])
            sonuc = im.fetchall()
            if sonuc:
                print("Sisteme giriş başarıyla gerçekleşti .İyi günler dileriz .")
                time.sleep(1)
                webbrowser.open_new_tab("https://www.ozdemirgrubu.com/")
                break
            else:
                print("Sisteme giriş başarısız.Lütfen tekrar deneyin veya kayıt olun.")
    elif key == "3":
        print("Çıkış yapılıyor....İYİ GÜNLER DİLERİZ. MİNDER MEDYA")
        time.sleep(2)
        break