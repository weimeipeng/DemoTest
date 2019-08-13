
for line in range(1,10):
    for i in range(1,line+1):
        print('%d*%d=%d' % (i,line,i*line),end="\t")
    print("")