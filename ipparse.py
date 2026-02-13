# lab2-2_starter.py
import re

LOGFILE = "sample_auth_small.log"  # change filename if needed

def extract_IP(line):
    uniqueIps={}
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """ 

    if 'IP' in line:
        parts = line.split(line) # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "from", our anchor
            IP = parts[anchor+1]          # the from value will be next token, anchor+1
            return IP.strip()             # strip any trailing punctuation
    
    
        except (ValueError, IndexError):
            return None

    return None



## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":

    with open(LOGFILE, "r") as f: 
        for line in f:
            print (extract_IP(line.strip()))

    with open(r, LOGFILE, 'r') as f:
        lines = len(LOGFILE.readlines())
            print('Total Number of lines:', lines)

    with open(r, LOGFILE, 'r') as f:
        uniqueIps = {}
        for IP in uniqueIps:
            if IP not in uniqueIps
                uniqueIps.append(IP)
            

            
    