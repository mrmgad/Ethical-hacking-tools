import requests

target_url = "https://www.eservices.gov.et/en"
# A small sample wordlist, or load from a file
wordlist = ["admin", "login", "api", "uploads", "test", "robots.txt","auth/login"]

def scan_directories(url, words):
    print(f"[*] Scanning {url}...")
    
    count = 0
    
    with open("/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt") as file:
        for word in file:
            word = word.strip()
            print(word)
            count += 1
            # Construct the full URL
            full_url = f"{url}/{word}"
           # print(f"{count} => {url}/{word}")
            try:
                # Send the request (verify=False ignores SSL issues)
                response = requests.get(full_url, timeout=5, verify=False)
                
                # Check the status code
                if response.status_code == 200:
                    print(f"[+] Found: {full_url} (Status: 200)")
                elif response.status_code == 403:
                    print(f"[!] Forbidden: {full_url} (Status: 403)")
                    
            except requests.exceptions.RequestException as e:
                print(f"[!] Error connecting to {full_url}: {e}")

if __name__ == "__main__":
    # Suppress insecure request warnings if using verify=False
    requests.packages.urllib3.disable_warnings()
    scan_directories(target_url, wordlist)
