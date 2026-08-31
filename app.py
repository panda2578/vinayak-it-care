from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Shree Vinayak IT Care</title>
<style>
body{margin:0;background:#0a1220;color:#fff;font-family:Arial}
.header{background:#0a1220;padding:12px 20px;display:flex;justify-content:space-between;border-bottom:1px solid #333}
.logo{display:flex;align-items:center;gap:12px}
.logo h1{margin:0;font-size:22px;line-height:1.1} .logo span{color:#ff6a00}
.sub{font-size:13px} .sub2{font-size:12px;color:#ffcc00}
.topinfo{display:flex;gap:18px;font-size:11px;margin-top:10px;flex-wrap:wrap}
.loginbox{background:#111a2b;border:1px solid #333;border-radius:12px;padding:18px;width:300px}
.loginbox input{width:100%;padding:10px;margin:6px 0;border-radius:8px;border:1px solid #333;background:#1a2438;color:#fff}
.btn{background:linear-gradient(90deg,#ff5a00,#ff8a00);border:none;padding:10px;width:100%;border-radius:8px;color:#fff;font-weight:bold;margin-top:10px}
.welcome{text-align:center;padding:25px}
.welcome h2{margin:0} .welcome h1{color:#ff6a00;margin:5px 0}
.catalog{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;padding:12px}
@media(max-width:800px){.catalog{grid-template-columns:1fr 1fr} .header{flex-direction:column} .loginbox{width:auto}}
.card{border-radius:14px;padding:14px;position:relative;min-height:140px}
.card h3{margin:8px 0 4px;font-size:14px} .card p{font-size:11px;opacity:.8;margin:0}
.explore{position:absolute;bottom:12px;right:12px;border:1px solid #ffffff55;padding:4px 10px;border-radius:16px;font-size:11px}
.blue{background:linear-gradient(135deg,#0d2a5a,#123a7a)} .green{background:linear-gradient(135deg,#0a4a2e,#126b44)}
.purple{background:linear-gradient(135deg,#3a1a5a,#5a2a8a)} .orange{background:linear-gradient(135deg,#7a2a0a,#a9441a)}
.teal{background:linear-gradient(135deg,#0a4a4a,#126a6a)} .gold{background:linear-gradient(135deg,#5a4a0a,#7a651a)}
.study{border:1px solid #333;border-radius:14px;margin:12px;padding:14px;display:flex;gap:12px;flex-wrap:wrap;align-items:center}
</style>
</head>
<body>
<div class="header">
  <div>
    <div class="logo">
      <div style="font-size:36px">🕉️</div>
      <div><h1>SHREE VINAYAK<br><span>IT CARE</span></h1><div class="sub">Laptop Repair Database & Board Viewer</div><div class="sub2">Repair | Restore | Resolve</div></div>
    </div>
    <div class="topinfo">
      <div>🛡️ 19+ Years Of Experience</div>
      <div>📍 Bhubaneswar, Odisha India</div>
      <div>📞 +91 9437 60 1000 Call / WhatsApp</div>
      <div>✉️ info@shreevinayakitcare.com Support</div>
    </div>
  </div>
  <div class="loginbox">
    <div>🔒 LOGIN</div>
    <input placeholder="👤 Username"><input placeholder="🔒 Password" type="password">
    <div style="font-size:11px;display:flex;justify-content:space-between;margin-top:6px"><label><input type="checkbox"> Remember Me</label><span style="color:#ffcc00">Forgot Password?</span></div>
    <button class="btn">LOGIN →</button>
    <div style="text-align:center;font-size:11px;margin-top:8px">New User? <span style="color:#ffcc00">Create an Account</span></div>
  </div>
</div>

<div class="welcome">
  <h2>WELCOME</h2><div>TO</div><h1>SHREE VINAYAK IT CARE</h1>
  <p style="font-size:13px;opacity:.7">Your One Stop Solution for Chip-Level Repairing, Board Diagnostics,<br>Component Search, and Technical Learning Resources.</p>
  <div>— REPAIR CATALOGUE —</div>
</div>

<div class="catalog">
  <div class="card blue"><div>💻</div><h3>LAPTOP REPAIR</h3><p>All Brands Supported<br>Chip-Level Repairing</p><div class="explore">Explore →</div></div>
  <div class="card green"><div>🖥️</div><h3>DESKTOP REPAIR</h3><p>Motherboard & Component Level Repairing</p><div class="explore">Explore →</div></div>
  <div class="card purple"><div>🖨️</div><h3>PRINTER REPAIR</h3><p>Laser, Inkjet, All-in-One Printer Solutions</p><div class="explore">Explore →</div></div>
  <div class="card orange"><div>📱</div><h3>MOBILE / TABLET REPAIR</h3><p>Hardware & Software Solutions</p><div class="explore">Explore →</div></div>
  <div class="card teal"><div>💾</div><h3>DATA RECOVERY</h3><p>Recover Deleted, Formatted & Lost Data</p><div class="explore">Explore →</div></div>
  <div class="card gold"><div>⚡</div><h3>POWER SUPPLY REPAIR</h3><p>SMPS, Adapter, DC Supply Repair & Fix</p><div class="explore">Explore →</div></div>
</div>

<div class="study">
  <div style="flex:1"><h3 style="margin:0">STUDY MATERIAL</h3><div style="color:#4da6ff;font-size:13px">Learn | Practice | Master</div><p style="font-size:11px">Access Schematics, BoardViews, Repair Guides, eBooks, and Technical Notes.</p><div class="explore" style="position:static;display:inline-block">Explore Study Material →</div></div>
  <div style="display:flex;gap:10px"><div style="background:#fff;color:#000;padding:10px;border-radius:8px;font-size:10px;text-align:center">SCH<br>Schematics</div><div style="background:#333;padding:10px;border-radius:8px;font-size:10px;text-align:center">Board<br>Board Views</div><div style="background:#fff;color:#000;padding:10px;border-radius:8px;font-size:10px;text-align:center">PDF<br>Repair Guides</div><div style="background:#222;padding:10px;border-radius:8px;font-size:10px;text-align:center">📚<br>eBooks & Notes</div></div>
</div>

<div style="text-align:center;font-size:10px;opacity:.6;padding:12px">© 2024 SHREE VINAYAK IT CARE. All Rights Reserved.</div>
</body>
</html>
"""

@app.route('/')
def home(): return HTML
@app.route('/motherboards')
def mb(): return HTML

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
