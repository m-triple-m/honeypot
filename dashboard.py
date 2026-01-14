from flask import Flask, render_template_string
from db import get_logs

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html>
<head>
<title>Honeypot Dashboard</title>
<style>
body { font-family: Arial; background:#111; color:#eee; }
table { width:100%; border-collapse: collapse; }
th, td { padding:10px; border:1px solid #444; }
</style>
</head>
<body>
<h2>Honeypot Intrusion Logs</h2>
<table>
<tr>
<th>ID</th><th>IP</th><th>Port</th><th>Data</th><th>Timestamp</th>
</tr>
{% for log in logs %}
<tr>
<td>{{log[0]}}</td>
<td>{{log[1]}}</td>
<td>{{log[2]}}</td>
<td>{{log[3]}}</td>
<td>{{log[4]}}</td>
</tr>
{% endfor %}
</table>
</body>
</html>
"""

@app.route("/")
def dashboard():
    logs = get_logs()
    return render_template_string(template, logs=logs)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
