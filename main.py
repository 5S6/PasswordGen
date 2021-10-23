import random
import threading
import time



def lettergen():
    length = random.randint(5, 6) #set your min and max (min, max)
    eval = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    return ''.join(random.choice(eval) for i in range(length))

def numbergen():
    length = random.randint(4, 5) #set your min and max (min, max)
    eval = "1","2","3","4","5","6","7","8","9","0"



    return ''.join(random.choice(eval) for i in range(length))


def main():
    
    
    
    
    final_pass = lettergen() + numbergen() + lettergen() + numbergen()

    print(final_pass)

    f1 = open("./output/passes.txt", "a+")
    f1.write(f"{final_pass}\n")
    f1.close
    


threads=[]


for i in range(100000):
  t = threading.Thread(target = main)
  t.Daemon = True
  threads.append(t)

for i in range(100000):
  threads[i].start()
  time.sleep(0.2)

for i in range(100000):
  threads[i].join()
