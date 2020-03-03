from trello import TrelloApi

api_key = '6bf3f33d3004f15142d5008a89947a9a'
token = '986d680c055595e6abef210b9330d33381cb966c3a0f67cfb7bd406f67fbd612'
trello = TrelloApi(api_key, token)
board_id = 'Kdtv941v'
dictionary = {}
column_dictionary = {}

def read_tasks():
    task_counter = 0
    for column in trello.boards.get_list(board_id):
        column_dictionary[column['name']] = column['id']
        if len(trello.lists.get_card(column['id'])) > 0:
            card_list = []
            for card in trello.lists.get_card(column['id']):
                task_counter += 1
                card_dict = {'id': task_counter, 'card_name':card['name'], 'card_id':card['id']}
                card_list.append(card_dict)
            dictionary[column['name']] = card_list
        else:
            dictionary[column['name']] = []
    for key in dictionary.keys():
        print('\n')
        print('"{}" - {} tasks now'.format(key, len(dictionary.get(key))))
        cycle_dict = dictionary.get(key)
        if len(dictionary.get(key)) == 0:
            print('\tNo tasks in this list!')
        else:
            for i in cycle_dict:
                print('\t{} - {}'.format(i['id'], i['card_name']))


def menu():
    read_tasks()
    print('What you want to do?')
    print('1 - create new list')
    print('2 - create new card')
    print('3 - move card')
    print('4 - delete card')
    print('5- Exit')
    choice_menu = int(input('Enter Your choice '))
    if choice_menu not in range (1,6):
        return menu()
    elif choice_menu == 1:
        new_list()
    elif choice_menu == 2:
        new_card()
    elif choice_menu == 3:
        move_card()
    elif choice_menu == 4:
        delete_card()
    elif choice_menu == 5:
        exit()

def new_list():
    name = input('Enter new list name - ')
    trello.boards.new_list(board_id, name, pos=99000)
    read_tasks()

def delete_card():
    read_tasks()
    card_id = int(input('Enter card number - '))
    for value in dictionary.values():
        if len(value) ==0:
            continue
        else:
            for i in value:
                if i['id'] ==card_id:
                    trello.cards.delete(i['card_id'])
    print('Done')
    read_tasks()


menu()

