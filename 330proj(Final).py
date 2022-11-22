#Take an input using symbols 0-9 and checks if the unlock and lock code are in the string
#Use "if code in input", unlock = "949271" lock = "949274"
#Can use raw_input() for a input directly into a string or input() for a direct type 
#display status of locked and unlocked
import random
import time
NO_OF_CHARS = 248
def NextState(pattern, M, state, x):
	if state < M and x == ord(pattern[state]):
		return state+1

	i=0
	for ns in range(state,0,-1):
		if ord(pattern[ns-1]) == x:
			while(i<ns-1):
				if pattern[i] != pattern[state-ns+1+i]:
					break
				i+=1
			if i == ns-1:
				return ns
	return 0

def createTable(pattern, M):
	global NO_OF_CHARS

	TU = [[0 for i in range(NO_OF_CHARS)]\
		for _ in range(M+1)]

	for state in range(M+1):
		for x in range(NO_OF_CHARS):
			z = NextState(pattern, M, state, x)
			TU[state][x] = z

	return TU

def search(pattern, txt):
    global NO_OF_CHARS
    U = len(pattern)
    N = len(txt)
    UT = createTable(pattern, U)
    status = "Locked"
    state = 0
    for i in range(N):
        state = UT[state][ord(txt[i])]
        if state == U:
            if txt[i-U+6] == '1' and status == "Locked":
                status = "unlocked"
                print("Unlocked at index: " + format(i-U+1))
            elif txt[i-U+6] == '4' and status == "unlocked":
                status = "Locked"
                print("Locked at index: " + format(i-U+1))
            
def manual():
    Un = "94927"
    inp = input("Enter A Code: ")
    bap = inp.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,./=-+_!@#$%^&*() :;[]{\}|`~'})
    print(bap)
    search(Un, bap)

def tester():
    status = "Locked!"
    tap = ""
    Ct = 0
    unlock = "949271"
    while status == "Locked!":
        tap = tap + random.choice(["0","1","2","3","4","5","6","7","8","9"])
        if len(tap) == 24:
            print(tap)
            if unlock in tap:
                status = "Unlocked!"
                search(unlock, tap)
                print("It took " + str((Ct * 12)) + " entries till Lock was broken!")
            tap = ""
            Ct = Ct + 1

def main():
    status = True
    while status:
        inp = input("Enter 'Manual' for manual entry \nor 'Forced' for forced entry \nor Enter 'Exit' to exit the program:")
        if inp == "Manual" or inp == "manual":
            manual()
            status = False
            time.sleep(10)
        elif inp == "Forced" or inp == "forced":
            tester()
            time.sleep(10)
            status = False
        elif inp == "Exit" or inp == "exit":
            status = False
            print("Goodbye!")
            time.sleep(5)
        

main()



        

