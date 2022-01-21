from sklearn.datasets import load_iris
 
#dataset which contains data on iris species, dataset included in scikit-learn
iris_dataset = load_iris() 

#to know more about the dataset
#print("Keys of Iris Dataset:{}".format(iris_dataset.keys()))

#to know about description of iris dataset
#print(iris_dataset['DESCR'])

#to know about features in Iris Dataset
print("Feature Names: {}".format(iris_dataset['feature_names']))

#Here feature names are sepal length, sepal width, petal length, petal width in cms

print("target names: {}".format(iris_dataset['target_names']))

#target names here are setosa, versicolor, virginica

#to know about number of rows and columns of data
print("Shape of the data: {}".format(iris_dataset['data'].shape))

#entire input data
print(iris_dataset['data'])

#target labels 0 is for setosa, 1 is for versicolor, 2 is for virginica
print(iris_dataset['target'])
