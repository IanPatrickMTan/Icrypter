import sys

def shift(x, y):
    if x + y < 0:
        return x + y + 256
    elif x + y > 255:
        return x + y - 256
    else:
        return x + y

if len(sys.argv) > 1:
    if len(sys.argv) == 4:
        fileDir, key, enc = sys.argv[1:]
    else:
        print('Wrong number of arguments, you need 3 (e.g. test.txt 10-10-10 y)')
        exit()
    try:
        key = key.split('-')
    except:
        print('Invalid key entered, please try again with a valid key.')
        exit()
    y = False
    for x in range(3):
        try:
            key[x] = int(key[x])
        except:
            y = True
    if y:
        print('Invalid key entered, please try again with a valid key.')
        exit()
    if not enc in ['Y', 'y', 'N', 'n', '']:
        print('Invalid option selected, please select again.')
else:
    fileDir = input('Dir: ')
    while True:
        try:
            key = input('Key: ').split('-')
            y = True
            for x in range(3):
                try:
                    key[x] = int(key[x])
                except:
                    y = False
            if y:
                break
            else:
                print('Invalid key entered, please try again with a valid key.')
        except:
            print('Invalid key entered, please try again with a valid key.')

    while True:
        enc = input('Are you encoding? (Y/n): ')
        if enc in ['Y', 'y', 'N', 'n', '']:
            break
        else:
            print('Invalid option selected, please select again.')
enc = True if enc in ['Y', 'y', ''] else False

print(f'Opening {fileDir}...', end = '')
try:
    targetFile = open(fileDir, 'rb')
    fileData = list(targetFile.read())
    targetFile.close()
    print('\033[92m   [OK]\033[0m')
except:
    print('\033[91m   [FAILED]\033[0m')
    exit()
print(f'{"Encrypting..." if enc else "Decrypting..."}\n\n[--------------------------------------------------] 0/{len(fileData)}', end = '\r')

n = int(key[0])
if enc:
    for x in range(len(fileData)):
        fileData[x] = shift(fileData[x], n % 256)
        n = (n * key[1] + key[2])
        p = int((x + 1) / len(fileData) * 50)
        print(f"[{'#' * p}{'-' * (50 - p)}] {x}/{len(fileData)}", end = '\r')
else:
    for x in range(len(fileData)):
        fileData[x] = shift(fileData[x], -(n % 256))
        n = (n * key[1] + key[2])
        p = int((x + 1) / len(fileData) * 50)
        print(f"[{'#' * p}{'-' * (50 - p)}] {x}/{len(fileData)}", end = '\r')

print(f'\n\n\033[92m{"[FILE ENCRYPTED]" if enc else "[FILE DECRYPTED]"}\033[0m\n\nWriting to {fileDir}...', end = '')
try:
    targetFile = open(fileDir, 'wb')
    targetFile.write(bytes(fileData))
    targetFile.close()
    print('\033[92m   [OK]\033[0m')
except:
    print('\033[91m   [FAILED]\033[0m')
    exit()
