import streamlit as st
import openai
import os

# Set your OpenAI key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

prompts = [
    "What key historical or systemic context is missing from this article?",
    "What perspectives from marginalized or non-elite sources might alter the framing?",
    "What are potential counter-narratives not explored by the article?",
    "Which important questions remain unasked in this reporting?",
    "What power structures or incentives might influence how this story is told?",
    "How could this story be reframed with a longer time horizon or retrospective analysis?"
]

st.title("🧠 Missed It Machine")
st.write("Paste a news article below to find what might have been missed.")

article = st.text_area("Your News Article", height=300)

if st.button("Analyze Article"):
    if not article:
        st.warning("Please paste an article first.")
    else:
        with st.spinner("Running analysis..."):
            insights = []
            for p in prompts:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a media analyst uncovering gaps in mainstream narratives."},
                        {"role": "user", "content": f"Article: {article}\n\n{p}"}
                    ],
                    temperature=0.7
                )
                insights.append(response['choices'][0]['message']['content'])
            st.success("Done!")
            for i, insight in enumerate(insights):
                st.markdown(f"**Prompt {i+1}: {prompts[i]}**")
                st.markdown(f"> {insight}")
