n=str(input("enter the text"))
x=int(input("enter the key value"))
print("cipher text")
for i in n:
    if i.isalpha():
        cipher=chr((ord(i)-ord('a' if i.islower() else 'A') +x)%26+ord('a' if i.islower() else 'A'))
        print(cipher,end="")
    else:
        print(i,end="")
      
