import sys

def add(x,y):
    return x+y    

def main():
    if len(sys.argv) == 3:
        print(add(int(sys.argv[1]),int(sys.argv[2])))
        #return (int(sys.argv[1])+int(sys.argv[2]))
    else:
        print("ERROR:",str(len(sys.argv)-1)," arguments given instead of 2")

if __name__ == "__main__":
    main()

