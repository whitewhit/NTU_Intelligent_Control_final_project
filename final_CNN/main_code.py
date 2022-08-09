import os
os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.7/bin")
import numpy as np
import tensorflow as tf
from keras.utils import np_utils


# 資料準備
seperate_time = 100
flower_list = ["cherry_blossoms","golden_needle_flower","hydrangea","kapok","lily","lotus","orchid","plum_bossom","sunflower","tung_flower"]
path_name = "D:/python files/cnn_pre_process"
x_img_train = np.load(path_name+'/x_img_train_64_ram.npy')
y_label_train = np.load(path_name+'/y_label_train_64_ram.npy')
training_batch_size = int(len(x_img_train)/seperate_time)
x_img_test = np.load(path_name+'/x_img_test_64.npy')
y_label_test = np.load(path_name+'/y_label_test.npy')
x_img_test_normalize = x_img_test.astype('float32') / 255.0
y_label_test_OneHot = np_utils.to_categorical(y_label_test)
accuracy = []
val_accuracy = []
loss = []
val_loss = []

for i in range(seperate_time):
    s = training_batch_size*i
    t = training_batch_size*(i+1)
    x_img_train_temp = x_img_train[s:t]
    y_label_train_temp = y_label_train[s:t]


    
    print(x_img_train_temp.shape)
    print(y_label_train_temp.shape)
    x_img_train_normalize = x_img_train_temp.astype('float32') / 255.0
    y_label_train_OneHot = np_utils.to_categorical(y_label_train_temp)

    # 建立模型
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Activation, Flatten, BatchNormalization
    from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
    from keras import regularizers

    weight_decay = 1e-4
    model = Sequential()

    model.add(Conv2D(32, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay), input_shape=x_img_train_normalize.shape[1:]))
    model.add(Activation('elu'))
    model.add(BatchNormalization())
    model.add(Conv2D(32, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    model.add(Activation('elu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(64, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    model.add(Activation('elu'))
    model.add(BatchNormalization())
    model.add(Conv2D(64, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    model.add(Activation('elu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.3))

    model.add(Conv2D(128, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    model.add(Activation('elu'))
    model.add(BatchNormalization())
    model.add(Conv2D(128, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    model.add(Activation('elu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.4))

    model.add(Conv2D(256, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    model.add(Activation('elu'))
    model.add(BatchNormalization())
    model.add(Conv2D(256, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    model.add(Activation('elu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.4))

    model.add(Conv2D(512, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    model.add(Activation('elu'))
    model.add(BatchNormalization())
    model.add(Conv2D(512, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    model.add(Activation('elu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.4))

    model.add(Flatten())
    model.add(Dense(10, activation='softmax'))

    print(model.summary())

    try:
        model.load_weights(path_name+"/model_weight.h5")
        print("載入模型成功!繼續訓練模型")
    except :    
        print("載入模型失敗!開始訓練一個新模型")

    model.compile(loss='categorical_crossentropy', optimizer='Nadam', metrics=['accuracy'])

    train_history=model.fit(x_img_train_normalize, y_label_train_OneHot,
                            validation_split=0.2,
                            epochs=5, batch_size=128, verbose=1) 

    model.save_weights(path_name+"/model_weight.h5")
    print("Saved model to disk")
    accuracy = accuracy+train_history.history['accuracy']
    val_accuracy = val_accuracy+train_history.history['val_accuracy']
    loss = loss+train_history.history['loss']
    val_loss = val_loss+train_history.history['val_loss']
import matplotlib.pyplot as plt

plt.plot(accuracy)
plt.plot(val_accuracy)
plt.title('Train History')
plt.ylabel("accuracy")
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# testing
scores = model.evaluate(x_img_test_normalize, y_label_test_OneHot, verbose=0)
prediction=np.argmax(model.predict(x_img_test_normalize), axis=-1)
label_dict={0:"cherry blossoms",1:"golden needle flower",2:"hydrangea",3:"kapok",4:"lily",5:"lotus",6:"orchid",7:"plum bossom",8:"sunflower",9:"tung flower"}

def plot_images_labels_prediction(images,labels,prediction, idx,num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num>25: num=25 
    for i in range(0, num):
        ax=plt.subplot(5,5, 1+i)
        ax.imshow(images[idx],cmap='binary')
                
        title=str(i)+','+label_dict[labels[i][0]]
        if len(prediction)>0:
            title+='=>'+label_dict[prediction[i]]
            
        ax.set_title(title,fontsize=10) 
        ax.set_xticks([]);ax.set_yticks([])        
        idx+=1 
    plt.show()
Predicted_Probability=model.predict(x_img_test_normalize)

def show_Predicted_Probability(y,prediction, x_img_test,Predicted_Probability,i):
    print('label:',label_dict[y[i][0]], 'predict:',label_dict[prediction[i]])
    plt.figure(figsize=(2,2))
    plt.imshow(np.reshape(x_img_test[i],(64, 64,3)))
    plt.show()
    for j in range(10):
        print(label_dict[j]+
              ' Probability:%1.9f'%(Predicted_Probability[i][j]))
show_Predicted_Probability(y_label_test,prediction,x_img_test,Predicted_Probability,0)

y_label_test.reshape(-1)
import pandas as pd
print(label_dict)
df = pd.crosstab(y_label_test.reshape(-1),prediction, rownames=['label'],colnames=['predict'],dropna=False)
print (df)