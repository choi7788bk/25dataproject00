import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

# 1. 서울시 청소년 시설 데이터 예시 (CSV 대신 샘플 데이터 사용)
# 실제로는 서울열린데이터광장 등에서 가져온 데이터를 사용 가능
data = {
    '시설명': ['강남청소년수련관', '은평청소년문화의집', '송파청소년센터'],
    '위도': [37.5172, 37.6190, 37.5013],
    '경도': [127.0473, 126.9279, 127.1124]
}
df = pd.DataFrame(data)

# 2. Streamlit UI
st.title("서울시 청소년 시설 지도")
st.markdown("서울시 내 청소년 시설 위치를 지도에 표시합니다.")

# 3. Folium 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)  # 서울 중심 좌표

# 4. Marker 추가
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=row['시설명'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# 5. Folium 지도 출력
folium_static(m)
