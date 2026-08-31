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

/* ===== HEADER - EXTRA SMALL NOW ===== */
.header{border:1px solid #1d4f84;border-radius:14px;overflow:hidden;background:linear-gradient(90deg,#071126,#07152e,#061124);position:relative;}
.header-top{min-height:72px;display:flex;align-items:center;padding:6px 18px;position:relative;overflow:hidden;}
.header-top::after{content:"";position:absolute;right:0;top:0;width:38%;height:70%;top:15%;border-radius:0 0 0 12px;background:linear-gradient(90deg,#07152e 10%,rgba(7,21,46,.3) 40%,rgba(0,0,0,.15)),url("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=50");background-size:cover;background-position:center;opacity:.38;z-index:0;}
.brand-area{display:flex;align-items:center;gap:10px;position:relative;z-index:2;}
.logo{width:48px;height:48px;min-width:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:26px;color:#ff9a00;border:1.5px solid #ff9700;background:radial-gradient(circle,#17284d,#050c1c 70%);box-shadow:0 0 6px #ff8500,0 0 12px rgba(255,130,0,.3);}
.brand h1{font-size:18px;line-height:.9;letter-spacing:1px;font-weight:900;color:#f4f6fb;}
.brand h1 span{display:block;color:#ff8500;font-size:16px;}
.brand p{margin-top:2px;font-size:9px;color:#c7d0df;}
.brand small{display:block;margin-top:1px;color:#ffb000;font-size:8px;font-weight:700;letter-spacing:.8px;}

.info-bar{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid #1d4f84;background:rgba(2,9,22,.88);}
.info-item{min-height:36px;display:flex;align-items:center;gap:7px;padding:4px 12px;border-right:1px solid #255486;}
.info-item:last-child{border-right:none;}
.info-icon{font-size:16px;color:#ffb000;}
.info-text b{display:block;font-size:10px;margin-bottom:1px;color:#fff;}
.info-text span{color:#aebbd0;font-size:8px;}

.main-layout{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:12px;margin-top:10px;}
.left-panel{border:1px solid #174878;border-radius:18px;padding:10px;background:linear-gradient(180deg,#061126,#030a17);}

.welcome{text-align:center;padding:12px 10px 10px;}
.welcome-text{font-size:19px;font-weight:800;letter-spacing:6px;color:#dfe7f4;}
.to{font-size:8px;letter-spacing:4px;margin-top:1px;color:#a7b5c8;}
.welcome h2{margin-top:3px;font-size:22px;color:#ff8500;letter-spacing:1px;font-weight:900;}
.orange-line{width:90px;height:2px;margin:7px auto;background:linear-gradient(90deg,transparent,#ff8500,transparent);position:relative;}
.orange-line::after{content:"◇";position:absolute;top:-10px;left:50%;transform:translateX(-50%);color:#ff9a00;background:#071126;padding:0 6px;font-size:16px;}
.welcome p{max-width:680px;margin:auto;line-height:1.4
