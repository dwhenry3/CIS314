#pip install tensorflow
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

data = ["Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.","Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure.","We are met on a great battlefield of that war.","We have come to dedicate a portion of that field as a final resting place for those who here gave their lives that that nation might live.","It is altogether fitting and proper that we should do this.","But in a larger sense we cannot dedicate, we cannot consecrate, we cannot hallow this ground.","The brave men, living and dead, who struggled here have consecrated it, far above our poor power to add or detract.","The world will little note, nor long remember, what we say here, but it can never forget what they did here.","It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced.","It is rather for us to be here dedicated to the great task remaining before us,that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion, that we here highly resolve that these dead shall not have died in vain, that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the earth."]
#data = ["The land upon which the proposed licensed premises would be situated is owned by C.S.P. Investments, Inc. (CSP).","CSP subdivided the entire property into two condominium units-Unit 1 and Unit 2-and a common area.","The condominium units would have separate tax assessments, as well as different real estate tax numbers.","Unit 1, the location of the proposed license premises, is being leased from CSP by Ohio Springs.","Ohio Springs' parent company, Sheetz, Inc., is leasing Unit 2 of the condominium, and the common area would be shared between the two entities.","The Declaration of Condominium restricts the use of each unit such that Unit 1 cannot be used for the sale of gasoline and Unit 2 cannot be used for the sale of alcohol."]
#data = ["This is my first sentence.","This is my second sentence.","This is my third sentence."]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(data)
total_words = len(tokenizer.word_index) + 1

sequences = tokenizer.texts_to_sequences(data)

input_sequences = []
for sequence in sequences:
    for i in range(1, len(sequence)):
        n_gram_sequence = sequence[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_length = max([len(seq) for seq in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length, padding='pre')

X = input_sequences[:, :-1]
y = input_sequences[:, -1]

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_words, 64),
    tf.keras.layers.LSTM(100),
    tf.keras.layers.Dense(total_words, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=100, verbose=1)

seed_text = "This is"
next_words = 10

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_length-1, padding='pre')
    predicted = np.argmax(model.predict(token_list), axis=1)
    #predicted = model.predict_classes(token_list, verbose=0)
    
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word

print(seed_text)