from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0, maximum-scale=1.0">

<title>SHREE VINAYAK IT CARE</title>

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap"
rel="stylesheet">

<style>

/* =====================================================
   GLOBAL
===================================================== */

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

html{
    scroll-behavior:smooth;
}

body{
    font-family:'Inter',sans-serif;

    background:
        radial-gradient(circle at 20% 10%,rgba(20,70,150,.18),transparent 30%),
        radial-gradient(circle at 80% 80%,rgba(255,120,0,.08),transparent 25%),
        #020814;

    color:#eaf1ff;
    min-height:100vh;
}

a{
    text-decoration:none;
    color:inherit;
}

.container{
    width:100%;
    max-width:1500px;
    margin:auto;
    padding:10px;
}


/* =====================================================
   MAIN BORDER CARD
===================================================== */

.main-border{
    border:1px solid #16477a;
    border-radius:18px;

    background:
        linear-gradient(
            180deg,
            rgba(5,16,36,.95),
            rgba(2,9,20,.98)
        );

    box-shadow:
        0 0 35px rgba(0,100,255,.08),
        inset 0 0 30px rgba(0,80,180,.04);
}


/* =====================================================
   HEADER
===================================================== */

.header{

    border:1px solid #1d4f84;
    border-radius:18px;

    overflow:hidden;

    background:
        linear-gradient(
            90deg,
            #071126 0%,
            #07152e 50%,
            #061124 100%
        );

    position:relative;
}

.header-top{

    min-height:145px;

    display:flex;

    align-items:center;

    padding:15px 30px;

    position:relative;

    overflow:hidden;
}


/* CIRCUIT BACKGROUND */

.header-top:after{

    content:"";

    position:absolute;

    right:0;
    top:0;

    width:58%;
    height:100%;

    background:
        linear-gradient(
            90deg,
            #07152e 0%,
            rgba(7,21,46,.15) 35%,
            rgba(0,0,0,.1)
        ),
        url("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1400&q=80");

    background-size:cover;
    background-position:center;

    opacity:.65;

    z-index:0;
}


/* LOGO AREA */

.brand-area{

    display:flex;

    align-items:center;

    gap:18px;

    position:relative;

    z-index:2;
}


.logo{

    width:105px;
    height:105px;

    min-width:105px;

    border-radius:50%;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:62px;

    color:#ff9a00;

    border:3px solid #ff9700;

    background:
        radial-gradient(
            circle,
            #17284d,
            #050c1c 70%
        );

    box-shadow:
        0 0 12px #ff8500,
        0 0 30px rgba(255,130,0,.5);
}


.brand h1{

    font-size:37px;

    line-height:.95;

    letter-spacing:2px;

    font-weight:900;

    color:#f4f6fb;
}

.brand h1 span{

    display:block;

    color:#ff8500;
}

.brand p{

    margin-top:8px;

    font-size:16px;

    color:#c7d0df;
}

.brand small{

    display:block;

    margin-top:5px;

    color:#ffb000;

    font-weight:700;

    letter-spacing:1px;
}


/* =====================================================
   HEADER INFO
===================================================== */

.info-bar{

    display:grid;

    grid-template-columns:
        repeat(4,1fr);

    border-top:
        1px solid #1d4f84;

    position:relative;

    z-index:3;

    background:
        rgba(2,9,22,.86);
}


.info-item{

    min-height:72px;

    display:flex;

    align-items:center;

    gap:15px;

    padding:12px 25px;

    border-right:
        1px solid #255486;
}


.info-item:last-child{

    border-right:none;
}


.info-icon{

    font-size:31px;

    color:#ffb000;
}


.info-text b{

    display:block;

    font-size:16px;

    margin-bottom:4px;

    color:#ffffff;
}

.info-text span{

    color:#aebbd0;

    font-size:13px;
}


/* =====================================================
   MAIN GRID
===================================================== */

.main-layout{

    display:grid;

    grid-template-columns:
        minmax(0,1fr) 420px;

    gap:14px;

    margin-top:8px;
}


/* =====================================================
   LEFT AREA
===================================================== */

