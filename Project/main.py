import streamlit as st
from views import login_page, image_upload_page, ocr_result_page, expiry_edit_page, inventory_page

# === Session Setup ===
if "page" not in st.session_state:
    st.session_state.page = "login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# === Navigation function ===
def go_to(page):
    st.session_state.page = page
    st.rerun()

# === Auth-Gated Page Dispatcher
def show_if_logged_in(page_function):
    if st.session_state.logged_in:
        page_function(go_to)
    else:
        st.warning("로그인이 필요합니다.")
        go_to("login")

# === Page Routing ===
page = st.session_state.page

if page == "login":
    login_page.show(go_to)
elif page == "upload":
    show_if_logged_in(image_upload_page.show)
elif page == "ocr_result":
    show_if_logged_in(ocr_result_page.show)
elif page == "expiry":
    show_if_logged_in(expiry_edit_page.show)
elif page == "inventory":
    show_if_logged_in(inventory_page.show)

