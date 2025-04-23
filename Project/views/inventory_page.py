import streamlit as st
from datetime import date
import pandas as pd


def show(go_to):
    st.title("📦 재고 목록 및 수정")

    # 1. Load ingredients with expiry from session (simulate DB)
    if "expiry_info" not in st.session_state:
        st.warning("유통기한 정보가 없습니다. 이전 단계부터 진행해주세요.")
        return

    if "inventory" not in st.session_state:
        # Initialize inventory from expiry_info
        st.session_state.inventory = [
            {"name": name, "expiry": st.session_state.expiry_info[name]}
            for name in st.session_state.expiry_info
        ]

    st.subheader("🧾 현재 재고 목록")

    new_inventory = []
    for i, item in enumerate(st.session_state.inventory):
        cols = st.columns([4, 4, 1])
        name = cols[0].text_input("재료명", value=item["name"], key=f"name_{i}")
        expiry = cols[1].date_input("유통기한", value=item["expiry"], key=f"expiry_{i}")
        delete = cols[2].button("❌", key=f"delete_{i}")

        if not delete:
            new_inventory.append({"name": name, "expiry": expiry})

    st.session_state.inventory = new_inventory  # update inventory

    # 2. Add new 재료 manually
    st.divider()
    st.subheader("➕ 새로운 재료 추가")
    new_name = st.text_input("재료 이름", key="new_name")
    new_expiry = st.date_input("유통기한", key="new_expiry", value=date.today())

    if st.button("추가"):
        if new_name:
            st.session_state.inventory.append({"name": new_name, "expiry": new_expiry})
            st.success(f"'{new_name}' 재료가 추가되었습니다.")
            st.rerun()

    st.subheader("📋 최종 재고 상태")
    if st.session_state.inventory:
        df = pd.DataFrame(st.session_state.inventory)
        df.index = df.index + 1  # ✅ Make index start from 1

    # === Sorting & Filtering Options ===
    st.markdown("🔍 정렬 및 필터 옵션")

    sort_by = st.selectbox("정렬 기준을 선택하세요", options=["이름순", "유통기한순"])
    if sort_by == "이름순":
        df = df.sort_values(by="name")
    elif sort_by == "유통기한순":
        df = df.sort_values(by="expiry")

    st.dataframe(df, use_container_width=True)

    if st.button("➡️ 레시피 추천 이동"):
        go_to("recipe")
