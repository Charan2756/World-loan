from flask import Flask, request
import csv, os, requests
from datetime import datetime
from urllib.parse import quote
app = Flask(__name__)
N = chr(10)
W = 'https://wa.me/message/CFCJWLOZ7IWZK1'
B = os.environ.get('BOT_TOKEN')
C = os.environ.get('CHAT_ID')

H = '''<style>
body{margin:0;background:#eef1f5;font-family:Arial;font-size:20px;padding-bottom:90px}
.top{padding:22px;text-align:center;background:#0a1f44;position:sticky;top:0;z-index:10}
.top b{font-size:36px;color:#fff}.top b span{color:#ffc107}
.top small{display:block;color:#ccc;font-size:16px;margin-top:4px}
.wrap{max-width:620px;margin:0 auto;padding:0 14px}
.card{background:#fff;border-radius:24px;padding:26px;box-shadow:0 4px 20px rgba(0,0,0,0.06);margin:16px 0}
.card h1{font-size:32px;text-align:center;margin:0}
.card h2{font-size:26px;margin:0 0 10px 0}
.muted{color:#777;font-size:18px;text-align:center}
.btn{background:linear-gradient(90deg,#0a1f44,#0066cc);color:#fff;padding:20px;border-radius:40px;display:block;text-align:center;text-decoration:none;font-size:22px;font-weight:bold;width:100%;border:none;cursor:pointer;box-sizing:border-box}
.btn-yellow{background:#ffc107;color:#111}
.loan{display:flex;justify-content:space-between;align-items:center;background:#f8f9fa;border-radius:16px;padding:16px;margin-bottom:12px;border:2px solid #eee}
.loan b{font-size:22px}.loan span{color:#0066cc;font-size:22px;font-weight:bold}
input,select{width:100%;padding:18px;font-size:20px;border-radius:14px;border:2px solid #ddd;box-sizing:border-box}
label{font-size:20px;font-weight:bold}
.badge{display:inline-block;background:#e8f5e9;color:#1b7a2e;padding:8px 14px;border-radius:20px;font-size:16px;font-weight:bold;margin:4px}
.testi{background:#f8f9fa;border-left:5px solid #ffc107;padding:14px;border-radius:12px;margin-bottom:12px;font-size:18px}
.faq b{font-size:20px}.faq p{color:#555;font-size:18px;margin:6px 0 16px 0}
.footer{text-align:center;color:#999;font-size:16px;padding:20px}
.calc-result{background:#0a1f44;color:#fff;border-radius:16px;padding:18px;text-align:center;font-size:22px;margin-top:14px}
.calc-result b{color:#ffc107;font-size:28px}
</style>
<div class=top><b>WORLD <span>LOAN</span></b><small>🌍 Fast Loans • Same Day Approval • Anywhere</small></div>
<a href="/apply" style="position:fixed;bottom:20px;right:20px;z-index:999;background:#25D366;color:#fff;width:68px;height:68px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:36px;text-decoration:none;box-shadow:0 6px 20px rgba(0,0,0,0.3)">💬</a>
'''

def send(t):
    try:
        u = 'https://api.telegram.org/bot' + B + '/sendMessage'
        requests.post(u, json={'chat_id': C, 'text': t}, timeout=10)
    except: pass

LOANS = [
 ('$20 Loan','Pay $23 in 7 days','$20'),
 ('$50 Loan','Pay $58 in 14 days','$50'),
 ('$100 Loan','Pay $115 in 30 days','$100'),
 ('$200 Loan','Pay $230 in 30 days','$200'),
 ('$500 Loan','Pay $575 in 30 days','$500'),
 ('$1000 Loan','Pay $1150 in 30 days','$1000'),
]

@app.route('/')
def home():
    cards = ''
    for name, desc, price in LOANS:
        cards += f'<div class=loan><div><b>{name}</b><br><small style="color:#777;font-size:16px">{desc}</small></div><div style="text-align:right"><span>{price}</span><br><a href=/apply?l={name.replace(" ","%20")} style="color:#0066cc;font-weight:bold;text-decoration:none">APPLY →</a></div></div>'
    return H + f'''<div class=wrap>
    <div class=card><h1>Need Cash Fast? 🌍</h1><p class=muted>Apply in 1 minute • Get answer on WhatsApp • No paperwork</p>
    <div style="text-align:center"><span class=badge>✅ Same Day</span><span class=badge>✅ No Paperwork</span><span class=badge>✅ Secure</span></div><br>
    {cards}
    <a class=btn href=/apply>APPLY FOR LOAN NOW</a>
    <p style="text-align:center;color:#777;font-size:18px">1. Fill Form - 2. We call you - 3. You get money<br><b>Please fill form first before WhatsApp</b></p></div>

    <div class=card><h2>🧮 Loan Calculator</h2>
    <label>How much do you need?</label><br><br>
    <input type=range id=amt min=20 max=1000 step=10 value=100 oninput="calc()">
    <p>Amount: $<b id=amtVal>100</b></p>
    <label>Months</label><select id=mon onchange="calc()"><option value=1>1 Month</option><option value=2>2 Months</option><option value=3>3 Months</option></select>
    <div class=calc-result>Total to pay: <b id=total>$115</b><br><span style="font-size:16px;color:#ccc">Monthly: $<span id=monthly>115</span></span></div>
    <script>function calc(){{let a=document.getElementById('amt').value;let m=document.getElementById('mon').value;document.getElementById('amtVal').innerText=a;let t=Math.round(a*1.15);document.getElementById('total').innerText='$'+t;document.getElementById('monthly').innerText=Math.round(t/m);}}calc();</script>
    </div>

    <div class=card><h2>How It Works</h2><p style="text-align:center">1️⃣ Fill the form<br>2️⃣ Submit your application<br>3️⃣ Then WhatsApp us to verify & get paid<br><br><b>We NEVER ask for your PIN or OTP on this website.</b><br>Keep your PIN on your own phone.</p></div>

    <div class=card><h2>⭐ What Customers Say</h2>
    <div class=testi>"Got $100 in same day. Very fast!"<br><b>- Tendai, Harare ⭐⭐⭐⭐⭐</b></div>
    <div class=testi>"Applied in 2 minutes, they WhatsApped me quickly."<br><b>- Chipo, Bulawayo ⭐⭐⭐⭐⭐</b></div>
    <div class=testi>"Trusted service, no hidden fees."<br><b>- Blessing, Mutare ⭐⭐⭐⭐⭐</b></div></div>

    <div class=card><div class=faq><h2>❓ FAQ</h2>
    <b>How fast do I get money?</b><p>Same day after you fill form + WhatsApp verification.</p>
    <b>What do I need to apply?</b><p>Just your name and phone number. No paperwork.</p>
    <b>Do you ask for my PIN?</b><p>NEVER. Anyone asking for PIN/OTP is a scammer.</p>
    <b>How do I pay back?</b><p>EcoCash, OneMoney, Bank Transfer, Cash or M-Pesa.</p></div>
    <a class=btn href="/apply">FILL FORM FIRST 📝</a>
    <p style="text-align:center;color:#777;font-size:17px">You must fill the form before chatting to us</p></div>
    </div><div class=footer>©️ 2026 World Loan • Secure & Trusted</div>'''

