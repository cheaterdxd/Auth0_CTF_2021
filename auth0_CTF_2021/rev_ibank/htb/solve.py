s = '{BTH_v3r_dn4pyrc4_0tf_3rn3ir }sd'
# print(len(s))
# print(s[::-1])
rev = ''
for i in range(0,int(len(s)/4)):
    print(i)
    a = s[i*4:(i+1)*4]
    print(a)
    rev += a[::-1]
    # print(s[i*4:(i+1)*4])
    # print(rev)

print(rev)