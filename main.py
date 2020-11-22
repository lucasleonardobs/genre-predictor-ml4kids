import streamlit as st
import awesome_streamlit as ast
import pages.home
import pages.about

PAGES = {
    "Home": pages.home,
    "Sobre o projeto": pages.about,
}

def main():
    """Main function of the App"""
    st.sidebar.title("Navegação")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    st.sidebar.info(
        "Esse projeto tem fins meramente educativos e está "
        "licenciado sobre a licensa MIT. "
        "Copyright (c) 2020 Lucas Leonardo, Wesley Alves"
    )

    with st.spinner(f"Carregando..."):
        ast.shared.components.write_page(page)

if __name__ == "__main__":
    main()