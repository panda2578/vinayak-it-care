from flask import Flask, render_template_string
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>SHREE VINAYAK IT CARE</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{font-family:'Inter',sans-serif;background:#08111e;color:#eaf0ff;min-height:100vh;overflow-x:hidden}
body::before{content:"";position:fixed;inset:-50%;background:conic-gradient(from 0deg,#ff7a0011,#00d4ff11,#ff7a0011);animation:rot 20s linear infinite;z-index:-1;filter:blur(40px)}
@keyframes rot{to{transform:rotate(360deg)}}
.container{max-width:1280px;margin:0 auto;padding:12px;width:100%}
.topbar{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;border:1.5px solid #ff7a00;border-radius:14px;padding:12px 18px;background:rgba(16,29,51,0.85)}
.brand{font-weight:900;font-size:18px}.brand span{color:#ff7a00}
.main{display:grid;grid-template-columns:1.8fr 0.9fr;gap:16px;margin-top:16px}
.services{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.card{background:rgba(16,29,51,0.9);border:1px solid #23365e;border-radius:14px;padding:16px;display:flex;gap:12px;transition:.3s}
.card:hover,.card:active{border-color:#ff7a00;transform:translateY(-3px)}
.login{background:rgba(16,29,51,0.95);border:1.6px solid #ff7a00;border-radius:16px;padding:20px;position:sticky;top:16px}
.login input{width:100%;padding:12px;margin-top:6px;border-radius:10px;border:1px solid #2a3e62;background:#0b1930;color:#fff}
.btn{width:100%;padding:13px;border:none;border-radius:10px;background:linear-gradient(90deg,#ff6a00,#ff9a00);color:#fff;font-weight:800;margin-top:12px}
.study{margin-top:18px;border:1.5px solid #ff7a00;border-radius:16px;padding:18px;background:rgba(16,29,51,0.7)}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}

/* THUMBNAIL - DESKTOP HOVER + MOBILE TAP BOTH */
.sbox{
  background:#101d33;border:1px solid #22365e;border-radius:14px;padding:14px;text-align:center;
  transition:all .35s ease;cursor:pointer;overflow:hidden;position:relative;
  touch-action: manipulation;
}
.sbox:hover, .sbox:active, .sbox.touch-active{
  border-color:#ff7a00;
  transform:translateY(-8px) scale(1.03);
  box-shadow:0 15px 35px rgba(255,122,0,0.3),0 0 20px rgba(255,122,0,0.15) inset;
  background:#132241;
}
.thumb{
  height:75px;border-radius:12px;background:#0c1a2f;display:grid;place-items:center;
  font-size:30px;margin-bottom:12px;border:1px solid #1a2f54;transition:all .35s ease;
}
.sbox:hover .thumb, .sbox:active .thumb, .sbox.touch-active .thumb{
  transform:scale(1.2) rotate(5deg);background:linear-gradient(135deg,#162e5a,#1e3c6e);
  border-color:#ff7a00;box-shadow:0 0 25px rgba(255,122,0,0.5);font-size:36px;
}
.sbox b{font-size:12.5px;transition:.3s;display:block}
.sbox:hover b, .sbox:active b, .sbox.touch-active b{color:#ff9a3d;letter-spacing:.8px}
.sbox p{font-size:10.5px;color:#8aa0c6;margin-top:4px}
footer{text-align:center;padding:22px;font-size:11px;opacity:.5}

/* RESPONSIVE - PORTRAIT */
@media(max-width:768px){
  .container{padding:10px}
  .main{grid-template-columns:1fr}
  .login{position:relative;top:0}
  .services{grid-template-columns:1fr 1fr}
  .grid4{grid-template-columns:1fr 1fr}
  .topbar{flex-direction:column;align-items:flex-start}
}
/* MOBILE LANDSCAPE - ROTATE FIX */
@media(max-width:900px) and (orientation: landscape){
  .main{grid-template-columns:1fr 0.9fr}
  .services{grid-template-columns:repeat(3,1fr)}
  .grid4{grid-template-columns:repeat(4,1fr)}
  .container{padding:8px 12px}
  .topbar{flex-direction:row}
}
@media(max-width:480px){
  .services{grid-template-columns:1fr}
  .grid4{grid-template-columns:1fr 1fr}
}
</style></head>
<body>
<div class="container">
<div class="topbar"><div class="brand">🛡️ <span>SHREE VINAYAK</span> IT CARE</div><div style="font-size:11px">📞 9437601000 | Bhubaneswar</div></div>
<div class="main">
<div><h2>Our Repair Services</h2><div style="font-size:12px;color:#8aa0c6;border-top:2px solid #ff7a00;display:inline-block;padding-top:6px;margin:8px 0 14px">Professional repair</div>
<div class="services">
<div class="card">💻 <div><b>LAPTOP</b><br><span style="font-size:11px">Motherboard</span></div></div>
<div class="card">🖥️ <div><b>DESKTOP</b><br><span style="font-size:11px">RAM, GPU</span></div></div>
<div class="card">🖨️ <div><b>PRINTER</b><br><span style="font-size:11px">Paper Jam</span></div></div>
<div class="card">📱 <div><b>MOBILE</b><br><span style="font-size:11px">Screen</span></div></div>
</div></div>
<div class="login"><h3>🔒 LOGIN</h3><input placeholder="Username" style="margin-top:10px"><input type="password" placeholder="Password"><button class="btn">Login</button></div>
</div>
<div class="study"><div style="margin-bottom:12px"><b>Study Material</b> <span style="font-size:11px;color:#8aa0c6">- Mobile pe TAP karo ✨</span></div>
<div class="grid4">
<div class="sbox"><div class="thumb">📄</div><b>Schematics</b><p>Diagrams</p></div>
<div class="sbox"><div class="thumb" style="color:#00ff9d">🔍</div><b>Board Views</b><p>PCB views</p></div>
<div class="sbox"><div class="thumb">📘</div><b>Guides</b><p>Step-by-step</p></div>
<div class="sbox"><div class="thumb">📚</div><b>eBooks</b><p>PDFs</p></div>
</div></div>
<footer>© 2026 SHREE VINAYAK IT CARE • Mobile Tap + Rotate Fixed</footer>
</div>

<script>
// Mobile TAP = Hover Effect
document.querySelectorAll('.sbox').forEach(box=>{
  box.addEventListener('touchstart', function(){
    document.querySelectorAll('.sbox').forEach(b=>b.classList.remove('touch-active'));
    this.classList.add('touch-active');
  }, {passive:true});
  box.addEventListener('touchend', function(){
    setTimeout(()=>{ this.classList.remove('touch-active') }, 800);
  });
});
// Fix rotation alignment
window.addEventListener('orientationchange', function(){
  setTimeout(()=>{ window.scrollTo(0,0); document.body.style.height = window.innerHeight+'px'; }, 200);
});
</script>
</body></html>
"""
@app.route('/')
def home(): return render_template_string(HTML)
@app.route('/<path:p>')
def any_page(p): return render_template_string(HTML)
if __name__=='__main__': app.run(host='0.0.0.0',port=5000,debug=True)
