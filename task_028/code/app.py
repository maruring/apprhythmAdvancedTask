import requests
import streamlit as st
import pandas as pd

st.title('先端課題028_APIを使ってみる Level2')
url = 'https://archive-api.open-meteo.com/v1/archive'
start_date = '2023-02-01'
end_date = '2023-02-14'

tokyo = {'latitude': 35.683, 'longitude': 139.767,
        'start_date': start_date, 'end_date': end_date,
        'hourly': 'temperature_2m'}
paris = {'latitude': 48.864716, 'longitude': 2.349014,
        'start_date': start_date, 'end_date': end_date,
        'hourly': 'temperature_2m'}

new_york = {'latitude': 40.730610, 'longitude': -73.935242,
            'start_date': start_date, 'end_date': end_date,
            'hourly': 'temperature_2m'}

def get_data(url, params):
    r = requests.get(url=url, params=params)
    return r

def create_chart_data(data_dict):
    dst_df = pd.DataFrame()
    for key, data in data_dict.items():
        sub_df = pd.DataFrame()
        dates = data['hourly']['time']
        temps = data['hourly']['temperature_2m']
        for date, temp in zip(dates, temps):
            sub_df = sub_df.append({'date': date, key: temp},
                                    ignore_index=True)
        sub_df["date"] = pd.to_datetime(sub_df["date"])
        sub_df = sub_df.set_index("date")
        dst_df = pd.concat([dst_df, sub_df], axis=1)
    
    return dst_df

if st.button(label='実行'):
    data_dict = {}
    for target in ['tokyo', 'paris', 'new_york']:
        if target == 'tokyo':
            params = tokyo
        elif target == 'paris':
            params = paris
        elif target == 'new_york':
            params = new_york
        response = get_data(url, params)
        data = response.json()
        data_dict[target] = data
    chart_data = create_chart_data(data_dict)
    st.line_chart(chart_data)
    st.balloons()
else:
    pass