from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SHREE VINAYAK IT CARE - Professional Repair Services</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{
  font-family:'Inter', sans-serif;
  color:#eaf0ff;
  background: radial-gradient(1200px 600px at 10% -10%, #ff7a0022, transparent),
              radial-gradient(1000px 500px at 90% 10%, #0066ff22, transparent),
              linear-gradient(180deg, #070f1f 0%, #0a162d 50%, #08111e 100%);
  min-height:100vh; overflow-x:hidden;
}
body::before{
  content:""; position:fixed; inset:-50%;
  background: conic-gradient(from 0deg, #ff7a0011, #00d4ff11, #ff7a0011);
  animation: rotateBg 20s linear infinite;
  z-index:-1; filter:blur(40px);
}
@keyframes rotateBg{ to{transform:rotate(360deg)} }

.container{max-width:1280px;margin:0 auto;padding:12px}

.topbar{
  display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;
  border:1.5px solid #ff7a00; border-radius:14px; padding:12px 18px;
  background: rgba(16,29,51,0.85); backdrop-filter: blur(10px);
}
.brand{font-weight:900; font-size:18px; letter-spacing:0.5px}
.brand span{color:#ff7a00}
.contact{font-size:11px; opacity:0.85; display:flex; gap:15px; flex-wrap:wrap}

.main{
  display:grid; grid-template-columns: 1.8fr 0.9fr; gap:16px; margin-top:16px;
}
.left h2{font-size:24px; font-weight:800}
.subline{
  margin:8px 0 16px; font-size:12px; color:#8aa0c6;
  border-top:2px solid #ff7a00; display:inline-block; padding-top:6px;
}
.services{
  display:grid; grid-template-columns: repeat(2, 1fr); gap:14px;
}
.card{
  background: rgba(16,29,51,0.9); border:1px solid #23365e; border-radius:14px;
  padding:16px; display:flex; gap:12px; align-items:center;
  transition: all 0.3s ease; cursor:pointer;
}
.card:hover{border-color:#ff7a00; transform: translateY(-3px); box-shadow: 0 8px 25px #ff7a0033}
.icon{
  min-width:56px; height:56px; border-radius:12px; display:grid; place-items:center;
  background: linear-gradient(135deg, #0f2240, #122a50); font-size:26px; border:1px solid #1e3a64
}
.card h3{font-size:13px; font-weight:800; letter-spacing:0.3px}
.card p{font-size:11px; color:#8aa0c6; margin-top:3px}

.login{
  background: rgba(16,29,51,0.95); border:1.6px solid #ff7a00; border-radius:16px; padding:20px;
  height:fit-content; position:sticky; top:16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
.login h3{font-size:18px; margin-bottom:2px}
.login small{font-size:12px; color:#8aa0c6}
.login label{font-size:11px; margin-top:14px; display:block; color:#a8bddb}
.login input{
  width:100%; padding:12px 12px; margin-top:6px; border-radius:10px;
  border:1px solid #2a3e62; background:#0b1930; color:#fff; outline:none;
}
.login input:focus{border-color:#ff7a00}
.row{ display:flex; justify-content:space-between; align-items:center; margin:12px 0; font-size:11px}
.btn{
  width:100%; padding:13px; border:none; border-radius:10px;
  background: linear-gradient(90deg, #ff6a00, #ff9a00); color:#fff;
  font-weight:800; font-size:15px; cursor:pointer;
}
.btn:hover{filter:brightness(1.1)}

.study{
  margin-top:18px; border:1.5px solid #ff7a00; border-radius:16px;
  padding:18px; background: rgba(16,29,51,0.7); backdrop-filter: blur(8px);
}
.study-head{display:flex; gap:12px; align-items:center; flex-wrap:wrap; margin-bottom:14px}
.study-head b{font-size:16px}
.study-head span{font-size:11px; color:#8aa0c6}
.grid4{display:grid; grid-template-columns: repeat(4, 1fr); gap:14px}

/* ===== THUMBNAIL HOVER EFFECT - PREMIUM ===== */
.sbox{
  background:#101d33; border:1px solid #22365e; border-radius:14px; padding:14px; text-align:center;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
  cursor:pointer; overflow:hidden; position:relative;
}
.sbox::after{
  content:""; position:absolute; top:0; left:-100%; width:100%; height:100%;
  background: linear-gradient(90deg, transparent, rgba(255,122,0,0.15), transparent);
  transition: 0.6s;
}
.sbox:hover::after{left:100%}
.sbox:hover{
  border-color:#ff7a00;
  transform:translateY(-8px) scale(1.03);
  box-shadow: 0 15px 35px rgba(255,122,0,0.3), 0 0 20px rgba(255,122,0,0.15) inset;
  background:#132241;
}
.thumb{
  height:75px; border-radius:12px; background:#0c1a2f; display:grid; place-items:center;
  font-size:30px; margin-bottom:12px; border:1px solid #1a2f54;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.sbox:hover .thumb{
  transform: scale(1.2) rotate(5deg);
  background: linear-gradient(135deg,#162e5a,#1e3c6e);
  border-color:#ff7a00;
  box-shadow: 0 0 25px rgba(255,122,0,0.5);
  font-size:36px;
}
.sbox b{font-size:12.5px
