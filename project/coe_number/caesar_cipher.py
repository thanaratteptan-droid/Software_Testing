def caesarCipher(s, k):
    result = []
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + k) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return "".join(result)