# -*- coding: utf-8 -*-

#!/usr/bin/env python
import RPi.GPIO as GPIO
import MFRC522


def write_text(Sector, text):

    # Keys
    DEFAULT_KEY = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

    # Selecting key
    KEY = DEFAULT_KEY

    def format_uid(uid):
        s = ""
        for i in range(0, len(uid)):
            s += "%x" % uid[i]
        return s.upper()

    RFID = MFRC522.MFRC522()

    print "# RFID Writer\n"
    print "Info: Leave the sector field empty to exit.\n"

    while True:
        (status, TagSize) = RFID.Request(RFID.PICC_REQIDL)

        if status != RFID.MI_OK:
            continue

        if Sector < 1 or Sector > (TagSize - 1):
            print "Sector out of range (1 - %s)\n" % (TagSize - 1)
            break

        # Selecting blocks
        BaseBlockLength = 4
        if Sector < 32:
            BlockLength = BaseBlockLength
            StartAddr = Sector * BlockLength
        else:
            BlockLength = 16
            StartAddr = 32 * BaseBlockLength + (Sector - 32) * BlockLength

        BlockAddrs = []
        for i in range(0, (BlockLength - 1)):
            BlockAddrs.append((StartAddr + i))
        TrailerBlockAddr = (StartAddr + (BlockLength - 1))

        # Initializing tag
        (Status, UID) = RFID.Anticoll()

        if Status != RFID.MI_OK:
            break

        # Writing data
        RFID.SelectTag(UID)
        status = RFID.Auth(RFID.PICC_AUTHENT1A, TrailerBlockAddr, KEY, UID)
        if status == RFID.MI_OK:
            data = bytearray()
            data.extend(bytearray(text.ljust(len(BlockAddrs) * 16)))
            i = 0
            for block_num in BlockAddrs:
                RFID.Write(block_num, data[(i*16):(i+1)*16])
                i += 1
            print "UID:  ", format_uid(UID)
            print "Data: ", text[0:(len(BlockAddrs) * 16)], "\n"
        else:
            print "Can't access sector", Sector, "!\n"
        RFID.StopCrypto1()
        break

    RFID.AntennaOff()
    GPIO.cleanup()


def write_token(token):

    token_split_arr = [token[i:i + 48] for i in range(0, len(token), 48)]
    
    for i in range(0, len(token_split_arr)):
        write_text(i + 1, token_split_arr[i])


write_token("eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbkBnbWFpbC5jb20iLCJyb2xlIjoiUk9MRV9BRE1JTiIsImlkIjoxMCwiaXNzIjoiU1NtYXJ0T2ZmaWNlIiwiaWF0IjoxNzMxNzMxOTI0LCJleHAiOjE3MzMwMjc5MjR9.bC7KRR1GOO1ZuzMTDLIoiYh0sSrz7AMOSnTDGp5sSJI")
