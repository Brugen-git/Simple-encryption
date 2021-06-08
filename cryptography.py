
import string
#swaps two letters to encrypt the message
wswap2 = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','BADCFEHGJILKNMPORQTSVUXWZYbadcfehgjilknmporqtsvuxwzy')
def crypt(text):
   return text.translate(wswap2)
def main():
   while True:
    print("Menu Driven Program")
    print("1.Encrypt a message")
    print("2.Decrypt a message")   
    print("3.Exit")
    choice=int(input("Enter your choice:")) 
    if choice==1:
        text = input("Enter your message: ")
        print("Encrypted message:",crypt(text))
    elif choice==2:
        text = input("Enter encrypted message: ")
        print("Decrypted message:",crypt(text))
    elif choice==3:
        break

if __name__ == "__main__":
    main()

 