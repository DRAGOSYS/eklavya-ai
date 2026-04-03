import streamlit as st
from google import genai
from google.genai import types
import json
import time

# --- INITIALIZATION ---
st.set_page_config(page_title="Eklavya AI", layout="centered", page_icon="🎯")

if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"],
        http_options=types.HttpOptions(api_version='v1beta')
    )
else:
    st.error("🔑 Missing API Key! Add it to your secrets.")
    st.stop()

# Use the latest stable April 2026 model
MODEL_ID = "gemini-3-flash-preview"

st.title("🎯 Eklavya: AI Learning Assistant")
st.caption("A multi-agent pipeline for grade-specific education")

grade = st.number_input("Target Grade", min_value=1, max_value=12, value=4)
topic = st.text_input("Topic", value="Types of angles")

if st.button("🚀 Run Agent Pipeline"):
    try:
        # --- STAGE 1: GENERATOR ---
        with st.status("🤖 Agent 1: Generating Content...", expanded=True) as status:
            gen_prompt = (
                f"Generate educational content for Grade {grade} on {topic}. "
                "Return ONLY JSON: {'explanation': '...', 'mcqs': [{'question': '...', 'options': [], 'answer': '...'}]}"
            )
            response = client.models.generate_content(model=MODEL_ID, contents=gen_prompt)
            
            # Parse and store data
            clean_gen = response.text.replace('```json', '').replace('```', '').strip()
            gen_data = json.loads(clean_gen)
            status.update(label="✅ Generation Complete", state="complete")

        time.sleep(2) # Prevent Rate Limits

        # --- STAGE 2: REVIEWER ---
        with st.status("🕵️ Agent 2: Reviewing Quality...", expanded=True) as status:
            rev_prompt = f"Review this for Grade {grade} students. Return ONLY JSON: {{'status': 'pass/fail', 'feedback': []}}. Content: {clean_gen}"
            rev_res = client.models.generate_content(model=MODEL_ID, contents=rev_prompt)
            
            clean_rev = rev_res.text.replace('```json', '').replace('```', '').strip()
            rev_data = json.loads(clean_rev)
            status.update(label="✅ Review Complete", state="complete")

        # --- STAGE 3: REFINEMENT (If needed) ---
        final_data = gen_data
        if rev_data.get("status") == "fail":
            with st.status("🛠️ Agent 3: Refining Content...", expanded=True) as status:
                refine_prompt = f"Improve this using feedback: {rev_data['feedback']}. Original: {clean_gen}. Return ONLY JSON."
                refine_res = client.models.generate_content(model=MODEL_ID, contents=refine_prompt)
                final_data = json.loads(refine_res.text.replace('```json', '').replace('```', '').strip())
                status.update(label="✅ Refinement Complete", state="complete")

        # --- NEW: DISPLAY LOGIC (This is what makes the content visible) ---
        st.divider()
        st.header("📖 Your Lesson")
        
        # 1. Display the Explanation
        st.markdown("### Explanation")
        st.info(final_data.get('explanation', 'No explanation generated.'))

        # 2. Display the MCQs
        st.markdown("### Practice Quiz")
        for i, q in enumerate(final_data.get('mcqs', [])):
            st.write(f"**Question {i+1}:** {q['question']}")
            
            # Display options neatly
            for option in q['options']:
                st.write(f"- {option}")
            
            # Use an expander to hide the answer initially
            with st.expander(f"View Answer for Q{i+1}"):
                st.success(f"Correct Answer: {q['answer']}")
        
        st.balloons()

    except Exception as e:
        st.error(f"⚠️ Error: {e}")