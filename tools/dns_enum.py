import socket
import time



subdomains = [
    "www", "mail", "smtp"
]

ports = [80,21,22,25,443]

domain = "dagicomputers.com"

sub_list = []

def info(domain):
    ip = socket.gethostbyname(domain)

    print(f"[+] Starting Dns Enumiration In {domain} ---> Ip : {ip[2][0]}")

    info = socket.getaddrinfo(domain,None)

    print(f"{len(info)} infos has been collected.")

    for i in info:
        print(i[4])

def subdoami(domain):
    global sub_list
    count = 0
    valid = 0
    fdomain = ""
    print(f"[+] Starting finding sub domains on {domain}")
    for i in subdomains:
        try:

            fdomain = i + "." + domain
            print(f"Found : {fdomain} , Ip : {socket.gethostbyname(fdomain)}")

            sub_list.append(fdomain)

            
            valid += 1
        except socket.gaierror:
            print(f"Not found. {fdomain}")
            pass
        count += 1
        time.sleep(0.5)
    print(f" {valid} subdomains found out of {count}")


# info(domain=domain)

subdoami(domain=domain)

def port(list,port):

    
    
    for i in list:
        print(f"starting scanning  on {i}")
        for l in port:
                    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    soc.settimeout(1)
                    res = soc.connect_ex((i,l))
                    

                    


                    if res == 0:
                        try:
                            banner = soc.recv(1024).decode('utf-8', errors='ignore').strip()
                            # print(banner)
                            if banner:
                                print(f"\n{i}'s Port {l} is open. ---> {banner}")
                            else:
                                print(f"\n{i}'s Port {l} is Open.")

                             
                        except:
                            print(f"\n{i}'s Port {l} is Open.")
                    else:
                        print(f"{i} : Closed {l}")
port(sub_list,ports)