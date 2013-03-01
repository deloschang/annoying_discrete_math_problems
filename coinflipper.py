# to solve annoying discrete mathematics outcome listing problems

def convert(number):
    if number == 0:
        print "T",
    if number == 1:
        print "H",

i = 0 
counter = 0 
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    convert(i)
                    convert(j)
                    convert(k)
                    convert(l)
                    convert(m)
                    print "\n"
                    counter += 1

print counter

