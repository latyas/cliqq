'''
function (a, e) {
                for (var c = [], d = 0; d < a.length; d++) c[d] = a.charAt(d) - 0;
                for (var b = 0, k = -1, d = 0; d < c.length; d++) {
                    b += c[d];
                    b %= e.length;
                    var f = 0;
                    if (b + 4 > e.length) for (var g = 4 + b - e.length, h = 0; h < 4; h++) f |= h < g ? (e.charCodeAt(b + h) & 255) << (3 - h) * 8 : (e.charCodeAt(h - g) & 255) << (3 - h) * 8;
                    else for (h = 0; h < 4; h++) f |= (e.charCodeAt(b + h) & 255) << (3 - h) * 8;
                    k ^= f
                }
                c = [];
                c[0] = k >> 24 & 255;
                c[1] = k >> 16 & 255;
                c[2] = k >> 8 & 255;
                c[3] = k & 255;
                k = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"];
                d = "";
                for (b = 0; b < c.length; b++) d += k[c[b] >> 4 & 15], d += k[c[b] & 15];
                return d
            }
'''

def getFriend2_hash(a, e):
    c = [int(i) for i in a]
    b = 0
    k = -1
    for d in xrange(len(c)):
        b += c[d]
        b %= len(e)
        f = 0
        if b + 4 > len(e):
            g = 4 + b - len(e)
            for h in xrange(4):
                f |= (ord(e[b + h]) & 255) << (3 - h) * 8 if h < g else (ord(e[h - g]) & 255) << (3 - h) * 8
        else:
            for h in xrange(4):
                f |= (ord(e[b + h]) & 255) << (3 - h) * 8
        k ^= f

    c = [0 for i in xrange(4)]
    c[0] = k >> 24 & 255
    c[1] = k >> 16 & 255
    c[2] = k >> 8 & 255
    c[3] = k & 255
    k = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    d = ""
    for b in xrange(len(c)):
        d += k[c[b] >> 4 & 15]
        d += k[c[b] & 15]
    return d

'''
			O = function(b, i) {
				for (var a = i + "password error", s = "", j = [];;) if (s.length <= a.length) {
					if (s += b, s.length == a.length) break
				} else {
					s = s.slice(0, a.length);
					break
				}
				for (var d = 0; d < s.length; d++) j[d] = s.charCodeAt(d) ^ a.charCodeAt(d);
				a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"];
				s = "";
				for (d = 0; d < j.length; d++) s += a[j[d] >> 4 & 15], s += a[j[d] & 15];
				return s
			},
'''

def getFriend2_hash2(b, i):
    a = str(i) + "password error"
    s = ""
    while 1:
        if len(s) <= len(a):
            s += str(b)
            if len(s) == len(a):break
            else:
                pass
        else:
            s = s[0:len(a)]
            break
    j = [0 for i in xrange(len(s))]

    for d in xrange(len(s)):
        j[d] = ord(s[d]) ^ ord(a[d])

	aa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
	ss = ""
    for d in xrange(len(j)):
        ss += aa[j[d] >> 4 & 15]
        ss += aa[j[d] & 15]
    return ss

import urllib2
import PyV8
import re

def getFriend_hash(b,i):
        
    data = urllib2.urlopen("http://0.web.qstatic.com/webqqpic/pubapps/0/50/eqq.all.js").read()
    data = data.split("P=function")[1].split(",b=function")[0]
    data = "P=function" + data


    js = PyV8.JSContext()         
    js.enter()                       

    data = data + ';P("' + b + '","' + i + '");'
    
    s = js.eval(data)
    return s
    
if __name__ == "__main__":
    uin = raw_input('uin:')
    ptwebqq = raw_input('ptwebqq:')
    print getFriend2_hash2(uin, ptwebqq)
