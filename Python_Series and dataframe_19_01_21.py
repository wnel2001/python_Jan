import pandas as pd

###Series and DataFrame###
# Dictionary format data converts to one-dimension  material
#Exampl_1
population1 = {'Seoul': 9700000,
               'Busan' :4500000,
               'Inchun':4000000,
               'Gaungju':2000000,
               'Deagu'  :2500000}
popu=pd.Series(population1)
print(popu)                         # Key from dictionary format data changed to index of Series


# Give low name and column name
X2=pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['a','b','c'], index=[1,2,3])
print(X2)

### give 'pop' on the column name of polulation data 

pd.DataFrame(popu, columns = ['pop'])

# one dimension array --> 2 dimension matrix data
# Can give column name of column vector (열 벡터의 열 이름을 부여 가능)


# Example_2
ind1 = {'Seoul':95,
        'Busan': 80,
        'Inchun': 85,
        'Gaungju': 75,
        'Deagu': 80 }
print(ind1)


# Convert to Series
ind=pd.Series(ind1)
print(ind)


# Create a DataFrame with the region name index
y=pd.DataFrame({'pop': popu, 'independent(%)': ind})   # each 1D convert to 2D
print(y)


#materials editing - Slicing
print(y['independent(%)'])  # Use column name as it is


#materials editing - Slicing
print(y['Busan' : 'Gaungju']) # row from Busan to Gaungu : Slicing Based on Index 


