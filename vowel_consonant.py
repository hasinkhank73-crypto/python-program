ch = input("Enter a character:")
ch = ch[0].lower()

if ch in('a', 'e', 'i', 'o', 'u'):
  print(ch, "is a vowel")
else:
  print(ch, "is a consonant")
