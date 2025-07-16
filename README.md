# SOC Log Event Analyzer

This Python project analyzes SSH log files to detect potential brute-force login attempts by tracking failed login attempts from IP addresses.

## Features

- Parses SSH log files for failed login attempts
- Detects IP addresses with repeated failed logins
- Helps SOC analysts identify suspicious activity quickly

## How to Run

1. Clone the repository  
2. Make sure you have Python 3 installed  
3. (Optional) Create and activate a virtual environment  
4. Run the script:

```bash
python main.py

🔍 Potential Brute-Force Attempts:
[!] 192.168.1.10 has 4 failed login attempts

 
