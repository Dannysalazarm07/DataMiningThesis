import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def print_total(df, n):
    for i in range(n):
        print(str(df.iloc[i,0]) + " " +str(df.iloc[i,-1]))

def inteval_bp(df):
    for i in range(0,df.shape[1],8):
        plt.figure()
        offset = 8
        if(df.shape[1] - i < 8):
            df.boxplot(column=df.columns[i:df.shape[1]].values.tolist())
        else:
            df.boxplot(column = df.columns[i:i+8].values.tolist())
        plt.show()
        #plt.savefig("boxplotF/Intervalo.png")
        plt.close()


#Defining path of file - "Ocurrencia de accidente ofídico"
accidente_ofidico_path = "datos/accidente ofidico.csv"

#Reading the csv file and storing it in a DataFrame
ocurrencia_ao_df = pd.read_csv(accidente_ofidico_path);

#Printing info of the whole DataFrame
#print(ocurrencia_ao_df.info(verbose=True, null_counts=True))

#Adding a new row "Total" with the sum of  all occurences in the whole period. The sum is performed from the 3 colum where the ocurrences data starts
ocurrences_starting_column = 3
ocurrencia_ao_df["Total"] = ocurrencia_ao_df.iloc[:,ocurrences_starting_column:].sum(axis = 1)
ocurrencia_ao_df.index = ocurrencia_ao_df["Codigo DANE"]


#print(ocurrencia_ao_df.info(verbose=True, null_counts=True))

#------------------------------------------Popultation-------------------------------
population_path = "datos/Pobalcion Municipios.csv"
population_df = pd.read_csv(population_path)
population_df.index = population_df['DPMP']
#Adding a new colum with the population averga beteewn 2007 and 2016 becouse of the data thta we have of the AO
population_df['Promedio 2007-2016'] = population_df.iloc[:, 6:16].mean(axis = 1)
#print(population_df.info(verbose=True, null_counts=True))
#print(population_df['Promedio 2007-2016'])

#------------------------------------------Initial Variables Data Set----------------------------------
variables_path = "datos/variables ambientales y socioeconomicas colombia.csv"
variables_df = pd.read_csv(variables_path, na_values=['N.A.','N.A'])
variables_df.index = variables_df['Codigo']
#Modifications to the original document
#1. AJ - 1103 delte spaces to the column
#2. AN - 1103 There was a percet number, i changed to a 0-1 rate . I changed the format cell to General

#print(variables_df.head())
#print(variables_df.tail())

#-------------------------------Adding ocurrences and population----------------------------------------
#Getting total column from AO dataset
total_oa = ocurrencia_ao_df['Total']
#Adding column of total ocurrences to the variables df
variables_df = pd.concat([variables_df, total_oa], axis = 1, join = 'inner')
#Getting total column from Population dataset
mean_popultaion_column = 'Promedio 2007-2016'
mean_popultaion = population_df[mean_popultaion_column]
#Adding column of average popultaion between 2007 and 2017 to the variables df
variables_df = pd.concat([variables_df, mean_popultaion], axis = 1, join = 'inner')
#Creatin a new colum with the rate od ocurrences each 100 thousand habs
variables_df['Ocurrencia por cada 100mil habitantes'] = variables_df['Total'] / variables_df[mean_popultaion_column] * 100000
#Copying the variables df to a new one to delete initial no needes information
variables_df.to_csv("variables_all.csv")
only_variables_df = variables_df.copy()
#Deleteing all information that is not a variable from the new Df
del only_variables_df['region']
del only_variables_df['subregion']
del only_variables_df['departamento']
del only_variables_df['municipio']
del only_variables_df['Codigo']
del only_variables_df['Total']
del only_variables_df['Promedio 2007-2016']
#print(only_variables_df.info())
#Renaming colummns
only_variables_df.rename(columns={'zonassusceptiblesdeinundaci?n': 'zonassusceptiblesdeinundacion'}, inplace=True)
#only_variables_df.to_csv("variables.csv")

#Save a img a boxplot for each column
'''for i in range(only_variables_df.shape[1]):
    plt.figure()
    only_variables_df.boxplot(column = [only_variables_df.columns[i]])
    plt.savefig("boxplot/" + str(only_variables_df.columns[i])+".png")
    plt.close()'''
only_variables_df.to_csv("PreLoadData/variables.csv")
#normalize DF with min -max (x - min / max - min)
normalized_df = (only_variables_df - only_variables_df.min()) / (only_variables_df.max() - only_variables_df.min())
normalized_df.to_csv("PreLoadData/normalized.csv")

'''for i in range(normalized_df.shape[1]):
    plt.figure()
    normalized_df.boxplot(column = [normalized_df.columns[i]])
    plt.savefig("boxplotNormal/" + str(normalized_df.columns[i])+".png")
    plt.close()'''
#show boxplot by intervals of 8 variables
#inteval_bp(normalized_df)



#print(variables_df.loc[50568]['Ocurrencia por cada 100mil habitantes'])

#corr_matrix = pd.DataFrame(index = only_variables_df.columns, columns = only_variables_df.columns)
#Getting the correlation matrix
corr_matrix = only_variables_df.corr()
corr_matrix_normalized = normalized_df.corr()

'''
for ix in corr_matrix.index:
    for col in corr_matrix.columns:
        var1 = only_variables_df[ix].values
        var2 = only_variables_df[col].values
        corr_matrix.loc[ix][col] = np.corrcoef(var1, var2)[0,1]
'''

corr_matrix.to_csv("correlation matrix.csv")
corr_matrix_normalized.to_csv("correlation matrix - normalized data.csv")


