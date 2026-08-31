from flask import Flask, render_template_string, request

app = Flask(__name__)
chat_messages = []
USERS = {"admin": "admin123", "vinayak": "7008541544"}

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>SHREE VINAYAK IT CARE</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
html{scroll-behavior:smooth;}
body{font-family:'Inter',sans-serif;background:radial-gradient(circle at 20% 10%,rgba(20,70,150,.18),transparent 30%),radial-gradient(circle at 80% 80%,rgba(255,120,0,.08),transparent 25%),#020814;color:#eaf1ff;min-height:100vh;overflow-x:hidden;}
a{text-decoration:none;color:inherit;}
.container{width:100%;max-width:1500px;margin:auto;padding:10px;}

/* =====================================================
   DESKTOP HEADER - SAME AS BEFORE
===================================================== */
.header{border:1px solid #1d4f84;border-radius:18px;overflow:hidden;background:linear-gradient(90deg,#071126,#07152e,#061124);position:relative;}
.header-top{min-height:115px;display:flex;align-items:center;padding:12px 25px;position:relative;overflow:hidden;}
.header-top::after{content:"";position:absolute;right:0;top:0;width:58%;height:100%;background:linear-gradient(90deg,#07152e 0%,rgba(7,21,46,.25) 35%,rgba(0,0,0,.25)),url("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1400&q=80");background-size:cover;background-position:center;opacity:.75;z-index:0;}
.brand-area{display:flex;align-items:center;gap:15px;position:relative;z-index:2;}
.logo{width:82px;height:82px;min-width:82px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:48px;color:#ff9a00;border:2px solid #ff9700;background:radial-gradient(circle,#17284d,#050c1c 70%);box-shadow:0 0 10px #ff8500,0 0 25px rgba(255,130,0,.45);}
.brand h1{font-size:30px;line-height:1;letter-spacing:1.5px;font-weight:900;color:#f4f6fb;}
.brand h1 span{display:block;color:#ff8500;}
.brand p{margin-top:6px;font-size:13px;color:#c7d0df;}
.brand small{display:block;margin-top:4px;color:#ffb000;font-size:11px;font-weight:700;letter-spacing:1px;}

.info-bar{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid #1d4f84;background:rgba(2,9,22,.88);}
.info-item{min-height:60px;display:flex;align-items:center;gap:10px;padding:9px 18px;border-right:1px solid #255486;}
.info-item:last-child{border-right:none;}
.info-icon{font-size:24px;color:#ffb000;}
.info-text b{display:block;font-size:13px;margin-bottom:3px;color:#ffffff;}
.info-text span{color:#aebbd0;font-size:11px;}

.main-layout{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:12px;margin-top:10px;}
.left-panel{border:1px solid #174878;border-radius:18px;padding:10px;background:linear-gradient(180deg,#061126,#030a17);}

.welcome{text-align:center;padding:14px 10px 10px;}
.welcome-text{font-size:23px;font-weight:800;letter-spacing:8px;color:#dfe7f4;}
.to{font-size:10px;letter-spacing:4px;margin-top:2px;color:#a7b5c8;}
.welcome h2{margin-top:4px;font-size:27px;color:#ff8500;letter-spacing:1px;font-weight:900;}
.orange-line{width:100px;height:2px;margin:9px auto;background:linear-gradient(90deg,transparent,#ff8500,transparent);position:relative;}
.orange-line::after{content:"◇";position:absolute;top:-11px;left:50%;transform:translateX(-50%);color:#ff9a00;background:#071126;padding:0 6px;font-size:20px;}
.welcome p{max-width:680px;margin:auto;line-height:1.45;font-size:12px;color:#c4cede;}
.welcome p span{color:#ff9a00;font-weight:800;}

.section-title{display:flex;align-items:center;justify-content:center;gap:15px;margin:10px 0;color:#c9d3e3;font-size:12px;font-weight:700;letter-spacing:6px;}
.section-title::before,.section-title::after{content:"";height:1px;flex:1;max-width:260px;background:linear-gradient(90deg,transparent,#2687d8);}
.section-title::after{background:linear-gradient(90deg,#2687d8,transparent);}

/* REPAIR GRID - DESKTOP NORMAL */
.repair-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;}
.repair-card{position:relative;min-height:145px;padding:11px;border-radius:12px;overflow:hidden;cursor:pointer;transition:transform .3s ease,box-shadow .3s ease;border:1px solid var(--card-border);background:linear-gradient(135deg,var(--card-bg1),var(--card-bg2));}
.repair-card:hover{transform:translateY(-5px) scale(1.015);box-shadow:0 12px 30px rgba(0,0,0,.55),0 0 20px var(--card-glow);}
.card-icon{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:20px;border:1px solid var(--card-border);background:rgba(0,0,0,.25);}
.card-device{position:absolute;right:10px;top:12px;font-size:46px;filter:drop-shadow(0 8px 8px rgba(0,0,0,.7));transition:transform .3s ease;}
.repair-card:hover .card-device{transform:scale(1.12) rotate(4deg);}
.repair-card h3{margin-top:14px;font-size:13px;font-weight:800;}
.repair-card p{margin-top:5px;font-size:10px;line-height:1.35;color:#d0d9e7;}
.explore-btn{display:inline-block;margin-top:7px;padding:4px 14px;border-radius:6px;font-size:10px;border:1px solid var(--card-border);background:rgba(0,0,0,.3);}

.blue{--card-bg1:#0d2a4f;--card-bg2:#061527;--card-border:#2786d6;--card-glow:rgba(30,130,255,.4);}
.green{--card-bg1:#103c29;--card-bg2:#061d14;--card-border:#27bb68;--card-glow:rgba(30,220,100,.35);}
.purple{--card-bg1:#311548;--card-bg2:#160a27;--card-border:#c24ae8;--card-glow:rgba(190,50,255,.35);}
.orange{--card-bg1:#512205;--card-bg2:#291003;--card-border:#ff8700;--card-glow:rgba(255,120,0,.4);}
.teal{--card-bg1:#07363d;--card-bg2:#041c22;--card-border:#17b9ca;--card-glow:rgba(0,200,220,.35);}
.yellow{--card-bg1:#4c3c02;--card-bg2:#251d00;--card-border:#e6c400;--card-glow:rgba(255,220,0,.35);}

.login-panel{border:1px solid #2a588a;border-radius:18px;padding:20px;background:linear-gradient(180deg,#0a1931,#071123);height:fit-content;position:sticky;top:10px;}
.login-title{text-align:center;font-size:17px;font-weight:800;letter-spacing:2px;margin-bottom:15px;}
.input-box{position:relative;margin-top:10px;}
.input-box span{position:absolute;left:12px;top:50%;transform:translateY(-50%);font-size:15px;}
.input-box input{width:100%;padding:12px 12px 12px 42px;border-radius:8px;border:1px solid #526176;background:#0a1425;color:white;font-size:13px;outline:none;}
.login-options{display:flex;justify-content:space-between;margin-top:10px;font-size:11px;color:#d6deea;}
.login-options a{color:#ffae32;}
.login-button{width:100%;border:none;margin-top:15px;padding:12px;border-radius:8px;cursor:pointer;font-size:16px;font-weight:800;color:white;background:linear-gradient(90deg,#ff6a00,#ff9800,#ff4e00);}

.study-section{margin-top:10px;display:grid;grid-template-columns:1.5fr repeat(4,1fr);gap:8px;}
.study-info{padding:10px;text-align:center;border-radius:10px;border:1px solid #235687;background:linear-gradient(135deg,#0a1b33,#06101f);}
.study-info h3{font-size:16px;}
.study-info .sub{margin-top:3px;color:#53b5ff;font-size:11px;}
.study-info p{margin:7px auto;max-width:290px;font-size:10px;line-height:1.4;color:#c0cbdb;}
.study-btn{display:inline-block;padding:6px 15px;border:1px solid #5dafff;border-radius:6px;font-size:10px;font-weight:700;}
.study-card{min-height:115px;padding:6px;border-radius:10px;text-align:center;border:1px solid #245789;background:linear-gradient(135deg,#0a1c34,#06101e);transition:.3s;}
.study-card:hover{transform:translateY(-4px);box-shadow:0 0 18px rgba(0,130,255,.25);}
.study-image{height:65px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:36px;background:#0c1627;}
.study-card h4{margin-top:6px;font-size:11px;color:#d9e2ef;}

.features{margin-top:10px;display:grid;grid-template-columns:repeat(5,1fr);border:1px solid #1f5486;border-radius:12px;overflow:hidden;background:#061224;}
.feature{padding:10px 8px;display:flex;align-items:center;justify-content:center;gap:6px;border-right:1px solid #2a5888;color:#d7dfeb;font-size:11px;text-align:center;}
.feature:last-child{border:none;}
.feature span{color:#ffb000;font-size:17px;}
.footer{text-align:center;margin-top:5px;padding:10px;color:#aeb9ca;font-size:11px;border:1px solid #174878;border-radius:0 0 15px 15px;background:#06101f;}

.floating-contact{position:fixed;right:20px;bottom:25px;z-index:9999;display:flex;flex-direction:column;gap:12px;}
.float-btn{width:54px;height:54px;border-radius:50%;display:flex;align-items:center;justify-content:center;position:relative;font-size:23px;color:#ffffff;border:2px solid rgba(255,255,255,.25);box-shadow:0 8px 22px rgba(0,0,0,.55);transition:transform .25s ease,box-shadow .25s ease;animation:floatingPulse 2.5s infinite;}
.float-btn::before{content:"";position:absolute;width:100%;height:100%;border-radius:50%;border:2px solid currentColor;opacity:.45;animation:ripple 2.2s infinite;}
.float-btn i{position:relative;z-index:2;transition:transform .25s ease;}
.float-btn:hover{transform:translateY(-5px) scale(1.12);box-shadow:0 15px 35px rgba(0,0,0,.75);}
.float-btn:hover i{transform:rotate(12deg) scale(1.1);}
.float-whatsapp{background:linear-gradient(135deg,#25d366,#128c4a);}
.float-call{background:linear-gradient(135deg,#2d9cff,#0055b8);}
.float-chat{background:linear-gradient(135deg,#ff9a00,#ff4d00);}
.float-btn::after{position:absolute;right:66px;padding:6px 11px;border-radius:6px;background:#071426;color:#ffffff;font-size:11px;font-weight:700;white-space:nowrap;opacity:0;transform:translateX(10px);pointer-events:none;transition:.25s;border:1px solid rgba(255,255,255,.15);}
.float-btn:hover::after{opacity:1;transform:translateX(0);}
.float-chat::after{content:"MESSAGE CHAT";}.float-call::after{content:"CALL NOW";}.float-whatsapp::after{content:"WHATSAPP";}
@keyframes floatingPulse{0%{transform:scale(1);}50%{transform:scale(1.05);}100%{transform:scale(1);}}
@keyframes ripple{0%{transform:scale(1);opacity:.5;}100%{transform:scale(1.5);opacity:0;}}

/* TABLET */
@media(max-width:1150px){.main-layout{grid-template-columns:1fr 320px;}.repair-grid{grid-template-columns:repeat(2,1fr);}.study-section{grid-template-columns:repeat(4,1fr);}.study-info{grid-column:span 4;}.features{grid-template-columns:repeat(3,1fr);}}
@media(max-width:850px){.main-layout{grid-template-columns:1fr;}.login-panel{position:relative;top:auto;}}

/* =====================================================
   ONLY MOBILE VERSION - HEADER SMALL + BG SMALL + CARD ANIMATION
===================================================== */
@media(max-width:600px){
    body{padding-bottom:80px;}
    .container{padding:0;}

    /* HEADER - AB HIDE NAHI HOGA, CHOTA HOGA */
    .header{display:block;border-radius:0 0 14px 14px;border:none;border-bottom:1px solid #1d4f84;margin-bottom:7px;}
    .header-top{min-height:58px;padding:6px 12px;}
    .header-top::after{width:32%;opacity:.32;background:linear-gradient(90deg,#07152e 0%,rgba(7,21,46,.35) 35%,rgba(0,0,0,.1)),url("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=500&q=50");background-size:cover;background-position:center;}
    .logo{width:42px;height:42px;min-width:42px;font-size:24px;border-width:1.5px;box-shadow:0 0 6px #ff8500;}
    .brand h1{font-size:14px;letter-spacing:.8px;}
    .brand h1 span{font-size:12px;}
    .brand p{font-size:8.5px;margin-top:2px;}
    .brand small{font-size:7px;margin-top:1px;letter-spacing:.5px;}
    
    .info-bar{grid-template-columns:repeat(2,1fr);}
    .info-item{min-height:34px;padding:5px 10px;border-bottom:1px solid #255486;}
    .info-item:nth-child(2){border-right:none;}
    .info-item:nth-child(3){border-right:1px solid #255486;}
    .info-item:nth-child(4){border-right:none;border-bottom:none;}
    .info-item:nth-child(3){border-bottom:none;}
    .info-icon{font-size:14px;}
    .info-text b{font-size:9px;margin-bottom:0;}
    .info-text span{font-size:7.5px;}

    .main-layout{margin-top:0;}
    .left-panel{border:none;border-radius:0;padding:7px;background:#030a17;}

    /* WELCOME - BACKGROUND IMAGE SMALL */
    .welcome{min-height:165px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:18px 12px 14px;border-radius:12px;overflow:hidden;background:linear-gradient(180deg,rgba(2,8,20,.9),rgba(2,8,20,.75)),url("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=50");background-size:cover;background-position:center 35%;box-shadow:inset 0 0 50px rgba(0,0,0,.7);}
    .welcome-text{font-size:14px;letter-spacing:3px;text-shadow:0 2px 8px #000;}
    .to{font-size:8px;letter-spacing:2px;}
    .welcome h2{font-size:17px;margin-top:3px;text-shadow:0 2px 10px #000;}
    .orange-line{width:70px;margin:6px auto;height:1.5px;}
    .orange-line::after{font-size:14px;top:-8px;background:rgba(3,10,20,.85);}
    .welcome p{font-size:9px;line-height:1.35;max-width:280px;text-shadow:0 1px 6px #000;}

    .section-title{margin:10px 0 8px;font-size:8.5px;letter-spacing:2.5px;gap:6px;}

    /* MOBILE CARD - HOVER + FLOAT ANIMATION */
    .repair-grid{grid-template-columns:repeat(2,1fr);gap:8px;}
    .repair-card{min-height:122px;padding:9px;border-radius:11px;animation:mobile
