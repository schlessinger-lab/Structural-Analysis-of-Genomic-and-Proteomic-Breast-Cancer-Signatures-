import plotly.express as px
import plotly.graph_objects as go
from statistics import stdev


def read_file(filename):
    x = []
    y = []
    with open(filename) as fo:
        for line in fo:
            split_line = line.split(',')
            x.append(float(split_line[0]))
            y.append(float(split_line[1]))
    return x,y

def read_accuracy(filename):
    accuracy = []
    auroc = []
    f1_val= []
    precision_val= []
    recall_val = []
    with open(filename) as fo:
        for line in fo:
            split_line = line[:-1].split(',')
            accuracy.append(float(split_line[1]))
            auroc.append(float(split_line[2]))
            f1_val.append(float(split_line[3]))
            precision_val.append(float(split_line[4]))
            recall_val.append(float(split_line[5]))
    # out_list = [accuracy/line_index, auroc/line_index, f1_val/line_index, precision_val/line_index, recall_val/line_index]
    pmsymbol = "\u00B1"
    out_str = str(round(sum(accuracy)/len(accuracy), 3)) + pmsymbol + str(round(stdev(accuracy),3)) + ',' + str(round(sum(auroc)/len(auroc),3)) + pmsymbol + str(round(stdev(auroc),3)) + ',' +str(round(sum(f1_val)/len(f1_val),3)) + pmsymbol + str(round(stdev(f1_val),3)) + ','+str(round(sum(precision_val)/len(precision_val),3)) + pmsymbol + str(round(stdev(precision_val),3)) + ','+str(round(sum(recall_val)/len(recall_val),3)) + pmsymbol + str(round(stdev(recall_val),3)) + '\n'
    return out_str

# def read_accuracy(filename):
#     # accuracy = 0
#     # auroc = 0
#     # f1_val= 0
#     # precision_val= 0 
#     # recall_val = 0
#     # line_index = 0
#     with open(filename) as fo:
#         for line in fo:
#             # line_index += 1
#             split_line = line[:-1].split(',')
#             accuracy += float(split_line[1])
#             auroc += float(split_line[2])
#             f1_val += float(split_line[3])
#             precision_val += float(split_line[4])
#             recall_val += float(split_line[5])
#     out_list = [accuracy/line_index, auroc/line_index, f1_val/line_index, precision_val/line_index, recall_val/line_index]
#     out_str = ''
#     for elt in out_list:
#         out_str = out_str + str(elt) + ','
#     return out_str


def plot(indir,tiss,outdir,plot_type):
    # file_types = ['norm_gtex_ss3_gn_', 'norm_gtex_gn_', 'norm_gtex_ss3_']
    file_types = ['norm_gtex_sages_gn_', 'norm_gtex_gn_', 'norm_gtex_sages_']
    # color_dict = {'norm_gtex_ss3_gn_': '#05D0EB', 'norm_gtex_gn_':'#3EB812', 'norm_gtex_ss3_':'#6409B8', 'random':'#939799'}
    color_dict = {'norm_gtex_sages_gn_': '#05D0EB', 'norm_gtex_gn_':'#3EB812', 'norm_gtex_sages_':'#6409B8', 'random':'#939799'}
    fig = go.Figure(layout_title_text=tiss, layout={'plot_bgcolor':'rgba(0,0,0,0)'})
    for f in file_types:
        x,y = read_file(indir+f+tiss+'_0_'+plot_type+'.csv')
        fig.add_trace(go.Scatter(x=x, y=y, name=f, mode='lines', line_color=color_dict[f]))
        # fig.add_trace(go.Scatter(x=x, y=y, name=f, mode='lines+markers', line_color=color_dict[f]))
    if plot_type == 'roc':
        fig.add_trace(go.Scatter(x=[0,1], y=[0,1], name='random', mode='lines', line_color=color_dict['random']))
    else:
         fig.add_trace(go.Scatter(x=[1,0], y=[0.5,0.5], name='random', mode='lines', line_color=color_dict['random']))
    # fig.show()
    fig.update_layout(font= {'size':25, 'family':"Times New Roman"}, legend={'yanchor':'bottom','xanchor':'right'})
    fig.update_xaxes({'gridcolor':'#D3D3D3', 'zerolinecolor':'#D3D3D3', 'range':[-0.01,1.01]})
    fig.update_yaxes({'gridcolor':'#D3D3D3', 'zerolinecolor':'#D3D3D3', 'range':[0,1.01]})
    fig.write_image(outdir+tiss+'_0_'+plot_type+'.jpeg')

