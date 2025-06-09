# eunpyeong-recycling-map-
# 은평구 의류 수거함 위치 웹앱

이 프로젝트는 서울 은평구 내에 설치된 의류 수거함의 위치를 지도에 표시하고, 사용자의 위치와 가장 가까운 수거함을 찾아주는 웹 애플리케이션입니다.  
Python 기반의 [Streamlit](https://streamlit.io/)과 GitHub를 활용하여 제작되었습니다.

## 🧭 주요 기능

- 은평구 의류 수거함 위치 지도 표시 (folium 사용)
- 위도/경도 입력 시, 가장 가까운 수거함 표시
- Streamlit Cloud를 통한 웹 배포

## 📂 사용된 데이터

- 출처: 공공데이터포털 (은평구 의류 수거함 위치 데이터)
- 파일: `data/collection_boxes.csv`

## 🚀 실행 방법 (로컬)

```bash
pip install -r requirements.txt
streamlit run app.py
