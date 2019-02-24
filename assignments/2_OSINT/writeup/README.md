# Writeup 2 - OSINT

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 pts)

1. What is `v0idcache`'s real name?
    * Elizabeth Moffet
2. Where does `v0idcache` work? What is the URL to their website?
    * She works at 1337bank.money. Website URL: [1337bank.money](http://1337bank.money/)
3. List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.
    * Her name is Elizabeth Moffet. Searched the username at very common websites such as Fb, github, twitter and got lucky with twitter.
    * She is a CEO at 1337bank.money.
    * Email: v0idcache@protonmail.com From website
    * Github: [https://github.com/v0idcache](https://github.com/v0idcache)
    * Twitter: [https://twitter.com/v0idcache](https://twitter.com/v0idcache). Follows UMD CSEC
    * Pastebin: Has a pastebin friend called fl1nch.
    * Address: Leeteinde 12, Broek, Waterland, 1151 AK, NL. did a search on [https://centralops.net/](https://centralops.net/co/DomainDossier.aspx). Which gave me the DNS provider and then ran a whois ` whois -h whois.namecheap.com "1337bank.money"` on the URL.
4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
    * 142.93.136.81
5. List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.
    * One was the robots.txt which was in the `/secret directory` on the website.
    * CMSC389R-{h1dd3n_1n_plain_5ight}. Found this on the website by doing inspect element.
    * CMSC389R-{h1ding_fil3s_in_r0bots_L0L}. Found this in robots.txt
6. What ports are open on the website? What services are running behind these ports? How did you discover this?
    * open ports are 80, 22 and 1337. Found this by running `nmap -sV`.
7. Which operating system is running on the server that is hosting the website? How did you discover this?
    * Ubuntu. Found this by running `nmap -O <ip-address>`
8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
    * CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}. Found this by running the DNS here [https://centralops.net/co/](https://centralops.net/co/)

### Part 2 (75 pts)
    For this part i made a new script `brute.py` and ran it through `rockyou.txt`.
    I found the password to be `linkinpark`. Tested it by doing `nc 142.93.136.81 1337` and logged using the credentials.
    Also found another flag CMSC389r-{brut3_f0rce_m4ster} inside the files folder whcih was in the `/home` directory.
