from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MYOB Platform Engineering</title>
    <style>
        body {
            margin: 0;
            font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: linear-gradient(135deg, #5E2B97, #E6007A);
            color: white;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .card {
            background: rgba(255, 255, 255, 0.12);
            border-radius: 16px;
            padding: 48px;
            max-width: 800px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
            text-align: center;
        }

        h1 {
            font-size: 2.6rem;
            margin-bottom: 16px;
        }

        h2 {
            font-size: 1.4rem;
            font-weight: 400;
            margin-bottom: 32px;
            opacity: 0.95;
        }

        .badges {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 32px;
        }

        .badge {
            background: rgba(255, 255, 255, 0.18);
            padding: 10px 16px;
            border-radius: 999px;
            font-size: 0.9rem;
            font-weight: 500;
            letter-spacing: 0.3px;
        }

        .footer {
            font-size: 0.9rem;
            opacity: 0.85;
        }

        .highlight {
            font-weight: 600;
            color: #FFD6EA;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Let’s do big things at MYOB</h1>
        <h2>Successfully delivered with modern cloud-native engineering</h2>

        <div class="badges">
            <div class="badge">Azure DevOps</div>
            <div class="badge">CI/CD Pipelines</div>
            <div class="badge">Docker</div>
            <div class="badge">Kubernetes (AKS)</div>
            <div class="badge">ArgoCD GitOps</div>
            <div class="badge">Flask (Python)</div>
        </div>

        <p>
            This application demonstrates a <span class="highlight">successful end-to-end implementation</span>
            using Azure DevOps for CI, Kubernetes for scalable runtime,
            and ArgoCD for declarative GitOps-based delivery.
        </p>

        <p class="footer">
            Platform Engineering • Reliability • Velocity • 2026
        </p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)