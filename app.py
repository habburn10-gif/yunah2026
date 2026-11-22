import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="오늘 뭐 먹지?",
    page_icon="🍱",
    layout="centered",
)

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
LUNCH_MENUS = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "국밥",
    "비빔밥",
    "짜장면",
    "짬뽕",
    "초밥",
    "우동",
    "쌀국수",
    "햄버거",
    "파스타",
    "떡볶이 & 순대",
    "샐러드 & 샌드위치",
    "부대찌개",
    "마라탕",
    "카레라이스",
]

# 화면 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘의 점심 메뉴를 뽑아보세요.")
st.divider()

# 추천 버튼 생성
if st.button(
    "🎲 점심 메뉴 추천받기", use_container_width=True, type="primary"
):
  # random.choice()를 이용해 리스트에서 무작위로 1개 선택
  selected_menu = random.choice(LUNCH_MENUS)

  # 결과 출력 및 축하 효과
  st.balloons()
  st.success(f"오늘의 추천 메뉴는 **[{selected_menu}]** 입니다! 맛있게 드세요 😋")
else:
  st.info("버튼을 클릭하면 메뉴가 추천됩니다.")

# 전체 메뉴 후보 확인용 접이식 메뉴판
with st.expander("📋 전체 메뉴 후보 보기"):
  st.write(", ".join(LUNCH_MENUS))
