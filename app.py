import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="나와 닮은 CEO 찾기",
    page_icon="📊",
    layout="centered"
)

# -----------------------------
# 질문 데이터 (8문항)
# -----------------------------
questions = [

    {
        "question": "Q1. 새로운 아이디어가 떠오르면?",
        "a": "일단 실행부터 해본다",
        "b": "현실성과 데이터를 먼저 본다",
        "type": "CA"
    },

    {
        "question": "Q2. 팀플에서 나는 보통?",
        "a": "리더 역할을 맡는다",
        "b": "조율자 역할을 맡는다",
        "type": "LT"
    },

    {
        "question": "Q3. 사업 아이템을 고른다면?",
        "a": "위험해도 혁신적인 것",
        "b": "안정적으로 오래 갈 것",
        "type": "CS"
    },

    {
        "question": "Q4. 내가 더 중요하게 생각하는 건?",
        "a": "창의성과 가능성",
        "b": "효율성과 결과",
        "type": "CA"
    },

    {
        "question": "Q5. 친구들이 나를 보는 느낌은?",
        "a": "추진력 있다",
        "b": "배려심 있다",
        "type": "LT"
    },

    {
        "question": "Q6. 기업 운영에서 가장 중요한 건?",
        "a": "시장 혁신",
        "b": "지속 가능한 성장",
        "type": "CS"
    },

    {
        "question": "Q7. 실패를 겪으면?",
        "a": "다시 더 크게 도전한다",
        "b": "원인을 분석한다",
        "type": "CA"
    },

    {
        "question": "Q8. 조직 분위기는?",
        "a": "빠르고 자유로운 게 좋다",
        "b": "안정적이고 체계적인 게 좋다",
        "type": "CS"
    }
]

# -----------------------------
# 결과 데이터
# -----------------------------
results = {

    "CLC": {
        "title": "혁신가형",
        "person": "Steve Jobs",
        "image": "images/jobs.jpg",

        "desc": """
당신은 창의성과 혁신을 중요하게 생각하는 타입입니다.

새로운 아이디어를 만드는 능력이 뛰어나며,
강한 비전과 추진력을 가지고 있습니다.
""",

        "famous": """
애플(Apple)의 공동 창업자.

아이폰과 맥북 등 혁신적인 제품으로
세계 IT 시장을 바꾼 인물입니다.
""",

        "strength": [
            "창의적 아이디어",
            "강한 추진력",
            "브랜드 감각"
        ],

        "job": [
            "마케팅",
            "브랜딩",
            "스타트업"
        ],

        "quote": "Innovation distinguishes between a leader and a follower."
    },

    "CLS": {
        "title": "비전리더형",
        "person": "Howard Schultz",
        "image": "images/schultz.jpg",

        "desc": """
사람 중심 리더십과 조직 문화를 중요하게 생각하는 타입입니다.
""",

        "famous": """
스타벅스를 세계적인 브랜드로 성장시킨 CEO.
""",

        "strength": [
            "공감 능력",
            "리더십",
            "조직 관리"
        ],

        "job": [
            "HR",
            "서비스경영",
            "브랜드경영"
        ],

        "quote": "Success is best when it’s shared."
    },

    "CTC": {
        "title": "소통혁신형",
        "person": "Elon Musk",
        "image": "images/musk.jpg",

        "desc": """
도전 정신과 실행력이 뛰어난 혁신형 타입입니다.
""",

        "famous": """
테슬라(Tesla), 스페이스X(SpaceX)의 CEO.
""",

        "strength": [
            "실행력",
            "도전 정신",
            "미래지향적 사고"
        ],

        "job": [
            "창업",
            "IT",
            "전략기획"
        ],

        "quote": "When something is important enough, you do it."
    },

    "CTS": {
        "title": "공감리더형",
        "person": "Oprah Winfrey",
        "image": "images/oprah.jpg",

        "desc": """
공감 능력과 커뮤니케이션 능력이 뛰어난 타입입니다.
""",

        "famous": """
세계적인 방송인 겸 미디어 사업가.
""",

        "strength": [
            "소통 능력",
            "공감",
            "영향력"
        ],

        "job": [
            "광고홍보",
            "미디어",
            "마케팅"
        ],

        "quote": "Turn your wounds into wisdom."
    },

    "ALC": {
        "title": "전략가형",
        "person": "Jeff Bezos",
        "image": "images/bezos.jpg",

        "desc": """
효율과 전략을 중요하게 생각하는 분석형 타입입니다.
""",

        "famous": """
아마존(Amazon)의 창업자.
""",

        "strength": [
            "전략적 사고",
            "효율성",
            "데이터 분석"
        ],

        "job": [
            "SCM",
            "경영전략",
            "생산관리"
        ],

        "quote": "Your margin is my opportunity."
    },

    "ALS": {
        "title": "투자분석형",
        "person": "Warren Buffett",
        "image": "images/buffett.jpg",

        "desc": """
신중하고 안정적인 성향의 분석 중심 타입입니다.
""",

        "famous": """
세계적인 투자자이자 버크셔 해서웨이 회장.
""",

        "strength": [
            "분석력",
            "안정성",
            "리스크 관리"
        ],

        "job": [
            "재무",
            "회계",
            "금융"
        ],

        "quote": "Risk comes from not knowing what you're doing."
    },

    "ATC": {
        "title": "디지털개척형",
        "person": "Mark Zuckerberg",
        "image": "images/zuck.jpg",

        "desc": """
기술과 디지털 환경에 강한 미래지향적 타입입니다.
""",

        "famous": """
메타(Meta)의 창업자.
""",

        "strength": [
            "디지털 감각",
            "빠른 실행",
            "기술 친화성"
        ],

        "job": [
            "IT창업",
            "플랫폼비즈니스",
            "서비스기획"
        ],

        "quote": "The biggest risk is not taking any risk."
    },

    "ATS": {
        "title": "협상전문가형",
        "person": "Jack Ma",
        "image": "images/jackma.jpg",

        "desc": """
설득력과 관계 형성 능력이 뛰어난 타입입니다.
""",

        "famous": """
알리바바(Alibaba)의 창업자.
""",

        "strength": [
            "협상 능력",
            "영업",
            "커뮤니케이션"
        ],

        "job": [
            "국제경영",
            "영업관리",
            "무역"
        ],

        "quote": "Never give up."
    }
}

