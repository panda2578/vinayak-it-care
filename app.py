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
   DESKTOP HEADER
===================================================== */

.header{
    border:1px solid #1d4f84;
    border-radius:18px;
    overflow:hidden;
    background:linear-gradient(90deg,#071126,#07152e,#061124);
    position:relative;
}

.header-top{
    min-height:115px;
    display:flex;
    align-items:center;
    padding:12px 25px;
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
            rgba(7,21,46,.25) 35%,
            rgba(0,0,0,.25)
        ),
        url("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1400&q=80");

    background-size:cover;
    background-position:center;
    opacity:.75;
    z-index:0;
}

.brand-area{
    display:flex;
    align-items:center;
    gap:15px;
    position:relative;
    z-index:2;
}

.logo{
    width:82px;
    height:82px;
    min-width:82px;

    border-radius:50%;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:48px;
    color:#ff9a00;

    border:2px solid #ff9700;

    background:radial-gradient(circle,#17284d,#050c1c 70%);

    box-shadow:
        0 0 10px #ff8500,
        0 0 25px rgba(255,130,0,.45);
}

.brand h1{
    font-size:30px;
    line-height:1;
    letter-spacing:1.5px;
    font-weight:900;
    color:#f4f6fb;
}

.brand h1 span{
    display:block;
    color:#ff8500;
}

.brand p{
    margin-top:6px;
    font-size:13px;
    color:#c7d0df;
}

.brand small{
    display:block;
    margin-top:4px;
    color:#ffb000;
    font-size:11px;
    font-weight:700;
    letter-spacing:1px;
}


/* =====================================================
   INFO BAR
===================================================== */

.info-bar{
    display:grid;
    grid-template-columns:repeat(4,1fr);

    border-top:1px solid #1d4f84;

    background:rgba(2,9,22,.88);
}

.info-item{
    min-height:60px;

    display:flex;
    align-items:center;
    gap:10px;

    padding:9px 18px;

    border-right:1px solid #255486;
}

.info-item:last-child{
    border-right:none;
}

.info-icon{
    font-size:24px;
    color:#ffb000;
}

.info-text b{
    display:block;
    font-size:13px;
    margin-bottom:3px;
    color:#ffffff;
}

.info-text span{
    color:#aebbd0;
    font-size:11px;
}


/* =====================================================
   MAIN LAYOUT
===================================================== */

.main-layout{
    display:grid;
    grid-template-columns:minmax(0,1fr) 360px;
    gap:12px;
    margin-top:10px;
}


/* =====================================================
   LEFT PANEL
===================================================== */

.left-panel{
    border:1px solid #174878;
    border-radius:18px;
    padding:10px;

    background:
        linear-gradient(180deg,#061126,#030a17);
}


/* =====================================================
   WELCOME
===================================================== */

.welcome{
    text-align:center;
    padding:14px 10px 10px;
}

.welcome-text{
    font-size:23px;
    font-weight:800;
    letter-spacing:8px;
    color:#dfe7f4;
}

.to{
    font-size:10px;
    letter-spacing:4px;
    margin-top:2px;
    color:#a7b5c8;
}

.welcome h2{
    margin-top:4px;
    font-size:27px;
    color:#ff8500;
    letter-spacing:1px;
    font-weight:900;
}

.orange-line{
    width:100px;
    height:2px;
    margin:9px auto;

    background:
        linear-gradient(90deg,transparent,#ff8500,transparent);

    position:relative;
}

.orange-line::after{
    content:"◇";

    position:absolute;
    top:-11px;
    left:50%;

    transform:translateX(-50%);

    color:#ff9a00;
    background:#071126;

    padding:0 6px;
    font-size:20px;
}

.welcome p{
    max-width:680px;
    margin:auto;
    line-height:1.45;
    font-size:12px;
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

    gap:15px;

    margin:10px 0;

    color:#c9d3e3;
    font-size:12px;
    font-weight:700;
    letter-spacing:6px;
}

.section-title::before,
.section-title::after{
    content:"";
    height:1px;
    flex:1;
    max-width:260px;

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
    gap:10px;
}


/* =====================================================
   REPAIR CARD
===================================================== */

.repair-card{
    position:relative;
    min-height:145px;
    padding:11px;

    border-radius:12px;
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
    transform:translateY(-5px) scale(1.015);

    box-shadow:
        0 12px 30px rgba(0,0,0,.55),
        0 0 20px var(--card-glow);
}

.card-icon{
    width:42px;
    height:42px;

    border-radius:50%;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:20px;

    border:1px solid var(--card-border);

    background:rgba(0,0,0,.25);
}

.card-device{
    position:absolute;
    right:10px;
    top:12px;

    font-size:46px;

    filter:
        drop-shadow(0 8px 8px rgba(0,0,0,.7));

    transition:transform .3s ease;
}

.repair-card:hover .card-device{
    transform:scale(1.12) rotate(4deg);
}

.repair-card h3{
    margin-top:14px;
    font-size:13px;
    font-weight:800;
}

.repair-card p{
    margin-top:5px;
    font-size:10px;
    line-height:1.35;
    color:#d0d9e7;
}

.explore-btn{
    display:inline-block;
    margin-top:7px;

    padding:4px 14px;

    border-radius:6px;
    font-size:10px;

    border:1px solid var(--card-border);

    background:rgba(0,0,0,.3);
}


/* =====================================================
   CARD COLORS
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
   LOGIN
===================================================== */

.login-panel{
    border:1px solid #2a588a;
    border-radius:18px;

    padding:20px;

    background:
        linear-gradient(180deg,#0a1931,#071123);

    height:fit-content;
    position:sticky;
    top:10px;
}

.login-title{
    text-align:center;
    font-size:17px;
    font-weight:800;
    letter-spacing:2px;
    margin-bottom:15px;
}

.input-box{
    position:relative;
    margin-top:10px;
}

.input-box span{
    position:absolute;
    left:12px;
    top:50%;

    transform:translateY(-50%);

    font-size:15px;
}

.input-box input{
    width:100%;

    padding:12px 12px 12px 42px;

    border-radius:8px;
    border:1px solid #526176;

    background:#0a1425;

    color:white;
    font-size:13px;

    outline:none;
}

.login-options{
    display:flex;
    justify-content:space-between;

    margin-top:10px;

    font-size:11px;
    color:#d6deea;
}

.login-options a{
    color:#ffae32;
}

.login-button{
    width:100%;

    border:none;

    margin-top:15px;
    padding:12px;

    border-radius:8px;

    cursor:pointer;

    font-size:16px;
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
    margin-top:10px;

    display:grid;

    grid-template-columns:
        1.5fr repeat(4,1fr);

    gap:8px;
}

.study-info{
    padding:10px;
    text-align:center;

    border-radius:10px;

    border:1px solid #235687;

    background:
        linear-gradient(135deg,#0a1b33,#06101f);
}

.study-info h3{
    font-size:16px;
}

.study-info .sub{
    margin-top:3px;
    color:#53b5ff;
    font-size:11px;
}

.study-info p{
    margin:7px auto;
    max-width:290px;

    font-size:10px;
    line-height:1.4;

    color:#c0cbdb;
}

.study-btn{
    display:inline-block;

    padding:6px 15px;

    border:1px solid #5dafff;
    border-radius:6px;

    font-size:10px;
    font-weight:700;
}

.study-card{
    min-height:115px;
    padding:6px;

    border-radius:10px;

    text-align:center;

    border:1px solid #245789;

    background:
        linear-gradient(135deg,#0a1c34,#06101e);

    transition:.3s;
}

.study-card:hover{
    transform:translateY(-4px);

    box-shadow:
        0 0 18px rgba(0,130,255,.25);
}

.study-image{
    height:65px;

    border-radius:6px;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:36px;

    background:#0c1627;
}

.study-card h4{
    margin-top:6px;
    font-size:11px;
    color:#d9e2ef;
}


/* =====================================================
   FEATURES
===================================================== */

.features{
    margin-top:10px;

    display:grid;

    grid-template-columns:
        repeat(5,1fr);

    border:1px solid #1f5486;

    border-radius:12px;

    overflow:hidden;

    background:#061224;
}

.feature{
    padding:10px 8px;

    display:flex;
    align-items:center;
    justify-content:center;

    gap:6px;

    border-right:1px solid #2a5888;

    color:#d7dfeb;

    font-size:11px;
    text-align:center;
}

.feature:last-child{
    border:none;
}

.feature span{
    color:#ffb000;
    font-size:17px;
}


/* =====================================================
   FOOTER
===================================================== */

.footer{
    text-align:center;

    margin-top:5px;
    padding:10px;

    color:#aeb9ca;
    font-size:11px;

    border:1px solid #174878;

    border-radius:
        0 0 15px 15px;

    background:#06101f;
}


/* =====================================================
   FLOATING BUTTONS
===================================================== */

.floating-contact{
    position:fixed;

    right:20px;
    bottom:25px;

    z-index:9999;

    display:flex;
    flex-direction:column;

    gap:12px;
}

.float-btn{
    width:54px;
    height:54px;

    border-radius:50%;

    display:flex;
    align-items:center;
    justify-content:center;

    position:relative;

    font-size:23px;

    color:#ffffff;

    border:2px solid rgba(255,255,255,.25);

    box-shadow:
        0 8px 22px rgba(0,0,0,.55);

    transition:
        transform .25s ease,
        box-shadow .25s ease;

    animation:
        floatingPulse 2.5s infinite;
}

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

.float-btn i{
    position:relative;
    z-index:2;

    transition:
        transform .25s ease;
}

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

.float-whatsapp{
    background:
        linear-gradient(
            135deg,
            #25d366,
            #128c4a
        );
}

.float-call{
    background:
        linear-gradient(
            135deg,
            #2d9cff,
            #0055b8
        );
}

.float-chat{
    background:
        linear-gradient(
            135deg,
            #ff9a00,
            #ff4d00
        );
}

.float-btn::after{
    position:absolute;

    right:66px;

    padding:6px 11px;

    border-radius:6px;

    background:#071426;

    color:#ffffff;

    font-size:11px;

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

.float-chat::after{
    content:"MESSAGE CHAT";
}

.float-call::after{
    content:"CALL NOW";
}

.float-whatsapp::after{
    content:"WHATSAPP";
}


@keyframes floatingPulse{

    0%{
        transform:scale(1);
    }

    50%{
        transform:scale(1.05);
    }

    100%{
        transform:scale(1);
    }

}

@keyframes ripple{

    0%{
        transform:scale(1);
        opacity:.5;
    }

    100%{
        transform:scale(1.5);
        opacity:0;
    }

}


/* =====================================================
   TABLET
===================================================== */

@media(max-width:1150px){

    .main-layout{
        grid-template-columns:
            1fr 320px;
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
   TABLET / MOBILE
===================================================== */

@media(max-width:850px){

    .main-layout{
        grid-template-columns:1fr;
    }

    .login-panel{
        position:relative;
        top:auto;
    }

}


/* =====================================================
   COMPACT MOBILE VERSION
===================================================== */

@media(max-width:600px){

    body{
        padding-bottom:80px;
    }

    .container{
        padding:0;
    }


    /* DESKTOP HEADER HIDE */

    .header{
        display:none;
    }


    .main-layout{
        margin-top:0;
    }


    .left-panel{
        border:none;
        border-radius:0;
        padding:7px;
        background:#030a17;
    }


    /* MOBILE WELCOME HEADER */

    .welcome{

        min-height:210px;

        display:flex;

        flex-direction:column;

        align-items:center;

        justify-content:center;

        padding:25px 12px 22px;

        border-radius:
            0 0 16px 16px;

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
            inset 0 0 70px rgba(0,0,0,.8);
    }


    .welcome-text{
        font-size:17px;
        letter-spacing:4px;

        text-shadow:
            0 2px 10px #000;
    }


    .to{
        font-size:9px;
        letter-spacing:3px;
    }


    .welcome h2{
        font-size:21px;
        margin-top:4px;

        text-shadow:
            0 2px 12px #000;
    }


    .orange-line{
        width:90px;
        margin:8px auto;
        height:2px;
    }


    .orange-line::after{
        font-size:18px;
        top:-9px;

        background:
            rgba(3,10,20,.8);
    }


    .welcome p{
        font-size:10.5px;
        line-height:1.45;
        max-width:310px;

        text-shadow:
            0 2px 8px #000;
    }


    /* SECTION TITLE */

    .section-title{
        margin:12px 0 10px;
        font-size:10px;
        letter-spacing:3px;
        gap:8px;
    }


    /* COMPACT 2 COLUMN CARDS */

    .repair-grid{
        grid-template-columns:
            repeat(2,1fr);

        gap:8px;
    }


    .repair-card{
        min-height:128px;
        padding:10px;
        border-radius:11px;
    }


    .card-icon{
        width:36px;
        height:36px;
        font-size:17px;
    }


    .card-device{
        right:8px;
        top:10px;
        font-size:40px;
    }


    .repair-card h3{
        margin-top:14px;
        font-size:10.5px;
        line-height:1.25;
        max-width:130px;
    }


    .repair-card p{
        margin-top:4px;
        font-size:8.5px;
        line-height:1.35;
    }


    .explore-btn{
        margin-top:7px;
        padding:4px 10px;
        font-size:9px;
        border-radius:6px;
    }


    /* LOGIN */

    .login-panel{
        margin:7px;
        padding:16px 14px;
    }


    .login-title{
        font-size:16px;
        margin-bottom:12px;
    }


    .input-box{
        margin-top:9px;
    }


    .input-box input{
        padding:11px 11px 11px 40px;
        font-size:12px;
    }


    .login-button{
        padding:11px;
        font-size:16px;
        margin-top:12px;
    }


    /* STUDY */

    .study-section{
        grid-template-columns:
            repeat(2,1fr);

        gap:7px;
        padding:0;
    }


    .study-info{
        grid-column:span 2;
        padding:10px;
    }


    .study-info h3{
        font-size:15px;
    }


    .study-info .sub{
        font-size:10px;
    }


    .study-info p{
        font-size:10px;
        margin:6px auto;
    }


    .study-btn{
        padding:6px 14px;
        font-size:10px;
    }


    .study-card{
        min-height:105px;
        padding:6px;
    }


    .study-image{
        height:60px;
        font-size:32px;
    }


    .study-card h4{
        margin-top:5px;
        font-size:10px;
    }


    /* FEATURES */

    .features{
        margin:7px;
        grid-template-columns:1fr;
    }


    .feature{
        border-right:none;

        border-bottom:
            1px solid #2a5888;

        padding:9px;
    }


    .feature:last-child{
        border-bottom:none;
    }


    /* FOOTER */

    .footer{
        margin:7px;
        border-radius:10px;
        font-size:10px;
    }


    /* FLOATING BUTTONS */

    .floating-contact{
        right:10px;
        bottom:14px;
        gap:9px;
    }


    .float-btn{
        width:48px;
        height:48px;
        font-size:20px;
    }


    .float-btn::after{
        display:none;
    }

}


/* =====================================================
   SMALL MOBILE
===================================================== */

@media(max-width:380px){

    .welcome h2{
        font-size:19px;
    }

    .welcome-text{
        font-size:15px;
    }

    .repair-card{
        min-height:120px;
        padding:8px;
    }

    .card-device{
        font-size:34px;
    }

    .repair-card h3{
        font-size:9.5px;
    }

    .repair-card p{
        font-size:8px;
    }

}

</style>

</head>


<body>

<div class="container">


<!-- =====================================================
     DESKTOP HEADER
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
<b>info@shreevinayakitcare.com</b>
<span>Support</span>
</div>
</div>

</div>

</div>



<!-- =====================================================
     MAIN
===================================================== -->

<div class="main-layout">


<!-- LEFT SIDE -->

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

<h3>MOBILE / TABLET</h3>

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

<h3>POWER SUPPLY</h3>

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
Access Schematics, BoardViews,
Repair Guides, eBooks and
Technical Notes.
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



<!-- LOGIN PANEL -->

<div class="login-panel">

<div class="login-title">
🔒 LOGIN
</div>

<form method="POST"
action="/login">


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

© 2026 SHREE VINAYAK IT CARE |
WhatsApp: 7008541544 |
All Rights Reserved.

</div>


</div>



<!-- =====================================================
     FLOATING BUTTONS
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

    <html lang="en">

    <head>

    <meta charset="UTF-8">

    <meta name="viewport"
    content="width=device-width, initial-scale=1.0">

    <title>
    SHREE VINAYAK IT CARE - Chat
    </title>

    <style>

    *{
        box-sizing:border-box;
    }

    body{
        margin:0;
        font-family:Arial,sans-serif;
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
        padding:18px;

        background:#0c2344;

        border-bottom:
        1px solid #27639c;
    }

    .chat-header h2{
        margin:0;
        color:#ff8a00;
        font-size:20px;
    }

    .chat-header p{
        margin:7px 0 0;
        font-size:12px;
        color:#55d66c;
    }

    .messages{
        flex:1;
        padding:18px;
    }

    .support-message{
        background:#122b4d;
        padding:14px;
        border-radius:14px;
        max-width:85%;
        line-height:1.5;
        font-size:14px;
    }

    .chat-input{
        display:flex;
        gap:8px;
        padding:10px;
        background:#08152a;
    }

    .chat-input input{
        flex:1;
        padding:13px;

        border:none;
        border-radius:25px;

        background:#10213d;
        color:white;

        outline:none;
    }

    .chat-input button{
        border:none;
        padding:10px 18px;

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

                👨‍🔧 Welcome to
                SHREE VINAYAK IT CARE.

                <br><br>

                Please write your
                repair issue here.

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

    <a href="/chat">
    ← Back to Chat
    </a>
    """


# =====================================================
# REPAIR PAGES
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
# RUN FLASK
# =====================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
