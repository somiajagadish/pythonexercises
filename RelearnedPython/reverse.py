def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        print(str(word))
        l -= 1
    return word
  
print(str(reverse("Hello World")))