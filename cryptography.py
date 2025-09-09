from collections import Counter

def break_cipher(encrypted_msg, letter_map):
    """Take encrypted text and swap letters based on our best guesses"""
    result = ""
    for char in encrypted_msg.upper():
        if char in letter_map:
            result += letter_map[char]
        else:
            result += char
    return result

def crack_substitution(encrypted_text):
    """Break a substitution cipher by analyzing letter frequencies"""
    # Most common English letters in order (based on typical usage)
    common_letters = "ETANOISHRDLCFMUPYBKGVXWQ"
    
    # Strip out everything except letters and make uppercase
    letters_only = ""
    for c in encrypted_text:
        if c.isalpha():
            letters_only += c.upper()
    
    # Count how often each letter appears
    letter_counts = Counter(letters_only)
    
    # Get cipher letters sorted by how frequently they appear
    sorted_cipher_letters = ""
    for letter, count in letter_counts.most_common():
        sorted_cipher_letters += letter
    
    # Match most frequent cipher letters to most common English letters
    substitution_map = {}
    for i in range(len(sorted_cipher_letters)):
        cipher_letter = sorted_cipher_letters[i]
        if i < len(common_letters):
            substitution_map[cipher_letter] = common_letters[i]
        else:
            # If we run out of common letters, just use 'Z'
            substitution_map[cipher_letter] = 'Z'
    
    # Try to decrypt the message
    decrypted = break_cipher(encrypted_text, substitution_map)
    
    return decrypted, substitution_map

# Test it out with some encrypted text
mystery_text = "lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"

# Run the attack
cracked_message, letter_mappings = crack_substitution(mystery_text)

print("Original encrypted text:")
print(mystery_text)
print("\nLetter substitutions we figured out:")
print(letter_mappings)
print("\nWhat we think the message says:")
print(cracked_message)