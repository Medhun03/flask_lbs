import pickle

def predict (height):
    model = pickle.lad(open('model.pkl','rb'))
    weight = moedl.predict(height)
    print(weight)
    return weight