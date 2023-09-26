import glob

id_dict = {}
with open('raw_bc_RNAsq/gene_id_key.csv') as fo:
    for line in fo:
        split_line = line[:-1].split(',')
        if split_line[1] != '""':
            id_dict[split_line[0][1:-1]] = split_line[1][1:-1]

file_list = glob.glob('raw_bc_RNAsq/*-tissue.csv')
for f in file_list:
    name = f.split('/')[-1]
    with open(f) as fo:
        index = -1
        tot_num = 0
        track_dict = {}
        for line in fo:
            index +=1 
            if index != 0 and index <= 1000:
                split_line = line[:-1].split(',')
                tot_num += int(split_line[1])
                track_dict[split_line[0][1:-1]] = int(split_line[1])
    if f.split('-')[-2] == 'tumor':
        out_folder = 'rna_tumor/'
    else:
        out_folder = 'rna_background/'
    fout = open(out_folder+name, '+w')
    for key in track_dict:
        if key in id_dict:
            fout.write(id_dict[key]+','+str(track_dict[key])+ '\n')
        else:
            print(key)
    fout.close()
