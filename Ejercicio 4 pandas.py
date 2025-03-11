import pandas as pd 
s1 = pd.Series([10, 20, 30], index=["a", "b", "d"])
s2 = pd.Series([40,50,60,70], index=["b", "c", "d", "e"])

print (s1)
print (s2)

resultado = s1 + s2
print (resultado)

#Para que los espacios no queden con NAN

resultado_con_fill = s1.add(s2, fill_value=0)
print (resultado_con_fill)

df1= pd.DataFrame({"A": [1,2], "B": [3,4]} ,index=[1,2])
df2= pd.DataFrame({"B": [5,6], "C": [7,8]} ,index=[2,3])
print ("Tabla df1")
print (df1)
print ("Tabla df2")
print (df2)

resultado_df = df1 + df2
print (resultado_df)

resultado_df = df1.add(df2, fill_value=0)
print (resultado_df)