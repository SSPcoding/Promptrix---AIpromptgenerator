import streamlit as st
import os
from dotenv import load_dotenv
import streamlit.components.v1 as components
from utils.navbar import navbar
from utils.prompts import generate_prompt,improve_prompt
import google.generativeai as genai


# ========================
# 🔐 Load API Key
# ========================
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ API Key not found. Please set GEMINI_API_KEY in your .env or Streamlit Secrets.")
    st.stop()

# Configure Gemini
genai.configure(api_key=API_KEY)

# ========================
# 📋 Copy to Clipboard (Custom Button)
# ========================
def copy_to_clipboard(text, label="📋 Copy Prompt", key="default"):
    copy_code = f"""
    <div id="copy-container-{key}">
        <script>
        function copyText_{key}() {{
            navigator.clipboard.writeText(`{text}`).then(function() {{
                var msgDiv = document.getElementById("copied-msg-{key}");
                if (msgDiv) {{
                    msgDiv.innerHTML = "✅ Prompt copied to clipboard!";
                }}
            }}, function(err) {{
                var msgDiv = document.getElementById("copied-msg-{key}");
                if (msgDiv) {{
                    msgDiv.innerHTML = "❌ Failed to copy text: " + err;
                }}
            }});
        }}
        </script>
        <button onclick="copyText_{key}()" style="
            background-color:#4CAF50;
            color:white;
            padding:8px 15px;
            border:none;
            border-radius:5px;
            cursor:pointer;
            margin-top:5px;">
            {label}
        </button>
        <div id="copied-msg-{key}" style="margin-top:5px;color:lightgreen;font-size:14px;"></div>
    </div>
    """
    components.html(copy_code, height=80)

# ========================
# 🎨 Streamlit UI
# ========================
st.set_page_config(page_title="Promptrix", page_icon="🤖")
navbar()
st.markdown("""<p style='font-size:22px; color:#E72929;'>🤖 AI Prompt Generator</p>""", unsafe_allow_html=True)
st.markdown("""<p style='font-size:22px; font-style: italic;'>Generate, refine, and preview optimized prompts for AI models.</p>""", unsafe_allow_html=True)


# Session state
if "latest_prompt" not in st.session_state:
    st.session_state.latest_prompt = None
if "all_prompts" not in st.session_state:
    st.session_state.all_prompts = []

# Tabs
tab1, tab2, tab3 = st.tabs(["🧙 Wizard", "🧐 Critic", "👀 Preview"])

# ========================
# 🧙 Wizard Tab
# ========================
with tab1:
    st.subheader("🧙 Wizard Mode – Generate Fresh Prompt")
    role = st.text_input("Enter Role (e.g., Data Analyst, Poet, Coder, etc.)")
    output_type = st.selectbox("select the format...", ["--select--","Text", "Code", "Image","Other"])
    if output_type == "Other":
        output_type = st.text_input("Specify output type")

    description = st.text_area("Enter Task/Description")
    target = st.selectbox("select the Audience...", ["--select--","Beginners","Intermediate","Experts","Leyman","Other"])
    if target == "Other":
        output_type = st.text_input("Specify target audience")

    constraints = st.selectbox("select constraints...", ["--select--","Use beginner-friendly words","Keep it under 200 words","Include real-world examples",
                                                        "focus on practical applications","Other"])
    if constraints == "Other":
        constraints = st.text_input("Specify constraint...")

    
    if st.button("🚀  Generate Prompt"):
        if role and output_type and description and target and constraints:
            with st.spinner("Crafting your optimized prompt..."):
                prompt = generate_prompt(role, output_type, description, target, constraints)
                st.session_state.latest_prompt = prompt
                st.session_state.all_prompts.append(prompt)

            st.markdown("### ✨ Optimized Prompt")
            st.markdown(
                f"""
                <div class="prompt-output">
                    {st.session_state.latest_prompt}
                """,
                unsafe_allow_html=True
            )
            copy_to_clipboard(prompt, key="wizard")
        else:
            st.warning("⚠️ Please fill all fields before generating.")

# ========================
# 🧐 Critic Tab
# ========================
with tab2:
    st.header("🧐 Critic Mode – Improve Existing Prompt")
    existing_prompt = st.text_area("Paste your existing prompt")

    if st.button("🔍 Improve Prompt"):
        if existing_prompt.strip():
            with st.spinner("Improving your prompt..."):
                improved = improve_prompt(existing_prompt)
                st.session_state.latest_prompt = improved
                st.session_state.all_prompts.append(improved)

            st.markdown("### ✨ Improved Prompt")
            st.markdown(
                f"""
                    <div class="prompt-output" style='padding:15px;border:1px solid #ddd;border-radius:10px;
                    background-color:transparent;color:white;font-size:16px;white-space:pre-wrap;'>
                    {st.session_state.latest_prompt}
                """,
                unsafe_allow_html=True
            )
            copy_to_clipboard(improved, key="critic")
        else:
            st.warning("⚠️ Please paste a prompt to improve.")

# ========================
# 👀 Preview Tab
# ========================
with tab3:
    st.header("👀 Preview Mode – Recent Prompts")
    if st.session_state.all_prompts:
        for idx, p in enumerate(reversed(st.session_state.all_prompts[-5:]), 1):
            st.markdown(
                f"""
                    <div class="prompt-output" style='padding:15px;margin-bottom:10px;border:1px solid #ddd;
                    border-radius:10px;background-color:transparent;color:white;
                    font-size:16px;white-space:pre-wrap;'>
                    {p}

                """,
                unsafe_allow_html=True
            )
            copy_to_clipboard(p, label=f"📋 Copy Prompt {idx}", key=f"preview{idx}")
    else:
        st.info("No prompts generated yet. Use Wizard or Critic first.")
