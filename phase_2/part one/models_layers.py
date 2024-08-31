import tensorflow

rescaling_layer = tensorflow.keras.layers.Rescaling(scale=255.0/(120-1), 
                                                    offset = (-1.0/(120-1)))


