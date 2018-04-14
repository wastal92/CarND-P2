from multiprocess_batch_iter import threaded_batch_iter
import pickle
#import numpy as np

validation_file = 'traffic-signs-data/valid.p'
with open(validation_file, mode='rb') as f:
    valid = pickle.load(f)
X_valid, y_valid = valid['features'], valid['labels']

batch_aug = threaded_batch_iter(batchsize = 100)
for x_batch, _ in batch_aug(X_valid, y_valid):
    print(x_batch.shape[0])
