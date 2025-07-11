import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/jpxmaestas/clementine_clash/clementine_clash/clementine_clash-1/regression_project/smoking_health_data_final.csv")

df.iloc[:,0] = pd.to_numeric(df.iloc[:, 0], errors='coerce')
mean = np.mean(df.iloc[:,0])
df.iloc[:,0] = df.iloc[:,0].fillna(mean)

age = df.iloc[:,0].tolist()

df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: 0 if x.strip() == 'male' else 1 if x.strip() == 'female' else x)
#0 if male
# 1 if female 

df.iloc[:, 2] = df.iloc[:, 2].apply(lambda x: 0 if x.strip() == 'no' else 1 if x.strip() == 'yes' else x)
#0 if non-smoker 
#1 if smoker 

systolic = []
diastolic = []
for i in range(len(df.iloc[:,4])):

    bp = str(df.iloc[i,4])
    temp = str(df.iloc[i,4])
    sys, dia = temp.split("/")
    sys = float(sys)
    dia = float(dia)

    systolic.append(sys)
    diastolic.append(dia)

systolic = np.nan_to_num(systolic, nan=np.mean(systolic))
diastolic = np.nan_to_num(diastolic, nan=np.mean(diastolic))
#split bp reading 

chol_mean = df.iloc[:,-1].mean()
cholesterol =  df.iloc[:,-1].fillna(chol_mean)
#cholesterol = cholesterol.fillna(chol_mean)

cig_mean = df.iloc[:,-2].mean()
cig_num = df.iloc[:,-2].fillna(cig_mean)
#cig_num = cig_num.fill_na(cig_num.mean())

plt.scatter(cig_num, cholesterol)

plt.xlabel("Number of Cigarettes")
plt.ylabel("Cholesterol")
plt.grid(True)




sig_chol = np.std(cholesterol)
sig_num = np.std(cig_num)
covariance = np.cov(cig_num, cholesterol)
cov_coef = covariance[0,1]


cor = cov_coef / (sig_chol * sig_num)


#y_bar = mean of chol


b = sig_chol * cor / sig_num 

a = chol_mean - b * cig_mean

plt.axline((0, a), slope=b, color='red', linestyle='--')

plt.savefig("output_plot.png")