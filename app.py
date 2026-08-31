from flask import Flask, render_template_string
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>SHREE VINAYAK IT CARE - 7008541544</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{font-family:'Inter',sans-serif;background:#070e1f;color:#e6efff;overflow-x:hidden}
.container{max-width:1320px;margin:0 auto;padding:10px}

/* HEADER - SAME AS SCREENSHOT */
.header{
  background:linear-gradient(90deg,#0a1429 0%, #0d1d3a 60%, #0a1933 100%);
  border:1px solid #1a2f54;border-radius:16px;padding:14px 18px;
  display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;
  position:relative;overflow:hidden
}
.header::after{
  content:"";position:absolute;right:0;top:0;width:38%;height:100%;
  background:linear-gradient(to left, rgba(0,0,0,0.8), transparent), url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=500');
  background-size:cover;opacity:0.4
}
.logo-wrap{display:flex;gap:14px;align-items:center;z-index:2}
.logo-circle{
  width:68px;height:68px;border-radius:50%;border:2px solid #ff7a00;
  background:radial-gradient(circle at 30% 30%, #1e3a6b, #070e1f);
  display:grid;place-items:center;font-size:36px;box-shadow:0 0 20px rgba(255,122,0,0.3)
}
.brand h1{font-size:28px;font-weight:900;line-height:1.05;letter-spacing:0.3px}
.brand h1 span{color:#ff7a00}
.brand .tag1{font-size:13.5px;color:#d0d9e8;margin-top:3px}
.brand .tag2{font-size:12.5px;color:#ffcc00;font-weight:600;margin-top:1px}
.info-strip{
  display:flex;gap:0;flex-wrap:wrap;margin-top:12px;
  border-top:1px solid #1a2f54;border-bottom:1px solid #1a2f54;
  padding:8px 0;z-index:2;width:100%
}
.info-item{flex:1;display:flex;gap:8px;align-items:center;font-size:11px;color:#9fb0cc;border-right:1px solid #1a2f54;padding:0 14px;min-width:180px}
.info-item:last-child{border:none}
.info-item b{color:#fff;display:block;font-size:11.5px}
.info-icon{color:#ffb700;font-size:16px}

/* MAIN LAYOUT */
.main-layout{display:grid;grid-template-columns:1fr 350px;gap:12px;margin-top:12px}
.left-side{}

/* WELCOME */
.welcome{text-align:center;padding:18px 10px 8px}
.welcome h2{font-size:30px;letter-spacing:3px;font-weight:800}
.welcome .to{font-size:13px;opacity:0.6;margin:2px 0}
.welcome h1{font-size:28px;color:#ff7a00;font-weight:900;letter-spacing:0.5px}
.welcome .divider{width:120px;height:2px;background:linear-gradient(90deg,transparent,#ff7a00,transparent);margin:8px auto;position:relative}
.welcome .divider::after{content:"⬢";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:#070e1f;padding:0 6px;color:#ff7a00;font-size:12px}
.welcome p{font-size:12.5px;color:#8fa0bd;max-width:620px;margin:10px auto 0;line-height:1.6}

/* REPAIR CATALOGUE TITLE */
.cat-title{text-align:center;margin:16px 0 12px;font-size:13px;letter-spacing:4px;color:#a8bbd8;position:relative;font-weight:600}
.cat-title::before,.cat-title::after{
  content:"";position:absolute;top:50%;width:90px;height:1px;
  background:linear-gradient(90deg,transparent,#00a6ff,transparent)
}
.cat-title::before{left:calc(50% - 200px)}.cat-title::after{right:calc(50% - 200px)}

/* REPAIR CARDS - 6 CARDS WITH THUMBNAIL HOVER */
.repair-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.r-card{
  border-radius:16px;padding:14px;min-height:182px;position:relative;overflow:hidden;
  border:1px solid rgba(255,255,255,0.08);cursor:pointer;
  transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  display:flex;flex-direction:column;justify-content:flex-end;
}
.r-card:hover, .r-card.m-hover{
  transform:translateY(-8px) scale(1.025);
  box-shadow:0 20px 45px rgba(0,0,0,0.7), 0 0 30px var(--glow);
  border-color:var(--glow);z-index:5;
}
.r-top{display:flex;justify-content:space-between;align-items:flex-start}
.r-icon{width:48px;height:48px;border-radius:50%;display:grid;place-items:center;font-size:22px;color:#fff;border:1.5px solid rgba(255,255,255,0.25)}
.r-thumb{
  width:58%;height:88px;object-fit:contain;position:absolute;right:8px;top:12px;
  filter:drop-shadow(0 10px 18px rgba(0,0,0,0.8));
  transition:all 0.45s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.r-card:hover .r-thumb, .r-card.m-hover .r-thumb{transform:scale(1.18) rotate(3deg) translateY(-5px);filter:drop-shadow(0 15px 25px rgba(0,0,0,0.9))}
.r-card h3{font-size:14.5px;font-weight:800;margin-top:55px;letter-spacing:0.2px}
.r-card p{font-size:11px;color:#cbd6e8;opacity:0.9;margin-top:4px;line-height:1.4}
.r-card .btn-exp{
  position:absolute;right:12px;bottom:12px;border:1px solid rgba(255,255,255,0.4);
  border-radius:20px;padding:5px 14px;font-size:11px;background:rgba(0,0,0,0.45);display:flex;gap:6px;align-items:center
}
.r-card:hover .btn-exp{background:rgba(255,255,255,0.15);border-color:#fff}

.c-blue{background:linear-gradient(135deg,#123072 0%, #0a1d45 100%);--glow:#3b82f6}.c-blue .r-icon{background:#2563eb}
.c-green{background:linear-gradient(135deg,#0f4a2e 0%, #0a2a1b 100%);--glow:#22c55e}.c-green .r-icon{background:#16a34a}
.c-purple{background:linear-gradient(135deg,#3a1f6b 0%, #1f113f 100%);--glow:#a855f7}.c-purple .r-icon{background:#9333ea}
.c-orange{background:linear-gradient(135deg,#7a2e0a 0%, #3d1a05 100%);--glow:#f97316}.c-orange .r-icon{background:#ea580c}
.c-teal{background:linear-gradient(135deg,#0a4a52 0%, #082a30 100%);--glow:#06b6d4}.c-teal .r-icon{background:#0891b2}
.c-yellow{background:linear-gradient(135deg,#5a4510 0%, #2f2405 100%);--glow:#eab308}.c-yellow .r-icon{background:#ca8a04}

/* LOGIN */
.login-panel{
  background:linear-gradient(180deg,#0e1a33 0%, #0a1226 100%);
  border:1px solid #23365e;border-radius:16px;padding:18px;
  position:sticky;top:12px;height:fit-content;box-shadow:0 10px 30px rgba(0,0,0,0.5)
}
.login-panel h3{font-size:14px;display:flex;gap:8px;align-items:center}
.login-panel input{
  width:100%;padding:11px 12px 11px 36px;border-radius:10px;border:1px solid #1e375f;
  background:#0d1c36;color:#fff;margin-top:10px;font-size:12px;outline:none
}
.input-wrap{position:relative}.input-wrap span{position:absolute;left:10px;top:21px;font-size:14px;color:#6b86ac}
.btn-login{width:100%;padding:11px;border:none;border-radius:10px;background:linear-gradient(90deg,#ff5a00,#ff8a00);color:#fff;font-weight:800;margin-top:12px;cursor:pointer;letter-spacing:0.5px}
.btn-login:hover{filter:brightness(1.15)}

/* STUDY MATERIAL - 4 THUMBNAILS WITH HOVER */
.study-section{
  margin-top:12px;border:1px solid #1c3156;border-radius:16px;
  padding:14px;background:linear-gradient(90deg,#0a162e 0%, #0e1d36 100%);
  display:grid;grid-template-columns:290px 1fr;gap:14px;align-items:center
}
.study-info h3{font-size:16px;font-weight:800}.study-info .sub{font-size:12.5px;color:#3b9bff;font-weight:600;margin-top:1px}
.study-info p{font-size:11px;color:#8aa0c6;margin:8px 0 12px;line-height:1.5}
.study-info .btn-study{border:1px solid #2a426c;border-radius:20px;padding:6px 16px;font-size:11px;display:inline-flex;gap:8px;align-items:center;background:rgba(0,0,0,0.3)}
.study-thumbs{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.t-card{text-align:center;cursor:pointer}
.t-img{
  height:92px;border-radius:12px;background:#0e1f3b;border:1px solid #1e375f;
  display:grid;place-items:center;overflow:hidden;position:relative;
  transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.t-img img{width:100%;height:100%;object-fit:cover;transition:0.4s}
.t-card:hover .t-img, .t-card.m-hover .t-img{
  transform:scale(1.1) translateY(-6px) rotate(2deg);
  border-color:#ff7a00;box-shadow:0 14px 30px rgba(0,0,0,0.6),0 0 20px rgba(255,122,0,0.4)
}
.t-card:hover .t-img img, .t-card.m-hover .t-img img{transform:scale(1.15)}
.t-card p{font-size:11px;margin-top:7px;color:#a8bbd8;transition:0.3s}.t-card:hover p{color:#ff9a3d;font-weight:600}

/* FOOTER */
.footer-strip{
  margin-top:12px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;
  border:1px solid #1c3156;border-radius:12px;padding:10px 14px;
  background:rgba(10,18,35,0.6);font-size:11px;color:#7f93b5
}
.footer-strip span{display:flex;gap:6px;align-items:center}
.copy{text-align:center;font-size:11px;opacity:0.4;padding:12px 0 4px}

/* RESPONSIVE + ROTATE FIX */
@media(max-width:1100px){.main-layout{grid-template-columns:1fr 320px}.repair-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:768px){
  .header::after{display:none}.info-item{border:none;min-width:50%;padding:4px 10px}
  .main-layout{grid-template-columns:1fr}.login-panel{order:-1;position:relative}
  .repair-grid{grid-template-columns:1fr 1fr}.study-section{grid-template-columns:1fr}.study-thumbs{grid-template-columns:repeat(2,1fr)}
  .footer-strip{flex-direction:column}
}
@media(max-width:480px){.repair-grid{grid-template-columns:1fr}.brand h1{font-size:22px}}
@media(max-width:900px) and (orientation:landscape){
  .main-layout{grid-template-columns:1fr 300px}.repair-grid{grid-template-columns:repeat(3,1fr)}.study-thumbs{grid-template-columns:repeat(4,1fr)}
}
</style>
</head>
<body>
<div class="container">

<!-- HEADER -->
<div class="header">
  <div style="z-index:2;width:100%">
    <div class="logo-wrap">
      <div class="logo-circle">🕉️</div>
      <div class="brand">
        <h1>SHREE VINAYAK<br><span>IT CARE</span></h1>
        <div class="tag1">Laptop Repair Database & Board Viewer</div>
        <div class="tag2">Repair | Restore | Resolve</div>
      </div>
    </div>
    <div class="info-strip">
      <div class="info-item"><div class="info-icon">👨‍🔧</div><div><b>19+ Years</b>Of Experience</div></div>
      <div class="info-item"><div class="info-icon">📍</div><div><b>Bhubaneswar, Odisha</b>India</div></div>
      <div class="info-item"><div class="info-icon">📞</div><div><b><a href="tel:+917008541544" style="color:#fff;text-decoration:none">+91 70085 41544</a></b><a href="https://wa.me/917008541544" style="color:#25D366;text-decoration:none">Call / WhatsApp</a></div></div>
      <div class="info-item"><div class="info-icon">✉️</div><div><b>info@shreevinayakitcare.com</b>Support</div></div>
    </div>
  </div>
</div>

<!-- MAIN -->
<div class="main-layout">
  <div class="left-side">
    <div class="welcome">
      <h2>WELCOME</h2><div class="to">TO</div><h1>SHREE VINAYAK IT CARE</h1>
      <div class="divider"></div>
      <p>Your One Stop Solution for Chip-Level Repairing, Board Diagnostics, Component Search, and Technical Learning Resources. Contact: 7008541544</p>
    </div>

    <div class="cat-title">REPAIR CATALOGUE</div>

    <!-- 6 REPAIR CARDS WITH THUMBNAILS -->
    <div class="repair-grid">
      <div class="r-card c-blue"><div class="r-top"><div class="r-icon">💻</div><img class="r-thumb" src="https://i.ibb.co/7X3Yq9m/laptop-open.png" alt="laptop"></div><h3>LAPTOP REPAIR</h3><p>All Brands Supported<br>Chip-Level Repairing</p><div class="btn-exp">Explore →</div></div>
      <div class="r-card c-green"><div class="r-top"><div class="r-icon">🖥️</div><div class="r-thumb" style="display:grid;place-items:center;font-size:50px">🖥️</div></div><h3>DESKTOP REPAIR</h3><p>Motherboard & Component<br>Level Repairing</p><div class="btn-exp">Explore →</div></div>
      <div class="r-card c-purple"><div class="r-top"><div class="r-icon">🖨️</div><div class="r-thumb" style="display:grid;place-items:center;font-size:50px">🖨️</div></div><h3>PRINTER REPAIR</h3><p>Laser, Inkjet, All-in-One<br>Printer Solutions</p><div class="btn-exp">Explore →</div></div>
      <div class="r-card c-orange"><div class="r-top"><div class="r-icon">📱</div><div class="r-thumb" style="display:grid;place-items:center;font-size:45px">📱</div></div><h3>MOBILE / TABLET REPAIR</h3><p>Hardware & Software<br>Solutions</p><div class="btn-exp">Explore →</div></div>
      <div class="r-card c-teal"><div class="r-top"><div class="r-icon">💾</div><div class="r-thumb" style="display:grid;place-items:center;font-size:50px">💾</div></div><h3>DATA RECOVERY</h3><p>Recover Deleted, Formatted<br>& Lost Data</p><div class="btn-exp">Explore →</div></div>
      <div class="r-card c-yellow"><div class="r-top"><div class="r-icon">⚡</div><div class="r-thumb" style="display:grid;place-items:center;font-size:50px">🔋</div></div><h3>POWER SUPPLY REPAIR</h3><p>SMPS, Adapter, DC Supply<br>Repair & Fix</p><div class="btn-exp">Explore →</div></div>
    </div>

    <!-- STUDY MATERIAL - 4 THUMBNAILS -->
    <div class="study-section">
      <div class="study-info">
        <h3>STUDY MATERIAL</h3><div class="sub">Learn | Practice | Master</div>
        <p>Access Schematics, BoardViews, Repair Guides, eBooks, and Technical Notes. For Support Call 7008541544</p>
        <div class="btn-study">Explore Study Material →</div>
      </div>
      <div class="study-thumbs">
        <div class="t-card"><div class="t-img"><div style="font-size:10px;text-align:left;padding:6px;line-height:1.2;color:#333;background:#fff;width:100%;height:100%">R1 10k<br>─╱╲─<br> IC 555<br>┌──┐</div></div><p>Schematics</p></div>
        <div class="t-card"><div class="t-img"><div style="background:#0a2a1a;width:100%;height:100%;display:grid;place-items:center;font-size:30px">🔬</div></div><p>Board Views</p></div>
        <div class="t-card"><div class="t-img"><div style="background:#fff;width:100%;height:100%;display:grid;place-items:center"><span style="font-size:12px;font-weight:900">PILL</span><span style="background:#e00;color:#fff;padding:2px 10px;border-radius:4px;font-size:11px;font-weight:800;margin-top:4px">PDF</span></div></div><p>Repair Guides</p></div>
        <div class="t-card"><div class="t-img"><div style="display:flex;gap:2px;align-items:end"><div style="width:14px;height:50px;background:#8b4513"></div><div style="width:14px;height:60px;background:#2e8b57"></div><div style="width:14px;height:55px;background:#4682b4"></div><div style="width:14px;height:45px;background:#cd853f"></div></div></div><p>eBooks & Notes</p></div>
      </div>
    </div>

    <div class="footer-strip">
      <span>🔧 Chip-Level Expertise</span><span>🏅 All Brands Supported</span><span>⚡ Fast & Reliable Service</span><span>💰 Affordable Pricing</span><span>🚚 Doorstep Pickup & Delivery - Call 7008541544</span>
    </div>
    <div class="copy">© 2024 SHREE VINAYAK IT CARE | WhatsApp: 7008541544 | All Rights Reserved.</div>
  </div>

  <!-- LOGIN WITH NUMBER -->
  <div class="login-panel">
    <h3>🔒 LOGIN</h3>
    <div class="input-wrap"><span>👤</span><input placeholder="Username"></div>
    <div class="input-wrap"><span>🔒</span><input type="password" placeholder="Password"></div>
    <div style="display:flex;justify-content:space-between;font-size:11px;margin:10px 2px"><label style="display:flex;gap:4px;align-items:center"><input type="checkbox" style="width:auto;margin:0"> Remember Me</label><span style="color:#ff9a00">Forgot Password?</span></div>
    <button class="btn-login">LOGIN →</button>
    <div style="text-align:center;font-size:11px;margin-top:12px;line-height:1.8">
      New User? <span style="color:#ff9a00">Create an Account</span><br>
      <a href="https://wa.me/917008541544" style="color:#25D366;text-decoration:none;font-weight:800;font-size:13px;display:inline-flex;gap:6px;align-items:center;margin-top:6px;border:1px solid #25D366;border-radius:20px;padding:4px 12px">📱 7008541544 WhatsApp</a><br>
      <a href="tel:+917008541544" style="color:#fff;text-decoration:none">📞 Call: 70085 41544</a>
    </div>
  </div>
</div>

</div>

<script>
// HOVER = TAP ON MOBILE FOR ALL 10 THUMBNAILS
document.querySelectorAll('.r-card, .t-card').forEach(card=>{
  card.addEventListener('touchstart', function(e){
    document.querySelectorAll('.r-card, .t-card').forEach(c=>c.classList.remove('m-hover'));
    this.classList.add('m-hover');
  },{passive:true});
  card.addEventListener('touchend', function(){
    setTimeout(()=>this.classList.remove('m-hover'),1000);
  });
});
// ROTATE FIX
window.addEventListener('orientationchange', ()=>setTimeout(()=>{window.scrollTo(0,0);document.body.style.height=window.innerHeight+'px'},250));
</script>
</body></html>
"""
@app.route('/')
def home(): return render_template_string(HTML)
@app.route('/<path:p>')
def catch_all(p): return render_template_string(HTML)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
