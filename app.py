from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>WORLD LOAN</title>
<style>
body{font-family:Arial;background:#0f172a;color:white;text-align:center;padding:20px}
.card{background:white;color:black;border-radius:15px;padding:20px;max-width:400px;margin:auto}
input,select{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:1px solid #ccc}
button{background:#16a34a;color:white;padding:14px;width:100%;border:none;border-radius:10px;font-size:18px;font-weight:bold}
.result{background:#dcfce7;padding:15px;border-radius:10px;margin-top:15px}
</style>
</head>
<body>
<h1>🌍 WORLD LOAN</h1>
<p>Fast Loans | EcoCash | OneMoney | Bank</p>
<div class="card">
<form method="POST">
<label>Your Name</label>
<input name="name" placeholder="Full Name" required>
<label>Phone / EcoCash Number</label>
<input name="phone" placeholder="077xxxxxxx" required>
<label>Loan Amount ($)</label>
<input type="number" name="amount" placeholder="e.g. 100" required>
<label>Months</label>
<select name="months">
<option value="1">1 Month</option>
<option value="2">2 Months</option>
<option value="3">3 Months</option>
<option value="6">6 Months</option>
</select>
<button type="submit">APPLY NOW</button>
</form>
{% if total %}
<div class="result">
<h3>Hi {{name}} ✅</h3>
<p>Loan: ${{amount}}</p>
<p>Interest (10%): ${{interest}}</p>
<h2>Total to Pay: ${{total}}</h2>
<p>We will contact you on {{phone}}</p>
</div>
{% endif %}
</div>
<p style="margin-top:20px;font-size:12px;">©️ 2026 WORLD LOAN - All Rights Reserved</p>
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    total = None
    interest = 0
    amount = 0
    name = ""
    phone = ""
    if request.method == "POST":
        name = request.form.get("name","")
        phone = request.form.get("phone","")
        amount = float(request.form.get("amount",0))
        months = int(request.form.get("months",1))
        interest = round(amount * 0.10 * months, 2)
        total = round(amount + interest, 2)
    return render_template_string(HTML, total=total, interest=interest, amount=amount, name=name, phone=phone)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
