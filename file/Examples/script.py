#!/usr/bin/env python3
def main():
    infile = open('infile.txt', 'r')
    outfile = open('outfile.txt', 'w+')
    for line in infile:
        print(line, file = outfile, end = '')
    outfile.flush()
    outfile.seek(0, 0)
    content = outfile.read()
    print(content, end = '')
    print('\n\n' + '=' * 100 + '\n\n')

    fhr = open('bigfile.txt', 'r')
    bufferSize = 5000
    buffer = fhr.read(bufferSize)
    fhw = open('bigfile-copy.txt', 'w+')
    while len(buffer):
        fhw.write(buffer)
        print('.', end = '')
        buffer = fhr.read(bufferSize)
    print("\nDone.")
    fhw.seek(0, 0)
    for line in fhw:
        print(line, end = '')

    print('\n\n' + '=' * 100 + '\n\n')

    # We are using the buffered IO
    inFileHandle = open('olives.jpg', 'rb')
    # olives.jpg size is 142.3 kB (142309 bytes)
    bufferSize = 50000
    outFileHandle = open('olives_copy.jpg', 'wb')
    for line in inFileHandle.readlines():
        print(line, end = '')
    print('')
    inFileHandle.seek(0, 0)
    buffer = inFileHandle.read(bufferSize)
    while len(buffer):
        outFileHandle.write(buffer)
        print('.', end = '')
        buffer = inFileHandle.read(bufferSize)

    print('\nDone')

    inFileObject = open('video.mov', 'rb')
    bufferSize = 100000
    outFileObject = open('video-copy.mov', 'wb')
    for line in inFileObject:
        print(line, end = '')
    print()
    inFileObject.seek(0, 0)
    buffer = inFileObject.read(bufferSize)
    while len(buffer):
        outFileObject.write(buffer)
        print('.', end = '')
        buffer = inFileObject.read(bufferSize)

    print('\nDone')

if __name__ == "__main__": main()
