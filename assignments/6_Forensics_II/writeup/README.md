# Writeup 6 - Forensics

Name: *Japneet Singh Arora*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Japneet Singh Arora*

## Assignment Writeup

### Part 1 (45 Pts)
1. Warmup: what IP address has been attacked? 
    The IP address that was attacked was `142.93.136.81`.

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.
    The hackers used the `SYN` post scan on TCP using nmap. This attack is very common to find vulnerable and open ports. 

3. What are the hackers' IP addresses, and where are they connecting from?
    The IP address of the hacker is `159.203.113.18`. They are connecting from Clifton, New Jersey.

4. What port are they using to steal files on the server?
    They are using port `20`.

5. Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,

    a) What kind of file is it?
        jpeg format image

    b) Where was this photo taken? Provide a country and city in your answer.
        The Hand, Rambla General Artigas, Punta Del Este, Maldonado, Uruguay

    c) When was this photo taken? Provide a timestamp in your answer.
        Sun, 23 December 2018 at 05:16:24 PM

    d) What kind of camera took this photo?
        Apple Iphone 8 (f/1.8 28mm focal length lens)
    
    e) How high up was this photo taken? Provide an answer in meters.
        4.5726 meters above sea level

6. Which file did the attackers leave on the server?
    greetz.fpff

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.
    Adding a firewall to disallow alien IP addresses and also setting complex passwords to avoid a brute force.

### Part 2 (55 Pts)

Parse `greetz.fpff`, and report the following information:
    1. When was `greetz.fpff` generated?
        Wednesday March 27 00:15:05 2019
    2. Who authored `greetz.fpff`?
        fl1nch
    4. List each section, giving us the data in it *and* its type.
        | Section |    Type   |  Length  |  Value |
        |    1    | ASCII 0x1 |    24    |  Hey you, keep looking :) |
        |    2    | COORD 0x6 |    0x6   |  (52.336035, 4.880673)    |
        |    3    | PNG 0x8   |   202776 |          Testudo          |
        |    4    | ASCII 0x1 |     44   | }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC |
        |    5    | ASCII 0x1 |     80   | Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30 |

    5. Report *at least* one flag hidden in `greetz.fpff`. Any other flag found will count as bonus points towards the *competition* portion of the syllabus.
        I found three flags as follows:
            1. Printed on embedded PNG image
                CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}
            2. Value for section 4 in reverse
                CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}
            3. Decoded base64 value for section 5
                CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}
