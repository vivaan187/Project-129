import pandas as pd

#reading csv file
brightest_stars = pd.read_csv("bright_stars.csv")
print(brightest_stars.head())
#Reading csv file to be cleaned
df1 = pd.read_csv("dwarf_stars.csv")

print(df1.head(n = 10))
#Dropping rows with empty cells
cleaned_df = df1.dropna()

#Changing datatype to float
cleaned_df = cleaned_df.astype({"Mass":"float"})
cleaned_df = cleaned_df.astype({"Radius":"float"})

#converting cleaned data to csv file
dwarf_stars = cleaned_df.to_csv("C:/Users/vivaa/Stars-project")

#reading cleaned data file
Dwarf = pd.read_csv(dwarf_stars)

#Multiply mass and radius with respective scalar values
Dwarf['Mass'] = Dwarf['Mass'].multiply(0.000954588)
Dwarf['Radius'] = Dwarf['Radius'].multiply(0.102763)

#merging cleaned data and bright star data sets
final_df = pd.merge(dwarf_stars,brightest_stars)

#converting to csv
final_df.to_csv("C:/Users/vivaa/Stars-project")


