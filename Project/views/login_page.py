import streamlit as st
from services import db_service

def show(go_to):
    st.title("🗄️ 뭐먹을냉 (식재료 관리 및 레시피 추천 서비스)")
    new_user = st.toggle("계정이 없으신가요? 회원가입")
    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")

    if new_user:
        password_confirm = st.text_input("비밀번호 확인", type="password")
        if st.button("회원가입"):
            if not username or not password or not password_confirm:
                st.error("아이디와 비밀번호(확인)를 모두 입력해주세요.")
            elif password != password_confirm:
                st.error("비밀번호가 일치하지 않습니다.")
            elif db_service.get_user(username):
                st.error("이미 존재하는 아이디입니다.")
            else:
                db_service.create_user({
                    "username": username,
                    "password": password,
                    "preferences": []
                })
                st.success("✅ 회원가입 완료! 이제 로그인해주세요.")
    else:
        if st.button("로그인"):
            if not username or not password:
                st.error("아이디와 비밀번호를 모두 입력해주세요.")
            else:
                user = db_service.get_user(username)
                if user and user.get("password") == password:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    go_to("upload")  # ✅ corrected here
                else:
                    st.error("❌ 아이디 또는 비밀번호가 잘못되었습니다.")
