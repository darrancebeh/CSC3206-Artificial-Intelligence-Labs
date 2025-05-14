import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/darrancebeh/csc-ai/week3/Iris Dataset/iris.data'

#2. Column names based on the iris.names
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv(file_path, header=None, names=column_names)

#3. Calculate the mean, min, max, and standard deviation of each column 
print("Summary Statistics for each column: ")
numeric_df = df.select_dtypes(include=['number'])

print(numeric_df.describe())
print("\n")

#4. Create a new column called class value
print("INVESTIGATE THE OUTPUT AFTER .factorize()")
df['class_value'] = pd.factorize(df['class'])[0]

print("DataFrame with 'class_value' column: ")
print(df.head())
print(df.tail())
print("\n")

#5. Group the data according to the class 
grouped_by_class = df.groupby('class')

print("Grouped DataFrame (object details): ")
print(grouped_by_class)
print("\n")

#6. Identify the function to extract each group using the name of the class 
print("Extracting 'Iris-setosa' group: ")
setosa_group = grouped_by_class.get_group('Iris-setosa')
print(setosa_group.head())
print("\n")

print("Extracting 'Iris-versicolor' group: ")
versicolor_group = grouped_by_class.get_group('Iris-versicolor')
print(versicolor_group.head())
print("\n")

print("Extracting 'Iris-virginica' group: ")
virginica_group = grouped_by_class.get_group('Iris-virginica')
print(virginica_group.head())
print("\n")

#7. Calculate the mean, min, max, and standard deviation of each column in each group 

print("Statistics for each group using describe(): ")
print(grouped_by_class[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].describe())
print("\n")

#8. Produce a scatter plot for any two columns using matplotlib library 
plt.figure(figsize=(10, 6))

colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}
for class_name, group in grouped_by_class:
    plt.scatter(group['sepal_length'], group['sepal_width'],
                color=colors[class_name], label=class_name, alpha=0.7)

plt.title('Sepal Length vs. Sepal Width by Class')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.grid(True)
plt.show()

#9. Identify the methods (at least 2) to loop through a data frame row by row 
print("\nMethod 1: Using DataFrame.iterrows().\nThis method iterates over DataFrame rows as (index, Series) pairs.")
print("\nMethod 2: Looping through df.values (NumPy array) by accessing the NumPy array and looping through it directly.")