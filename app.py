import streamlit as st
from ctransformers import AutoModelForCausalLM

st.title("📍 AI Roadmap Generator")
st.write("Get a step-by-step learning path for any career or goal!")

st.write("⏳ Loading model... Please wait.")

# Load the LLaMA-2 model
try:
    model = AutoModelForCausalLM.from_pretrained(
        "model",
        model_file="llama-2-7b-chat.Q2_K.gguf",
        model_type="llama",
        max_new_tokens=500,
        temperature=0.7
    )
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")

# User input
goal = st.text_input("🎯 What do you want to become or learn?")

# Generate roadmap
if st.button("Generate Roadmap"):
    if not goal:
        st.warning("⚠️ Please enter your goal.")
    else:
        with st.spinner("🛠️ Generating your roadmap..."):
            prompt = f"Create a detailed learning roadmap for someone who wants to become a {goal}. Include skills, tools, and steps in order from beginner to advanced."
            result = model(prompt)

        st.success("✅ Here is your personalized roadmap:")
        st.write(result)
