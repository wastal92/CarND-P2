
class batch_iterator(object):
    '''
    Batch iterator to make transformations on the data. 
    Uses multiprocessing so that batches can be created on CPU while GPU runs previous batch
    '''
    def __init__(self, batchsize):
        self.batchsize = batchsize

    def __call__(self, X, y):
        self.X, self.y = X, y
        return self

    def __iter__(self):
        '''
        multi thread the iter so that the GPU does not have to wait for the CPU to process data
        runs the _gen_batches function in a seperate process so that it can be run while the GPU is running previous batch
        '''
        num_samples = len(self.y)
        batches = range(0, num_samples, self.batchsize)
        for batch in batches:
            X_batch = self.X[batch:batch + self.batchsize]
            y_batch = self.y[batch:batch + self.batchsize]

            # do some stuff to the batches like augment images or load from folders

            yield [X_batch, y_batch]


# ==================================================================================================================
# to use it do the following when looping over epochs
#batch_iter = threaded_batch_iter(batchsize=128)

#for epoch in range(epochs):
    # ...
    #for X_batch, y_batch in batch_iter(X_train, y_train):
        # ...