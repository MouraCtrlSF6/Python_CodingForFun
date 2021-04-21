word = input("Type a sentence: ")
n_word = list(word)
f=0
words=0

for i in range(len(word)):
    if word[i]>='a' and word[i]<='z' or word[i]>='A' and word[i]<='Z':
        if f==0:
            f=1
            words += 1 
            if word[i]>='a' and word[i]<='z':
                n_word[i] = chr(ord(word[i])-32)
        elif word[i]>='A' and word[i]<='Z':
            n_word[i] = chr(ord(word[i])+32)
    elif word[i]==' ':
        f=0
word = ''.join(n_word)
print(f"NewSentenceIs: {word} \nAndItHas: {words} words.\n")