@app.route('/apply')
def form():
    l = request.args.get('l','')
    opts = ''
    for name, desc, price in LOANS:
        sel = 'selected' if l in name else ''
        opts += f'<option {sel}>{name} - {desc}</option>'
    return H + f'''<div class=wrap><div class=card><h1 style="text-align:left">Apply For Loan 🌍</h1><p style="font-size:18px;color:#777">Fill ALL fields to unlock WhatsApp chat</p>
    <form method=POST action=/submit>
    <p><label>Your Full Name</label></p><input name=name required placeholder="Your full name">
    <p><label>Phone Number</label></p><input name=phone required placeholder="e.g. 0771234567">
    <p><label>Choose Loan</label></p><select name=loan required>{opts}</select>
    <p><label>Why do you need the loan?</label></p><select name=purpose required><option>Business</option><option>School Fees</option><option>Rent</option><option>Emergency</option><option>Other</option></select>
    <p><label>How will you pay back?</label></p><select name=pay required><option>EcoCash</option><option>OneMoney</option><option>Bank Transfer</option><option>Cash</option><option>M-Pesa</option></select>
    <br><br><button class=btn>SUBMIT APPLICATION → UNLOCK WHATSAPP</button></form></div></div><div class=footer>©️ 2026 World Loan</div>'''

@app.route('/submit', methods=['POST'])
def submit():
    n = request.form.get('name',''); p = request.form.get('phone',''); l = request.form.get('loan',''); pur = request.form.get('purpose',''); pay = request.form.get('pay','')
    if not n or not p or not l:
        return H + '<div class=wrap><div class=card><h1>Please fill ALL fields</h1><a class=btn href=/apply>GO BACK</a></div></div>'
    with open('leads.csv','a',newline='') as f:
        csv.writer(f).writerow([datetime.now().isoformat(),n,p,l,pur,pay])
    send('New World Loan Application'+N+'Name: '+n+N+'Phone: '+p+N+'Loan: '+l+N+'Purpose: '+pur+N+'Payback: '+pay)
    msg = quote(f"Hi World Loan, I am {n}. I just applied for {l}. My phone is {p}. Purpose: {pur}. Payback: {pay}. Please help me.")
    wa_link = f"{W}?text={msg}" if "message/" not in W else W
    return H + f'''<div class=wrap><div class=card><h1>Thank you, {n}! ✅</h1><p style="text-align:center">Your application for <b>{l}</b> is received.</p><p style="text-align:center">We will WhatsApp <b>{p}</b> shortly.</p><p style="text-align:center;font-size:18px;color:#777">Do NOT share your PIN or OTP with anyone, even us.</p><a class=btn style="background:#25D366" href="{W}">CHAT ON WHATSAPP NOW 💬</a><br><p style="text-align:center;color:#555;font-size:17px">When WhatsApp opens, just tap SEND - your details are already ready</p><a class=btn style="background:#ffc107;color:#111" href=/>APPLY AGAIN</a></div></div>'''

@app.route('/leads')
def leads():
    rows = ''
    try:
        with open('leads.csv') as f:
            for r in csv.reader(f):
                rows += f'<div style="background:#f8f9fa;padding:12px;border-radius:12px;margin-bottom:10px;font-size:18px"><b>{r[1] if len(r)>1 else ""}</b> - {r[2] if len(r)>2 else ""}<br>{r[3] if len(r)>3 else ""} | {r[4] if len(r)>4 else ""} | {r[5] if len(r)>5 else ""}<br><small style="color:#999">{r[0] if r else ""}</small></div>'
    except: rows = '<p>No leads yet</p>'
    return H + f'<div class=wrap><div class=card><h1>Admin - All Leads</h1>{rows}<a class=btn href=/>BACK HOME</a></div></div>'

@app.route('/health')
def health(): return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