def get_replicate_results(indir,tiss,out_file):
    # file_types = ['norm_gtex_ss3_gn_', 'norm_gtex_gn_', 'norm_gtex_ss3_']
    file_types = ['norm_gtex_sages_gn_', 'norm_gtex_gn_', 'norm_gtex_sages_']
    for f in file_types:
        filename = indir+f+tiss+ '_accuracy_pred.csv'
        if f == 'norm_gtex_sages_gn_':
            nameout = 'Structural Features and Gene Names'
        elif f == 'norm_gtex_gn_':
            nameout = 'Gene Names'
        else:
            nameout = 'Structural Features  '
        out = nameout + ',' + tiss + ',' +read_accuracy(filename)[:-1] + '\n'
        fout = open(out_file, 'a+', encoding='utf-8-sig')
        fout.write(out)
        fout.close()

def read_accuracy2(filename):
    accuracy = []
    auroc = []
    f1_val= []
    precision_val= []
    recall_val = []
    with open(filename) as fo:
        for line in fo:
            split_line = line[:-1].split(',')
            accuracy.append(float(split_line[1]))
            auroc.append(float(split_line[2]))
            f1_val.append(float(split_line[3]))
            precision_val.append(float(split_line[4]))
            recall_val.append(float(split_line[5]))
    return accuracy, auroc, f1_val, precision_val, recall_val

def get_replicate_results2(indir,out_file):
    tissues = ['Bladder', 'Uterus', 'Ovary', 'BloodVessel', 'Stomach', 'Liver', 'Colon', 'Blood', 'Spleen', 'Heart', 'Prostate', 'Pancreas', 'Vagina', 'FallopianTube', 'CervixUteri', 'AdiposeTissue', 'AdrenalGland', 'Brain', 'Pituitary', 'Thyroid', 'Nerve', 'Testis', 'Skin', 'Esophagus', 'SmallIntestine', 'SalivaryGland', 'Muscle', 'Kidney', 'Lung', 'Breast']
    file_types = ['norm_gtex_sages_gn_', 'norm_gtex_gn_', 'norm_gtex_sages_']
    
    for f in file_types:
        accuracy = []
        auroc = []
        f1_val= []
        precision_val= []
        recall_val = []
        for tiss in tissues:
            filename = indir+f+tiss+ '_accuracy_pred.csv'
            accuracy1, auroc1, f1_val1, precision_val1, recall_val1 = read_accuracy2(filename)
            accuracy = accuracy+ accuracy1
            auroc = auroc + auroc1
            f1_val= f1_val + f1_val1
            precision_val= precision_val + precision_val1
            recall_val = recall_val + recall_val1
        
        pmsymbol = "\u00B1"
        out_str = f + ',' + str(round(sum(accuracy)/len(accuracy), 3)) + pmsymbol + str(round(stdev(accuracy),3)) + ',' + str(round(sum(auroc)/len(auroc),3)) + pmsymbol + str(round(stdev(auroc),3)) + ',' +str(round(sum(f1_val)/len(f1_val),3)) + pmsymbol + str(round(stdev(f1_val),3)) + ','+str(round(sum(precision_val)/len(precision_val),3)) + pmsymbol + str(round(stdev(precision_val),3)) + ','+str(round(sum(recall_val)/len(recall_val),3)) + pmsymbol + str(round(stdev(recall_val),3)) + '\n'
        fout = open(out_file, 'a+')
        fout.write(out_str)
        fout.close()
        

        # if f == 'norm_gtex_sages_gn_':
        #     nameout = 'Structural Features and Gene Names'
        # elif f == 'norm_gtex_gn_':
        #     nameout = 'Gene Names'
        # else:
        #     nameout = 'Structural Features'

        


indir = 'gtex_tiss_pred_out/'
# indir = 'gtex_tiss_pred_output/'
# outdir= 'tis_pred_images/'
# outdir='prettyfig2/'
# outdir='updated_PR_GTEX/'
tissues = ['Bladder', 'Uterus', 'Ovary', 'BloodVessel', 'Stomach', 'Liver', 'Colon', 'Blood', 'Spleen', 'Heart', 'Prostate', 'Pancreas', 'Vagina', 'FallopianTube', 'CervixUteri', 'AdiposeTissue', 'AdrenalGland', 'Brain', 'Pituitary', 'Thyroid', 'Nerve', 'Testis', 'Skin', 'Esophagus', 'SmallIntestine', 'SalivaryGland', 'Muscle', 'Kidney', 'Lung', 'Breast']
# tissues = ['Breast']
# out_file = outdir + 'all_gtex_performance.csv'
out_file ='average_all_gtex_performance.csv'
fout = open(out_file, 'a+')
fout.write('data_type,tissue,accuracy,auroc,f1,precision,recall\n')
fout.close()

# out_file = 'all_gtex_performance.csv'
# for tiss in tissues:
    # plot(indir,tiss,outdir,'roc')
    # plot(indir,tiss,outdir,'prc')
get_replicate_results2(indir,out_file)