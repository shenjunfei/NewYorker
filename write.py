import pickle
import random

with open("data/ID50000", 'wb') as f:
    pickle.dump(followers_ids, f)

with open("data/ID50000", 'rb') as f:
    followers_ids = pickle.load(f)

sampled_ids = random.sample(followers_ids, 10000)

with open("data/sampled_ids", 'wb') as f:
    pickle.dump(sampled_ids, f)

with open("data/sampled_ids", 'rb') as f:
    my_list = pickle.load(f)