.left-panel{

    border:
        1px solid #174878;

    border-radius:18px;

    padding:12px;

    background:
        linear-gradient(
            180deg,
            #061126,
            #030a17
        );
}


/* =====================================================
   WELCOME
===================================================== */

.welcome{

    text-align:center;

    padding:
        18px 10px 12px;
}


.welcome .welcome-text{

    font-size:28px;

    font-weight:800;

    letter-spacing:10px;

    color:#dfe7f4;
}


.welcome .to{

    font-size:12px;

    letter-spacing:5px;

    margin-top:2px;

    color:#a7b5c8;
}


.welcome h2{

    margin-top:5px;

    font-size:34px;

    color:#ff8500;

    letter-spacing:2px;

    font-weight:900;
}


.orange-line{

    width:120px;

    height:3px;

    margin:12px auto;

    background:
        linear-gradient(
            90deg,
            transparent,
            #ff8500,
            transparent
        );

    position:relative;
}


.orange-line:after{

    content:"◇";

    position:absolute;

    top:-13px;

    left:50%;

    transform:translateX(-50%);

    color:#ff9a00;

    background:#071126;

    padding:0 8px;

    font-size:26px;
}


.welcome p{

    max-width:720px;

    margin:auto;

    line-height:1.5;

    font-size:15px;

    color:#c4cede;
}

.welcome p span{

    color:#ff9a00;

    font-weight:800;
}


/* =====================================================
   SECTION TITLE
===================================================== */

.section-title{

    display:flex;

    align-items:center;

    justify-content:center;

    gap:20px;

    margin:
        12px 0 14px;

    color:#c9d3e3;

    font-size:15px;

    font-weight:700;

    letter-spacing:10px;
}


.section-title:before,
.section-title:after{

    content:"";

    height:2px;

    flex:1;

    max-width:300px;

    background:
        linear-gradient(
            90deg,
            transparent,
            #2687d8
        );
}


.section-title:after{

    background:
        linear-gradient(
            90deg,
            #2687d8,
            transparent
        );
}


/* =====================================================
   REPAIR GRID
===================================================== */

.repair-grid{

    display:grid;

    grid-template-columns:
        repeat(3,1fr);

    gap:12px;
}


/* =====================================================
   REPAIR CARD
===================================================== */

.repair-card{

    position:relative;

    min-height:150px;

    padding:14px;

    border-radius:13px;

    overflow:hidden;

    cursor:pointer;

    transition:
        transform .3s ease,
        box-shadow .3s ease;

    border:
        1px solid var(--card-border);

    background:
        linear-gradient(
            135deg,
            var(--card-bg1),
            var(--card-bg2)
        );
}


.repair-card:hover{

    transform:
        translateY(-6px)
        scale(1.015);

    box-shadow:
        0 14px 35px rgba(0,0,0,.55),
        0 0 22px var(--card-glow);
}


/* ICON */

.card-icon{

    width:48px;
    height:48px;

    border-radius:50%;

    display:flex;

    align-items:center;
    justify-content:center;

    font-size:24px;

    border:
        1px solid var(--card-border);

    background:
        rgba(0,0,0,.25);
}


/* PRODUCT IMAGE */

.card-device{

    position:absolute;

    right:15px;

    top:18px;

    font-size:58px;

    filter:
        drop-shadow(
            0 10px 10px rgba(0,0,0,.7)
        );

    transition:
        transform .3s ease;
}


.repair-card:hover
.card-device{

    transform:
        scale(1.15)
        rotate(4deg);
}


.repair-card h3{

    margin-top:22px;

    font-size:16px;

    font-weight:800;
}


.repair-card p{

    margin-top:7px;

    font-size:13px;

    line-height:1.45;

    color:#d0d9e7;
}


.explore-btn{

    display:inline-block;

    margin-top:10px;

    padding:
        6px 22px;

    border-radius:7px;

    font-size:13px;

    border:
        1px solid var(--card-border);

    background:
        rgba(0,0,0,.3);

    transition:.25s;
}


.repair-card:hover
.explore-btn{

    background:
        rgba(255,255,255,.1);
}


