import pandas as pd


d = {'col1': [1, 2, 3, 4], 'col2': [11, 22, 33, 44] , 'col3': [111, 222, 333, 444], 'col4': [1111, 2222, 3333, 4444], 'col5': [11111, 22222, 33333, 44444]}
df = pd.DataFrame(data=d)
print(df)
print(df.iloc[:,2:])
print(df.shape)
print(df.info())
accidente_ofidico_path = "datos/accidente ofidico.csv"

#Reading the csv file and storing it in a DataFrame
ocurrencia_ao_df = pd.read_csv(accidente_ofidico_path);

#Printing info of the whole DataFrame
#print(ocurrencia_ao_df.info(verbose=True, null_counts=True))

#Adding a new row "Total" with the sum of  all occurences in the whole period. The sum is performed from the 3 colum where the ocurrences data starts
ocurrences_starting_column = 3
#ocurrencia_ao_df["Total"] = ocurrencia_ao_df.iloc[:,ocurrences_starting_column:].sum(axis = 1)
ocurrencia_ao_df.index = ocurrencia_ao_df["Codigo DANE"]
print(ocurrencia_ao_df.iloc[:,2:])
print(ocurrencia_ao_df.shape)
print(ocurrencia_ao_df.info(verbose=True, null_counts=True))

