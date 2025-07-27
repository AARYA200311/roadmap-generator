from ctransformers import AutoModelForCausalLM

print("⏳ Loading model...")

model = AutoModelForCausalLM.from_pretrained(
    "model",
    model_file="llama-2-7b-chat.Q2_K.gguf",
    model_type="llama",
    max_new_tokens=300,
    temperature=0.7
)

print("✅ Model loaded successfully!")
