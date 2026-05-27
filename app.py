import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 애니 추천 플레이스",
    page_icon="🎬",
    layout="centered"
)

# 2. MBTI별 애니메이션 데이터 베이스 (추천 데이터)
# 필요에 따라 타이틀과 설명, 이미지를 자유롭게 변경해보세요!
MBTI_ANIME_DB = {
    "INFP": {
        "title": "나츠메 우인장 (Natsume's Book of Friends)",
        "desc": "잔잔한 감동과 따뜻한 힐링이 필요한 인프피에게 딱! 요괴를 보는 소년과 고양이 선생의 가슴 따뜻한 이야기입니다.",
        "genre": "힐링, 판타지, 일상"
    },
    "INFJ": {
        "title": "바이올렛 에버가든 (Violet Evergarden)",
        "desc": "깊은 감정과 인간의 마음에 대해 탐구하는 인프제에게 추천합니다. 아름다운 작화와 깊은 여운을 남기는 스토리라인이 특징입니다.",
        "genre": "드라마, 로맨스, 판타지"
    },
    "ENFP": {
        "title": "하이큐!! (Haikyu!!)",
        "desc": "에너제틱하고 꿈을 향해 달리는 엔프피의 열정을 깨워줄 스포츠 애니! 보기만 해도 가슴이 웅장해지고 긍정 에너지가 솟아납니다.",
        "genre": "스포츠, 성장, 청춘"
    },
    "ENFJ": {
        "title": "귀멸의 칼날 (Demon Slayer)",
        "desc": "정의롭고 동료를 소중히 여기는 엔프제라면 주인공 탄지로의 따뜻한 리더십과 꺾이지 않는 마음에 깊이 몰입할 것입니다.",
        "genre": "액션, 판타지, 소년만화"
    },
    "INTP": {
        "title": "슈타인즈 게이트 (Steins;Gate)",
        "desc": "지적 호기심이 왕성하고 인과관계 분석을 좋아하는 인팁을 위한 최고의 타임리프 미스터리 스릴러입니다.",
        "genre": "SF, 미스터리, 스릴러"
    },
    "INTJ": {
        "title": "데스노트 (Death Note)",
        "desc": "철저한 전략과 두뇌 싸움을 즐기는 인티제에게 추천합니다. 선과 악의 경계에서 벌어지는 치열한 심리전이 매력적입니다.",
        "genre": "스릴러, 두뇌싸움, 다크 판타지"
    },
    "ENTP": {
        "title": "조설제해 / 릭 앤 모티 (Rick and Morty)",
        "desc": "독창적이고 킹받는 유머를 즐기는 엔팁에게 딱 맞는 SF 블랙코미디! 예측 불가능한 전개가 도파민을 자극합니다.",
        "genre": "SF, 블랙코미디, 애니메이션"
    },
    "ENTJ": {
        "title": "코드 기아스 반역의 를르슈 (Code Geass)",
        "desc": "세상을 바꾸려는 야망과 철저한 리더십을 가진 엔티제와 닮은 주인공! 거대한 스케일의 전략적 승부를 확인해보세요.",
        "genre": "메카닉, 전략, 드라마"
    },
    # 나머지 8개 MBTI도 기본 데이터 추가 (커스텀 가능)
    "ISFP": {"title": "지브리 시리즈 (이웃집 토토로 등)", "desc": "예술적 감수성이 풍부하고 평화를 사랑하는 잇프피를 위한 아늑한 감성.", "genre": "애니메이션, 판타지"},
    "ISFJ": {"title": "너에게 닿기를 (Kimi ni Todoke)", "desc": "소중한 사람들을 묵묵히 챙기는 잇프제의 순수하고 따뜻한 감성을 채워줄 로맨스.", "genre": "로맨스, 학원물"},
    "ESFP": {"title": "케이온! (K-ON!)", "desc": "인생은 즐겁게! 낙천적이고 흥이 넘치는 엣프피를 위한 방과 후 밴드 일상물.", "genre": "일상, 음악, 코미디"},
    "ESFJ": {"title": "나의 히어로 아카데미아", "desc": "협동과 상생, 모두를 지키는 따뜻한 사회를 지향하는 엣프제에게 추천하는 히어로물.", "genre": "액션, 히어로, 소년만화"},
    "ISTP": {"title": "진격의 거인 (Attack on Titan)", "desc": "상황 판단이 빠르고 냉철한 잇팁이 몰입하기 좋은 치밀한 세계관과 압도적인 액션 스케일.", "genre": "다크 판타지, 액션"},
    "ISTJ": {"title": "사이코 패스 (PSYCHO-PASS)", "desc": "원리원칙과 시스템 분석을 선호하는 잇티제의 흥미를 자극할 디스토피아 형사물.", "genre": "SF, 범죄, 스릴러"},
    "ESTP": {"title": "체인소 맨 (Chainsaw Man)", "desc": "스릴과 강렬한 자극을 즐기며 본능에 충실한 엣티제에게 추천하는 트렌디하고 화끈한 액션.", "genre": "다크 판타지, 액션"},
    "ESTJ": {"title": "강철의 연금술사 리메이크", "desc": "완벽한 플롯과 체계적인 세계관, 목표를 향해 흔들림 없이 나아가는 대작.", "genre": "판타지, 액션, 드라마"}
}

# 3. UI 메인 타이틀
st.title("🎬 MBTI 맞춤형 애니메이션 추천기")
st.write("여러분의 MBTI를 선택하시면 성향에 꼭 맞는 인생 애니메이션을 추천해 드립니다.")

st.markdown("---")

# 4. 사용자 입력 받기
mbti_list = sorted(list(MBTI_ANIME_DB.keys()))
selected_mbti = st.selectbox(
    "💡 당신의 MBTI를 선택하세요:",
    mbti_list,
    index=None,
    placeholder="여기를 눌러 선택하세요..."
)

# 5. 결과 출력 로직
if selected_mbti:
    anime_info = MBTI_ANIME_DB[selected_mbti]
    
    st.balloons() # 축하 효과 일시 등장
    
    # 결과 창 예쁘게 꾸미기
    st.success(f"✨ **{selected_mbti}** 타입에게 추천하는 애니메이션은?")
    
    # 카드 형태의 시각적 박스
    with st.container(border=True):
        st.subheader(anime_info["title"])
        st.caption(f"**장르:** {anime_info['genre']}")
        st.write("")
        st.write(anime_info["desc"])
        
    # 추가 인터랙션 (좋아요 버튼 맛보기)
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("❤️ 좋아요"):
            st.toast("추천이 마음에 드셨다니 다행입니다!")
else:
    st.info("MBTI를 선택하면 추천 결과가 여기에 나타납니다.")

# 6. 푸터(Footer)
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | [MBTIanime](https://github.com/meyul/MBTIanime)")
