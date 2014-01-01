# multi processing

from subprocess import Popen
import os

def children(num, div):
    fnames = 'div%d_%d_%d'
    chunk = num // div
    children = []
    for i in range(div - 1):
        fname = fnames % (num, div, i)
        if os.path.isfile(fname + '.npy'):
            print 'Chunk', i, 'already computed'
            continue
        print "Spawning", fname, chunk * i, 'to', chunk * (i + 1)
        children.append(Popen(['python', 'gen.py', str(chunk * (i + 1)), fname, str(chunk * i)]))
    fname = fnames % (num, div, i + 1)
    if not os.path.isfile(fname + '.npy'):
        print "Spawning", fname, chunk * (i + 1), 'to', num
        children.append(Popen(['python', 'gen.py', str(num), fname, str(chunk * (i + 1))]))
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
        print 'Usage: multi.py num divisions'
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
    children(number, divisions)

if __name__ == '__main__':
    main()

