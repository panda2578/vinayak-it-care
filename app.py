from flask import Flask, render_template_string, request

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

<!-- FONT AWESOME ICONS -->
<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

<style>

/* =====================================================
   GLOBAL
===================================================== */

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    -webkit-tap-highlight-color:transparent;
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
    overflow-x:hidden;
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
   HEADER
===================================================== */

.header{
    border:1px solid #1d4f84;
    border-radius:18px;
    overflow:hidden;

    background:
        linear-gradient(90deg,#071126 0%,#07152e 50%,#061124 100%);

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

.header-top::after{
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
            rgba(7,21,46,.20) 35%,
            rgba(0,0,0,.20)
        ),
        url("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1400&q=80");

    background-size:cover;
    background-position:center;
    opacity:.70;
    z-index:0;
}


/* =====================================================
   BRAND
===================================================== */

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
        radial-gradient(circle,#17284d,#050c1c 70%);

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
   HEADER INFORMATION
===================================================== */

.info-bar{
    display:grid;
    grid-template-columns:repeat(4,1fr);

    border-top:1px solid #1d4f84;

    position:relative;
    z-index:3;

    background:rgba(2,9,22,.88);
}

.info-item{
    min-height:72px;

    display:flex;
    align-items:center;
    gap:15px;

    padding:12px 25px;

    border-right:1px solid #255486;
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
   MAIN LAYOUT
===================================================== */

.main-layout{
    display:grid;
    grid-template-columns:minmax(0,1fr) 420px;
    gap:14px;
    margin-top:10px;
}


/* =====================================================
   LEFT PANEL
===================================================== */

.left-panel{
    border:1px solid #174878;
    border-radius:18px;
    padding:12px;

    background:
        linear-gradient(180deg,#061126,#030a17);
}


/* =====================================================
   WELCOME
===================================================== */

.welcome{
    text-align:center;
    padding:18px 10px 12px;
    position:relative;
}

.welcome-text{
    font-size:28px;
    font-weight:800;
    letter-spacing:10px;
    color:#dfe7f4;
}

.to{
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
        linear-gradient(90deg,transparent,#ff8500,transparent);

    position:relative;
}

.orange-line::after{
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

    margin:12px 0 14px;

    color:#c9d3e3;
    font-size:15px;
    font-weight:700;
    letter-spacing:8px;
}

.section-title::before,
.section-title::after{
    content:"";
    height:2px;
    flex:1;
    max-width:300px;

    background:
        linear-gradient(90deg,transparent,#2687d8);
}

.section-title::after{
    background:
        linear-gradient(90deg,#2687d8,transparent);
}


/* =====================================================
   REPAIR GRID
===================================================== */

.repair-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:12px;
}


/* =====================================================
   REPAIR CARD
===================================================== */

.repair-card{
    position:relative;
    min-height:160px;
    padding:14px;

    border-radius:13px;
    overflow:hidden;
    cursor:pointer;

    transition:
        transform .3s ease,
        box-shadow .3s ease;

    border:1px solid var(--card-border);

    background:
        linear-gradient(
            135deg,
            var(--card-bg1),
            var(--card-bg2)
        );
}

.repair-card:hover{
    transform:translateY(-6px) scale(1.015);

    box-shadow:
        0 14px 35px rgba(0,0,0,.55),
        0 0 22px var(--card-glow);
}

.card-icon{
    width:48px;
    height:48px;

    border-radius:50%;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:24px;

    border:1px solid var(--card-border);

    background:rgba(0,0,0,.25);
}

.card-device{
    position:absolute;
    right:15px;
    top:18px;

    font-size:58px;

    filter:
        drop-shadow(0 10px 10px rgba(0,0,0,.7));

    transition:transform .3s ease;
}

.repair-card:hover .card-device{
    transform:scale(1.15) rotate(4deg);
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

    padding:6px 22px;

    border-radius:7px;
    font-size:13px;

    border:1px solid var(--card-border);

    background:rgba(0,0,0,.3);
}


/* =====================================================
   REPAIR CARD COLORS
===================================================== */

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
    border:1px solid #2a588a;
    border-radius:18px;

    padding:26px;

    background:
        linear-gradient(180deg,#0a1931,#071123);

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

    transform:translateY(-50%);

    font-size:18px;
}

.input-box input{
    width:100%;

    padding:15px 15px 15px 48px;

    border-radius:9px;
    border:1px solid #526176;

    background:#0a1425;

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

    color:white;

    background:
        linear-gradient(
            90deg,
            #ff6a00,
            #ff9800,
            #ff4e00
        );
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

    border:1px solid #235687;

    background:
        linear-gradient(135deg,#0a1b33,#06101f);
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

    padding:9px 24px;

    border:1px solid #5dafff;
    border-radius:7px;

    font-weight:700;
}

.study-card{
    min-height:140px;
    padding:8px;

    border-radius:12px;

    text-align:center;

    border:1px solid #245789;

    background:
        linear-gradient(135deg,#0a1c34,#06101e);

    transition:.3s;
}

.study-card:hover{
    transform:translateY(-5px);

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

    border:1px solid #1f5486;

    border-radius:14px;

    overflow:hidden;

    background:#061224;
}

.feature{
    padding:14px 12px;

    display:flex;
    align-items:center;
    justify-content:center;

    gap:9px;

    border-right:1px solid #2a5888;

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

    border:1px solid #174878;

    border-radius:
        0 0 18px 18px;

    background:#06101f;
}


/* =====================================================
   PREMIUM FLOATING CONTACT BUTTONS
===================================================== */

.floating-contact{
    position:fixed;

    right:20px;
    bottom:25px;

    z-index:9999;

    display:flex;
    flex-direction:column;

    gap:14px;
}


/* BUTTON */

.float-btn{
    width:58px;
    height:58px;

    border-radius:50%;

    display:flex;
    align-items:center;
    justify-content:center;

    position:relative;

    font-size:25px;

    color:#ffffff;

    border:2px solid rgba(255,255,255,.25);

    box-shadow:
        0 8px 25px rgba(0,0,0,.55);

    transition:
        transform .25s ease,
        box-shadow .25s ease;

    animation:
        floatingPulse 2.5s infinite;
}


/* RIPPLE RING */

.float-btn::before{
    content:"";

    position:absolute;

    width:100%;
    height:100%;

    border-radius:50%;

    border:2px solid currentColor;

    opacity:.45;

    animation:
        ripple 2.2s infinite;
}


/* ICON */

.float-btn i{
    position:relative;
    z-index:2;

    transition:
        transform .25s ease;
}


/* HOVER */

.float-btn:hover{
    transform:
        translateY(-5px)
        scale(1.12);

    box-shadow:
        0 15px 35px rgba(0,0,0,.75);
}

.float-btn:hover i{
    transform:
        rotate(12deg)
        scale(1.1);
}


/* WHATSAPP */

.float-whatsapp{
    background:
        linear-gradient(
            135deg,
            #25d366,
            #128c4a
        );

    box-shadow:
        0 0 14px rgba(37,211,102,.8),
        0 8px 25px rgba(0,0,0,.6);
}


/* CALL */

.float-call{
    background:
        linear-gradient(
            135deg,
            #2d9cff,
            #0055b8
        );

    box-shadow:
        0 0 14px rgba(45,156,255,.8),
        0 8px 25px rgba(0,0,0,.6);
}


/* CHAT */

.float-chat{
    background:
        linear-gradient(
            135deg,
            #ff9a00,
            #ff4d00
        );

    box-shadow:
        0 0 14px rgba(255,120,0,.8),
        0 8px 25px rgba(0,0,0,.6);
}


/* LABEL */

.float-btn::after{
    position:absolute;

    right:72px;

    padding:7px 13px;

    border-radius:7px;

    background:#071426;

    color:#ffffff;

    font-size:12px;

    font-weight:700;

    white-space:nowrap;

    opacity:0;

    transform:
        translateX(10px);

    pointer-events:none;

    transition:.25s;

    border:
        1px solid rgba(255,255,255,.15);
}


.float-btn:hover::after{
    opacity:1;

    transform:
        translateX(0);
}


/* TOOLTIP TEXT */

.float-chat::after{
    content:"MESSAGE CHAT";
}

.float-call::after{
    content:"CALL NOW";
}

.float-whatsapp::after{
    content:"WHATSAPP";
}


/* PULSE */

@keyframes floatingPulse{

    0%{
        transform:scale(1);
    }

    50%{
        transform:scale(1.06);
    }

    100%{
        transform:scale(1);
    }

}


/* RIPPLE */

@keyframes ripple{

    0%{
        transform:scale(1);
        opacity:.55;
    }

    100%{
        transform:scale(1.55);
        opacity:0;
    }

}


/* =====================================================
   TABLET
===================================================== */

@media(max-width:1150px){

    .main-layout{
        grid-template-columns:
            1fr 340px;
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
        grid-column:span 4;
    }

    .features{
        grid-template-columns:
            repeat(3,1fr);
    }

}


/* =====================================================
   MOBILE / TABLET
===================================================== */

@media(max-width:850px){

    .main-layout{
        grid-template-columns:1fr;
    }

    .login-panel{
        position:relative;
        top:auto;
    }

    .repair-grid{
        grid-template-columns:
            repeat(2,1fr);
    }

}


/* =====================================================
   MOBILE
===================================================== */

@media(max-width:600px){

    body{
        padding-bottom:90px;
    }

    .container{
        padding:0;
    }


    /* HIDE HEADER */

    .header{
        display:none;
    }


    .main-layout{
        margin-top:0;
    }


    .left-panel{
        border:none;
        border-radius:0;
        padding:8px;
        background:#030a17;
    }


    /* WELCOME IMAGE BACKGROUND */

    .welcome{

        min-height:310px;

        display:flex;

        flex-direction:column;

        align-items:center;

        justify-content:center;

        padding:
            40px 15px 35px;

        border-radius:
            0 0 18px 18px;

        overflow:hidden;

        background:

        linear-gradient(
            180deg,
            rgba(2,8,20,.88),
            rgba(2,8,20,.72)
        ),

        url("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80");

        background-size:cover;
        background-position:center;

        box-shadow:
            inset 0 0 80px rgba(0,0,0,.8);
    }


    .welcome-text{
        font-size:21px;
        letter-spacing:6px;

        text-shadow:
            0 2px 10px #000;
    }


    .welcome h2{
        font-size:26px;
        line-height:1.25;

        text-shadow:
            0 2px 12px #000;
    }


    .welcome p{
        font-size:13px;
        max-width:340px;

        text-shadow:
            0 2px 8px #000;
    }


    .orange-line::after{
        background:
            rgba(3,10,20,.8);
    }


    .section-title{
        font-size:12px;
        letter-spacing:4px;
        gap:8px;

        margin-top:20px;
    }


    .repair-grid{
        grid-template-columns:1fr;
        gap:10px;
    }


    .repair-card{
        min-height:145px;
    }


    .login-panel{
        margin:8px;
        padding:20px 15px;
        border-radius:16px;
    }


    .study-section{
        grid-template-columns:
            repeat(2,1fr);

        padding:8px;
    }


    .study-info{
        grid-column:span 2;
    }


    .features{
        margin:8px;
        grid-template-columns:1fr;
    }


    .feature{
        border-right:none;

        border-bottom:
            1px solid #2a5888;
    }


    .feature:last-child{
        border-bottom:none;
    }


    .footer{
        margin:8px;
        border-radius:12px;
        font-size:12px;
    }


    /* FLOATING BUTTONS */

    .floating-contact{
        right:14px;
        bottom:18px;
        gap:12px;
    }


    .float-btn{
        width:56px;
        height:56px;
        font-size:24px;
    }


    /* TOOLTIP ALWAYS HIDE ON MOBILE */

    .float-btn::after{
        display:none;
    }

}


/* =====================================================
   SMALL MOBILE
===================================================== */

@media(max-width:380px){

    .welcome h2{
        font-size:22px;
    }

    .welcome-text{
        font-size:18px;
    }

    .study-section{
        grid-template-columns:1fr;
    }

    .study-info{
        grid-column:span 1;
    }

}

</style>

</head>


<body>


<div class="container">


<!-- =====================================================
     HEADER - DESKTOP ONLY
===================================================== -->

<div class="header">


<div class="header-top">

<div class="brand-area">


<div class="logo">
ॐ
</div>


<div class="brand">

<h1>
SHREE VINAYAK
<span>IT CARE</span>
</h1>

<p>
Laptop Repair Database & Board Viewer
</p>

<small>
Repair | Restore | Resolve
</small>

</div>


</div>

</div>



<!-- HEADER INFO -->

<div class="info-bar">


<div class="info-item">

<div class="info-icon">
👨‍🔧
</div>

<div class="info-text">

<b>19+ Years</b>

<span>
Of Experience
</span>

</div>

</div>



<div class="info-item">

<div class="info-icon">
📍
</div>

<div class="info-text">

<b>
Bhubaneswar, Odisha
</b>

<span>
India
</span>

</div>

</div>



<div class="info-item">

<div class="info-icon">
📞
</div>

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

<div class="info-icon">
✉️
</div>

<div class="info-text">

<b>
info@shreevinayakitcare.com
</b>

<span>
Support
</span>

</div>

</div>


</div>

</div>



<!-- =====================================================
     MAIN LAYOUT
===================================================== -->

<div class="main-layout">


<!-- LEFT PANEL -->

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

<span>
7008541544
</span>

</p>

</div>



<!-- REPAIR CATALOGUE -->

<div class="section-title">
REPAIR CATALOGUE
</div>


<div class="repair-grid">


<a href="/laptop">

<div class="repair-card blue">

<div class="card-icon">
💻
</div>

<div class="card-device">
💻
</div>

<h3>
LAPTOP REPAIR
</h3>

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

<div class="card-icon">
🖥️
</div>

<div class="card-device">
🖥️
</div>

<h3>
DESKTOP REPAIR
</h3>

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

<div class="card-icon">
🖨️
</div>

<div class="card-device">
🖨️
</div>

<h3>
PRINTER REPAIR
</h3>

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

<div class="card-icon">
📱
</div>

<div class="card-device">
📱
</div>

<h3>
MOBILE / TABLET REPAIR
</h3>

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

<div class="card-icon">
💾
</div>

<div class="card-device">
💽
</div>

<h3>
DATA RECOVERY
</h3>

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

<div class="card-icon">
⚡
</div>

<div class="card-device">
🔌
</div>

<h3>
POWER SUPPLY REPAIR
</h3>

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

<h3>
STUDY MATERIAL
</h3>

<div class="sub">
Learn | Practice | Master
</div>

<p>
Access Schematics,
BoardViews, Repair Guides,
eBooks and Technical Notes.
</p>

<a href="/study"
class="study-btn">

Explore Study Material →

</a>

</div>



<a href="/study/schematics">

<div class="study-card">

<div class="study-image">
📐
</div>

<h4>
Schematics
</h4>

</div>

</a>



<a href="/study/boardview">

<div class="study-card">

<div class="study-image">
🔬
</div>

<h4>
Board Views
</h4>

</div>

</a>



<a href="/study/guides">

<div class="study-card">

<div class="study-image">
📄
</div>

<h4>
Repair Guides
</h4>

</div>

</a>



<a href="/study/ebooks">

<div class="study-card">

<div class="study-image">
📚
</div>

<h4>
eBooks & Notes
</h4>

</div>

</a>


</div>


</div>



<!-- =====================================================
     LOGIN PANEL
===================================================== -->

<div class="login-panel">


<div class="login-title">
🔒 LOGIN
</div>


<form method="POST"
action="/login">


<div class="input-box">

<span>
👤
</span>

<input
type="text"
name="username"
placeholder="Username"
required>

</div>



<div class="input-box">

<span>
🔒
</span>

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


</div>


</div>



<!-- =====================================================
     FEATURES
===================================================== -->

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

© 2026 SHREE VINAYAK IT CARE
|
WhatsApp: 7008541544
|
All Rights Reserved.

</div>


</div>



<!-- =====================================================
     PREMIUM FLOATING BUTTONS
===================================================== -->

<div class="floating-contact">


<!-- CHAT -->

<a
href="/chat"
class="float-btn float-chat"
title="Message Chat">

<i class="fa-solid fa-comment-dots"></i>

</a>


<!-- CALL -->

<a
href="tel:+917008541544"
class="float-btn float-call"
title="Call Now">

<i class="fa-solid fa-phone"></i>

</a>


<!-- WHATSAPP -->

<a
href="https://wa.me/917008541544"
class="float-btn float-whatsapp"
title="WhatsApp"
target="_blank">

<i class="fa-brands fa-whatsapp"></i>

</a>


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

    username = request.form.get("username", "")

    return f"""
    <h2>Login Received</h2>
    <p>Welcome {username}</p>
    <a href="/">← Back to Home</a>
    """


# =====================================================
# CHAT
# =====================================================

@app.route("/chat")
def chat():

    return """
    <!DOCTYPE html>
    <html>
    <head>

    <meta name="viewport"
    content="width=device-width, initial-scale=1.0">

    <title>SHREE VINAYAK IT CARE - Chat</title>

    <style>

    *{
        box-sizing:border-box;
    }

    body{
        margin:0;
        font-family:Arial;
        background:#020814;
        color:white;
    }

    .chat-box{
        max-width:650px;
        margin:auto;
        min-height:100vh;

        display:flex;
        flex-direction:column;

        background:#071226;
    }

    .chat-header{
        padding:20px;

        background:#0c2344;

        border-bottom:
        1px solid #27639c;
    }

    .chat-header h2{
        margin:0;
        color:#ff8a00;
    }

    .messages{
        flex:1;
        padding:20px;
    }

    .support-message{
        background:#122b4d;
        padding:15px;
        border-radius:14px;
        max-width:85%;
        line-height:1.5;
    }

    .chat-input{
        display:flex;
        gap:8px;
        padding:12px;
        background:#08152a;
    }

    .chat-input input{
        flex:1;
        padding:14px;

        border:none;
        border-radius:25px;

        background:#10213d;
        color:white;

        outline:none;
    }

    .chat-input button{
        border:none;
        padding:12px 20px;

        border-radius:25px;

        background:#ff7600;
        color:white;

        font-weight:bold;
        cursor:pointer;
    }

    </style>

    </head>

    <body>

    <div class="chat-box">

        <div class="chat-header">

            <h2>
            💬 SHREE VINAYAK IT CARE
            </h2>

            <p>
            🟢 Support Available
            </p>

        </div>


        <div class="messages">

            <div class="support-message">

                👨‍🔧 Welcome to SHREE VINAYAK IT CARE.

                <br><br>

                Please write your repair issue here.

            </div>

        </div>


        <form
        class="chat-input"
        method="POST"
        action="/send-message">

            <input
            type="text"
            name="message"
            placeholder="Type your message..."
            required>

            <button type="submit">
            Send
            </button>

        </form>

    </div>

    </body>
    </html>
    """


# =====================================================
# SEND CHAT MESSAGE
# =====================================================

@app.route("/send-message", methods=["POST"])
def send_message():

    message = request.form.get("message", "")

    print("Customer Message:", message)

    return f"""
    <h2>Message Sent Successfully ✅</h2>
    <p>{message}</p>
    <a href="/chat">← Back to Chat</a>
    """


# =====================================================
# REPAIR SECTIONS
# =====================================================

@app.route("/laptop")
def laptop():
    return "<h2>Laptop Repair Section</h2>"


@app.route("/desktop")
def desktop():
    return "<h2>Desktop Repair Section</h2>"


@app.route("/printer")
def printer():
    return "<h2>Printer Repair Section</h2>"


@app.route("/mobile")
def mobile():
    return "<h2>Mobile / Tablet Repair Section</h2>"


@app.route("/data-recovery")
def data_recovery():
    return "<h2>Data Recovery Section</h2>"


@app.route("/power-supply")
def power_supply():
    return "<h2>Power Supply Repair Section</h2>"


# =====================================================
# STUDY MATERIAL
# =====================================================

@app.route("/study")
def study():
    return "<h2>Study Material</h2>"


@app.route("/study/schematics")
def schematics():
    return "<h2>Schematics</h2>"


@app.route("/study/boardview")
def boardview():
    return "<h2>Board Views</h2>"


@app.route("/study/guides")
def guides():
    return "<h2>Repair Guides</h2>"


@app.route("/study/ebooks")
def ebooks():
    return "<h2>eBooks & Notes</h2>"


# =====================================================
# RUN APP
# =====================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
