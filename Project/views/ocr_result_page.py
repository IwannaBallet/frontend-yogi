import streamlit as st

sample_ingredients = ["우유", "달걀", "버터", "브로콜리"]

def show(go_to):
    st.title("📋 OCR 결과 확인 및 수정")
    st.markdown("OCR로 인식된 재료들을 확인하고 직접 수정하거나 재료를 추가/삭제할 수 있습니다.")

    # 세션 상태 초기화
    if "editable_ingredients" not in st.session_state:
        st.session_state.editable_ingredients = sample_ingredients.copy()
    if "manually_added" not in st.session_state:
        st.session_state.manually_added = []

    # 수정/삭제 UI
    st.subheader("🔍 인식된 재료 수정 및 삭제")
    updated_list = []
    remove_indices = []
    for i, item in enumerate(st.session_state.editable_ingredients):
        cols = st.columns([6, 1])
        edited = cols[0].text_input(f"재료 {i+1}", value=item, key=f"edit_{i}")
        remove = cols[1].button("❌", key=f"remove_{i}")
        if remove:
            remove_indices.append(i)
        else:
            updated_list.append(edited)
    # 삭제 반영
    for idx in sorted(remove_indices, reverse=True):
        del updated_list[idx]
    st.session_state.editable_ingredients = updated_list

    # 재료 추가
    st.subheader("➕ 재료 직접 추가")
    new_ingredient = st.text_input("새로운 재료 입력", key="new_input")
    if st.button("추가"):
        if new_ingredient.strip():
            st.session_state.manually_added.append(new_ingredient.strip())
            st.success(f"'{new_ingredient.strip()}' 이(가) 추가되었습니다.")
            st.rerun()

    # 최종 목록
    st.subheader("📝 최종 재료 목록")
    final_ingredients = st.session_state.editable_ingredients + st.session_state.manually_added
    st.write(final_ingredients)

    # 최종 확인 버튼
    if st.button("✅ 재고에 추가"):
        st.success("재고에 저장되었습니다! (프론트엔드 시뮬레이션)")
        go_to("expiry")  
