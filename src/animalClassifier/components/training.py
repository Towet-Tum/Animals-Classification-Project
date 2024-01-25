import os 
import tensorflow as tf 
from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from animalClassifier.entity.config_entity import TrainingConfig



class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def train_val_gen(self):
        train_ds = os.path.join("artifacts", "data_ingestion", "animals", "train")
        val_ds = os.path.join("artifacts", "data_ingestion", "animals", "val")

        train_datagen = ImageDataGenerator(
        rescale = 1./255,  
        shear_range = 0.1, 
        zoom_range = 0.1,  
        horizontal_flip = True,  
        width_shift_range = 0.1,
        height_shift_range = 0.1 
        )

        val_datagen = ImageDataGenerator(rescale=1./255)

        train_generator = train_datagen.flow_from_directory(
            train_ds,
            target_size = (self.config.IMG_SIZE, self.config.IMG_SIZE),
            batch_size = self.config.BATCH_SIZE,
            class_mode = 'categorical'
        )

        val_generator = val_datagen.flow_from_directory(
            val_ds,
            target_size = (self.config.IMG_SIZE, self.config.IMG_SIZE),
            batch_size = self.config.BATCH_SIZE,
            class_mode = 'categorical'
        )
        return train_generator, val_generator
    
    
    def train(self):
        train_gen, val_gen = self.train_val_gen()
        pretrained_model = tf.keras.applications.Xception(weights=self.config.WEIGHTS,
                                                           include_top=self.config.INCLUDE_TOP, 
                                                           input_shape=[self.config.IMG_SIZE, self.config.IMG_SIZE, 3])
        pretrained_model.trainable=False
        vgg16_model = tf.keras.Sequential([
            pretrained_model,
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(5, activation='softmax')
        ])

        vgg16_model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

        vgg16_model.fit(train_gen,epochs=self.config.EPOCHS,
                        steps_per_epoch=len(train_gen)/self.config.BATCH_SIZE,
                    validation_steps = len(val_gen)/self.config.BATCH_SIZE,
                    validation_data=val_gen)
        vgg16_model.save(self.config.model_path)