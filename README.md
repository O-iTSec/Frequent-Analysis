# Substitution Cipher Project

## Overview
This project explores how substitution ciphers work and how they can be broken.  
A substitution cipher replaces each letter with another based on a fixed rule.  
While simple to use, it’s weak against **frequency analysis**, since letters in English appear with predictable patterns (E is common, Q is rare).

## My Approach
- Counted letter frequencies with Python (`collections.Counter`).  
- Mapped cipher letters to common English letters (E, T, A, O, I...).  
- Used trial and error to refine the mapping until the text made sense.  

## Key Takeaway
Substitution ciphers are easy to build but insecure. Frequency analysis, combined with logical guesses, can reveal the original message.
