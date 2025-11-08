import streamlit as st

# 앱 제목
st.title("💤 수면 습관 체크리스트")
st.write("아래 항목을 체크하여 자신의 수면 습관을 점검해보세요!")

# 체크리스트 항목
st.subheader("🕐 수면 패턴")
sleep_time = st.checkbox("매일 같은 시간에 잠자리에 든다")
wake_time = st.checkbox("매일 같은 시간에 일어난다")
enough_sleep = st.checkbox("하루에 7시간 이상 잔다")

st.subheader("📱 취침 전 습관")
no_phone = st.checkbox("잠들기 전 30분 동안 스마트폰을 보지 않는다")
no_caffeine = st.checkbox("오후 3시 이후에는 카페인을 섭취하지 않는다")
relax = st.checkbox("잠들기 전에 스트레칭이나 명상을 한다")

st.subheader("🛏️ 수면 환경")
dark_room = st.checkbox("방이 어둡고 조용하다")
comfortable_bed = st.checkbox("매트리스와 베개가 편안하다")
right_temp = st.checkbox("방 온도가 적절하다")

# 점수 계산
score = sum([
    sleep_time, wake_time, enough_sleep,
    no_phone, no_caffeine, relax,
    dark_room, comfortable_bed, right_temp
])

st.markdown("---")
st.subheader("🌙 결과 분석")

# 결과 메시지
if score >= 8:
    st.success(f"✅ 매우 건강한 수면 습관을 가지고 있습니다! (총 {score}/9점)")
elif score >= 5:
    st.info(f"😴 나쁘지 않아요! 약간의 개선으로 더 좋은 수면 습관을 만들 수 있습니다. (총 {score}/9점)")
else:
    st.warning(f"⚠️ 수면 습관을 개선할 필요가 있어요. 수면 시간을 일정하게 하고 취침 전 전자기기 사용을 줄여보세요. (총 {score}/9점)")

# 추가 메모 작성
st.markdown("---")
st.subheader("📝 오늘의 수면 메모")
note = st.text_area("오늘 수면에 대해 기록해보세요 (예: 몇 시에 잤는지, 몇 번 깼는지 등)")
if st.button("저장하기"):
    st.success("기록이 저장되었습니다! 좋은 밤 되세요 🌙")
