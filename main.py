import time
import math
import docx


def readFile(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def findReverseNumber(a, m):
    k = -1
    b = 1
    while (a * b) % m != 1:
        b += 1
    return b


def encryptAffineCifer(text, a, b, alphabet):
    encryptedText = ""
    for s in text:
        if s in alphabet:
            encryptedText += alphabet[(alphabet.index(s)
                                       * a + b) % len(alphabet)]
        else:
            encryptedText += s
    return encryptedText


def doubleEncryptAffineCifer(text, a1, b1, a2, b2, alphabet):
    return encryptAffineCifer(encryptAffineCifer(text, a1, b1, alphabet), a2, b2, alphabet)


def decryptAffineCifer(text, a, b, alphabet):
    decryptedText = ""
    reverseA = findReverseNumber(a, len(alphabet))
    for s in text:
        if s in alphabet:
            decryptedText += alphabet[(reverseA * (alphabet.index(s) +
                                                   len(alphabet) - b)) % len(alphabet)]
        else:
            decryptedText += s
    return decryptedText


def doubleDecryptAffineCifer(text, a1, b1, a2, b2, alphabet):
    return decryptAffineCifer(decryptAffineCifer(text, a2, b2, alphabet), a1, b1, alphabet)


def hackAffineCifer(encryptedText, originalText, alphabet, keys):
    generated = [i + 1 for i in range(len(alphabet))]
    decryptedText = ""
    for a1 in keys:
        for b1 in keys:
            for a2 in keys:
                for b2 in keys:
                    hackedText = doubleEncryptAffineCifer(
                        originalText, a1, b1, a2, b2, alphabet)
                    if encryptedText == hackedText:
                        print('Hacked')
                        print(originalText)
                        return [a1, b1, a2, b2]
    return decryptedText


def main():
    alphabet = "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя"
    keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
            59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

    a1 = 7
    b1 = 11
    a2 = 19
    b2 = 17

    text = readFile('./input.docx')
    print("Вхідний текст: ")
    print(text)

    startTime = time.perf_counter_ns()
    encryptedText = doubleEncryptAffineCifer(
        text, a1, b1, a2, b2, alphabet)

    print("Час шифрування: ", (time.perf_counter_ns() - startTime)/1000000)
    print('\nЗашифрований текст:', '\n')
    print(encryptedText)

    startTime = time.perf_counter_ns()
    decryptedText = doubleDecryptAffineCifer(
        encryptedText, a1, b1, a2, b2, alphabet)
    print("Час розшифрування: ", (time.perf_counter_ns() - startTime)/1000000)
    print('Розшифрований текст', '\n')
    print(decryptedText)

    startTime = time.perf_counter_ns()
    hackAffineCifer(encryptedText, text, alphabet, keys)
    print("Час злому: ", (time.perf_counter_ns() - startTime)/1000000)


main()
