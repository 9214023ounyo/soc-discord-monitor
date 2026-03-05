import requests,time,random,re,datetime
WEBHOOK_URL="https://discordapp.com/api/webhooks/1478384553776386133/g8m5PyZ5uginMLtz-KOgELs6nFwEnsSmTVDiw1l3lV3JvAR16M65_m1aIrUGHqywX7Uq"
def alert(sev,txt):requests.post(WEBHOOK_URL,json={"content":f"🚨{sev}: {txt}"})
while True:
 try:
  t=random.randint(5,15)
  if t>8:alert("HIGH BRUTE FORCE",f"{t} SSH fails TOR IP")
  re.search(r'\d{3}-\d{2}-\d{4}',"SSN:123-45-6789")and alert("CRITICAL PII","SSN exposed")
  print("✅Sent");time.sleep(60)
 except:time.sleep(30)