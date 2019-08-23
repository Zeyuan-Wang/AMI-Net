

# Hyperparams
class config(object):

    # training
    epochs = 500
    batch_size = 64

    # adam
    learning_rate = 0.00001
    beta_1 = 0.9
    beta_2 = 0.98
    epsilon = 1e-8

    # embedding
    embedding = 128

    # multi-head attention
    num_heads = 4

    # dropout
    dropout_rate = 0.3

    # early stopping tolerance epochs
    tolerance = 100
