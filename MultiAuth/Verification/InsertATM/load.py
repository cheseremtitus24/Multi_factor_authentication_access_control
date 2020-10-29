import pickle
hold = None
with open('insert1.pkl','rb') as oufile:
    hold = pickle.load(oufile)
    oufile.close()

print(hold)