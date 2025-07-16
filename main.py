import re

def detect_brute_force(file_path, threshold=3):
    failed_logins = {}

    with open(file_path, 'r') as log:
        for line in log:
            if "Failed password" in line:
                ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if ip_match:
                    ip = ip_match.group(1)
                    failed_logins[ip] = failed_logins.get(ip, 0) + 1

    print("🔍 Potential Brute-Force Attempts:")
    for ip, count in failed_logins.items():
        if count >= threshold:
            print(f"[!] {ip} has {count} failed login attempts")

if __name__ == "__main__":
    detect_brute_force("logs/auth.log")

