from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers.advanced_activations import LeakyReLU, PReLU
from keras.utils import np_utils, generic_utils, to_categorical
from keras import backend as K
K.set_image_dim_ordering('th')
import numpy as np
import keras

batch_size = 64
nb_classes = 10
nb_epoch = 100

img_channels = 3
img_rows = 112
img_cols = 112

X_train = np.load('x_train.npy')
X_test = np.load('x_test.npy')
Y_train = np.load('y_train.npy')
Y_test = np.load('y_test.npy')
#X_train = X_train.reshape()
#X_train =X_train.reshape(X_train.shape[0], img_rows, img_cols,3)
#X_test=X_test.reshape(X_test.shape[0],img_rows,img_cols,3)
#if K.image_data_format() == 'channels_first':
#	x_train = x_train.reshape(3, img_rows, img_cols
#	x_test = x_test.reshape(3, img_rows, img_cols)
#	#input_shape = (1, img_rows, img_cols)
#else:
#	x_train = x_train.reshape(img_rows, img_cols, 3)
#	x_test = x_test.reshape(img_rows, img_cols, 3)
#	#input_shape = (img_rows, img_cols, 1)

#x_train = x_train.astype('float32')
#x_test = x_test.astype('float32')
#x_train /= 255
#x_test /= 255
#print('x_train shape:', x_train.shape)
#print(x_train.shape[0], 'train samples')
#print(x_test.shape[0], 'test samples')




print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

print('Y_train shape:', Y_train.shape)
print('Y_test shape:', Y_test.shape)

#Y_train = keras.utils.to_categorical(Y_train, nb_classes)
#Y_test = keras.utils.to_categorical(Y_test, nb_classes)#convert label into one-hot vector
Y_train = to_categorical(Y_train, nb_classes)
Y_test = to_categorical(Y_test, nb_classes)#convert label into one-hot vector

print('Y_train shape:', Y_train.shape)
print('Y_test shape:', Y_test.shape)

#exit()

model = Sequential()

#Layer 1
model.add(Conv2D(filters=128, kernel_size=(5,5), padding='valid', input_shape=[3,112,112]))#Convo$

#keras.layers.BatchNormalization(axis=1, momentum=0.99, epsilon=0.001, center=True, scale=True, beta_initializer='zeros', gamma_initializer='ones', moving_mean_initializer='zeros', moving_variance_initializer='ones', beta_regularizer=None, gamma_regularizer=None, beta_constraint=None, gamma_constraint=None)
model.add(Activation('relu'))#Activation function
model.add(AveragePooling2D(pool_size=(2, 2)))
#14x14 output

#Layer 2
model.add(Conv2D(filters=128, kernel_size=(5,5), padding='valid'))#Convo$
model.add(Activation('relu'))#Activation function
model.add(AveragePooling2D(pool_size=(2, 2)))
#6x6
#keras.layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, beta_initializer='zeros', gamma_initializer='ones', moving_mean_initializer='zeros', moving_variance_initializer='ones', beta_regularizer=None, gamma_regularizer=None, beta_constraint=None, gamma_constraint=None)

#Layer 3
model.add(Conv2D(filters=64, kernel_size=(5,5), padding='valid'))#Convo$
model.add(Activation('relu'))#Activation function
model.add(AveragePooling2D(pool_size=(2, 2)))
#2x2
#layer 4
#model.add(Conv2D(filters=64, kernel_size=(5,5), padding='valid'))#Convo$
#model.add(Activation('relu'))#Activation function
#model.add(AveragePooling2D(pool_size=(2, 2)))


#Dense layer
model.add(Flatten())# shape equals to [batch_size, 32] 32 is the number of filters
model.add(Dropout(0.5))
model.add(Dense(10))#Fully connected layer
model.add(Activation('softmax'))

#opt = keras.optimizers.rmsprop(lr=0.001, decay=1e-6)
#opt = keras.optimizers.Adadelta(lr=1.0, decay=1e-6)
#opt = keras.optimizers.Adam(lr=0.001,decay=1e-6)
opt = keras.optimizers.Adamax(lr=0.002 ,decay=1e-6)
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])


def train():
    model.fit(X_train, Y_train,
              batch_size=batch_size,
              epochs=nb_epoch,
              validation_data=(X_test,Y_test),
	      shuffle=True)

train()


