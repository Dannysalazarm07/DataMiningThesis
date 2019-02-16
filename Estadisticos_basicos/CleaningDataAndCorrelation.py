import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def missing_data_rows(i_original, i_no_missing):
    i_original = i_original.values
    i_no_missing = i_no_missing.values
    rows = []
    for i in i_original:
        if(not(i in i_no_missing)):
            rows.append(i)
    return  rows

def  missing_data_rows_to_csv(df, df_no_missing_values):
    missing_rows = (missing_data_rows(df.index, df_no_missing_values.index))
    missing_register = df.loc[missing_rows]
    missing_register.to_csv("MissingData/missingDataRegister.csv")

#not finished
def scatter_plot(df):
    plt.scatter(range(0,len(df.index.values)), df.iloc[:,8] , c='b', marker='o', label='1')
    #plt.scatter(x, y, c='r', marker='s', label='-1')
    plt.legend(loc='upper left')
    plt.show()

#print the varibles with a correlation higher than the limit value
def print_high_correlation_variables(df, limit):
    corretaltion_data = []
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if ((df.iloc[i, j] >= limit or df.iloc[i, j] <= -limit) and df.iloc[i, j] < 1):
                corretaltion_data.append([df.index[i], df.columns[j], df.iloc[i, j]])
    for i in corretaltion_data:
        print(str(i[0]) + "," + str(i[1]) + "," + str(i[2]))

#Reading the df
original_values_variables_path = "PreLoadData/variables.csv"
df = pd.read_csv(original_values_variables_path, index_col=0 )
df.info()
#drop rows with missing values
df_no_missing_values = df.dropna(axis = 0)

#get the rows with missing data and print to a csv file
#missing_data_rows_to_csv(df, df_no_missing_values)

#trying to do scatter plot, it´s not complete becouse we did the work easier with MS Excrl
#scatter_plot(df_no_missing_values)

#Getting correlation matrix of the data with no missing data
df_nmv_corr = df_no_missing_values.corr()
print(df_nmv_corr.head())

#Function that prints the variables with a correlation higher than 0.5
print_high_correlation_variables(df_nmv_corr, 0.5)



