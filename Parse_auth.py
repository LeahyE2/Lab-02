# lab2.3_starter.py
import json
from collections import defaultdict
from datetime import datetime

LOGFILE = "sample_auth_small.log"

def parse_auth_line(line):
    """
    Parse an auth log line and return (timestamp, ip, event_type)
    Example auth line:
    Mar 10 13:58:01 host1 sshd[1023]: Failed password for invalid user admin from 203.0.113.45 port 52344 ssh2
    We will:
     - parse timestamp (assume year 2025)
     - extract IP (token after 'from')
     - event_type: 'failed' if 'Failed password', 'accepted' if 'Accepted password', else 'other'
    """
    parts = line.split()
    # timestamp: first 3 tokens 'Mar 10 13:58:01'
    ts_str = " ".join(parts[0:3])
    try:
        ts = datetime.strptime(f"2025 {ts_str}", "%Y %b %d %H:%M:%S")
    except Exception:
        ts = None
    ip = None

    event_type = "other"
    if "Failed password" in line:
        event_type = "failed"
    elif "Accepted password" in line or "Accepted publickey" in line:
        event_type = "accepted"
    if " from " in line:
        try:
            idx = parts.index("from")
            ip = parts[idx+1]
        except (ValueError, IndexError):
            ip = None
    return ts, ip, event_type

    
if __name__ == "__main__":
    per_ip_timestamps = defaultdict(list)
    with open(LOGFILE) as f:
        for line in f:
            ts, ip, event = parse_auth_line(line)
            print('X', ts,ip,event)
    
            print(str (ts))

            if ts and ip and event == "failed":   # checks that ts and ip are not null, and that event=="failed"
                ts_str = ts.strftime("%b %d %H:%M:%S") #Formats the timestamp as "Mar 10 13:45:01"
                per_ip_timestamps[ip].append(ts_str)

                
    
    for ip, times in per_ip_timestamps.items():
        
        print(json.dumps(per_ip_timestamps,indent=2)) # This prints the contents of the dictionary in a ledgible format
                                                # indent=2 means that each level of the dictionary is indented by 2 spaces               
    
    
    
    