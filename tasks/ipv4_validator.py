import re

def validate_ipv4(ipv4):
    pattern = r'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    if re.match(pattern, ipv4):
        print("valid")
    else:
        print("invalid")

validate_ipv4(input())