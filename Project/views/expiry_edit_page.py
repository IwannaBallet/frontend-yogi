import streamlit as st
from datetime import date, timedelta

# Sample fallback (would ideally pull from st.session_state or DB)
sample_ingredients = st.session_state.get("ocr_results", ["우유", "계란", "브로콜리"])

# Mock LLM date predictor (for later: use real LLM or DB of shelf life)
def suggest_expiry(item_name):
    default_days = {
        "우유": 7,
        "계란": 14,
        "브로콜리": 5,
    }
    return date.today() + timedelta(days=default_days.get(item_name, 10))

def show(go_to):
    st.title("📆 유통기한 지정 및 수정")
    st.markdown("인식된 재료에 대해 유통기한을 설정하세요. 기본값은 AI가 제안합니다.")

    if "expiry_info" not in st.session_state:
        st.session_state.expiry_info = {}

    for item in sample_ingredients:
        suggested = suggest_expiry(item)
        user_date = st.date_input(
            f"'{item}'의 유통기한 선택",
            value=st.session_state.expiry_info.get(item, suggested),
            key=f"expiry_{item}"
        )
        st.session_state.expiry_info[item] = user_date

    st.write("📦 최종 유통기한 목록:")
    st.json(st.session_state.expiry_info)

    if st.button("✅ 재고 저장 및 재고 목록으로"):
        st.success("재고에 유통기한이 저장되었습니다!")
        go_to("inventory")  # or "alert" or "recipe"
