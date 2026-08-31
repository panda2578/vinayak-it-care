from flask import Flask, render_template_string
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>SHREE VINAYAK IT CARE</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{font-family:'Inter',sans-serif;background:#050c1a;color:#e6efff;overflow-x:hidden}
body::before{content:"";position:fixed;inset:-30%;background:conic-gradient(from 0deg,#ff7a0010,#00d4ff0f,#ff7a0010);animation:rot 25s linear infinite;z-index:-1;filter:blur(50px)}
@keyframes rot{to{transform:rotate(360deg)}}
.container{max-width:1300px;margin:0 auto;padding:12px}
.header{display:flex;justify-content:space-between;gap:12px;background:linear-gradient(90deg,#0a162d 60%,#0a1e3a);border:1px solid #1a2f54;border-radius:16px;padding:14px 18px;position:relative;overflow:hidden}
.header::after{content:"";position:absolute;right:0;top:0;width:45%;height:100%;background:url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600') center/cover;opacity:0.25;mask-image:linear-gradient(to left, black 60%, transparent)}
.logo{display:flex;gap:12px;align-items:center;z-index:1}
.logo-icon{width:62px;height:62px;border-radius:50%;background:radial-gradient(#1a2f5a,#0a1120);border:2px solid #ff7a00;display:grid;place-items:center;font-size:34px}
.brand h1{font-size:26px;font-weight:900;line-height:1.1}.brand h1 span{color:#ff7a00}
.brand p{font-size:13px;color:#cbd6ea;margin-top:2px}.brand small{font-size:12px;color:#ffcc00}
.info-bar{display:flex;gap:18px;flex-wrap:wrap;margin-top:10px;font-size:11px;color:#9fb0cc;z-index:1}
.info-bar a{color:#9fb0cc;text-decoration:none}
.main-grid{display:grid;grid-template-columns:1fr 340px;gap:14px;margin-top:14px}
.welcome{text-align:center;padding:12px 10px 6px}
.welcome h2{font-size:28px;letter-spacing:2px}.welcome h3{font-size:12px;opacity:.6}.welcome h1{font-size:26px;color:#ff7a00;margin:4px 0}
.welcome p{font-size:12px;color:#8aa0c6;max-width:600px;margin:8px auto;line-height:1.6}
.catalogue-title{text-align:center;margin:14px 0 10px;font-size:14px;letter-spacing:3px;color:#c7d6ee;position:relative}
.catalogue-title::before,.catalogue-title::after{content:"";position:absolute;top:50%;width:80px;height:1px;background:linear-gradient(90deg,transparent,#00a6ff)}.catalogue-title::before{left:calc(50% - 180px)}.catalogue-title::after{right:calc(50% - 180px)}
.repair-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.repair-card{border-radius:16px;padding:14px;position:relative;overflow:hidden;min-height:175px;border:1px solid rgba(255,255,255,0.1);cursor:pointer;transition:all .4s cubic-bezier(.175,.885,.32,1.275)}
.repair-card:hover,.repair-card:active,.repair-card.m-active{transform:translateY(-6px) scale(1.02);box-shadow:0 18px 40px rgba(0,0,0,.6),0 0 25px var(--glow);border-color:var(--glow);z-index:2}
.repair-card .icon{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;font-size:20px;margin-bottom:8px;border:1px solid rgba(255,255,255,.2)}
.repair-card h3{font-size:14px;margin-top:50px}.repair-card p{font-size:11px;color:#c5d2e6;opacity:.85;margin-top:3px;line-height:1.4}
.repair-card .explore{position:absolute;right:10px;bottom:10px;border:1px solid currentColor;border-radius:20px;padding:4px 12px;font-size:11px;background:rgba(0,0,0,.4)}
.repair-card img{position:absolute;right:6px;top:10px;width:52%;height:68%;object-fit:contain;filter:drop-shadow(0 8px 15px rgba(0,0,0,.7));transition:.4s}
.repair-card:hover img{transform:scale(1.12) rotate(2deg)}
.c1{background:linear-gradient(135deg,#0f2a5a 0%,#0a1933 100%);--glow:#3b82f6}.c1 .icon{background:#1e4db7}
.c2{background:linear-gradient(135deg,#0f4a35 0%,#0a241b 100%);--glow:#22c55e}.c2 .icon{background:#15803d}
.c3{background:linear-gradient(135deg,#2e1a5a 0%,#1a102f 100%);--glow:#a855f7}.c3 .icon{background:#7e22ce}
.c4{background:linear-gradient(135deg,#7a2e0a 0%,#3d1605 100%);--glow:#f973
