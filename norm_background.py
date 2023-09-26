import glob

fs = glob.glob('weighted_gtex_all/Breast*')

targs = {}
for f in fs:
    with open(f) as fo:
        for line in fo:
            split_line = line[:-1].split(',')
            if split_line[0] not in targs:
                targs[split_line[0]] = [float(split_line[1])]
            else:
                targs[split_line[0]] = targs[split_line[0]] + [float(split_line[1])]

for t in targs:
    f1 = open('gtex_breast.csv', 'a+')
    f1.write(t + ',' + str(sum(targs[t])/len(targs[t])) + '\n' )
    f1.close()