/* CARD COLORS */

.blue{
    --card-bg1:#0d2a4f;
    --card-bg2:#061527;
    --card-border:#2786d6;
    --card-glow:rgba(30,130,255,.4);
}

.green{
    --card-bg1:#103c29;
    --card-bg2:#061d14;
    --card-border:#27bb68;
    --card-glow:rgba(30,220,100,.35);
}

.purple{
    --card-bg1:#311548;
    --card-bg2:#160a27;
    --card-border:#c24ae8;
    --card-glow:rgba(190,50,255,.35);
}

.orange{
    --card-bg1:#512205;
    --card-bg2:#291003;
    --card-border:#ff8700;
    --card-glow:rgba(255,120,0,.4);
}

.teal{
    --card-bg1:#07363d;
    --card-bg2:#041c22;
    --card-border:#17b9ca;
    --card-glow:rgba(0,200,220,.35);
}

.yellow{
    --card-bg1:#4c3c02;
    --card-bg2:#251d00;
    --card-border:#e6c400;
    --card-glow:rgba(255,220,0,.35);
}


/* =====================================================
   LOGIN PANEL
===================================================== */

.login-panel{

    border:
        1px solid #2a588a;

    border-radius:18px;

    padding:26px;

    background:
        linear-gradient(
            180deg,
            #0a1931,
            #071123
        );

    height:fit-content;

    position:sticky;

    top:10px;
}


.login-title{

    text-align:center;

    font-size:20px;

    font-weight:800;

    letter-spacing:2px;

    margin-bottom:20px;
}


.input-box{

    position:relative;

    margin-top:14px;
}


.input-box span{

    position:absolute;

    left:14px;

    top:50%;

    transform:
        translateY(-50%);

    font-size:18px;
}


.input-box input{

    width:100%;

    padding:
        15px 15px 15px 48px;

    border-radius:9px;

    border:
        1px solid #526176;

    background:
        #0a1425;

    color:white;

    font-size:15px;

    outline:none;
}


.login-options{

    display:flex;

    justify-content:space-between;

    margin-top:14px;

    font-size:13px;

    color:#d6deea;
}


.login-options a{

    color:#ffae32;
}


.login-button{

    width:100%;

    border:none;

    margin-top:20px;

    padding:15px;

    border-radius:10px;

    cursor:pointer;

    font-size:21px;

    font-weight:800;

    letter-spacing:1px;

    color:white;

    background:
        linear-gradient(
            90deg,
            #ff6a00,
            #ff9800,
            #ff4e00
        );

    box-shadow:
        0 5px 18px rgba(255,100,0,.25);
}


.new-user{

    text-align:center;

    margin-top:25px;

    color:#d1dae8;

    font-size:15px;
}


.new-user span{

    color:#ffad2e;
}


.whatsapp-btn{

    display:block;

    text-align:center;

    margin-top:25px;

    padding:12px;

    border-radius:10px;

    border:
        1px solid #83d941;

    color:#8ce45d;

    font-size:18px;

    font-weight:800;

    letter-spacing:1px;
}


.call-btn{

    display:block;

    text-align:center;

    margin-top:22px;

    font-size:20px;

    color:#d7deea;
}


/* =====================================================
   STUDY MATERIAL
===================================================== */

.study-section{

    margin-top:12px;

    display:grid;

    grid-template-columns:
        1.5fr repeat(4,1fr);

    gap:12px;
}


.study-info{

    padding:12px;

    text-align:center;

    border-radius:12px;

    border:
        1px solid #235687;

    background:
        linear-gradient(
            135deg,
            #0a1b33,
            #06101f
        );
}


.study-info h3{

    font-size:19px;

    letter-spacing:1px;
}


.study-info .sub{

    margin-top:4px;

    color:#53b5ff;

    font-size:14px;
}


.study-info p{

    margin:10px auto;

    max-width:290px;

    font-size:13px;

    line-height:1.45;

    color:#c0cbdb;
}


.study-btn{

    display:inline-block;

    padding:
        9px 24px;

    border:
        1px solid #5dafff;

    border-radius:7px;

    font-weight:700;
}


