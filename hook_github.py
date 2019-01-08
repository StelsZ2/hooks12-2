#!usr/bin/env python3
import sys, re
comMesFile = open(sys.argv[1])
comMes = comMesFile.read().strip()
dlug = 50
if (len(comMes)) > dlug:
    print("nie pasuje")
    sys.exit(1)
print("pasuje")
sys.exit(0)
