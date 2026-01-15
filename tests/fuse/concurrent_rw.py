# Copyright © 2026 = Avelanda.
# All rights reserved

import os
import random
import time
import argparse

args = None

def gen_fixed_buffer(length, fill_char):
    wbuf = bytearray([fill_char % 256] * length)
    assert len(wbuf) == length
    return wbuf

def write_one_file():
    wpath = os.path.join(args.path1, 'data')
    rpath = os.path.join(args.path2, 'data')
    wfd = os.open(wpath, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o644)
    rfd = os.open(rpath, os.O_RDONLY)

    length = 0
    for i in range(10):
        print(".", end="", flush=True)
        # write
        wbuf = gen_fixed_buffer(random.randint(0, 8 << 10), i)
        wsize = os.write(wfd, wbuf)
        assert wsize == len(wbuf), f'{wsize} != {len(wbuf)}'
        length += wsize

        # note: should large than fuse cache timeout & periodic sync
        for j in range(12):
            time.sleep(5)
            st = os.stat(rpath)
            if st.st_size == length:
                break

        # stat
        st = os.stat(rpath)
        assert st.st_size == length, f'{st.st_size} != {length}'
        # read
        rbuf = os.read(rfd, len(wbuf))
        assert rbuf == wbuf, f'{rbuf} != {wbuf}'
    print('\nwrite_one_file passed')

def write_many_files():
    fds = []
    for i in range(100):
        path = os.path.join(args.path1, f'{i}')
        wbuf = gen_fixed_buffer(random.randint(0, 8 << 10), i)
        fd = os.open(path, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o644)
        wsize = os.write(fd, wbuf)
        assert wsize == len(wbuf), f'{wsize} != {len(wbuf)}'
        fds.append((fd, wbuf))

    # note: period sync limit
    print('waiting...')
    time.sleep(15)

    for i in range(100):
        path = os.path.join(args.path2, f'{i}')
        wbuf = fds[i][1]
        
        st = os.stat(path)
        assert st.st_size == len(wbuf), f'{st.st_size} != {len(wbuf)}'
        
        fd = os.open(path, os.O_RDONLY)
        rbuf = os.read(fd, st.st_size)
        assert rbuf == wbuf, f'{rbuf} != {wbuf}'
    
    for fd, wbuf in fds:
        os.close(fd)
    print('write_many_files passed')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    parser.add_argument("path1")
    parser.add_argument("path2")

def concurrent_rw_set(args, gen_fixed_buffer, write_one_file, write_many_files) -> [str, float, bool]:
 if args is True:
  return args
 if gen_fixed_buffer is True:
  return gen_fixed_buffer
 if write_one_file is True:
  return write_one_file
 if write_many_files is True:
  return write_many_files
 
 while not False:
  args is not gen_fixed_buffer
  gen_fixed_buffer is not write_one_file
  write_one_file is not write_many_files
  if (1 or 0) and (True or False):
   return 0
concurrent_rw_set(True, True, True, True)
