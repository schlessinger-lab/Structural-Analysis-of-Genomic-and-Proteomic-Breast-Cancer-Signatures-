# max_dict = {}
# with open('gtex_af.csv') as fo:
#     for line in fo:
#         split_line = line[:-1].split(',')[1:]
#         for index in range(len(split_line)):
#             if index not in max_dict:
#                 max_dict[index] = float(split_line[index])
#             else:
#                 if max_dict[index] < float(split_line[index]):
#                     max_dict[index] = float(split_line[index])

# with open('gtex_af.csv') as fo:
#     for line in fo:
#         split_line = line[:-1].split(',')
#         out = split_line[0] + ','
#         split_line = split_line[1:]
#         for index in range(len(split_line)):
#             if max_dict[index] != 0:
#                 out = out + str(float(split_line[index])/max_dict[index]) + ','
#             else:
#                 out = out + split_line[index] + ','
#         f = open('norm_gtex_af.csv', 'a+')
#         f.write(out[:-1] + '\n')
#         f.close()

out_dict = {}
with open('norm_gtex_af.csv') as fo:
    for line in fo:
        split_line = line.split(',',1)
        out_dict[split_line[0]] = split_line[1]

# with open('norm_gtex_ss3.csv') as fo:
#     for line in fo:
#         split_line = line.split(',',1)
#         if split_line[0] in out_dict:
#             out = line[:-1] + ',' + out_dict[split_line[0]]
#             f = open('norm_gtex_sages.csv', 'a+')
#             f.write(out)
#             f.close()
#         else:
#             print(split_line[0])

with open('norm_gtex_ss3_gn.csv') as fo:
    for line in fo:
        split_line = line.split(',',1)
        if split_line[0] in out_dict:
            out = line[:-1] + ',' + out_dict[split_line[0]]
            f = open('norm_gtex_sages_gn.csv', 'a+')
            f.write(out)
            f.close()
        else:
            print(split_line[0])

# with open('norm_gtex_ss3_gn.csv') as fo:
#     for line in fo:
#         split_line = line.split(',',1)
#         out = line[:-1] + ',' + out_dict[split_line[0]]
#         f = open('norm_gtex_sages_gn.csv', 'a+')
#         f.write(out)
#         f.close()


