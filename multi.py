# multi processing

from subprocess import Popen
import os

def children(num, div, start = 0):
    fnames = 'div%d_%d_%d_%d'
    chunk = (num - start) // div
    children = []
    for i in range(div - 1):
        fname = fnames % (num, div, start, i)
        if os.path.isfile(fname + '.npy'):
            print 'Chunk', i, 'already computed'
            continue
        print "Spawning", fname, start + chunk * i, 'to', start + chunk * (i + 1)
        children.append(Popen(['python', 'gen.py', str(start + chunk * (i + 1)), fname, str(start + chunk * i)]))
    fname = fnames % (num, div, start, i + 1)
    if not os.path.isfile(fname + '.npy'):
        print "Spawning", fname, start + chunk * (i + 1), 'to', num
        children.append(Popen(['python', 'gen.py', str(num), fname, str(start + chunk * (i + 1))]))
    done = 0
    while done < len(children):
        for i in range(len(children)):
            if type(children[i]) is int:
                continue
            r = children[i].poll()
            if r is not None:
                print "Child", i, "exited with", r
                done += 1
                children[i] = r
    print "Done!"

def main():
    import sys
    if len(sys.argv) < 3:
        print 'Usage: multi.py num divisions [start]'
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except:
        print 'First argument must be an integer'
        sys.exit(2)
    try:
        divisions = int(sys.argv[2])
    except:
        print 'Second argument must be an integer'
        sys.exit(3)
    start = 0
    try:
        start = int(sys.argv[3])
    except:
        print 'Third argument must be an integer'
        sys.exit(4)
    children(number, divisions, start)

if __name__ == '__main__':
    main()

