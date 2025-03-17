#pip install transformers torch
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load a pretrained GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Input prompt
prompt = "What is butter?"

# Tokenize input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
output = model.generate(
    inputs["input_ids"],
    max_new_tokens=250,
    num_beams=5,  # Use beam search for diversity
    no_repeat_ngram_size=2,  # Avoid repetition
    #temperature=0.7,  # Sampling temperature
)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("---------------------------")
print(generated_text)
