#!/usr/bin/env python3

def gdgdgd():
    na1 = []
    na2 = []

def lol():
    a1 = []
    a2 = []
    for i in range(65, 91):
        a1.append(chr(i))
    for i in range(97, 123):
        a1.append(chr(i))
    for i in range(48, 58):
        a1.append(chr(i))

    a1.append(chr(43))
    a1.append(chr(47))
    a2 = a1[::-1]
    return a2
    

def cHalala(a, b):
    l = 256
    na1 = []
    na2 = []
    na3 = []
    for i in range(l):
        na1.append(a[i%len(a)])
        na2.append(i)

    j = 0
    for i in range(l):
        j = (j + na2[i] + na1[i]) % l
        num = na2[i]
        na2[i] = na2[j]
        na2[j] = num

    j = 0
    k = 0
    x = 0
    for i in range(len(b)):
        x = (x+1) % l
        k = (k + na2[x]) % l
        num2 = na2[x]
        na2[x] = na2[k]
        na2[k] = num2
        num3 = na2[(na2[x] + na2[k]) % l]
        na3.append(b[i] ^ num3)

    return na3

if __name__ == "__main__":
    pwx = [ 66, 105, 98, 105, 115, 117, 112 ]
    dada1 = [
        168,
        67,
        19,
        121,
        221,
        127,
        192,
        223,
        162,
        198,
        81,
        12
    ]
    dada2 = [
        128,
        84,
        4,
        118,
        204,
        118,
        181,
        132,
        224,
        199,
        124
    ]
    dada3 = [
        237,
        122,
        44,
        114,
        203,
        96,
        146,
        138,
        233,
        228,
        79,
        15,
        17,
        39,
        254,
        153,
        47,
        163,
        114,
        83,
        49,
        18,
        4
    ]
    dada4 = [
        129,
        71,
        3,
        110,
        152,
        64,
        155,
        140,
        254,
        201,
        29,
        4,
        19,
        2,
        228,
        137,
        40,
        168,
        111,
        93,
        7,
        11,
        18,
        69,
        14,
        150,
        146,
        76,
        147,
        125,
        214,
        164,
        5,
        37,
        211,
        92,
        249,
        216,
        199
    ]
    kernel32 = ''.join( chr(i) for i in cHalala(pwx, dada1))
    createfile = ''.join( chr(i) for i in cHalala(pwx, dada2) )
    textfile = ''.join( chr(i) for i in cHalala(pwx, dada3) )
    s = ''.join( chr(i) for i in cHalala(pwx, dada4) )
    print(createfile)
    print(textfile)
    print(s)

    dada5 = [
          148,
          84,
          8,
          99,
          221,
          85,
          154,
          129,
          233
    ]
    writefile = ''.join( chr(i) for i in cHalala(pwx, dada5) )
    print(writefile)

    bs64 = lol()
    byt = "sqVv//z////7////AAD//0f/////////v///////////////////////////////////////////////f/////HgRfH/S/Yy3kf+szLeq5eWjN+PjZCYjZ6S35yekZGQi9+dmt+NipHflpHfu7Cs35KQm5rR8vL12/////////+vuv//m3n9/1yWUWX//////////w//3d/0/c///73////7///////////////f//////9//v/////f/////f//+//////////5//////////9f/////f////////z/n3r//7////////+////////////v////////3//////////////v//////////////////////////9///93/P//////////////////////////////////Y5///8f////////////////////////////////////////////////////////////////////////////////f//+3///////////////Ri5qHi////66+////3////73////9///////////////////f//+f0Y2MjZz///93/P///3/////7////u///////////////////v///v/////////////////////////////////////////////////////+3/////f/6/5vd///Hwf///v/////////////////////////////////////////////////////////////////////////h/dfs///11ezP+v86/////v//7v1xluel4aX1+XLi///+7Pn5cuL///7s+PxxlnLh///+7Pfp89Tr7vn3/ff9cZaibmHu+Pf3Yffop/P3+c0X6drz8tTZ9u7492un7vn3a6f5ovLu+Pdr7Pru+Pfu+PZrYe749u76Yffop/P3+c0p6drz2vL01Ln46Kf0+Pmi9Pbu+Phrp/L2+aLy7vj4a+z67vj47vj2a2Hu+Pbu+mHu+O74+Gvu+PZrp/mia+z77vf3/Pdu7vueLWP36Kfz9/xxls1L7vfV////7M/7/+z////9///u/fz77f/X+f//+dL5jOv///WF1f/sz/z/VP////z//+799fna89P693GW0vrpH/TU9vfpcOH///4f9PjX6v//9fL5cZbg387Q9vlxlpXX6f//9eC/1/b///n24Pbgltfo///19uTg49fo///19ufg0dfo///11K72+XGWldfp///14L/X9v//+fbg9uCd1+j///X25+DS1+j///X25uCY1+j///X25eCT1+j///X25ODU1+j///X24+Ch1+j///X24uCb1+j///Xr89X/7M/9/8v////7///ujf7//4/X5///9dP5jc7//4/Vgf7///vX9f//+fyB/v//+9f3///59dfm///1+ZDl///11eWNev//j9Xh/dfs///11Z3g7nLh///+2i/9///71+T///V//v//+9W9rLW9/v/+///////z////icvRz9HMz8zOxv/////6/5P////H6f//3IH//1vp//874///3KyLjZaRmIz/////l8z//3v+///cqqz/E8v//+/////cuKq2u////wPL///D9v//3L2TkJ3//////////f///qgC/cv2/f///wX+zP/p///+////2P////b///+m/v//6f///8T////k////qv7//+3////9/////v////7////7/////v////n////+/////v////3////6//////+K7v7///////n/UPFV6fn/4/BV6fn/WvKW6fD/Nen///n/MvKX7Pn/j/GX7Pn/rvGX7Pn//PCX7Pn/MPGX7Pn/F/GX7Pn/G/KX7Pn/RvJ06fn/gvJ06fn/5/GX7Pn/APIQ8Pn/Oe3F6Pn/yvHF6Pn/dPKC4/n/KOdH7vn/W/pG8Pn/QO5H7vn/6et06fn/cvF06fn/TPNH7vn/HOZH7vn/Te9H7vn/nfJV6fn/tvNH7vn/lf9H7vn/wPBH7vX/uuvH7vn/nelH7vn/nulH7vn/De906fn/E/Rp/fn/J/DP5Pn/j+hV6fn/UuRH7vn/fvRH7v////+Z/v/////+//7//v/v/7vwCOuy//7//v/+/+//se4I67L//v/3///+//+Q/v//sv/9//D//f7//1H9//+q//z/8P/9/v//6Ob//6r/sf7w//3+//9w/P//nv+l/vD//f7//2j8//+e/6X+7P/s/v//9f7//47/pf7o/+7/+/xY+Mz+1v1U+Pn5A/1Q+Kl/KehN+Kl/4v9N+Kl/rv9N+Kl/dP9N+Kl/Q/9N+Kl/Zf9N+Kl/m/pN+Kl/6/9N+Kl/t/9N+Kl/ff9N+Kl/TP9N+Kl/bv9N+Kl/ePxN+Kl/gvxN+Kl/hPhN+Kl/1+RN+Kl/L/BN+Kl/XfNN+Kl/JOlN+Kl/v/pN+Kl/afpN+Kl/9edN+Kl/t/hN+Kl/zPdN+Kl//epN+Kl/D+pN+Kl/W+VN+Kl/8/pN+Kl//etN+Kl/h+tN+Kl/CfNN+Kl/UfVN+Kl/OfRN+Kl/G+tN+Kl/N+dN+Kl/OvNN+Kl/rvxN+Kl/u/xN+Kl/kfpN+Kl/qehN+Kl/gOhN+Kl/Be9N+Kl/3+dN+Kl/3ftN+Kl/9fRN+Kl/bPNN+Kl/KfpN+Kl/9u9N+Kl/lu1N+Kl/9eVN+Kl/deVN+Kl/JutN+Kl/oeRN+Kl/BelN+Kl/m/lN+Kl/JuRN+Kl/veNN+Kl/A/RN+Kl/ouVN+Kl/JulN+Kl/EetN+Kl/rPNN+Kl/selN+Kl/cu5N+Kl/xvhN+Kl/SehN+Kl/n+9N+Kl/cu1N+Kl/1OlN+Kl/0vxN+Kl/jPRN+Kl/Le9N+Kl/j/xN+Kl/YvdN+Kl/avtN+Kl/LOpN+Kl/fvVN+Kl/JfRN+Kl/IuVN+Kl/Q/RN+Kl/zvNN+Kl/cfVN+Kl/7uNN+Kl/vuRN+Kl/Vu5N+Kl/rexN+Kl/EOxN+Kl/pfdN+Kl/t/tN+Kl/pu5N+Kl/su9N+Kl/q+tN+Kl/Nu9N+Kl/pftN+Kl/vfdN+Kl/dORN+Kl/3PZN+Kl/aPZN+Kl/ze1N+Kl/yvZN+Kl/LvZN+Kl/WfxN+Kl/k+tN+Kl/VfNN+Kl/5+lN+Kl/3elN+Kl/VPBN+Kl/gvlN+Kl/X/RN+Kl/g+1N+Kl/K/xN+Kl/hexN+Kl/g/pN+Kl/CfxN+Kl/d+ZN+Kl/PvVN+Kl/8vtN+Kl/2O9N+Kl/U+ZN+Kl/OutN+Kl/b+xN+Kl/TvhN+Kl/4PRN+Kl/0ONN+Kl/GvRN+Kl/uulN+Kl/yeZN+Kl/1fhN+Kl/NfBN+Kl/YvhN+Kl/ue1N+Kl/jO9N+Kl/UOpN+Kl/t+pN+Kl/O+5N+Kl/5eNN+Kl/auhN+Kl/qe1N+Kl/BfVN+Kl/uPZN+Kl/4fNN+Kl/redN+Kl/Q+pN+Kl/zudN+Kl/7+pN+Kl/1upN+Kl/yOpN+Kl/1+1N+Kl/pfVN+Kl/t/VN+Kl/XexN+Kl/mfNN+Kl/SexN+Kl/W+hN+Kl/TO1N+Kl/F/pN+Kl/jPtN+Kl/dPpN+Kl/KPhN+Kl/6/dN+Kl/qeNN+Kl/9+5N+Kl/V/dN+Kl/j+pN+Kl/QPZN+Kl/SudN+Kl/Ju5N+Kl/7O5N+Kl/qvtN+Kl/e+5N+Kl/m/tN+Kl/fPtN+Kl/PvhN+Kl/+vdN+Kl/leNN+Kl/3PdN+Kl/2u5N+Kl/yvtN+Kl/7vxN+Kl/kvZN+Kl/VfZN+Kl/ffZN+Kl/HfxN+Kl/p/ZN+Kl/TOtN+Kl/D+ZN+Kl/Yu1N+Kl/guRN+Kl/He9N+Kl/sORN+Kl/YOtN+Kl/kuRN+Kl/JuxN+Kl/+ehN+Kl/6PZN+Kl/svRN+Kl/nfRN+Kl/J/NN+Kl/suNN+Kl/NuxN+Kl/UPlN+Kl/5O9N+Kl/XvlN+Kl/HvBN+Kl/YfVN+Kl/2eRN+Kl/t/lN+Kl/qfhN+Kl/PfpN+Kl/jPVN+Kl/y/pN+Kl/aOZN+Kl/cuNN+Kl/ZvBN+Kl/yOlN+Kl/yf9N+Kl/j/9N+Kl/Xv9N+Kl/Pf9N+Kl/K/9N+Kl/B/9N+Kl/2P5N+Kl/vf5N+Kl/q/5N+Kl//v9N+Kl/3P9N+Kl/qP9N+Kl/c+tN+Kl/GOlN+Kl/1fpN+Kl/FvNN+Kl/9fNN+Kl/7vhN+Kl/auVN+Kl/4+pN+Kl/OOpN+Kl/o+pN+Kl/pvlN+Kl/g+lN+Kl/IehN+Kl/fvNN+Kl/M/xN+Kl/QOZN+Kl/X+dN+Kl/TeNN+Kl/C+dN+Kl/Gf9N+Kl/G+pN+Kl/nvxN+Kl/4PlN+Kl/C/ZN+Kl/SftN+Kl/G/ZN+Kl/0fVN+Kl/MOZN+Kl/guZN+Kl/k/BN+Kl/OOhN+Kl/jflN+Kl/9ORN+Kl/FPVN+Kl/WftN+Kl/Ye9N+Kl/MPlN+Kl/LvVN+Kl/ePdN+Kl/jPNN+Kl/AflN+Kl/WeNN+Kl/6ORN+Kl/yPlN+Kl/wvNN+Kl/1fRN+Kl/8vlN+Kl/bPlN+Kl/4vhN+Kl/uOZN+Kl/+uxN+Kl/qPBN+Kl/CvtN+Kl/tPBN+Kl/SOVN+Kl/sPpN+Kl/Ze5N+Kl/xO9N+Kl/u/JN+Kl/gvBN+Kl/e+9N+Kl/iOdN+Kl/J/tN+Kl///VN+Kl/oudN+Kl/A/dN+Kl/EvhN+Kl/fPhN+Kl/sPdN+Kl/eupN+Kl/HvdN+Kl/N/tN+Kl/wudN+Kl/6/VN+Kl/OPdN+Kl/Ku1N+Kl/xuVN+Kl/5uhN+Kl/TPdN+Kl/4PxN+Kl/F/lN+Kl/Hu5N+Kl/P/lN+Kl//elN+Kl/RfxN+Kl/lfhN+Kl/j+VN+Kl/R+RN+Kl/GuRN+Kl/aONN+Kl/DeVN+Kl/DvRN+Kl/B/pN+Kl/NuVN+Kl/5+xN+Kl/lPdN+Kl/3vJN+Kl/4OVN+Kl/ouZN+Kl/1+tN+Kl/zOxN+Kl/7e1N+Kl/b+dN+Pn5A/1Q+Kl/4/1J+Kl/Vf5J+Kl/+v1J+Kl/Gv1J+Kl/X/1J+Kl/N/1J+Kl/Cf5J+Kl/Kf1J+Kl/PP5J+Kl/KP5J+Kl/G/5J+P////9//2nfh/1F+P7//////3//ad8//UD4/f//////f/9p3zH+Ovj7//////9//2nfTfQ1+Pr//////3//ad9r9Dr49P//////f/9p3/fmKPjy/7ff/////3nnq+n5/+7/r9//////af/2/B/47v/b3v////9p/wHqFvjs/7ve/////2n/I+YP+On/A97/////ef8D65n/6P/D3f////95/8PkCfjn/7zd/////3nnq+n5/+f/tN3/////buel6QX45////////P9556vpAfjn///////8/zn+ufT79+X///////z/Of6+9O/33v///////P85/sj04PfV///////8/3nnq+kB+NT///////z/Of659Nn30v///////P85/r70zPfN///////8/zn+yPS798b////+/178///+/5T1///9/178///+/5f1/9/////////+/yD0///9/1nq///8//Ty/f/7/wTu/v/6/0r6/9/////////+/ynn///+///n///9/23w///8/9bm/f/7/xrn///+/5D1///9/9f8///+/z3u///9/2fu///8/0/v///+/0zk///+/2Dk///+/yHn///9/771///+/3D9///9/3H+///8/3f9///7/2P+///6/0P+///5/2r+///4/479///+/3D9///9/3H+///8/3f9///7/2P+///6/0P+///5/2r+///4/479///3/z/v///2/yHn///+//zl///+/yHn///9/771///+/5X9///9/1z+///8/0T9/f/7/0j9/v/6/379///+/5X9///9/1z+///8/0T9/f/7/0j9/v/6/379///5/z/v///4/yHn/f/+/0j9/v/9/379///8//zl9v+r6f7/7v+r6fn/5v+r6fX/1v+r6e//zv+r6e//xv+r6e//vv+r6e//tv+r6e//rv+r6e//pv+r6e//nv+r6er/lv+r6e//jv+r6e//hv+r6e//dv+r6eX/bv+r6fn/Rv+r6d//Jv+r6fn/Zv+r6fn/Bv+r6fn//v5f5rv/9v5f5rX/7v7F8LD/5v5256T/3v7G/p//3v7u75n/1v5c5JP/9v/v/4D/9v/r/4D/9v/n/3v/9v/j/3b/9v/f/3H/9v/b/2z/9v/X/2f/9v/T/2f/9v/P/2L/9v/L/13/9v/H/1j/9v/D/1P/9v+//07/9v+7/0n/9v+3/0T/9v+z/z//9v+v/zr/9v+r/zX/9v+n/zD/9v+j/yv/9v+f/yb/9v+b/yH/9v+X/xz/9v+T/xf/9v+P/xL/9v+L/w3/9v+H/wj/9v+D/wP/9v9///7+9v97//n+9v93//T+9v9z/+/+9v9v/+r+9v9r/+X+9v9n/+D+9v9j/9v+9v9f/9b+9v9b/9H+9v9X/8z+9v9T/8f+9v9P/8L+9v9L/73+9v9H/73+9v9D/7j+9v8//7P+9v87/67+9v83/6n+9v8z/6T+9v8v/5/+9v8r/5r+9v8n/5X+9v8j/5D+9v8f/4v+9v8b/4b+9v8X/4H+9v8T/3z+9v8P/3f+9v8L/3L+9v8H/23+9v8D/2j+9v///mP+9v/7/l7+9v/3/ln+9v/z/lT+9v/v/k/+9v/r/kr+9v/n/kX+9v/j/kD+9v/f/jv+9v/b/jb+9v/X/jH+9v/T/iz+9v/P/if+9v/L/iL+9v/H/h3+9v/D/hj+9v+//hP+9v+7/g7+9v+3/gn+9v+z/gT+9v+v/v/99v+r/vr99v+n/vX99v+j/vD99v+f/uv99v+b/ub99v+X/uH99v+T/tz99v+P/tf99v+L/tL99v+H/s399v+D/sj99v9//sP99v97/r799v93/rn99v9z/rT99v9v/q/99v9r/qr99v9n/qX99v9j/qD99v9f/pv99v9b/pb99v9X/pH99v9T/oz99v9P/of99v9L/oL99v9H/n399v9D/nj99v8//nP99v87/m799v83/mn99v8z/mT99v8v/l/99v8r/lr99v8n/lX99v8j/lD99v8f/kv99v8b/kb99v8X/kH99v8T/jz99v8P/jf99v8L/jL99v8H/i399v8D/ij99v///SP99v/7/R799v/3/Rn99v/z/RT99v/v/Q/99v/r/Qr99v/n/QX99v/j/QD99v/f/fv89v/b/fb89v/X/fH89v/T/ez89v/P/ef89v/L/eL89v/H/d389v/D/dj89v+//dP89v+7/c789v+3/cn89v+z/cT89v+v/b/89v+r/br89v+n/bX89v+j/bD89v+f/av89v+b/ab89v+X/aH89v+T/Zz89v+P/Zf89v+L/ZL89v+H/Y389v+D/Yj89v9//YP89v97/X789v93/Xn89v9z/XT89v9v/W/89v9r/Wr89v9n/WX89v9j/WD89v9f/Vv89v9b/Vb89v9X/VH89v9T/Uz89v9P/Uf89v9L/UL89v9H/T389v9D/Tj89v8//TP89v87/S789v83/Sn89v8z/ST89v8v/R/89v8r/Rr89v8n/RX89v8j/RD89v8f/Qv89v8b/Qb89v8X/QH89v8T/fz79v8P/ff79v8L/fL79v8H/e379v8D/ej79v///OP79v/7/N779v/3/Nn79v/z/NT79v/v/M/79v/r/Mr79v/n/MX79v/j/MD79v/f/Lv79v/b/Lb79v/X/LH79v/T/Kz79v/P/Kf79v/L/KL79v/H/J379v/D/Jj79v+//JP79v+7/I779v+3/In79v+z/IT79v+v/H/79v+r/Hr79v+n/HX79v+j/HD79v+f/Gv79v+b/Gb79v+X/GH79v+T/Fz79v+P/Ff79v+L/FL79v+H/E379v+D/Ej79v9//EP79v97/D779v93/Dn79v9z/DT79v9v/C/79v9r/Cr79v9n/CX79v9j/CD79v9f/Bv79v9b/Bb79v9X/BH79v9T/Az79v9P/Af79v9L/AL79v9H/P369v9D/Pj69v8//PP69v87/O769v83/On69v8z/OT69v8v/N/69v8r/Nr69v8n/NX69v8j/ND69v8f/Mv69v8b/Mb69v8X/MH69v8T/Lz69v8P/Lf69v8L/LL69v8H/K369v8D/Kj69v//+6P69v/7+5769v/3+5n69v/z+5T69v/v+4/69v/r+4r69v/n+4X69v/j+4D69v/f+3v69v/b+3b69v/X+3H69v/T+2z69v/P+2f69v/L+2L69v/H+1369v/D+1j69v+/+1P69v+7+0769v+3+0n69v+z+0T69v+v+z/69v+r+zr69v+n+zX69v+j+zD69v+f+yv69v+b+yb69v+X+yH69v+T+xz69v+P+xf69v+L+xL69v+H+w369v+D+wj69v9/+wP69v97+/759v93+/n59v9z+/T59v9v++/59v9r++r59v9n++X59v9j++D59v9f+9v59v9b+9b59v9X+9H59v9T+8z59v9P+8f59v9L+8L59v9H+7359v9D+7j59v8/+7P59v87+6759v83+6n59v8z+6T59v8v+5/59v8r+5r59v8n+5X59v8j+5D59v8f+4v59v8b+4b59v8X+4H59v8T+3z59v8P+3f59v8L+3L59v8H+2359v8D+2j59v//+mP59v/7+l759v/3+ln59v/z+lT59v/v+k/59v/r+kr59v/n+kX59v/j+kD59v/f+jv59v/b+jb59v/X+jH59v/T+iz59v/P+if59v/L+iL59v/D+h359v+/+hj59v+7+hP59v+3+mf/9v+z+nv/9v+v+nb/9v+r+g759v+n+gn59v+j+kn/9v+f+gT59v+b+v/42P98/3v/0f/0/7D30f/s/6f30f/k/4j30f/c/3/30f/U/2/30f/M/2/30f/E/2/30f+8/3/30f+0/2n30f+s/2/30f+k/2/30f+c/1H30f+U/yf30f+M/xr3fP9s/3v/HP90/8z2/P50/8z29P9a+Oj/Wvj3//n/+vj+/+7////2/9n/yv/G/6n/l+6//vz/BuT+/7z++v8O6P7/v/74//rj/v///vb/TfT+/7/+9P9r9P7///7y//fm/v/Gnv///f/7f////v////////////////8I6///+///////////////if/E/P/////7//////////////+J/0fu//////r//f/5//3/+P/8//f//P/2//v/////tpGJnpOWm6+ejZ6Smouajc7P/76dnpGbkJGam6ielovP/7aRiZ6Tlpuvno2ekpqLmo3Ozv+2kYmek5abr56NnpKai5qNzv++nZ6Rm5CRmpuonpaLzv+2kYmek5abr56NnpKai5qNzs3/tpGLzM3/tpGJnpOWm6+ejZ6Smouajc3/vp2ekZuQkZqbqJ6Wi83/vp2ekZuQkZqbqJ6Wi8nM/7aRiZ6Tlpuvno2ekpqLmo3M/76dnpGbkJGam6ielovM/7aRiZ6Tlpuvno2ekpqLmo3L/7aRiZ6Tlpuvno2ekpqLmo3K/7aRiZ6Tlpu2kp6YmqiWkc7J/7aRiZ6Tlpuvno2ekpqLmo3J/6CgrIuei5acvo2Nnoa2kZaLq4aPmqyWhZrCzsj/tpGJnpOWm6+ejZ6Smouajcj/mJqLoKqrucf/tpGJnpOWm6+ejZ6Smouajcf/tpGJnpOWm6+ejZ6Smouajcb/w7KQm4qTmsH/w6+Nlomei5q2ko+TmpKakYuei5aQkbuai56Wk4zB/7u+u767vv+5vrm+ub7/rL6svqy+/7O9s72zvf+vvri6oLqnuryqq7qgrbq+u/+8u7y7vLv/r764uqC4qr6tu/+1vqy7vb6su/+vvri6oLGwvL68t7r/r764uqCorbarurywsr22sbr/r764uqCtur67qK22q7r/r764uqC6p7q8qqu6oK26vruorbaruv+vvri6oLqnuryqq7r/z8fOucbKyc25vb26u8i7ys/Mx7rKy87Izc3Mzc28vse+ub25u8rKury8zbu5vc/Ivcq9zb7LusjNzsvLy8bLuf+3ube5t7n/q7mruau5/7SztLC0s7Sz/7CzsLOws/+ssqyyrLL/ubG5sbmx/6yGjIuaktG2sP+vvri6oLGwvry8uqys/7GrrKu+q6qs/7G9qP+xvauo/7SytLOxvaf/r764uqCtur67sLGzpv+vvri6oKittqu6vLCvpv+vvri6oLqnuryqq7qgqK22q7q8sK+m/4mek4qaoKD/m56bnv+ct56TnpOe/7GQi7Kej4+am7uei57/sZCrh5mymouem56Lnv+vnpiamZaTmq6KkIue/5KMnJCNk5ad/6+NkJyajIy2kbWQnf+vjZCcmoyMsZCLtpG1kJ3/u5aZmZqNmpGcmr6Lu5z/vZ6btpGWi5aek6+c/7SajZGak76PnP+qjJqNvo+c/56MnIyejJz/nIyenoychYec/4eFh5z/sJ2VmpyLr56Ll6yGkYueh72em/+tmpyQiZqNhrGQi7Gampuam/+vnpiamZaTmq6KkIueuoecmpqbmpv/vo2Nnoa9kIqRm4y6h5yampuam/+smpKej5eQjZqzlpKWi7qHnJqam5qb/6yKjI+akZu8kIqRi7qHnJqam5qb/6uXjZqem6iejKyKjI+akZuam/+smpyLlpCRsZCLuoeLmpGbmpv/vpycmoyMu5qRlpqb/62ekZiasZCLs5CclJqb/6yajYmajbuWjJ6dk5qb/76cnJCKkYu7loyenZOam/+smo2Jmo2xkIu7loyenZOam/+rlpKajbGQi7yekZyak5qb/62ajoqajIu8npGcmpOam/+2kK+NlomWk5qYmrmelpOam/+zkJi4jZCIi5e5npaTmpv/q42ekYyenIuWkJGvjZCPnpiei5aQkbmelpOam/+rkraRlouWnpOWhZ6LlpCRuZ6Wk5qb/6+NlpKejYarjZ6RjI+QjYu8kJGRmpyLuZ6Wk5qb/7yekZyak5Oam/+5lpOarZqRnpKam/+xkIu+k5O+jIyWmJGam/+rjZ6RjJ6ci5aQkbGQi7WQlpGam/++nZ6Rm5CRmpv/r42QnJqMjLyTkJGam/+yiouekYuxkIuwiJGam/+xkJGasp6Pj5qb/6yQkpqxkIuyno+Pmpv/sZ6LlomasImajZOej4+am/+Tj7CJmo2Tno+Pmpv/r42QmZaTlpGYsZCLrIuQj4+am/+tmpiWjIuNhq2anJCJmo2am/+vnoyMiJCNm7qHj5aNmpv/rZCTk52enJSrlpKajbqHj5aNmpv/uZCNkoy+iouXrZqOipaNmpv/rIaRnJeNkJGWhZ6LlpCRrZqOipaNmpv/vJeanJSwioutmo6Klo2am/+5lpOauZCNnJqbvJOQjJqb/7mWk5q8k5CMmpv/t56Rm5OajLyTkIyam/+vkI2LvJOQjJqb/6+QjYu8kJGRmpyLlpCRrZqZioyam/+plo2KjLaRmZqci5qb/6+Wj5q8kJGRmpyLmpv/r5aPmruWjJyQkZGanIuam/+tkruWjJyQkZGanIuam/+zj5ytmpyalomavYqZmZqNuoePmpyLmpv/s5CYvJCNjYqPi5aQkbuai5qci5qb/6+NkJyajIy2jK+NkIuanIuam/+5lpOau5qTmouam/+plo2KjLuak5qLmpv/s5CclLGQi7iNnpGLmpv/sZCLtpKPk5qSmpGLmpv/qZCTipKaspCKkYuam/+vjZCZlpOWkZixkIusi56Ni5qb/62SvpONmp6bhqyLno2Lmpv/vpOajYuam/+rjZ6RjJ6ci5aQkb6TjZqem4a+nZCNi5qb/7yLk7mWk5qxkIusio+PkI2Lmpv/up6MsZCLrIqPj5CNi5qb/6uQkLKekYa4ipabjK2ajoqajIuam/+rkJCynpGGs4qWm4ytmo6KmoyLmpv/q42ekYyenIuWkJGxkIutmo6KmoyLmpv/uIqWm4y6h5eeioyLmpv/s4qWm4y6h5eeioyLmpv/vpiakYuMuoeXnoqMi5qb/62HvpyLvJCSkpaLi5qb/7GQi7yQkpKWi4uam/+rjZ6RjJ6ci5aQkb6TjZqem4a8kJKSlouLmpv/q42ekYyenIuWkJGek7CPmpGxkIu+k5OQiJqb/7OPnK2ajoqajIuMsZCLvpOTkIiam/+2kYmek5abvJab/7aRiZ6Tlpuslpv/t56Rm5OasZCzkJGYmo2pnpOWm/+si42anpKylpGWiZqNjJaQkbGQi6mek5ab/7yKjY2akYurjZ6RjJ6ci5aQkbGQi6mek5ab/6uNnpGMnpyLlpCRrZqOipqMi7GQi6mek5ab/7mWk5q2kYmek5ab/7CdlZqci7Gekpq2kYmek5ab/7CdlZqci6+ei5e2kYmek5ab/6+NlomWk5qYmrGQi7eak5v/uZOQnou7mpGQjZKek7CPmo2ekZv/rZqMkIqNnJq7nouesZCLuZCKkZv/rZqMkIqNnJqxnpKasZCLuZCKkZv/sJ2VmpyLsZ6SmrGQi7mQipGb/62ajJCKjZyaq4aPmrGQi7mQipGb/6+NkJyam4qNmrGQi7mQipGb/7CdlZqci6+ei5exkIu5kIqRm/+wjZuWkZ6TsZCLuZCKkZv/u5OTsZCLuZCKkZv/vI2Sr42Qi5CckJOxkIu5kIqRm/+si42anpKylpGWiZqNjJaQkbGQi7mQipGb/7qRi42Gr5CWkYuxkIu5kIqRm/+SmouXkJv/tpOTuZCNkpqbr56MjIiQjZv/qI2QkZivnoyMiJCNm/+ejJuejJv/j4ib/7GQi6yekpq7momWnJr/sZCsipyXu5qJlpya/7GQspqblp62kbuaiZacmv+2kYmek5abrZqem7KQm5r/r56YmrmeipOLuIqejZuvnpia/6yanIuWkJGxkIu2kp6Ymv+zj5y2kYmek5abvJCRkZqci5aQkaqMnpia/7aRiZ6TlpuymoyMnpia/7GQrIqcl6+NlomWk5qYmv+okI2UlpGYrJqLs5aSloutnpGYmv+6nquQkLOejZia/7mWk5qrkJCzno2Ymv+6kZu2kYmQlJr/vZqYlpG2kYmQlJr/tpGMi56RnJqxkIu+iZ6Wk56dk5r/r5aPmrGQi76JnpaTnp2Tmv+2kYmek5abt56Rm5Oa/62KkYuWkpq5lpqTm7eekZuTmv+8k5CMmreekZuTmv+2kYmek5abr5CNi7eekZuTmv+ojZaLmrmWk5r/upGbsJm5lpOa/6+emJq5noqTi6+emJaRmLmWk5r/sZCsipyXuZaTmv+xkLqejLCRuZaTmv+rkqmQk56LlpOa/7aRiZ6Tlpu6nrGekpr/tpGJnpOWm7yQko+Ki5qNsZ6Smv+2kYmek5abvpyckIqRi7Gekpr/qI2QkZipkJOKkpr/vZ6buZaTmquGj5r/qZ6Tipqrho+a/7uTk7KWmJeLvZq2kYyanIqNmv+zkJiQkbmelpOKjZr/rZqMkIqNnJq2kaqMmv+rkJSakb6TjZqem4a2kaqMmv+2kp6YmrGQi76LvZ6Mmv+tmo+ejYya/7uei56znoua/7KKk4uWnJ6Mi7uak5qYnoua/7GQi5eWkZirkKuajZKWkZ6Lmv+2kYmek5abr5aPmqyLnoua/7yekZGQi7uak5qLmv+vnpiauZ6Kk4u8kI+GsJGojZaLmv+RsYqSnZqNsJm9houajKuQqI2Wi5r/q42ekYyenIuam7Kej4+WkZiqkYyKj4+QjYuam62akpCLmv+rjZ6RjJ6ci5aQkYyqkYyKj4+QjYuam62akpCLmv+8kJKPlpOajbiakZqNnouam76Li42WnYqLmv+4ipabvouLjZadioua/6qRiZqNlpmWnp2TmryQm5q+i4uNlp2Ki5r/u5qdipiYnp2Tmr6Li42WnYqLmv+8kJKployWnZOavouLjZadioua/76MjJqSnZOGq5aLk5q+i4uNlp2Ki5r/voyMmpKdk4arjZ6bmpKejZS+i4uNlp2Ki5r/q56NmJqLuY2ekpqIkI2UvouLjZadioua/76MjJqSnZOGuZaTmqmajYyWkJG+i4uNlp2Ki5r/rJqcio2Wi4avmo2SloyMlpCRvouLjZadioua/76MjJqSnZOGvJCRmZaYio2ei5aQkb6Li42WnYqLmv++jIyakp2ThruajJyNlo+LlpCRvouLjZadioua/6qRkp6Rnpiam7mKkZyLlpCRr5CWkYuajb6Li42WnYqLmv+8kJKPlpOei5aQka2ak56HnouWkJGMvouLjZadioua/76MjJqSnZOGr42Qm4qci76Li42WnYqLmv++jIyakp2ThryQj4aNlpiXi76Li42WnYqLmv++jIyakp2ThryQko+ekYa+i4uNlp2Ki5r/rYqRi5aSmryQko+ei5adlpOWi4a+i4uNlp2Ki5r/qI2Wi5q9houa/7Gei5aJmv+tkrGQi76ci5aJmv+rjZ6RjJ6ci5aQkbGQi76ci5aJmv+7mp2KmJiajbaRnpyLloma/7OQmK2ajJaFmraRiZ6TlpusloWa/5uIrJaFmv+8npGLq5qNkpaRnouarJqTmf+smpyLlpCRq5CQvZaY/6yGjIuaktGrl42anpuWkZj/u5qTmouar5qRm5aRmP+6kZyQm5aRmP+vlo+as5aMi5qRlpGY/6yGjIuaktGtipGLlpKa0amajYyWkJGWkZj/qJ6NkZaRmP+4mousi42WkZj/r5aPmryTkIyWkZj/q5eNmp6btoyrmo2SlpGei5aRmP+8kIqTm7GQi62ajJaFmrOQmP+wnZWanIurho+aspaMkp6LnJf/tpGZkLOakZiLl7KWjJKei5yX/62aiZaMlpCRspaMkp6LnJf/rZqSkIuauZaTmqmajYyWkJGyloySnoucl/+tmpyKjYyWiZq7loyPnoucl/+W/76MhpGcvJ6Tk52enJT/nJ6Tk52enJT/vZ6brIuenJT/vZ6btpGWi5aek6yLnpyU/7mTkJ6LrIuenJS8l5qclP+yno2Ml56T/7aRmZCNkp6LlpCRnpP/tpGJnpOWm76ck/+9npu2kZeajZaLnpGcmr6ck/+2kYmek5abqZCTipKas56dmpP/rIaMi5qS0byQko+QkZqRi7KQm5qT/4yXno2UoJyek5P/vYqZmZqNq5CQrJKek5P/lJqNkZqTzM3Rm5OT/72enYagrJeejY/Rm5OT/7uWjJS5ipOT/6qRjIqcnJqMjJmKk/+7lo2anIuQjYaxkIutkv+qkZ6dk5qrkLmNmpqpkv+shoyLmpL/upGKkv+xkLaSj5qNjJCRnouWkJGrkJSakf+xkKuQlJqR/7yekYutmpyQiZqNqJaLl7eekZuTmrCPmpH/k4+xipKdmo2wmb2Gi5qMqI2Wi4uakf+rjZ6RjJ6ci5aQkYyxkIu5jZCFmpH/s56Mi76bkpaR/7CdlZqci7Gekpq8kJOTloyWkJH/qpGUkZCIka2aiZaMlpCR/7GQrIqcl7OQmJCRrJqMjJaQkf+4ip6Nm6+emJqplpCTnouWkJH/rJeejZaRmKmWkJOei5aQkf++nJyajIyplpCTnouWkJH/uZOQnou2kYmek5absI+ajZ6LlpCR/7aRiZ6TlpuokI2UjIuei5aQkf+smpyKjZaLhr6ci5aQkf+ylpGWiZqNjJaQkbaRnpycmoyMlp2TmrmNkJKsj5qclpmWmpurjZ6RjJ6ci5aQkf+2kYmek5abq42ekYyenIuWkJH/upmMsZCLvpOTkIiam7aRq42ekYyenIuWkJH/vJ6RkZCLuoeanIqLmrmWk5q2kauNnpGMnpyLlpCR/6qRnp2TmquQu5qTmouarJqci5aQkf+shoyLmpLRrZqZk5qci5aQkf+2kYmek5abr56Ymq+NkIuanIuWkJH/rJqci5aQka+NkIuanIuWkJH/r56MjIiQjZutmoyLjZaci5aQkf++nJyQipGLrZqMi42WnIuWkJH/tpOTmpiek7mKkZyLlpCR/6+NlomWk5qYmpu2kYyLjYqci5aQkf+2k5OamJ6TtpGMi42KnIuWkJH/r56YmrmeipOLq42ekYyWi5aQkf+8npOTlpGYvJCRiZqRi5aQkf+rjZ6RjJ6ci5aQka2ajoqWjZqbr42QkpCLlpCR/6iWkczNuoecmo+LlpCR/7GQkbyQkYuWkYqenZOauoecmo+LlpCR/7uei56wiZqNjYqR/6+emJq5noqTi7uakp6Rm6WajZD/sp6Pj5qbuZaTmqyWhZqlmo2Q/7aRi5qYmo27lomWm5q9hqWajZD/uZOQnou7lomWm5q9hqWajZD/tpGckJKPnouWnZOauZaTmrKej/+slpGYk5qsi5qP/7yNnoyXu4qSj/+zkJGYtYqSj/+9np2GoKyXno2P/7GQi5aZhryTmp6Rio//sZCsipyXuI2Qio//rI+anJaek7iNkIqP/7Kakp2ajbaRuI2Qio//spqSnZqNsZCLtpG4jZCKj/+2kYmek5abr42Wkp6NhriNkIqP/7Kakp2ajYyvjZaSno2GuI2Qio//tpGJnpOWm6yanIqNlouGu5qMnI3/q42ekYyenIuWkJG2kYmek5absp6NjJeek5O9ipmZmo3/k4+9ipmZmo3/tpGJnpOWm7CIkZqN/7GQrIqcl6qMmo3/rI+anJaek6qMmo3/tpGJnpOWm6+ejZ6Smouajf+zkJiQkayajYmajf+xkIuWmYa6kYqSu5aN/5ySjf+6kZOWjIuSmpGLsZCLrIqPmo2WkI3/u56LnrqNjZCN/7yNnLqNjZCN/7aRr56YmrqNjZCN/7aRi5qNkZ6Tuo2NkI3/up68kI2Nio+Luo2NkI3/0ZyLkI3/0Zyci5CN/6q2kYuvi43/rIaMi5qS0buWnpiRkIyLlpyM/6uQkLKekYarl42anpuM/6yGjIuaktGtipGLlpKa0baRi5qNkI+smo2JlpyajP+shoyLmpLRrYqRi5aSmtG8kJKPlpOajayajYmWnJqM/7uanYqYmJaRmLKQm5qM/7GQspCNmrqRi42Wmoz/q5CQsp6RhrCPmpGam7mWk5qM/7GQspCNmrmWk5qM/6uQkLKekYavnpiWkZi5lpOajP+8npGLvI2anouaspCNmqyLjZqekrKWkZaJmo2MlpCRjP+shoyLmpLRrJqcio2Wi4bRr5qNkpaMjJaQkYz/uZaTmrOQnJSam6iWi5ewkZOGrZqem5qNjP+tipGLlpKat5qTj5qNjP+5lpOas5CclJqbqJaLl6iNlouajYz/sZCzkJiQkayajYmajYz/tpGJnpOWm7OQmJCRt5CKjYz/tpGJnpOWm7aRmZC8k56MjP+8npOTnZ6clL2Gj56MjP+sipycmoyM/6uXjZqem7GQi7aRr42QnJqMjP+4mouvjZCcvpubjZqMjP+Tj76bm42ajIz/sI+zkJyUvY2anpS2ka+NkJiNmoyM/7CdlZqci7Gekpq6h5aMi4z/uI2Qio+6h5aMi4z/sJ2VmpyLsZCzkJGYmo26h5aMi4z/qoyajbqHloyLjP+rjZ6RjJ6ci5aQkayKj5qNlpCNuoeWjIuM/7yNkq+NkIuQnJCTvpONmp6bhrqHloyLjP+ynoeWkoqSsYusi56Lioz/tpGJnpOWm7aSnpias5q5kI2Snov/tpGJnpOWm7aSnpiauZCNkp6L/62aj56NjJqwnZWanIv/l7CdlZqci/+QnZWanIv/k4+Zk7CTm6+NkIuanIv/tpGJnpOWm7aSnpiar42Qi5qci/+plo2Lip6Tr42Qi5qci/++k5OQnJ6LlpCRr42Qi5qci/+Zk7GaiK+NkIuanIv/uZaTmrOQnJS8kJGZk5aci/+rjZ6RjJ6ci5aQkZ6TvJCRmZOWnIv/q42ekYyenIuWkJGsnJCPmryek5OdnpyUjLGQi6yai/+vkI2LsZCLrJqL/6+QjYu+k42anpuGrJqL/7yekYuonpaL/5CPoLqHj5OWnJaL/72em6iQjZSWkZismouzlpKWi/+8kJKSlouSmpGLs5aSlov/vJCRi42Qk7y6h5aL/42Ui42Ui/+2voyGkZytmoyKk4v/uZOQnou2kZqHnpyLrZqMipOL/42ajIqTi/+7nouei4aPmrKWjJ6TlpiRkpqRi/+rh5mymouem56Lnr6TjZqem4avjZqMmpGL/7yekYuwj5qRspaRlomajYyWkJGolouXspCblpmGtpGLmpGL/7qes5aMi7aRnJCRjJaMi5qRi/+5lpOatpuakYuWi4axkIuvmo2MloyLmpGL/72Nmp6Uj5CWkYv/rI+anJaek76cnJCKkYv/sZCuipCLnoy5kI2+nJyQipGL/62SspqLnpuei568kI2Nio+L/6uHmb6Li42WnYqLmryQjY2Kj4v/tpGJnpOWm7uaiZacmq2ajoqajIv/tpGbkIqdi6uNnpGMnpyLlpCRjLqHloyL/7KajIyemJqzkIyL/7mWk5q8l5qclJqbsIqL/7aQq5aSmpCKi/+shoyLmpLRq5qHi/+bipuK/7GQi7Kej4+am6mWmoj/uZOQnouqkZuajZmTkIj/vYqZmZqNsImajZmTkIj/tpGLmpiajbCJmo2Zk5CI/7mTkJ6LsImajZmTkIj/tpGJnpOWm6+ejZ6SmouajbKWh/+Unob/tpGWi5aek5aFmr6NjZ6G/52GnYb/vJ6Ri72Nmp6Uq42ekYyenIuWkJGek7uaj5qRm5qRnIb/r56Ni5aek7yQj4b/vJ6Ri7yNkIyMrZK9kIqRm56Nhv+zkJ6bs5adjZ6Nhv+5jZqas5adjZ6Nhv+xkLKakpCNhv+8npGLu5aMnp2TmrKekZuei5CNhv+xkJG6h5aMi5qRi7qeupGLjYb/u5qJlpyavYqMhv+vlo+avYqMhv+2kYmek5abrIqdvoqLl5CNlouG/7aRiZ6Tlpu2m76Ki5eQjZaLhv+shoyLmpLRrJqcio2Wi4b/r5aPmrqSj4uG/6uHmbuWjbGQi7qSj4uG/6mQk4qSmruWjYuG/7aRiZ6Tlpu2kp6YmrGQi7KF///Q0f+j/7L/mv+M/4z/nv+Y/5r/uf+N/5D/kv++/4r/i/+X/5D/jf/R/4v/h/+L//+smf+M/5v/iv+b/4r/m/+K/5v/iv+b/4r/nP+G/53/mv+N/4f/3/+W/4z/3/+R/5D/i//f/4v/l/+a/9//mf+T/57/mP/f/5v/iv+b/4r/m/+K//9/Ar3/nv+d/4b/3/+s/5f/nv+N/5T/3/+b/4r/m/+K/5v/iv+b/4r/m/+K//X/uf+W/5H/m//f/4v/l/+a/9//kv+W/5H/lv/f/4z/l/+e/43/lP/f/5v/kP+b/5D/m/+Q/5v/kP+b/5D/9f+5/5b/kf+b/9//i/+X/5r/3/+R/57/iv+Y/4v/l/+G/9//jP+X/57/jf+U/9//m/+e/5v/nv+b/57/m/+e/5v/nv/1/7H/kP/f/57/iv+L/5f/kP+N/9P/3/+W/5H/jP+L/57/kf+L/9//iP+W/5H/wP/1/7H/kP+L/9//jP+Q/9//mv+e/4z/hv/f/5f/mv+X//+zHtqnjwr3ulqajyzbtNrO//vf/v73/N///vrf/v7u7vvf/v7x+9/+/v363/7+7r763/7+7qbx+Pb39/f39/fi9+L34vr8+P729fj74vrw+rri+uf6//7n8P77//7m9Pn//P7n9/r7+P7i+vv//v3x+v//7X9u+t/+8eL69v/9/u1/Zu5/YvdIhaOp5ssfdvv/////+/7////7/f////v8////+8D////7f/////t+////+33////7fP////tA////+z/////7//7///v+/v//+/3+///7/P7///v7/v//+/r+///7+f7///v4/v//+/f+///79v7///v1/v//+/T+///78/7///vy/v//+/H+///77/7///vu/v//++3+///77P7///vr/v//++n+///75/7///vd/v//+9z+///72/7///vW/v//+9X+///71P7///v///+/+/7//7/7/f//v/v8//+/+/b//7/7////f/v+//9/+/3//3/7/P//f/v7//9/+/r//3/7+f//f/v1//9/+/L//3/77v//f/vs//9/++v//3/75f//f/vZ//9/+9T//3/7////P/v+//8/+/3//z/7/P//P/v7//8/+/r//z/7+f//P/v4//8/+/f//z/79v//P/v1//8/+/T//z/78///P/vy//8/+/H//z/78P//P/vv//8/++7//z/77f//P/vs//8/++j//z/75v//P/vl//8/++T//z/74v//P/ve//8/+93//z/73P//P/vb//8/+9r//z/71///P/vV//8/+9L//z/7z///P/vM//8/+8v//z/7yv//P/vG//8/+8X//z/7xP//P/vD//8/+8L//z/7wf//P/vA//8/+7///z/7vv//P/u9//8/+7z//z/7u///P/u6//8/+7n//z/7uP//P/u3//8/+7b//z/7tf//P/u0//8/+7P//z/7sv//P/ux//8/+7D//z/7r///P/uu//8/+63//z/7rP//P/ur//8/+6r//z/7qf//P/uo//8/+6f//z/7pv//P/ul//8/+6T//z/7o///P/ui//8/+6H//z/7oP//P/uf//8/+57//z/7nf//P/uc//8/+5v//z/7mv//P/uZ//8/+5j//z/7l///P/uW//8/+5X//z/7lP//P/uT//8/+5L//z/7kf//P/uQ//8/+4///z/7jv//P/uN//8/+4z//z/7i///P/uK//8/+4n//z/7iP//P/uH//8/+4b//z/7hf//P/uE//8/+4P//z/7gv//P/uB//8/+4D//z/7f///P/t+//8/+33//z/7fP//P/t7//8/+3r//z/7ef//P/t4//8/+3f//z/7dv//P/t1//8/+3T//z/7c///P/ty//8/+3H//z/7cP//P/tv//8/+27//z/7bf//P/ts//8/+2v//z/7av//P/tp//8/+2j//z/7Z///P/tU//8/+1P//z/7Uv//P/tR//8/+1D//z/7T///P/tO//8/+03//z/7TP//P/tL//8/+0r//z/7Sf//P/tI//8/+0f//z/7K///P/sq//8/+yf//z/7Jv//P/sk//8/+xr//z/7EP//P/sP//8/+w7//z/7Df//P/sM//8/+wv//z/7Cv//P/sJ//8/+wj//z/7B///P/sG//8/+wX//z/74f7/P/vg/v8/+9/+/z/73v7/P/vd/v8/+9z+/z/72/7/P/va/v8/+9n+/z/72P7/P/vX/v8/+9b+/z/71f7/P/vU/v8/+9P+/z/70v7/P/vR/v8/+9D+/z/7z/7/P/vO/v8/+83+/z/7zP7/P/vL/v8/+8r+/z/7yP7/P/vH/v8/+8b+/z/7xf7/P/us/P8/+6v8/z/7/Pr/P/v/+P8/+/74/z/7/fj/P/v8+P8/+/v4/z/7+vj/P/v5+P8/+/j4/z/79/j/P/vt+P8/+/n3/z/7/vb/P/v99v8/+/z2/z/7+/b/P/v69v8/+/n2/z/7+Pb/P/v+/+Y/+/3/5j/7/P/mP/v7/+Y/+/r/5j/7+f/mP/v4/+Y/+/f/5j/79v/mP/v1/+Y/+/T/5j/78//mP/vw/+Y/++//5j/77v/mP/vt/+Y/++z/5j/76//mP/vq/+Y/++n/5j/76P/mP/vn/+Y/++b/5j/73v/mP/vd/+Y/+9z/5j/72//mP/va/+Y/+9n/5j/71//mP/vW/+Y/+8//5j/7zv/mP/vN/+Y/+8z/5j/7y//mP/vK/+Y/+8n/5j/7yP/mP/vH/+Y/+8b/5j/7xf/mP/vE/+Y/+8P/5j/7wv/mP/vB/+Y/+8D/5j/7v//mP/u+/+Y/+73/5j/7vP/mP/u7/+Y/+7r/5j/7AAAAAPvv////+9/////7v/////v7////+/f////7//3///v/+///f2HR/n97rIaMi5qS0ayanIqNlouG0a+ajZKWjIyWkJGM0ayanIqNlouGr5qNkpaMjJaQkb6Li42WnYqLmtPfkoyckI2Tlp3T36majYyWkJHCy9HP0c/Rz9PfvIqTi4qNmsKRmoqLjZ6T09+vip2Tlpy0moarkJSakcKdyMieypzKyc7GzMuaz8fG6v6r/e+slJaPqZqNlpmWnJ6LlpCR/v79/Pni+vz57tv9+fb8+e7r/Pnu5/v//ufx+v/95+fx+//+/efz//r95+L69u/27+6u9//7/efm9u/29//94vri+uL6+f/8/ufm9vr//v7i+vzf//H8///++t/9/uPn9N/47uvx9vbn9vbn8d/27Zrx9vbn9vbn7Zbj+d/+7uvtmvPf+v3n4vr27/bv7q7v3/jtmufi+vbv9u/uru2W4/Xf/P3v9u/uru2a9/7/9///////4f7//v+r/emojZ6PsZCRuoecmo+LlpCRq5eNkIiM/vf+//3///////D+//W9np2GoKyXno2P///6/v/////o/v/tvJCPho2WmJeL3z1W39/Nz83P///W/v/bmZ3Jz8mdyc/Sm5vLzdLLnpzG0saazcjSnJydycidyJnHzcad///z/v/4ztHP0c/Rz///sv7/49Gxuqu5jZ6SmoiQjZTTqZqNjJaQkcKJy9HI0c3+/6vx67mNnpKaiJCNlLuWjI+TnoaxnpKa69GxuqvfuY2ekpqIkI2U38vRyNHN9/7//P///////////yMydEP//////f///5r///8rn///K73//////////////////+////////////////////+trLus1a06qIGjhblzngMiMH0wj/7///+8xaOqjJqNjKOchpWWmqOMkIqNnJqjjZqPkIyjvZ6dhqCsl56Nj6O9np2GoKyXno2Po5CdlaOtmpOanoyao72enYagrJeejY/Rj5ud/+AG3J2b7LGreJkiRdxqOrAN//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////7/7////+f//3////////////////////7//v///8///3////////////////////7//////7f///+nf///0/z/////////////0/zL////qf+s/6D/qf+6/63/rP+2/7D/sf+g/7b/sf+5/7D//////0L7EAH///7////+//////////7//////8D/////////+/////3///////////////////+7/////v+p/57/jf+5/5b/k/+a/7b/kf+Z/5D//////9v/+////6v/jf+e/5H/jP+T/57/i/+W/5D/kf////////9P+3P9///+/6z/i/+N/5b/kf+Y/7n/lv+T/5r/tv+R/5n/kP///5f9///+/8//z//P/8//z//L/53/z////+X//v/+/7z/kP+S/5L/mv+R/4v/jP/////////d//7//v+8/5D/kv+P/57/kf+G/7H/nv+S/5r////////////B//T//v+5/5b/k/+a/7v/mv+M/5z/jf+W/4//i/+W/5D/kf//////vf+e/53/hv+g/6z/l/+e/43/j///////z//3//7/uf+W/5P/mv+p/5r/jf+M/5b/kP+R///////O/9H/z//R/8//0f/P////wf/w//7/tv+R/4v/mv+N/5H/nv+T/7H/nv+S/5r///+9/57/nf+G/6D/rP+X/57/jf+P/9H/m/+T/5P//////7f/7f/+/7P/mv+Y/57/k/+8/5D/j/+G/43/lv+Y/5f/i////7z/kP+P/4b/jf+W/5j/l/+L/9//Vv/f/9//zf/P/83/z////9X//v/+/7P/mv+Y/57/k/+r/43/nv+b/5r/kv+e/43/lP+M////////////uf/w//7/sP+N/5b/mP+W/5H/nv+T/7n/lv+T/5r/kf+e/5L/mv///73/nv+d/4b/oP+s/5f/nv+N/4//0f+b/5P/k///////yf/0//7/r/+N/5D/m/+K/5z/i/+x/57/kv+a//////+9/57/nf+G/6D/rP+X/57/jf+P///////L//f//v+v/43/kP+b/4r/nP+L/6n/mv+N/4z/lv+Q/5H////O/9H/z//R/8//0f/P////x//3//7/vv+M/4z/mv+S/53/k/+G/9//qf+a/43/jP+W/5D/kf///87/0f/P/9H/z//R/8//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
    for i in byt:
        print(bs64.index(i), end='')
