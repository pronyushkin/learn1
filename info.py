
def test_info() :
	user_info = { 'first_name':'fn','last_name':'ln'}
	print(user_info['first_name'], user_info['last_name'])
	print('словарь: ', user_info)
	user_info['first_name'] = input('введите имя: ') 
	user_info['last_name' ] = input('введите фамилию: ' )
	print('имя: ', user_info['first_name'])
	print('фамилия: ', user_info['last_name'])
	print('словарь: ', user_info)	

if __name__ == '__main__':
	test_info() 

