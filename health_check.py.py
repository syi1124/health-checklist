import streamlit as st

st.title("🌿 청소년 건강 습관 체크리스트 🌿")
st.write("각 질문에 해당되면 ✅ 체크해주세요!\n")

questions = [
    "1. 하루에 7시간 이상 숙면을 취하나요?",
    "2. 하루 3끼 식사를 규칙적으로 하나요?",
    "3. 아침을 거르지 않나요?",
    "4. 하루 30분 이상 몸을 움직이나요?",
    "5. 스마트폰 사용 시간을 하루 3시간 이하로 제한하나요?",
    "6. 카페인 음료(커피, 에너지 드링크)를 자주 마시지 않나요?",
    "7. 스트레스를 받을 때 건강한 방법(운동, 대화 등)으로 풀고 있나요?",
    "8. 하루에 물을 6잔 이상 마시나요?",
    "9. 자세를 바르게 유지하려 노력하나요?",
    "10. 정기적으로 건강검진(시력, 체중, 치아 등)을 받나요?"
]

score = 0
answers = []

for q in questions:
    ans = st.checkbox(q)
    answers.append(ans)

if st.button("결과 확인하기"):
    score = sum(answers)
    st.subheader(f"✅ 당신의 건강 습관 점수는 {score}점 / 10점입니다!")

    if score == 10:
        st.success("완벽해요! 지금처럼 꾸준히 건강을 유지하세요 💪")
    elif score >= 7:
        st.info("좋아요! 대부분의 건강 습관을 잘 지키고 있어요 👍")
    elif score >= 4:
        st.warning("보통이에요. 몇 가지 습관을 조금만 바꾸면 더 건강해질 수 있어요 🌱")
    else:
        st.error("주의! 건강 습관을 개선할 필요가 있어요 ⚠️ 작은 습관부터 바꿔봐요!")

st.write("---")
st.caption("💡 제작: 청소년 건강 프로젝트")
