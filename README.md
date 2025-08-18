# Caesar Cipher Cryptanalysis Tool  

A simple but extended Caesar cipher encoder/decoder with brute-force and cryptanalysis options.  
Supports both English and Italian.  

## Features
- Encode any text with Caesar shift.  
- Brute-forces and prints all 25 possible decryptions.  
- Dictionary + frequency analysis scoring (Italian or English).
- Possibility to choose which analysis is more important in "evaluation" function
- Outputs scores that indicate the most likely plaintext.  

## Example for encrypting
Input: "ILOVEPIZZA" Shift: "3"
Output: "LORYHSLCCD"

## Example for decrypting
Input: "LORYHSLCCD"
Output: 3  : ILOVEPIZZA - 534.610

## What next
Vigenère and polyalphabetic ciphers.
