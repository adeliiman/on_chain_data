import streamlit as st
import requests
import datetime
import pandas as pd

st.header('Blockchain Data')

#api_key = st.sidebar.text_input('api_key','49d21f854775ce12342a69f13500413d767554972ca75cfd2cfb7b2baa7c1fb2')
api_key = '49d21f854775ce12342a69f13500413d767554972ca75cfd2cfb7b2baa7c1fb2'
days = st.sidebar.slider('days?', 30, 2000, 1000)
symbol_list = ['BTC', 'ETH', 'DASH', 'DOGE']
symbol = st.sidebar.selectbox('symbol', symbol_list)
url = 'https://min-api.cryptocompare.com/data/blockchain/histo/day?fsym={}&limit={}&api_key={}'.format(symbol, days, api_key)
#url = 'https://min-api.cryptocompare.com/data/blockchain/histo/day?fsym=ETH&toTs={}&api_key={}'.format(api_key,time)
@st.cache
def on_chain_function():
	resp = requests.get(url)
	data = resp.json()
	data = data['Data']['Data']

	time_list = []
	height_list = []
	zero_balance_addresses_all_time_list = []
	unique_addresses_all_time_list = []
	new_addresses_list = []
	active_addresses_list = []
	transaction_count_list = []
	transaction_count_all_time_list = []
	large_transaction_count_list = []
	average_transaction_value_list = []
	hashrate_list = []
	difficulty_list = []
	block_size_list = []
	current_supply_list = []
	block_time_list = []

	for d in data:
	    time_list.append(datetime.datetime.fromtimestamp(d['time']))
	    height_list.append(d['block_height'])
	    zero_balance_addresses_all_time_list.append(d['zero_balance_addresses_all_time'])
	    unique_addresses_all_time_list.append(d['unique_addresses_all_time'])
	    new_addresses_list.append(d['new_addresses'])
	    active_addresses_list.append(d['active_addresses'])
	    transaction_count_list.append(d['transaction_count'])
	    transaction_count_all_time_list.append(d['transaction_count_all_time'])
	    large_transaction_count_list.append(d['large_transaction_count'])
	    average_transaction_value_list.append(d['average_transaction_value'])
	    hashrate_list.append(d['hashrate'])
	    difficulty_list.append(d['difficulty'])
	    block_size_list.append(d['block_size'])
	    current_supply_list.append(d['current_supply'])
	    block_time_list.append(d['block_time'])
    
	dict = {'time': time_list, 'height': height_list, 'transaction_count': transaction_count_list, 
	       'transaction_count_all_time': transaction_count_all_time_list, 'difficulty': difficulty_list, 'block_size': block_size_list, 'hashrate': hashrate_list, 'large_transaction_count': large_transaction_count_list,
	       'average_transaction_value': average_transaction_value_list, 'zero_balance_addresses_all_time': zero_balance_addresses_all_time_list, 
	       'unique_addresses_all_time': unique_addresses_all_time_list, 'new_addresses_list': new_addresses_list, 
	       'active_addresses': active_addresses_list,    
	        'current_supply': current_supply_list,
	       'block_time': block_time_list}
	df = pd.DataFrame(dict)
	return df
	
show_data = st.checkbox('show data?')
save = st.sidebar.checkbox('save?')
path = st.sidebar.text_input('path ...', '{}'.format(symbol)+'{}.csv'.format(days))
if show_data:
	df = on_chain_function()
	st.dataframe(df)
	if save:	
		df.to_csv(str(path))
	
	

