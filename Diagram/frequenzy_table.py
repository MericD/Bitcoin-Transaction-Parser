import numpy as np
import array
from Diagram import hex_config as hc


def freq_tab(array_con):
    
    c = np.array(30)   
    c.astype(int)
    c= array.array('i',(0 for _ in range(30)))

    content = []
    content = [[] for x in range(0,30)]

    for binary in array_con:

        if str(binary).startswith('@') and len(binary) < 40:
            c[1] +=1
            content[1].append(binary)
        elif str(binary).endswith('==') and len(binary) < 30:
            c[2] +=1
            content[2].append(binary)
        elif str(binary).endswith('=') and len(binary) == 44:
            c[3] +=1
            content[3].append(binary)
        elif str(binary).startswith('{"') or str(binary).endswith('"}') :
            c[4] +=1
            content[4].append(binary)
        elif str(binary).endswith('_usd') or str(binary).endswith('uds') or str(binary).endswith('usd') or (str(binary).endswith('USD')) or ('usd' in binary) :
            c[5] +=1
            content[5].append(binary)
        elif (("\\"+"/") in binary) and (len(binary) == 40):
            c[6] +=1
            content[6].append(binary)
        elif (len(binary) == 21) and ('_' == binary[10]):
            c[7] +=1
            content[7].append(binary)
        elif (len(binary) == 40):
            if all(i in (hc.upper_alph + hc.lower_alph + hc.symbol) for i in binary):
                c[9] +=1
                content[9].append(binary)
        elif str(binary).startswith('TN'):
            c[10] +=1
            content[10].append(binary)
        elif '|' in binary:
            c[11] +=1
            content[11].append(binary)
        elif (len(binary) == 34) or (len(binary) == 39):
            if str(binary).startswith('1'):
                c[12] +=1
                content[12].append(binary)
        elif str(binary).startswith('2'):
            c[13] +=1
            content[13].append(binary)
        elif str(binary).startswith('3'):
            c[14] +=1
            content[14].append(binary)
        elif (len(binary) == 46) and str(binary).startswith('Qm'):
            c[15] +=1
            content[15].append(binary)
        elif all(i in hc.lower_alph for i in binary):
            c[16] +=1
            content[16].append(binary)
        elif all(i in hc.upper_alph for i in binary):
            c[17] +=1
            content[17].append(binary)
        elif all(i in (hc.upper_alph + hc.lower_alph) for i in binary):
            c[18] +=1
            content[18].append(binary)
        elif  (len(binary) == 58):
            if str(binary).startswith('6'):
                c[19] +=1
                content[19].append(binary)
        elif (len(binary) == 36):
            if ('-' == binary[9]):
                c[20] +=1
                content[20].append(binary)
        elif (len(binary) >= 30):
            if all(i in hc.hex_dig for i in binary[-10:]):
                c[21] +=1
                content[21].append(binary)
        elif (len(binary) == 28):
            if str(binary).endswith('='):
                c[22] +=1
                content[22].append(binary)
        elif str(binary).startswith('---') and str(binary).endswith('---'):
            c[23] +=1
            content[23].append(binary)
        elif (len(binary) > 5):
            if ':' == binary[5]: 
                c[24] +=1
                content[24].append(binary)
        else:
            c[0] +=1
            content[0].append(binary)
    print(str(content[24]) + str(c[24]))
    
  
    return c, content