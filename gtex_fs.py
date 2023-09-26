from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_recall_curve
from sklearn.feature_selection import RFE
from sklearn.metrics import f1_score 
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

def read_data(csv_file, tissue):
    x1 = []
    x0 = []
    with open(csv_file) as fo:
        for line in fo:
            split_line = line[:-1].split(',')
            id = split_line[0].split('_')[0].replace('-','')
            temp=[]
            for elt in split_line[1:]:
                if elt != '':
                    temp.append(float(elt))
                else:
                    temp.append(0)
            if id == tissue:
                x1.append(temp)
            else:
                x0.append(temp)
    return x1,x0

def predict_gtex(classifier, random_state, test_size, data_file_name, folder_out, tissue, num_features_to_select):
    name = data_file_name[:-4]
    x1,x0 = read_data(data_file_name,tissue)
    y1 = [1]*len(x1)
    y0 = [0]*len(x0)
    X1_train, X1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=test_size, random_state=random_state)
    X0_train, X0_test, y0_train, y0_test = train_test_split(x0, y0, test_size=test_size, random_state=random_state)
    minxtrain = min(len(X1_train), len(X0_train))
    minxtest = min(len(X1_test), len(X0_test))
    minytrain = min(len(y1_train), len(y0_train))
    minytest = min(len(y1_test), len(y0_test))
    X_train = X1_train[:minxtrain] + X0_train[:minxtrain]
    y_train = y1_train[:minytrain] + y0_train[:minytrain]
    X_test = X1_test[:minxtest] + X0_test[:minxtest]
    y_test = y1_test[:minytest] + y0_test[:minytest]

    selector = RFE(classifier, n_features_to_select=num_features_to_select)
    selector = selector.fit(X_train, y_train)
    rank = selector.ranking_
    f = open(folder_out + name+'_fs.csv', 'a+')
    f.write(str(random_state))
    for index in range(len(rank)):
        f.write(',' + str(rank[index]))
    f.write('\n')    
    f.close()
    return rank

def run_crossfold(n, test_size, data_file_name, folder_out, num_features_to_select):
    # gtex_tiss_key = ['Bladder', 'Uterus', 'Ovary', 'BloodVessel', 'Stomach', 'Liver', 'Colon', 'Blood', 'Spleen', 'Heart', 'Prostate', 'Pancreas', 'Vagina', 'FallopianTube', 'CervixUteri', 'AdiposeTissue', 'AdrenalGland', 'Brain', 'Pituitary', 'Thyroid', 'Nerve', 'Testis', 'Skin', 'Esophagus', 'SmallIntestine', 'SalivaryGland', 'Muscle', 'Kidney', 'Lung', 'Breast']
    gtex_tiss_key = ['Breast']
    for tiss in gtex_tiss_key:
        print(tiss)
        for i in range(n):
            print(i)
            predict_gtex(RandomForestClassifier(random_state=i), i, test_size, data_file_name, folder_out, tiss, num_features_to_select)

run_crossfold(10, 0.2, 'norm_gtex_sages_gn.csv', '', 1)

# def feature_select(name, num_features_to_select, classifier, random_state, test_size, data_file_name1,data_file_name0, folder_out, write=True):
#     x1 = read_data(data_file_name1)
#     y1 = [1]*len(x1)
#     x0 = read_data(data_file_name0)
#     y0 = [0]*len(x0)
#     X1_train, X1_test, y1_train, y1_test = train_test_split(x0, y0, test_size=test_size, random_state=random_state)
#     X0_train, X0_test, y0_train, y0_test = train_test_split(x1, y1, test_size=test_size, random_state=random_state)
#     minxtrain = min(len(X1_train), len(X0_train))
#     minxtest = min(len(X1_test), len(X0_test))
#     minytrain = min(len(y1_train), len(y0_train))
#     minytest = min(len(y1_test), len(y0_test))
#     X_train = X1_train[:minxtrain] + X0_train[:minxtrain]
#     y_train = y1_train[:minytrain] + y0_train[:minytrain]

#     selector = RFE(classifier, n_features_to_select=num_features_to_select)
#     selector = selector.fit(X_train, y_train)
#     rank = selector.ranking_
#     if write:
#         for index in range(len(rank)):
#             f = open(folder_out + name+'_fs.csv', 'a+')
#             f.write(str(index) + ',' + str(rank[index]) + '\n')
#             f.close()
#     return rank


# # random_state = 0
# # for random_state_val in range(10):
# #     predict_surg('aorticevent_pred', RandomForestClassifier(random_state=random_state_val), random_state_val, 0.1,'indication_RuptureDisection.csv','indication_NOTrupturedisection.csv', 'pred_out/', write=True)
# # feature_select('aorticevent_pred',1, RandomForestClassifier(random_state=0), 0, 0.1,'indication_RuptureDisection.csv','indication_NOTrupturedisection.csv', 'pred_out/',write=True)



