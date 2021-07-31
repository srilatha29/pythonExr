
import re
import calendar
import time
import os
import random
import string


arr = [0, -1, 2, -3, 1]
s = ()
triplet = []
for i in range(0, len(arr)-2):
    for j in range(i+1,len(arr)-1):
        for k in range(j+1, len(arr)):
            if arr[i] + arr[j] + arr[k] == 0:
                s = (arr[i], arr[j], arr[k])
                triplet.append(s)

print(triplet)
                
        



"""

l = [(1,2),(3,4),(5,9),(5,6),(6,7)]

if range(5,6)  in range(5,9):
    print('true')
else:
    print('False')

output = '''
show ip int bri TenGigabitEthernet0/1/2
Interface              IP-Address      OK? Method Status                Protocol
Te0/1/2                6.6.6.4         YES DHCP   up                    up      
ASR1002-hx#'''
if re.search('\S+ +6\.6\.6\.\d+.*', output):
        print('ppass')
else:
    print('fail')
"
#User function Template for python3
global matrix
N = int(input('Enter the dimension of matrix:'))
arr = [int(x) for x in input('input {0} space seperaated values:'.format(N*N)).split()]
matrix = []
for i in range(0,N*N,N):
    matrix.append(arr[i:i+N])
print(matrix)
def rotate():
    global    matrix
    left = len(matrix)
    eleft = len(matrix[0])
    rotate_90 = list()
    j = eleft
    #print(j)
    while j > 0:
        l1 = []
        for i in range(left):
            #print(i)
            l1.append(matrix[i][j-1])
            #i += 1
        rotate_90.append(l1)
        j -= 1
    #print(rotate_90)
    matrix=rotate_90
    #return(matrix)

rotate()
print(matrix)

#=============
def alternateSort(arr, N):
    # Your code goes here
    try:
        left = N
        iter= int(N/2)
        half = int(N/2)
        arr.sort(reverse=True)
        #print(iter)
        right = 0
        new_list = []
        while iter > 0:
            new_list.append(arr[right])
            new_list.append(arr[left-1])
            left -=1
            right +=1
            iter-=1
        if N%2 == 1:
            #print(half)
            new_list.append(arr[half])
        print(new_list) 
        return new_list
    except Exception as err:
        print("there is sommething wrong {0}".format(err))
print (alternateSort([1,2,3,4,5,6,7,8,9], 9))

##================================
l1 = ['srilatha', 'devineni', 'bigboss','pavan']
l1.reverse()
l3 = [x[::-1] for x in l1]

print(l3)
print(l1)
l2 =[]
for str in l1:
    temp = ''
    left = len(str)
    while left > 0:
        temp+= str[left-1]
        left -=1
    l2.append(temp)
    
print(l2)



nbr_of_bits = 0
while 8 
for l in range(0 ,32

l1 = [10,4,6,3,2]
l2 = [5,6,2,4,1]

l3 = l1
l3.append(55)
print(l1)
l3 = list(l1)

l3.append(30)
print(l1)
print(l3)


t1 = (1,4,6,2,3)
t2 = t1
print (id(t1))
print (id(t2))
del t1
print(t2)

l1 = [10,4,6,3,2]
l2 = [5,6,2,4,1]
print(min(l1 + l2))
l1.sort()
l2.sort()
print(min(l1[0] , l2[0]))
class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = float(balance)
        print(f'Hi {owner} your account is opened with HDFC rs{balance}')

    def deposit(self,value):
        self.balance =  self.balance + value
        print('amount deposited is %f'%self.balance)
        #return  self.amt
    def withdraw(self,value):
        if value <= self.balance:
            self.balance =  self.balance - value
            print('amount withdrawn is %f Balance is %f'%(value, self.balance))
        else:
            print('insufficient balance')
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"
accnt1 = Account('Jose', 100)
print(accnt1)
accnt1.deposit(300)
accnt1.withdraw(50)
accnt1.withdraw(100)
accnt1.withdraw(300)


number = 100
numbe_12 = 200
print(numbe_12)
#/ws/sdevinen-bgl/piinfra/obs_vtest_scripts/snmp/logs

def descending_order(num):
    numb = str(num)
    l1 = []
    num = ''
    for char in numb:
        l1.append(char)
    l1.sort()
    for char in l1:
        num += char
    return int(num)
print(descending_order(423))

string = "geeks forg geeks geeks geeks geeks"
last = len(string)
rev = ""
print(last)
while last > 0:
    print(last)
    rev += string[last-1]
    last -= 1
    
print(rev)  
# Prints the string by replacing all
# geeks by Geeks

first = string[0].upper()

fourth = string[3].upper()
str1= string.replace(string[0],first,5)
str2 = str1.replace(string[3],fourth,5)
print(str2)



cwd = os.getcwd()
print('current woring directory is {cwd}'.format(cwd=cwd))
files = os.listdir()
for file in files:
    file1 = re.sub('F57049_rsh_rcp', 'snmp_cli', file)
    orig_file_name = os.path.join(cwd,file)
    print(orig_file_name)
    modfied_file_name = os.path.join(cwd,file1)
    os.rename(orig_file_name, modfied_file_name)
    print(modfied_file_name)
    
files = os.listdir()       
print(files)

def palindrom(text):
    l = len(text)
    flag = 0
    left = 0
    right = l-1
    nrIters = int(l/2)
    while nrIters >= 0:
        if text[left] == text[right]:
            print(text[left])
        else:
            flag = 1
            break
        left+=1
        right-=1
        nrIters -=1

    if not flag:
        print('given strin is paliindrom')
    else:
        print('not a palindrom')
            
palindrom(input())
#palindrom('madam')

Sample_String = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(text):
    upper = []
    upper_count = 0
    lower_count = 0
    lower = []
    for x in text:
        if  x == ' ':
            continue
        elif x.isupper():
            upper.append(x)
            upper_count+=1
        elif x.islower():
            lower.append(x)
            lower_count+=1
        else:
            pass
    return upper,lower, upper_count, lower_count      
    
print(up_low(Sample_String))

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])
myfile = open('myfile.txt',mode='a')
myfile.write("This is creating to learn \n")

l = ['one', 1 , 1,3.15]
print(hex(id(l)))
print(l)
l.append(2)

print(l)
l.pop(2)
print(f"3'rd time {l}")
#l = ['one', 1, 3.15, 1]
print(hex(id(l)))
t = ('one', 1, 1,3.15)
print(t)
print(t.index(1))
print(t.index(1))
print(hex(id(t)))

set1 = {5, 6}
set1.add(3)
set1.add(4)
print(set1)
s=set('ppop')
s.add('parr')
print(s)

s = 'sh ip bgp neighbor'
print(f'my namem is this s \t strinig {s}')
print(f'\rmy namem is this s \t strinig {s}')


op = '''
BGP neighbor is 22.22.2.1,  remote AS 1, internal link
  BGP version 4, remote router ID 0.0.0.0
  BGP state = Idle, down for never
  Last update received:'''

if re.search('(?:sh ip bgp neighbor\\n)?BGP neighbor is 22\.22\.2\.1,.*\\n.*\\n.*bgp +state += +idle, +down', op,re.I):
    print('pass')
else:
    print('no')



ip_add = set()
ip_add.add((('11.15.21.17','11.15.26.145')))
ip_add.add((('11.15.21.145','11.15.26.17')))
print(len(ip_add))

result3 ='[1]+  Running      timeout 120 tcpdump -i ens192 port 161 -w capture_file196.pcap &'
result3 ='[1]+  Running'
print(result3)

if re.search('\+ +Running', result3):
    print(' AMMMMMMMMMMM SRRRRRRRRR **&&%&$@--------->>>>>>>>>>>>>>>>')
    ps_id = re.search('\[(\d+)\]\+ +Running', result3).group(1)
    print('kill %'+'%s'%(ps_id))


output = '''
  %Insertion failed - prefix-list entry exists:
  ip prefix-list fooadd: 2 entries
     seq 10 permit 10.1.1.0/24
    seq 20 permit 10.1.1.0/24''' 

if re.search('.*insertion +failed +- +prefix-list +entry +exists',output,re.I):
    print('''ip prefix-list fooadd with dupilcate 
            entries is not configures''')
    
output = '''nyquist-9500#show ip cef 13.13.13.0 255.255.255.0 detail 
13.13.13.0/24, epoch 3, flags [rib only nolabel, rib defined all labels]
  recursive via 8.8.8.1
    recursive via 8.8.8.0/24
      nexthop 5.5.5.2 TenGigabitEthernet2/0/1'''
m =re.search('nexthop +(\S+) +(\S+)',output)
    
print(m.group(2))

list = ['13.13.13.0', '14.14.14.0', '15.15.15.0','16.16.16.0',
        '17.17.17.0', '18.18.18.0', '19.19.19.0', '20.20.20.0']
print(list)


output = '%NTP: failed to initialize NTP process'

if re.search('.*NTP: +failed +to +initialize +NTP+ process', output):
    print('ntp error messages')
else:
    print('n essages')

f = open('/Users/sdevinen/Desktop/vty-delete.txt','w+')
for i in range(530, 0, -1):
    f.write('no line vty %d\r\n' %(i))
 
f = open('/Users/sdevinen/Desktop/vty.txt','w+')
for i in range(530):
    
    f.write('line vty %d\r\n' %(i))
    if (i % 2 != 0): 
        f.write('transport input rlogin ssh\r\n')
    else: 
        f.write('transport input telnet\r\n')


f = open('/Users/sdevinen/Desktop/vty-delete.txt','w+')
for i in range(530):
    f.write('line vty %d\r\n' %(i))
    f.write('transport input rlogin ssh\r\n')

    
def sshTime(self,user,tHost):
host,port = tHost
print "Connecting %s@%s:%d " % (user,host,int(port))para = paramiko.Transport(sock)
para.local_version="SSH-2.0-Blabla"

try:
para.connect(username=lab)

except EOFError,e:
print "Error: %s" % e
return -1

except paramiko.SSHException,e:
print "Error: %s" % e
return -2

#results in a long wait on sshd side, as it needs to calc the password
#only if the user exists
passwd = 'A'*39000

#time measurement
timeStart = int(time.time())

try:
para.auth_password(user,passwd)
except paramiko.AuthenticationException,e:
print e
except paramiko.SSHException,e:
print e

timeDone = int(time.time())

#simple time calculation
timeRes = timeDone-timeStart

if timeRes &gt; 20:
print "User: %s exists" % user
para.close()
return

else:
print "User: %s not found" % user   

l = list()
for line in ssh_out.split('\n'):
    item = line.split(' ')[0]
    print('item is |%s|'%item)
    if re.search('^\d+$' , item):
        l.append(item)
b = set(l)
print(b)

def close_ssh(device, l=[]):
    
    for vty in l:
        print('clear line vty %s'%vty)

close_ssh('uut' , b)


output = '''show sntp
SNTP server                Stratum   Version    Last Received
2001:DB8:0:4::10A            2           4        00:00:30      Synced'''

#utput = '''SNTP server                Stratum   Version    Last Received
#10.106.26.228               2           4        00:00:09      Synced'''
m = re.search('((?:\d+\.\d+\.\d+\.\d+)|(?:(?:[a-f0-9]+::?)+[a-f0-9]+)) +\d+ +\d+ +\S+ +synced', output,re.I)
if m:
    s=m.group(1)
    print("NTP client is synchronized %s"%s)
else:
    print('notmatche')

server_ip= '5.5.5.1'
server_ip_to_match= '\.'.join(server_ip.split('.'))
output = '''Clock is synchronized, stratum 3, reference is 5.5.5.1        
nominal freq is 250.0000 Hz, actual freq is 249.9962 Hz, precision is 2**10
ntp uptime is 18600 (1/100 of seconds), resolution is 4016
reference time is E0F65DDF.91EB86B0 (14:07:51.570 IST Thu Aug 8 2019)
clock offset is 52.0000 msec, root delay is 1.00 msec
root dispersion is 7994.92 msec, peer dispersion is 189.48 msec
loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000015041 s/s
system poll inter'''

if re.search('clock +is +synchronized.*%s'%server_ip_to_match, output,re.I):
    print('matched')
else:
    print('fail')

jos = 'joshi'
print(f'candidate name is {jos}')

output = '''SNTP server                Stratum   Version    Last Received
10.106.26.228               2           4        00:00:09      Synced'''
if re.search('\d+\.\d+\.\d+\.\d+ +\d+ +\d+ +\S+ +synced', output,re.I):
    print('matched')
else:
    print('unmatched')
    
fd = open('srilatha-test.txt', '+')
fd.write("python is python")
fd.close()



mylist = [0,'srilatha' , 4, 5.3]
val = mylist[1].upper()
mylist[1] = mylist[1].upper()
print(mylist)


l1 = [ 1,2,3,4,5,6]
l3 = l1
l2 = l1[0:]
l2[0] = 7
print(l1)
l3[0]=8

print(l1)

name = 'Srilatha'
age = 37
f = 100/77
print (f'my name is: {name}, age:{age}') 
print (f'value of f is {f}')
print(f'value of f is {f:#<10.4f} end.')
print(f'value of f is {f:*>10.4f} end.')
print(f'value of f is {f:-^10.3f} end.')
print('he sais his name was %s' %'fred')
print('he sais his name was %s' %name)
print('he sais his name was %r' %name)

def randomStringDigits(stringLength=6):
    '''Generate a random string of letters and digits '''
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
print ("Generating a Random String including letters and digits")
print ("First Random String is  ", randomStringDigits(8))
print ("Second Random String is ", randomStringDigits(8))
print ("Third Random String is  ", randomStringDigits(8))

i = 239
sri = dict()
while i:
    sri[i] = randomStringDigits(i)
    i = i-1
print (sri)
    

output = '''username lab privilege 15 password 6 lab
username cisco privilege 15 password 6 cisco
username priv0 privilege 0 password 6 priv0
username lab123 privilege 15 password 6 lab123'''
username = 'lab1234'
password = 'lab123'
priv = '15'
for line in output.split('\n'):
    
    m = re.match('username +%s +privilege +%s +password +6 +(\S+)'%(username,priv) , line)
    if m:
        print(line)
        type6_pwd= m.group(1)
        print('type 6 password id %s'%type6_pwd)

if not type6_pwd:
    print('no user')

cmd = 'sftp://sdevinen:dfgr@10.106.253.128//tftp/sdevinen/file flash:'
m = re.search('sftp://(.*?):(.*?)@(.*?)//(.*)/(.*?) +.*',cmd)
if m:
    username = m.group(1)
    password = m.group(2)
    src_mgmt_ip = m.group(3)
    src_path = m.group(4)
    src_file = m.group(5)
    print(username,password, src_mgmt_ip , src_file, src_path)
            




"
#print (re.search'(?:.*(?:\\n.*)?.*(?:\??\[confirm\])?\#?)',output))
#print (re.search('(?:(?:.*(?:\\n.*)*.*)(do you want to over write\? \[confirm\]))|(.*(?:\\n.*)*.*\\#)',output,re.I).group(1))
#print (re.search('(?:(?:(?:.*\\n)+.*)(write.*\[confirm\]))|(.*(?:\\n.*)*.*\\#)',output,re.I).group(1))
out = re.search('(?:.*(?:\\n.*)*.*((?:write.*\[confirm\])|(?:\\#)))',output,re.I).group(1)
if re.search('confirm',out,re.I):
    print('yes')
else:
    print('no match')
uut_output = ''' sh fips status
Switch and Stacking are  not running in FIPS mode'''
res =0
res = re.search('switch *and *stacking *are *not *running *in *fips *mode', uut_output, re.I)
print(res)
res = re.search('switch *and *stacking *are *running *in *fips *mode', uut_output, re.I)
print(res)



#month_number = {v: k for k,v in enumerate(calendar.month_abbr)}
month_number = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
print(month_number)

str = 'i am new to this town'
str = "%WEBSERVER-5-LOGIN_PASSED: Switch 1 R0/0: nginx: Login Successful from host 10.232.9.5 by user 'cisco'"
user = 'cisco'

cmd  = '.*WEBSERVER.*LOGIN_PASSED.* by +user.*\'(%s)\'' %(user)
output = re.search(cmd,str,flags = (re.I&re.M)).group(1)
print(output)
res = 1

import time
import datetime
print (time.localtime())
print (time.localtime().tm_gmtoff)
l = time.localtime().tm_gmtoff // 3600
print (l)

print ('priting')
print (len('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxcccccccccccccc'))
'''

'''
if re.search(r"\b(?=\w)TEXTO\b(?!\w)", subject, re.IGNORECASE):
    # Successful match
else:
fips_dir = '/rootCA/'
password =  'cisco123'
cmds = [
        'mkdir %s' % fips_dir,
        
        'openssl genrsa -out %srootCA.key 2048' % fips_dir,
        
        'openssl req -subj /C=/ST=/L=/O=/CN=rootCA -x509 -new -nodes -key %srootCA.key -sha256 -days 9999 -out %srootCA.pem' % (fips_dir, fips_dir),
        
        'openssl genrsa -out %sdevice.key 2048' % fips_dir,
        'openssl req -subj /C=/ST=/L=/O=/CN=%s -new -key %sdevice.key -out %sdevice.csr' % ('nyq12', fips_dir, fips_dir),
        'openssl x509 -req -in %sdevice.csr -CA %srootCA.pem -CAkey %srootCA.key -CAcreateserial -out %sdevice.crt -days 9999 -sha256' % (fips_dir, fips_dir, fips_dir, fips_dir),
        'openssl rsa -des3 -in %sdevice.key -out %sdevice.des3.key -passout pass:%s' % (fips_dir, fips_dir, password),
        'openssl genrsa -out %sclient.key 2048' % fips_dir,
        'openssl req -subj /C=/ST=/L=/O=/CN=fips_client -new -key %sclient.key -out %sclient.csr' % (fips_dir, fips_dir),
        'openssl x509 -req -in %sclient.csr -CA %srootCA.pem -CAkey %srootCA.key -CAcreateserial -out %sclient.crt -days 9999 -sha256' % (fips_dir, fips_dir, fips_dir, fips_dir),
        ]

print ('openssl genrsa -out %srootCA.key 2048' % fips_dir)
print('openssl req -subj /C=/ST=/L=/O=/CN=rootCA -x509 -new -nodes -key %srootCA.key -sha256 -days 9999 -out %srootCA.pem' % (fips_dir, fips_dir))
for c in cmds:
    print ("cmd", c)

14 March 2018

Hi Nitya
11:50 AM
Hi
12:06 PM
Do u've any https scripts already in regression
can u give me path
12:07 PM
ya.. im having
i will give
12:07 PM
Is it tcl? Python ?
12:07 PM
tcl only
12:07 PM
k
12:07 PM
Let me see them
12:08 PM
regression/tests/functionality/ios-infra/ios-mps/HTTP/httpserver/http_srvstress
this is one script
12:08 PM
what is your requirement ?
12:09 PM
I don't know how to access these files
i just want to see existing library
12:11 PM
that is cvs file
12:11 PM
inside ats tree path you can check it out
/home/rbalagur/ats5.1.0/regression/tests/functionality/ios-infra/ios-mps/HTTP/httpserver/http_srvstress
this is full path
12:12 PM
You can checkout inside your tree
12:13 PM
'''
"""


