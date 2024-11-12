from django.http import HttpResponse
import os
from datetime import datetime
import subprocess
from django.views import View 
# Create your views here.

class htopView(View):
    def get(self, request):
        name = "Sai Rohith Tadangi"
        username = "sairohith"
        server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

        return HttpResponse(f"""<h1>System Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <pre><strong>Top Output:</strong>\n{top_output}</pre>""")