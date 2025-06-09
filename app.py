import streamlit as st
import pandas as pd
from geopy.distance import geodesic
import folium
from streamlit_folium import st_folium

# 데이터 불러오기
df = pd.read_csv("data/collection_boxes.csv")

# 스트림릿 UI
st.title("은평구 의류 수거함 위치 안내")
st.write("지도에서 수거함 위치를 확인하고, 가까운 수거함을 찾아보세요.")

# 지도 생성
map_center = [df['위도'].mean(), df['경도'].mean()]
m = folium.Map(location=map_center, zoom_start=13)

# 마커 표시
for idx, row in df.iterrows():
    folium.Marker(
        [row["위도"], row["경도"]],
        popup=row["설치장소"]
    ).add_to(m)

# 사용자 위치 입력
st.subheader("내 위치에서 가까운 수거함 찾기")
user_lat = st.number_input("위도 입력", format="%.6f")
user_lon = st.number_input("경도 입력", format="%.6f")

if user_lat and user_lon:
    user_location = (user_lat, user_lon)

    # 거리 계산
    df["거리"] = df.apply(lambda row: geodesic(user_location, (row["위도"], row["경도"])).meters, axis=1)
    nearest = df.loc[df["거리"].idxmin()]

    st.success(f"가장 가까운 수거함: {nearest['설치장소']} ({nearest['거리']:.1f} m)")

    # 가까운 수거함 마커 강조
    folium.Marker(
        [nearest["위도"], nearest["경도"]],
        popup="가장 가까운 수거함",
        icon=folium.Icon(color="red")
    ).add_to(m)

# 지도 렌더링
st_data = st_folium(m, width=700, height=500)
