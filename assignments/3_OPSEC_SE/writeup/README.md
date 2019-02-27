# Writeup 3 - Operational Security and Social Engineering

Name: *Japneet Singh Arora*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *Japneet Singh Arora*

## Assignment Writeup

### Part 1 (40 pts)
I would pose as an IT guy from her own company and send her an email on the address i found on the bank's website. Since, she is the CEO it is very likely she wont rember all of her employees name. I would say in the email tht we had a security breach and i believe that some bank details were leaked and one could obviously be yours. I would then tell her to call me on the phone number as soon as she recieves this email. the phone number i would provide would be using a VoIP which is linked over Skype with a throaway email. Once she makes a call i would use a background noise with a lot of phones ringing and people responding, so that it feels like the majority of the department is busy with the same issue. I would then try to connect on an emotional level, by saying that it has been a very busy day since we are not sure how many accounts are leaked and i haven't had breakfast or lunch. Once she sympathises with me being a senior employee, I would make my move. I would then ask her some securoty questions that is the most common method of retrieving password. Since most people dont remember their security questions i would try to get her mother's maiden name, city she was born and her pet's name in a means to try get her account details. Once this is done i would ask her what browser she is working with. Then i will prompt her to open up her back account and ask her i she sees any fraudlent transactions. Obviosuly there would be no such transaction and she would say no, then i would simply ask her for her atm pin and act like i am changing it but then i would make a excuse that the site is down and you can change it on your own time.

### Part 2 (60 pts)

1337Bank's server had a lot of vulnerabilities. 
1. The most vulnerable was the password and the username. Running such a big bank requires one to carefully use usernames. What Elizabeth did wrong was use the same username for her professional and personal accounts. She also used very easy and sensitive password. A strong password includes atleast 12 characters with a mix of uppercase, lowercase, special characters and numbers. 

2. This follows the last one. The open port had unlimited tries for password. This gives the hacker the upper hand when trying to crack the password this is becasue he can brute force as much as he wants like in our case by using a python script. The best thing woould be to implement an account lockdown on password tries greater than three. Apart from brute force the hacker could also use attacks such as SQL injection and XSS attacks, these types of attack interfere with the database and a web server should always be ready for these kinds of attacks as well. To protect against these attacks you could use several open source software like Netsparker, OpenVAS, Xenotix XSS which provide security against attacker methods.

3. The open port 1337 was also one of the biggest mistake. Such a big company should never leave open ports and that too the one that gives out login access. One way to prevent that is to use HTTPS, which gurantees that only those users are talking to the server that it expects, i.e nobody can intercept or change the content they are seeing.
Another possible thing is using Firewall. There are many types of firewalls such as packet layer, circuit level, application layer. The most beneficial wouldbe application layer which would allow only valid data at the application level before connecting. Another helpful step would be setting up IDS. IDS stands for Intrusion Detection System,it sends out early warnings to system administrators. 

Sources:
[https://www.pandasecurity.com/usa/support/card?id=31463](https://www.pandasecurity.com/usa/support/card?id=31463)
[https://www.owasp.org/index.php/Blocking_Brute_Force_Attacks](https://www.owasp.org/index.php/Blocking_Brute_Force_Attacks)
[https://www.itproportal.com/2008/03/26/what-firewall-do-and-what-firewalls-dont-do/](https://www.itproportal.com/2008/03/26/what-firewall-do-and-what-firewalls-dont-do/)
[https://www.creativebloq.com/web-design/website-security-tips-protect-your-site-7122853]
(https://www.creativebloq.com/web-design/website-security-tips-protect-your-site-7122853)