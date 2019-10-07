import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=FutureWarning)
    import tensorflow as tf
    from tensorflow import keras
    import numpy as np
    from tensorflow.keras.preprocessing.text import Tokenizer
print('ready')

# import tensorflow as tf
# print(tf.__version__)
# from tensorflow import keras
# import numpy as np
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# load the data
# fashion mnist is included in tf distribution:
fashion_mnist = keras.datasets.fashion_mnist
# train data vs. validation/test data
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

# see the size of the dataset
print(len(train_labels),train_labels.shape, train_labels[0])
print(len(train_images),train_images.shape)
# print(train_images[0])
# print(np.array_str(train_images[0], max_line_width=200))

index = np.random.randint(1,60000)
print(np.array_str(train_images[index], max_line_width=200))
plt.imsave('sample-{}.png'.format(index),train_images[index])
imgplot = plt.imshow(train_images[index])
plt.show()


# labels
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print("the number {} image is {}".format(index,class_names[train_labels[index]]))
