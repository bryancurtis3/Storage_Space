
file = "mailexchange.txt"
f = open(file, "r")

line = f.read()
lineMX = line.split("\n")

file = "quota.txt"
f = open(file, "r")

line = f.read()
lineQ = line.split("\n")

lengthMX = len(lineMX)
n = 0
i = 0
q = 0
y = 0
t = 0
qu = 0
it = 0
dom = -1

mxList = []

checker = "good"
clean = []
user = []
cleaned = []



for m in range(lengthMX - 1):
    domainMX = []
    mx = []


    if "\t" not in lineMX[m] and ' ' not in lineMX[m] or lineMX[m][0] == ";" :
        m += 1



    # Extracts domain line by line
    while lineMX[m][q] != "\t" and lineMX[m][q] != ' ':
        domainMX += lineMX[m][q]
        q += 1

    # Extracts MX's
    for r in range(len(lineMX[m])):
        t = r + 2

        if lineMX[m][r] == "X":
            while t < len(lineMX[m]):
                mx += lineMX[m][t]
                t += 1


    # Prints domain with matching MX
    domainMX = "".join(domainMX)
    domainMX = domainMX.lower()
    #print(domainMX)

    mx = "".join(mx)
    #print(mx)
    mxList.append(mx)
    q = 0

    if "google" in mx.lower():
        
        if checker != domainMX or checker == "good":
            clean = list(domainMX)
            clean[-1] = ''
            clean = "".join(clean)
            #print(clean)

            cleaned.append(clean)

            checker = domainMX
            #print(checker)

#___________________PHASE_TWO______________________

duck = sorted(cleaned)

#print(duck)


file = "trueuserdomains.txt"
f = open(file, "r")

line = f.read()
line = line.split("\n")

y = 0
x = 0
z = 0
i = 0
lineNums = []
rested = []
domain = ''
#print("\n\n")
#print(cleaned)
#print("\n\n")


for n in range(len(line)):
    sep = ': '
    rest = line[n].split(sep, 1)[1]
    first = line[n].split(sep, 1)[0]
    rested.append(rest)
    
    for x in range(len(cleaned)):
        
        if first == cleaned[x]:
            lineNums.append(n)
                

            
unrested = []
#print(rested)
for bee in range(len(lineNums)):
    unrested.append(rested[lineNums[bee]])

rerested = sorted(unrested)
recleaned = sorted(cleaned)

#print(rerested)
#print(recleaned)

#print(lineNums)




#print(rerested)

for qu in range(len(lineQ)):
    clean = ''
    rest = ''

    
    if "---" in lineQ[qu]:
        dom += 1
    

    if "megabyte_limit: '" in lineQ[qu]:
        limit = lineQ[qu].split(": ", 1)[1]
        limit = limit.strip("'")
        limit = float(limit)



    if "megabytes_used" in lineQ[qu]:
        sep = ': '
        rest = lineQ[qu].split(sep, 1)[1]
        rest = rest.strip("'")
        rest = float(rest)
        percent = round(rest/limit, 3)
        percent *= 100

        if rest >= 3000:
            print(rerested[dom], "\t", rest, "\t", percent, end = "% used\n")
          