/* STUDY CARD */

.study-card{

    min-height:140px;

    padding:8px;

    border-radius:12px;

    text-align:center;

    border:
        1px solid #245789;

    background:
        linear-gradient(
            135deg,
            #0a1c34,
            #06101e
        );

    transition:.3s;
}


.study-card:hover{

    transform:
        translateY(-5px);

    box-shadow:
        0 0 20px rgba(0,130,255,.25);
}


.study-image{

    height:85px;

    border-radius:7px;

    display:flex;

    align-items:center;
    justify-content:center;

    font-size:48px;

    overflow:hidden;

    background:#0c1627;
}


.study-card h4{

    margin-top:9px;

    font-size:14px;

    color:#d9e2ef;
}


/* =====================================================
   FEATURES
===================================================== */

.features{

    margin-top:12px;

    display:grid;

    grid-template-columns:
        repeat(5,1fr);

    border:
        1px solid #1f5486;

    border-radius:14px;

    overflow:hidden;

    background:
        #061224;
}


.feature{

    padding:14px 12px;

    display:flex;

    align-items:center;

    justify-content:center;

    gap:9px;

    border-right:
        1px solid #2a5888;

    color:#d7dfeb;

    font-size:14px;

    text-align:center;
}


.feature:last-child{

    border:none;
}


.feature span{

    color:#ffb000;

    font-size:22px;
}


/* =====================================================
   FOOTER
===================================================== */

.footer{

    text-align:center;

    margin-top:4px;

    padding:15px;

    color:#aeb9ca;

    font-size:14px;

    border:
        1px solid #174878;

    border-radius:0 0 18px 18px;

    background:#06101f;
}


/* =====================================================
   TABLET RESPONSIVE
===================================================== */

@media(max-width:1150px){

    .main-layout{
        grid-template-columns:
            1fr 350px;
    }

    .repair-grid{
        grid-template-columns:
            repeat(2,1fr);
    }

    .study-section{
        grid-template-columns:
            repeat(4,1fr);
    }

    .study-info{
        grid-column:
            span 4;
    }

    .features{
        grid-template-columns:
            repeat(3,1fr);
    }

    .feature:nth-child(3){
        border-right:none;
    }

}


/* =====================================================
   MOBILE / SMALL TABLET
===================================================== */

@media(max-width:850px){

    .main-layout{
        grid-template-columns:
            1fr;
    }

    .login-panel{
        position:relative;
        top:auto;
    }

    .header-top{
        padding:20px;
    }

    .header-top:after{
        opacity:.25;
        width:100%;
    }

    .info-bar{
        grid-template-columns:
            repeat(2,1fr);
    }

    .info-item:nth-child(2){
        border-right:none;
    }

}


/* =====================================================
   MOBILE
===================================================== */

@media(max-width:600px){

    .container{
        padding:5px;
    }

    .brand-area{
        gap:12px;
    }

    .logo{
        width:70px;
        height:70px;
        min-width:70px;

        font-size:40px;
    }

    .brand h1{
        font-size:23px;
        letter-spacing:1px;
    }

    .brand p{
        font-size:11px;
    }

    .brand small{
        font-size:11px;
    }

    .info-bar{
        grid-template-columns:
            1fr;
    }

    .info-item{
        border-right:none;

        border-bottom:
            1px solid #1d4f84;

        padding:10px 15px;
    }

    .info-item:last-child{
        border-bottom:none;
    }

    .welcome .welcome-text{
        font-size:19px;
        letter-spacing:6px;
    }

    .welcome h2{
        font-size:25px;
    }

    .welcome p{
        font-size:13px;
    }

    .section-title{
        font-size:12px;
        letter-spacing:5px;
        gap:8px;
    }

    .repair-grid{
        grid-template-columns:
            1fr;
    }

    .repair-card{
        min-height:145px;
    }

    .study-section{
        grid-template-columns:
            repeat(2,1fr);
    }

    .study-info{
        grid-column:
            span 2;
    }

    .features{
        grid-template-columns:
            1fr;
    }

    .feature{
        border-right:none;

        border-bottom:
            1px solid #2a5888;
    }

    .feature:last-child{
        border-bottom:none;
    }

    .login-panel{
        padding:20px 15px;
    }

}


