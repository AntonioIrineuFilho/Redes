def SameNetwork(ip1, ip2, numMask):
    mask = ""
    ip1Bin = ""
    ip2Bin = ""
    andIp1Mask = ""
    andIp2Mask = ""
    for i in range(1, 33):
        if (i <= numMask):
            mask += "1"
        else:
            mask += "0"

    for i in range(4):
        lcontIp1 = []
        lcontIp2 = []
        contIp1 = int(ip1[i])
        contIp2 = int(ip2[i])
        for j in range(8):
            lcontIp1.append(contIp1 % 2)
            contIp1 = contIp1 // 2
            lcontIp2.append(contIp2 % 2)
            contIp2 = contIp2 // 2
        for k in range(7, -1, -1):
            ip1Bin += str(lcontIp1[k])
            ip2Bin += str(lcontIp2[k])

    for i in range(32):
        andIp1Mask += str(int(ip1Bin[i]) and int(mask[i]))
        andIp2Mask += str(int(ip2Bin[i]) and int(mask[i]))
        
    if (andIp1Mask == andIp2Mask):
        return True
    else:
        return False