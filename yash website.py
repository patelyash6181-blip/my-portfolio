import http.server
import socketserver

# Professional Portfolio with Correct Company Names
html_content = """
<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yashkumar Patel | Professional Profile</title>
    <style>
        :root { --main-dark: #0f172a; --accent-blue: #2563eb; --accent-red: #dc2626; --light-bg: #f8fafc; }
        body { font-family: 'Segoe UI', Tahoma, sans-serif; background: var(--light-bg); margin: 0; color: #334155; line-height: 1.6; }
        
        .header { background: var(--main-dark); color: white; text-align: center; padding: 60px 20px; border-bottom: 4px solid var(--accent-blue); }
        .header h1 { margin: 0; font-size: 32px; letter-spacing: 1px; }
        .header p { margin: 10px 0; font-size: 18px; color: #94a3b8; }
        
        .btn-group { margin-top: 20px; }
        .btn { display: inline-block; padding: 10px 25px; border-radius: 5px; text-decoration: none; font-weight: 600; margin: 5px; transition: 0.3s; }
        .btn-linkedin { background: #0077b5; color: white; }
        .btn-mail { border: 1px solid #94a3b8; color: #94a3b8; }
        .btn:hover { opacity: 0.8; transform: translateY(-2px); }

        .container { max-width: 850px; margin: 30px auto; padding: 0 20px; }
        .card { background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
        
        .section-title { font-size: 20px; font-weight: 700; color: var(--main-dark); margin-bottom: 20px; border-left: 5px solid var(--accent-blue); padding-left: 15px; }
        
        .item { margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px solid #f1f5f9; }
        .item:last-child { border: none; }
        .item-title { font-weight: 700; color: #1e293b; font-size: 18px; margin: 0; }
        .item-subtitle { color: var(--accent-blue); font-weight: 600; font-size: 15px; margin: 5px 0; }
        .item-desc { font-size: 14px; color: #64748b; }

        .skill-tag { display: inline-block; background: #f1f5f9; color: #475569; padding: 5px 12px; border-radius: 4px; font-size: 13px; margin: 4px; font-weight: 600; border: 1px solid #e2e8f0; }
        .tech { background: var(--main-dark); color: white; border: none; }

        .details-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; font-size: 14px; }
        @media (max-width: 600px) { .details-grid { grid-template-columns: 1fr; } }
        
        footer { text-align: center; padding: 40px 20px; color: #94a3b8; font-size: 12px; }
    </style>
</head>
<body>

    <div class="header">
        <h1>Yashkumar Patel</h1>
        <p>IT Student & Professional Sales Associate</p>
        <div class="btn-group">
            <a href="https://www.linkedin.com/in/yashkumar-patel-825a0a281?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank" class="btn btn-linkedin">LinkedIn Profile</a>
            <a href="mailto:patelyash6181@gmail.com" class="btn btn-mail">Email Me</a>
        </div>
    </div>

    <div class="container">
        <div class="card">
            <div class="section-title">Professional Experience</div>
            <div class="item">
                <p class="item-title">Sales Associate</p>
                <p class="item-subtitle">Westside - A Unit of Trent Limited</p>
                <p class="item-desc">Working as a part-time Sales Associate, handling customer relations and store operations.</p>
            </div>
            <div class="item">
                <p class="item-title">Cashier Associate</p>
                <p class="item-subtitle">Star Bazaar - A TATA Enterprise</p>
                <p class="item-desc">May 2024 - March 2025 | Successfully managed checkout counters and banking operations.</p>
            </div>
        </div>

        <div class="card">
            <div class="section-title">Education</div>
            <div class="item">
                <p class="item-title">Diploma in Information Technology</p>
                <p class="item-subtitle">Gujarat Technological University (GTU)</p>
                <p class="item-desc">Dr. S. & S.S. Ghandhy College of Engineering & Technology, Surat (Ongoing)</p>
            </div>
            <div class="item">
                <p class="item-title">Gov ITI (NCVT) - Instrument Mechanics</p>
                <p class="item-subtitle">Completed (2025)</p>
                <p class="item-desc">Aggregate Score: 63.92%</p>
            </div>
        </div>

        <div class="card">
            <div class="section-title">Skills & Competencies</div>
            <div>
                <span class="skill-tag tech">Python</span>
                <span class="skill-tag tech">Java</span>
                <span class="skill-tag tech">Machine Learning</span>
                <span class="skill-tag tech">HTML & CSS</span>
                <span class="skill-tag tech">SEO & Digital Marketing</span>
                <span class="skill-tag">Cash Counter Operations</span>
                <span class="skill-tag">Banking</span>
                <span class="skill-tag">Interpersonal Skills</span>
            </div>
        </div>

        <div class="card">
            <div class="section-title">Personal Information</div>
            <div class="details-grid">
                <div><b>DOB:</b> 30/03/2005</div>
                <div><b>Address:</b> 317, Devashish Society, Rander, Surat</div>
                <div><b>Languages:</b> Gujarati, Hindi, English</div>
                <div><b>Nationality:</b> Indian</div>
            </div>
        </div>
    </div>

    <footer>
        © 2026 Yashkumar Patel | Portfolio Developed in Pyroid 3
    </footer>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

PORT = 8000
print(f"Server is running: http://localhost:{PORT}")
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
