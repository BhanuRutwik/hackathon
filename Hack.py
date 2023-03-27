import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# load the data
df = pd.read_csv('code_changes.csv')

# encode the 'impacted_tests' column as integers
le = LabelEncoder()
df['impacted_tests'] = le.fit_transform(df['impacted_tests'])

# tokenize the code changes
tokenizer = Tokenizer(num_words=5000, oov_token='<OOV>')
tokenizer.fit_on_texts(df['Method_Names'])
sequences = tokenizer.texts_to_sequences(df['Method_Names'])

# pad the sequences to ensure consistent length
max_length = max([len(seq) for seq in sequences])
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

# define the model
model = Sequential([
    Embedding(input_dim=5000, output_dim=64, input_length=max_length),
    LSTM(64),
    Dense(32, activation='relu'),
    Dense(df['impacted_tests'].nunique(), activation='softmax')
])

# compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the model
history = model.fit(padded_sequences, df['impacted_tests'], epochs=10, validation_split=0.6)

print(history.history['accuracy'])
# predict the test cases for a new code change
# new_code_change = ['-    print("Adion operation")', '+    print("Addition operation1")', '-    print("subtraction operation")', '+    print("subtraction operat")', '+    print("extra activites")', '+        print("divide error")']
new_code_change = ['subtract' ]
new_sequence = tokenizer.texts_to_sequences([new_code_change])
new_padded_sequence = pad_sequences(new_sequence, maxlen=max_length, padding='post')
pred = model.predict(new_padded_sequence)[0]
pred_test = le.inverse_transform([np.argmax(pred)])
print("Predicted impacted test case:", pred_test[0])
