import streamlit as st

def navbar():
    # Initialize theme in session state
    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    # Navbar layout
    
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown("<h1 style='margin:0; color:#E72929; -webkit-text-stroke: 0.4px white;'>PrompTrix</h1>", unsafe_allow_html=True)
        st.subheader("_'Prompt better, Create faster'_")
    with col2:
        toggle = st.toggle("☀️", value=(st.session_state.theme == "dark"))
        st.session_state.theme = "light" if toggle else "dark"
    
    st.markdown("""
    <hr style="border: 1.8px solid #B6B09F;" />
    """, unsafe_allow_html=True)

    # Inject CSS depending on theme
    if st.session_state.theme == "dark":
        st.markdown(
            """
            <style>
                .stApp {
                    background-color: #021526!important;
                    color: white !important;
                }
                .stTextInput label, .stTextArea label, .stSelectbox label {
                    color: white !important;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
                .stApp {
                    background-color: #EEE6CA !important;
                    color: red  !important;
                }
                .stTextInput label, .stTextArea label, .stSelectbox label {
                    color: black !important;
                }
                .stTabs [data-baseweb="tab"] {
                    color: black;            
                    font-weight: bold;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
