import os, sys, json, time, random, sqlite3, pymysql, traceback, zlib, asyncio, urllib.request, threading
start = time.time()
# Others
#sys.dont_write_bytecode = True
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))

import modules as module

# Imports Components