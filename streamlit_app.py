import streamlit as st
import requests

# Streamlit UI
st.title("💬 AI-Powered Q&A")

query = st.text_input("Ask a question:")
if st.button("Get Answer"):
    if query:
        response = requests.post("https://3ae2593a-f3d2-4010-9a12-5053234c8ba7-00-1wnfsg3z2n3gn.pike.replit.dev/ask",
                                 json={"query": query})
        answer = response.json().get("answer", "No response")
        st.write("**Answer:**", answer)
    else:
        st.warning("Please enter a question.")
