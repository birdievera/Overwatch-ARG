'''
Step 1: Cut out all the vertical barcodes from the frame in question (frame 3).
Step 2: Run them all through http://www.onlinebarcodereader.com/, turns out they 
are Code 128 encoded (kudos to /u/zachpip/).
Results:
barcode1 - FEC-820-BA9-BAD-BAF-824-FEA-5-F28-980-5B0-F59
barcode2 - 4B1-2C7-F83-748-7F4-719-AAA-2C8-1F6-47C-5A8-DBA
barcode3 - 7F-1541-85D-E5D-35D-1C41-157F-500-49D-122-11D8-D9C
barcode4 - 279-919-4AA-800-1E9-308-3F1-EDC-CB3-602-DE9-8
barcode5 - 153-690-BF0-CA1-2B-D03-9C8-866-DF7-EF9-C21-20
barcode6 - 1FD7-1F79-1582-1252-806-1B4B-1FB7-1050-532-9A9-1870-1FEF
barcode7 - 3A0-A43-AFF-793-658-C-FE4-821-BA4-BA8-BAA-82F-FED
barcode8 - B6A-BD4-496-324-A2F-3C3-78E-723-634-B9-287-EFA-172
barcode9 - 1B5E-17F9-83D-160-1BFE-1D14-956-318-5F1-6D7-1BC-C24-18CF

Step 3: Convert to ASCII, HEX and binary

'''
barcodes = ["FEC-820-BA9-BAD-BAF-824-FEA-5-F28-980-5B0-F59",
            "4B1-2C7-F83-748-7F4-719-AAA-2C8-1F6-47C-5A8-DBA",
            "7F-1541-85D-E5D-35D-1C41-157F-500-49D-122-11D8-D9C",
            "279-919-4AA-800-1E9-308-3F1-EDC-CB3-602-DE9-8",
            "153-690-BF0-CA1-2B-D03-9C8-866-DF7-EF9-C21-20",
            "1FD7-1F79-1582-1252-806-1B4B-1FB7-1050-532-9A9-1870-1FEF",
            "3A0-A43-AFF-793-658-C-FE4-821-BA4-BA8-BAA-82F-FED",
            "B6A-BD4-496-324-A2F-3C3-78E-723-634-B9-287-EFA-172",
            "1B5E-17F9-83D-160-1BFE-1D14-956-318-5F1-6D7-1BC-C24-18CF"]


if __name__ == "__main__":
    decoded = ''.join((''.join(bin(int(num, 16))[2:]
                               for num in barcode.split('-')) 
                       for barcode in barcodes))
    #print str.rjust(50, '0')
    print (decoded)