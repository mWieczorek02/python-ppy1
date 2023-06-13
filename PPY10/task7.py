import pickle

if __name__ == "__main__":
    ids = ["001", "003", "011"]
    with open('data.pickle', 'wb') as handle:
        pickle.dump(ids, handle)
