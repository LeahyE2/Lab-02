import re

pattern = r"\d+\.\d+\.\d+\.\d+"
line = "Failed password for invalid user bob from 10.0.0.5"
re.search(pattern, line) 

with open('auth.log', 'r') as f:
    content = f.read() 
    print(content)

    ips = [] 
    found_ips = []

    for ip in content:
        ips.append(ip) #adds each ip to the list

    unique_ips = set(ips)

    print("Unique IPs: ", unique_ips)
    for ip in unique_ips:
        print(ip)

with open('unique_ips.txt', 'w') as f: #f is file handle 'w'used to write to a file
    f.write(ip)
        



