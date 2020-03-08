# Public key generation
## Overview
---------------
Implement the Encryption-Decryption scheme described in this [paper](https://www.tandfonline.com/doi/abs/10.1080/09720529.2015.1085738) and analyze ways to generate a Generator Matrix to boost security.
## Introduction
---------------
The main aim of this project is to develop a python library implementing said scheme and devloping it further over time
## Prerequisites
----------------
* Python 3.6.7
* Numpy 1.18.1

## Usage
### Encryption
```python
# To encrypt
from public_key import PublicKeyCrypto

p = PublicKeyCrypto()

p.encrypt(plain_text="PutPtextwithoutspaces")
```
### Decryption
```python
# To decrypt
from public_key import PublicKeyCrypto

p = PublicKeyCrypto()

p.decrypt(c1="cipher1.npy",c2="cipher2.npy",keys = "key.npy")
```