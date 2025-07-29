from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure Flask App</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background: linear-gradient(to right, #1e3c72, #2a5298);
                font-family: Arial, sans-serif;
                color: white;
                text-align: center;
                padding-top: 100px;
                margin: 0;
            }
            h1 {
                color: #00ffcc;
                font-size: 3em;
                margin-bottom: 10px;
            }
            h2 {
                color: #ffff99;
                font-size: 1.5em;
                font-weight: normal;
                margin-bottom: 40px;
            }
            .version {
                font-size: 1.2em;
                color: #ffcccb;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Hello from Rajveer, Vikas & Amit Sir Flask App!</h1>
        <h2>Deployed via GitHub Actions CI/CD to Azure</h2>
        <div class="version">
            ✅ Deployment Version: <strong>v1.0.6</strong>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
