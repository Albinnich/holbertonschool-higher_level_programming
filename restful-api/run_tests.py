import subprocess
import time
import requests

server = subprocess.Popen(['python3', 'task_03_http_server.py'])

time.sleep(1)

try:
    requests.get('http://localhost:8000/')
    subprocess.run(['python3', 'test_03_http_server.py'])
finally:
    server.terminate()
