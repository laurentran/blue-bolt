# function from 'execute python module' to remove encoding

def azureml_main(dataframe1 = None, dataframe2 = None):
    dataframe1[1] = dataframe1['text'].str.replace('<[^<]+?>', ' ', case=False)
    return dataframe1,