
#1

def revAlternateK(s, k, Len):
    i = 0
    while (i < len(s)):
        if (i + k > Len):
            break
        ss = s[i:i + k]
        s = s[:i] + ss[::-1] + s[i + k:]
        i += 2 * k
    return s;
s = "abcdefg"
Len = len(s)
k = 2
print(revAlternateK(s, k, Len))

#2

bad_chars = ["CON"]
input_str = "PCONECONCONN"
for i in bad_chars:
    input_str = input_str.replace(i, ' ')
print("output_str = " +'"'+str(input_str)+'"')

#3

Input_str = "ATTCGGTAG"
res = Input_str.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T')
var = res.replace('C', '%temp%').replace('G', 'C').replace('%temp%', 'G')
print("Output_str = " + var)

#4

v = "2012-18-10 Speaker Harman"
v = v.replace('-', '')
print((v.split(' ')[0]))

#OR

v = "2012-18-10 Speaker Harman"
print("output_string = "+'"'+(v.split(' ')[0]).replace('-','')+'"')