# -----------------------------
# 세션 상태
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

# -----------------------------
# 메인 화면
# -----------------------------
st.title("📊 나와 닮은 CEO 찾기")
st.subheader("질문에 답하고 나와 가장 닮은 CEO를 확인해보세요!")

progress = st.session_state.page / len(questions)
st.progress(progress)

# -----------------------------
# 질문 화면
# -----------------------------
if st.session_state.page < len(questions):

    q = questions[st.session_state.page]

    st.write(f"## {q['question']}")

    answer = st.radio(
        "답변 선택",
        [q["a"], q["b"]],
        key=st.session_state.page
    )

    if st.button("다음 ➡️"):

        st.session_state.answers.append({
            "answer": answer,
            "type": q["type"],
            "a": q["a"]
        })

        st.session_state.page += 1
        st.rerun()

# -----------------------------
# 결과 계산
# -----------------------------
else:

    creative = 0
    analytic = 0

    leader = 0
    teamwork = 0

    challenge = 0
    stable = 0

    for item in st.session_state.answers:

        if item["type"] == "CA":

            if item["answer"] == item["a"]:
                creative += 1
            else:
                analytic += 1

        elif item["type"] == "LT":

            if item["answer"] == item["a"]:
                leader += 1
            else:
                teamwork += 1

        elif item["type"] == "CS":

            if item["answer"] == item["a"]:
                challenge += 1
            else:
                stable += 1

    result = ""

    result += "C" if creative >= analytic else "A"
    result += "L" if leader >= teamwork else "T"
    result += "C" if challenge >= stable else "S"

    final = results[result]

    # 결과 출력
    st.balloons()

    st.success(f"당신과 가장 닮은 CEO는 '{final['person']}' 입니다!")

    st.image(final["image"], width=320)

    st.header(final["title"])
    st.subheader(final["person"])

    st.write("## 👤 CEO 소개")
    st.write(final["famous"])

    st.write("---")

    st.write("## 📊 당신의 성향 분석")
    st.write(final["desc"])

    st.write("---")

    st.write("## 💡 당신의 강점")

    for s in final["strength"]:
        st.write(f"✔ {s}")

    st.write("---")

    st.write("## 🎯 추천 분야")

    for j in final["job"]:
        st.write(f"📌 {j}")

    st.write("---")

    st.write("## 🗣 대표 명언")
    st.info(final["quote"])

    st.write("---")

    st.write(f"### 🔍 결과 코드: {result}")

    # 다시하기
    if st.button("🔄 다시 테스트하기"):

        st.session_state.page = 0
        st.session_state.answers = []

        st.rerun()