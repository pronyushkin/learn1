import getans
from getans import get_ans

def cmd_help():
	print('доступные команды:')
	print('\tq - выход')
	print('\t1 - поиск имени в списке')
	print('\t2 - как дела')
	print('\t3 - бот')


def find_person( l, name ):
	while len(l):
		print('проверяем ', l[-1] )
		if l[-1] == name:
			print(name,' нашелся')
			return
		l.pop()
	print(name,' не найден')

def cmd_findname():
	l = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
	name = 'Валера'
	print( 'Ищем ',name ,' в списке:', l ) 
	find_person( l, name )

def ask_user():
	ans = ''
	try:
		while not ans == 'Хорошо':
			ans = input('Как дела? ')
		print('так держать')
	except KeyboardInterrupt:
		print('ну и ладно')

def cmd_bot():
	ans = ''
	while not ans == 'Пока!':
		ans = input('Как дела?')
		print(get_ans( ans ) )

def main():
	cmd_help()
	cmd = ''
	while not cmd == 'q':
		cmd = input('введите команду (q)')
		if cmd == '1':
			cmd_findname()			
		elif cmd == '2':
			ask_user()
		elif cmd == '3':
			cmd_bot()
		else :
			cmd_help()


if __name__ == '__main__':
    main() 
