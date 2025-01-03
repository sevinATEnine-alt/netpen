import hashlib, time
testingHash = "04cac6b295ad3f6b11e6c1ac67ce5a8bd24b04aca5f6a515767bcf7431365de6"
i = 0

init = time.time()

print('Started')
print(f'Start: {init}')

while i < 1000000:
    modi =  str(i).rjust(6, '0').encode()
    test = hashlib.sha256(modi).hexdigest()
    if(test == testingHash):        
        print(f"FOUND!\n\n{test}\n{modi}")
        finish = time.time()
        print(f'Finish: {finish}')
        print(f'Elapsed: {finish-init}')
        break
    i += 1