/* =====================================================
   VERY SMALL MOBILE
===================================================== */

@media(max-width:380px){

    .brand h1{
        font-size:19px;
    }

    .brand p{
        font-size:10px;
    }

    .logo{
        width:60px;
        height:60px;
        min-width:60px;

        font-size:34px;
    }

    .study-section{
        grid-template-columns:
            1fr;
    }

    .study-info{
        grid-column:
            span 1;
    }

}

</style>
</head>


<body>

<div class="container">


<!-- ================= HEADER ================= -->

<div class="header">

<div class="header-top">

<div class="brand-area">

<div class="logo">ॐ</div>

<div class="brand">

<h1>
SHREE VINAYAK
<span>IT CARE</span>
</h1>

<p>Laptop Repair Database & Board Viewer</p>

<small>Repair | Restore | Resolve</small>

</div>

</div>

</div>


<!-- INFO BAR -->

<div class="info-bar">

<div class="info-item">

<div class="info-icon">👨‍🔧</div>

<div class="info-text">
<b>19+ Years</b>
<span>Of Experience</span>
</div>

</div>


<div class="info-item">

<div class="info-icon">📍</div>

<div class="info-text">
<b>Bhubaneswar, Odisha</b>
<span>India</span>
</div>

</div>


<div class="info-item">

<div class="info-icon">📞</div>

<div class="info-text">

<b>
<a href="tel:+917008541544">
+91 70085 41544
</a>
</b>

<span style="color:#55d66c">
Call / WhatsApp
</span>

</div>

</div>


<div class="info-item">

<div class="info-icon">✉️</div>

<div class="info-text">

<b>
info@shreevinayakitcare.com
</b>

<span>Support</span>

</div>

</div>

</div>

</div>



<!-- ================= MAIN ================= -->

<div class="main-layout">


<!-- LEFT -->

<div class="left-panel">


<!-- WELCOME -->

<div class="welcome">

<div class="welcome-text">
WELCOME
</div>

<div class="to">
TO
</div>

<h2>
SHREE VINAYAK IT CARE
</h2>

<div class="orange-line"></div>

<p>
Your One Stop Solution for Chip-Level Repairing,
Board Diagnostics, Component Search and Technical
Learning Resources.
Contact:
<span>7008541544</span>
</p>

</div>



<!-- REPAIR TITLE -->

<div class="section-title">
REPAIR CATALOGUE
</div>



<!-- REPAIR CARDS -->

<div class="repair-grid">


<a href="/laptop">

<div class="repair-card blue">

<div class="card-icon">💻</div>

<div class="card-device">💻</div>

<h3>LAPTOP REPAIR</h3>

<p>
All Brands Supported<br>
Chip-Level Repairing
</p>

<div class="explore-btn">
Explore →
</div>

</div>

</a>



<a href="/desktop">

<div class="repair-card green">

<div class="card-icon">🖥️</div>

<div class="card-device">🖥️</div>

<h3>DESKTOP REPAIR</h3>

<p>
Motherboard & Component<br>
Level Repairing
</p>

<div class="explore-btn">
Explore →
</div>

</div>

</a>



<a href="/printer">

<div class="repair-card purple">

<div class="card-icon">🖨️</div>

<div class="card-device">🖨️</div>

<h3>PRINTER REPAIR</h3>

<p>
Laser, Inkjet, All-in-One<br>
Printer Solutions
</p>

<div class="explore-btn">
Explore →
</div>

</div>

</a>



<a href="/mobile">

<div class="repair-card orange">

<div class="card-icon">📱</div>

<div class="card-device">📱</div>

<h3>MOBILE / TABLET REPAIR</h3>

<p>
Hardware & Software<br>
Solutions
</p>

<div class="explore-btn">
Explore →
</div>

</div>

</a>



<a href="/data-recovery">

<div class="repair-card teal">

