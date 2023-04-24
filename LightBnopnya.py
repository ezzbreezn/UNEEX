import sys, io, encodings

codings = ['cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257',
           'cp1258', 'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp864', 'cp866',
           'cp869', 'cp874', 'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16', 'iso8859_4', 'iso8859_5',
           'koi8_r', 'latin_1', 'mac_croatian', 'mac_greek', 'mac_iceland', 'mac_latin2']

s = sys.stdin.read().strip()

def encoding(s):
    for c1 in codings:
        try:
            s1 = s[0:4].encode(c1)
            e1 = s[-4:].encode(c1)
        except:
            continue
        for c2 in codings:
            try:
                s2 = s1.decode(c2)
                e2 = e1.decode(c2)
            except:
                continue
            if s2 == 'ПРОЦ' and e2 == 'КНЦ;':
                try:
                    s = s.encode(c1).decode(c2)
                except:
                    continue
                else:
                    print(s)
                    return 
            for c3 in codings:
                try:
                    s3 = s2.encode(c3)
                    e3 = e2.encode(c3)
                except:
                    continue
                for c4 in codings:
                    try:
                        s4 = s3.decode(c4)
                        e4 = e3.decode(c4)
                    except:
                        continue
                    if s4 == 'ПРОЦ' and e4 == 'КНЦ;':
                        try:
                            s = s.encode(c1).decode(c2).encode(c3).decode(c4)
                        except:
                            continue
                        else:
                            print(s)
                            return
                    for c5 in codings:
                        try:
                            s5 = s4.encode(c5)
                            e5 = e4.encode(c5)
                        except:
                            continue
                        for c6 in codings:
                            try:
                                s6 = s5.decode(c6)
                                e6 = e5.decode(c6)
                            except:
                                continue
                            if s6 == 'ПРОЦ' and e6 == 'КНЦ;':
                                try:
                                    s = s.encode(c1).decode(c2).encode(c3).decode(c4).encode(c5).decode(c6)
                                except:
                                    continue
                                else:
                                    print(s)
                                    return

encoding(s)





