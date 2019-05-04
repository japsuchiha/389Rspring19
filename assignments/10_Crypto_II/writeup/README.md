# Crypto II Writeup

Name: *Japneet Singh Arora*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Japneet Singh Arora*

## Assignment Writeup

### Part 1 (70 Pts)
Flag: CMSC389R-{m3ss@g3_!n_A_b0ttl3}

### Part 2 (30 Pts)

1.  My observation for the two images is that in the first one that is ecb we can still tell that there are two shapes and can figure something out but for the second one we can't say anything since its all noisy and grainy.

2.  ECB is much less secure than CBC since ECB is essentially the first generation of the AES and is the most basic form of cipher encryption. ECB concatenates each previous block with the next block which makes it simple to use. On the other hand in CBC, each ciphertext block is dependent on all plaintext blocks processed upto that point. This adds an extra level of complexity to the encrypted data.