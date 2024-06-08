import subprocess
import time
import requests

def wait_for_server(url, timeout=10):
    for _ in range(timeout):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.ConnectionError:
            time.sleep(1)
    return False

server = subprocess.Popen(['python3', 'task_03_http_server.py'])

time.sleep(2)

if wait_for_server('http://localhost:8000/'):
    try:
        subprocess.run(['python3', 'test_03_http_server.py'], check=True)
    finally:
        server.terminate()
else:
    print("Server did not start successfully.")
    server.terminate()
