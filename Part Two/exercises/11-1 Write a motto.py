motto = open("motto.txt", 'a')
motto.close()
motto = open("motto.txt", "w")
motto.write("Fiat Lux!\n")
motto.close()

try:
    motto = open("motto.txt", "r")
    print(motto.read())
    motto.close()
    motto = open("motto.txt", "a")
    motto.write("let there be light!\n")
    motto.close()
    print("------")
    print("appended \" let there be light!\" to motto.txt")
    print("------")
    motto = open("motto.txt", "r")
    print(motto.read())
    motto.close()
except IOError:
    print("File not found. Please ensure the file exists.")