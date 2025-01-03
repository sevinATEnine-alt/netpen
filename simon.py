import hashlib, threading, itertools, time

password = 0
toBeCracked = "04cac6b295ad3f6b11e6c1ac67ce5a8bd24b04aca5f6a515767bcf7431365de6"

def cracker():
    global password
    while True:
        password += 1
        p = str(password-1).rjust(6,"0")
        if (toBeCracked == hashlib.sha256(p.encode()).hexdigest()):
            print(f"FOUND!\n\n{p}\n{toBeCracked}")
            finish = time.time()
            print(f'Finish: {finish}')
            print(f'Elapsed: {finish-init}')
            quit()

print('Initializing')

threads = []

init = time.time()

print('Started')
print(f'Start: {init}')

for i in range(0, 10):
   thread = threading.Thread(target=cracker)
   thread.start()
   threads.append(thread)

for thread in threads:
   thread.join()