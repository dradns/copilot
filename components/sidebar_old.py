import streamlit as st
#from dotenv import load_dotenv
import os

#load_dotenv()

def sidebar():
    with st.sidebar:
        st.markdown(
            "# Business requirements\n"
            "1. Вот так оформляется [Ссылка](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Ask a question about the document💬\n"
        )

        st.markdown("---")


        st.markdown("# System requirements")
        st.markdown(
            "📖KnowledgeGPT allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/mmz-001/knowledge_gpt) "  # noqa: E501
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by [mmz_001](https://twitter.com/mm_sasmitha)")
        st.markdown("---")

        st.markdown("# Acceptance criteria")
        st.markdown(
            "📖KnowledgeGPT allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/mmz-001/knowledge_gpt) "  # noqa: E501
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by [mmz_001](https://twitter.com/mm_sasmitha)")
        st.markdown("---")

        st.markdown(
            "# Settings\n"
            "Enter your API key below🔑\n"  # noqa: E501
        )
        api_key_input = st.text_input(
            "API Key",
            type="password",
            placeholder="Paste your API key here",
            help="You can get your API key from https://platform.openai.com/account/api-keys",  # noqa: E501
            value=os.environ.get("API_KEY", None)
            or st.session_state.get("API_KEY", ""),
        )


        st.session_state["API_KEY"] = api_key_input