<div class="card-icon">💾</div>

<div class="card-device">💽</div>

<h3>DATA RECOVERY</h3>

<p>
Recover Deleted, Formatted<br>
& Lost Data
</p>

<div class="explore-btn">
Explore →
</div>

</div>

</a>



<a href="/power-supply">

<div class="repair-card yellow">

<div class="card-icon">⚡</div>

<div class="card-device">🔌</div>

<h3>POWER SUPPLY REPAIR</h3>

<p>
SMPS, Adapter, DC Supply<br>
Repair & Fix
</p>

<div class="explore-btn">
Explore →
</div>

</div>

</a>


</div>



<!-- STUDY MATERIAL -->

<div class="study-section">


<div class="study-info">

<h3>STUDY MATERIAL</h3>

<div class="sub">
Learn | Practice | Master
</div>

<p>
Access Schematics, BoardViews,
Repair Guides, eBooks and
Technical Notes.
</p>

<a href="/study"
class="study-btn">

Explore Study Material →

</a>

</div>



<div class="study-card">

<div class="study-image">
📐
</div>

<h4>Schematics</h4>

</div>



<div class="study-card">

<div class="study-image">
🔬
</div>

<h4>Board Views</h4>

</div>



<div class="study-card">

<div class="study-image">
📄
</div>

<h4>Repair Guides</h4>

</div>



<div class="study-card">

<div class="study-image">
📚
</div>

<h4>eBooks & Notes</h4>

</div>


</div>

</div>



<!-- LOGIN PANEL -->

<div class="login-panel">

<div class="login-title">
🔒 LOGIN
</div>


<form method="post" action="/login">


<div class="input-box">

<span>👤</span>

<input
type="text"
name="username"
placeholder="Username"
required>

</div>



<div class="input-box">

<span>🔒</span>

<input
type="password"
name="password"
placeholder="Password"
required>

</div>



<div class="login-options">

<label>

<input type="checkbox">

Remember Me

</label>

<a href="#">
Forgot Password?
</a>

</div>



<button
class="login-button"
type="submit">

LOGIN →

</button>


</form>



<div class="new-user">

New User?

<span>
Create an Account
</span>

</div>


<a
href="https://wa.me/917008541544"
class="whatsapp-btn">

📱 7008541544 WhatsApp

</a>


<a
href="tel:+917008541544"
class="call-btn">

📞 Call: 70085 41544

</a>


</div>

</div>



<!-- FEATURES -->

<div class="features">


<div class="feature">

<span>🛠</span>

Chip-Level Expertise

</div>


<div class="feature">

<span>🏅</span>

All Brands Supported

</div>


<div class="feature">

<span>⚡</span>

Fast & Reliable Service

</div>


<div class="feature">

<span>💰</span>

Affordable Pricing

</div>


<div class="feature">

<span>🚚</span>

Doorstep Pickup & Delivery

</div>


</div>



<!-- FOOTER -->

<div class="footer">

© 2024 SHREE VINAYAK IT CARE
&nbsp; | &nbsp;
WhatsApp: 7008541544
&nbsp; | &nbsp;
All Rights Reserved.

</div>


</div>

</body>
</html>
"""


# =====================================================
# HOME
# =====================================================

@app.route("/")
def home():
    return render_template_string(HTML)


# =====================================================
# LOGIN
# =====================================================

@app.route("/login", methods=["POST"])
def login():
    return "Login system next step me database se connect hoga."


# =====================================================
# REPAIR PAGES
# =====================================================

@app.route("/laptop")
def laptop():
    return "Laptop Repair Section"


@app.route("/desktop")
def desktop():
    return "Desktop Repair Section"


@app.route("/printer")
def printer():
    return "Printer Repair Section"


@app.route("/mobile")
def mobile():
    return "Mobile & Tablet Repair Section"


@app.route("/data-recovery")
def data_recovery():
    return "Data Recovery Section"


@app.route("/power-supply")
def power_supply():
    return "Power Supply Repair Section"


@app.route("/study")
def study():
    return "Study Material Section"


# =====================================================
# RUN
# =====================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
