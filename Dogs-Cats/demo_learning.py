import os

# print(os.listdir('../../data'))
from keras_preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

FAST_RUN = True
IMAGE_WIDTH=128
IMAGE_HEIGHT=128
IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
IMAGE_CHANNELS=3

import pandas as pd
filenames = os.listdir("../../data/train")


categories = [filename.split('.')[0]
              for filename in filenames]

df = pd.DataFrame({
    'filename': filenames,
    'category': categories
})
# print(df.head)

import seaborn as sns
import matplotlib.pyplot as plt
# temp = df['category'].value_counts()
# print(temp)
# df['category'].value_counts().plot.bar()
# plt.show()

# import random
# from keras_preprocessing.image import load_img
# sample = random.choice(filenames)
# image = load_img("../../data/train/"+sample)
# plt.imshow(image)
# plt.show()

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, \
    Dropout, Flatten, Dense, Activation, BatchNormalization

model = Sequential()

model.add(Conv2D(32, (3, 3),
                 activation='relu',
                 input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax')) # 2 because we have cat and dog classes

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop', metrics=['accuracy'])

# model.summary()

from keras.callbacks import EarlyStopping, ReduceLROnPlateau
earlystop = EarlyStopping(patience=10)
learning_rate_reduction = ReduceLROnPlateau(monitor='val_acc',
                                            patience=2,
                                            verbose=1,
                                            factor=0.5,
                                            min_lr=0.00001)
callbacks = [earlystop, learning_rate_reduction]

train_df, validate_df = train_test_split(df,
                                         test_size=0.20,
                                         random_state=42)
train_df = train_df.reset_index(drop=True)
validate_df = validate_df.reset_index(drop=True)

# plt.subplot(1,3,1)
# df['category'].value_counts().plot.bar()
# plt.subplot(1,3,2)
# train_df['category'].value_counts().plot.bar()
# plt.subplot(1,3,3)
# validate_df['category'].value_counts().plot.bar()
# plt.show()



total_train = train_df.shape[0]
total_validate = validate_df.shape[0]
batch_size=15

train_datagen = ImageDataGenerator(
    rotation_range=15,
    rescale=1./255,
    shear_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    width_shift_range=0.1,
    height_shift_range=0.1
)

train_generator = train_datagen.flow_from_dataframe(
    train_df,
    "../../data/train",
    x_col='filename',
    y_col='category',
    target_size=IMAGE_SIZE,
    class_mode='categorical',
    batch_size=batch_size
)


validation_datagen = ImageDataGenerator(rescale=1./255)
validation_generator = validation_datagen.flow_from_dataframe(
    validate_df,
    "../../data/train",
    x_col='filename',
    y_col='category',
    target_size=IMAGE_SIZE,
    class_mode='categorical',
    batch_size=batch_size
)

# example_df = train_df.sample(n=1).reset_index(drop=True)
# example_generator = train_datagen.flow_from_dataframe(
#     example_df,
#     "../../data/train",
#     x_col='filename',
#     y_col='category',
#     target_size=IMAGE_SIZE,
#     class_mode='categorical'
# )
#
# plt.figure(figsize=(12, 12))
# for i in range(0, 25):
#     plt.subplot(5, 5, i+1)
#     X_batch, Y_batch = example_generator[0]
#     image = X_batch[0]
#     plt.imshow(image)
#
# plt.tight_layout()
# plt.show()

epochs=3 if FAST_RUN else 50
history = model.fit_generator(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=total_validate//batch_size,
    steps_per_epoch=total_train//batch_size,
    callbacks=callbacks
)