import subprocess
import re

def validate_hostname(hostname):
    pattern = re.compile(
        r'^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*'
        r'([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$|'
        r'^\d{1,3}(\.\d{1,3}){3}$'
    )
    return re.match(pattern, hostname)

def run_ping(hostname, count):
    result = subprocess.run(
        ['ping', '-c', str(count), hostname],
        capture_output=True,
        text=True
    )
    return result.stdout

def run_dig(hostname, record_type):
    if record_type == "PTR":
        result = subprocess.run(
            ['dig', '-x', hostname],
            capture_output=True,
            text=True
        )
    else:
        result = subprocess.run(
            ['dig', record_type, hostname],
            capture_output=True,
            text=True
        )
    return result.stdout

