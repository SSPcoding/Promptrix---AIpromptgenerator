import streamlit as st

def navbar():
    # Initialize theme in session state
    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    if "toggle_state" not in st.session_state:
        st.session_state.toggle_state = False  # default toggle is off

    # Navbar layout
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown(
            "<h1 style='margin:0; color:red; -webkit-text-stroke: 0.4px white;'>PrompTrix</h1>",
            unsafe_allow_html=True
        )
        st.subheader("_'Prompt better, Create faster'_")
    with col2:
        # toggle is bound to toggle_state
        toggle = st.toggle("🌙", value=st.session_state.toggle_state)

        # Update theme ONLY if toggle value changed
        if toggle != st.session_state.toggle_state:
            st.session_state.toggle_state = toggle
            st.session_state.theme = "dark" if toggle else "light"

    # Divider
    st.markdown("""<hr style="border: 1.8px solid #B6B09F;" />""", unsafe_allow_html=True)

    # Inject CSS depending on theme
    if st.session_state.theme == "dark":
        st.markdown(
            """
            <style>
                /* App background + base text */
                [data-testid="stAppViewContainer"]{
                    background-color:#021526 !important;
                }
                /* Make all markdown text white */
                [data-testid="stMarkdownContainer"] *{
                    color:#ffffff !important;
                }
                /* Labels for inputs */
                .stTextInput label, .stTextArea label, .stSelectbox label{
                    color:#ffffff !important;
                }
                /* Optional: tabs */
                .stTabs [data-baseweb="tab"]{
                    color:#ffffff !important;
                    font-weight:bold;
                }
                /* Your custom output box */
                .prompt-output{
                    padding:15px;
                    border:1px solid #ddd;
                    border-radius:10px;
                    background-color:transparent;
                    color:#ffffff !important;
                    font-size:16px;
                    white-space:pre-wrap;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
                /* App background */
                [data-testid="stAppViewContainer"]{
                    background-color:#EEE6CA !important;
                }
                /* Make all markdown text RED (headings, paragraphs, etc.) */
                [data-testid="stMarkdownContainer"] *{
                    color:#ff0000 !important;
                }
                /* Keep form labels black for readability */
                .stTextInput label, .stTextArea label, .stSelectbox label{
                    color:#000000 !important;
                }
                /* Tabs styling */
                .stTabs [data-baseweb="tab"]{
                    color:#000000 !important;
                    font-weight:bold;
                }
                /* Your custom output box */
                .prompt-output{
                    padding:15px;
                    border:1px solid #555;
                    border-radius:10px;
                    background-color:transparent;
                    color:#000000 !important;
                    font-size:16px;
                    white-space:pre-wrap;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
