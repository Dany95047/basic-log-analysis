"""
Minimal EVTX parse script so GitHub language stats detect Python.
"""

from Evtx.Evtx import Evtx

def peek_evtx(path):
    with Evtx(path) as evtx:
        for i, record in enumerate(evtx.records()):
            print(record.xml())
            if i >= 2:
                break

if __name__ == "__main__":
    print("This script demonstrates EVTX parsing in Python.")
    print("Run peek_evtx('data/Security.evtx') to preview first records.")