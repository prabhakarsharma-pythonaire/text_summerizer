import tensorflow as tf

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

if len(tf.config.list_physical_devices('GPU')) > 0:
  # Enable memory growth for first GPU device
  tf.config.experimental.set_memory_growth(tf.config.list_physical_devices('GPU')[0], True)
  print("GPU memory growth enabled")

# Run a TensorFlow operation to verify GPU usage
print(tf.reduce_sum(tf.random.normal([1000, 1000])))
