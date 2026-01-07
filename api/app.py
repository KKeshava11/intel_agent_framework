from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from core.agent import Agent
from flows.summarize_flow import run_pdf_flow
from flows.pdf_flow import run_pdf_flow
from flows.qa_flow import qa_flow
from PyPDF2 import PdfReader

app = FastAPI()
agent = Agent(name="IntelAgent")

# -----------------------------
# Home page / Web UI
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Intel Agent Framework</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background:#f4f7f9; margin:0; padding:0; }
            .container { max-width:900px; margin:40px auto; padding:20px; }
            h1 { text-align:center; color:#2c3e50; font-size:2.5em; }
            .card { background:#fff; padding:25px; margin-bottom:30px; border-radius:12px; box-shadow:0 8px 20px rgba(0,0,0,0.08); transition: transform 0.2s; }
            .card:hover { transform: translateY(-5px); }
            h2 { color:#2980b9; margin-top:0; border-bottom:2px solid #2980b9; padding-bottom:5px; }
            textarea, input[type=text], input[type=file] { width:100%; padding:12px; margin-top:8px; margin-bottom:15px; border-radius:8px; border:1px solid #ccc; font-size:1em; }
            button { background:#2980b9; color:white; border:none; padding:12px 25px; font-size:1em; border-radius:8px; cursor:pointer; transition: background 0.2s; }
            button:hover { background:#1f6391; }
            .response-box { background:#ecf0f1; padding:15px; border-radius:8px; margin-top:10px; white-space: pre-wrap; font-family: monospace; max-height:400px; overflow-y:auto; }
            footer { text-align:center; margin-top:40px; color:#7f8c8d; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Intel Agent Framework</h1>

            <!-- Resume Analyzer -->
            <div class="card">
                <h2>Resume Analyzer</h2>
                <form action="/analyze-resume" method="post" enctype="multipart/form-data">
                    <textarea name="resume_text" rows="10" placeholder="Paste resume text here (optional if uploading PDF)"></textarea>
                    <input type="file" name="resume_pdf" accept=".pdf" />
                    <button type="submit">Analyze Resume</button>
                </form>
            </div>

            <!-- PDF Summarizer -->
            <div class="card">
                <h2>PDF Summarizer</h2>
                <form action="/extract-pdf" method="post" enctype="multipart/form-data">
                    <input type="file" name="pdf_file" accept=".pdf" />
                    <button type="submit">Summarize PDF</button>
                </form>
            </div>

            <!-- PDF/Text Q&A -->
            <div class="card">
                <h2>PDF/Text Q&A</h2>
                <form action="/qa" method="post" enctype="multipart/form-data">
                    <textarea name="text_input" rows="8" placeholder="Paste text here (optional)"></textarea>
                    <input type="file" name="pdf_file" accept=".pdf" />
                    <input type="text" name="question" placeholder="Enter your question here" required />
                    <button type="submit">Ask Question</button>
                </form>
            </div>

            <footer>
                &copy; 2026 Intel Agent Framework
            </footer>
        </div>
    </body>
    </html>
    """

# -----------------------------
# Resume Analyzer (PDF or text)
# -----------------------------
@app.post("/analyze-resume", response_class=HTMLResponse)
def analyze_resume(resume_text: str = Form(""), resume_pdf: UploadFile = File(None)):
    try:
        text = resume_text or ""
        # If PDF uploaded, extract text
        if resume_pdf:
            reader = PdfReader(resume_pdf.file)
            pdf_text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    pdf_text += page_text + "\n"
            text += pdf_text  # combine textarea + PDF text if both provided

        if not text.strip():
            return """
            <html>
                <body>
                    <h2>No resume text provided.</h2>
                    <a href="/">Back</a>
                </body>
            </html>
            """

        result = summarize_flow(agent, text)
        return f"""
        <html>
            <body>
                <h2>Resume Analysis Result</h2>
                <div class="response-box">{result}</div>
                <br><a href="/">Back</a>
            </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html>
            <body>
                <h2>Error analyzing resume</h2>
                <pre>{str(e)}</pre>
                <br><a href="/">Back</a>
            </body>
        </html>
        """
