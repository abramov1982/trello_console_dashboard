from trello import TrelloApi

api_key = '6bf3f33d3004f15142d5008a89947a9a'
token = '986d680c055595e6abef210b9330d33381cb966c3a0f67cfb7bd406f67fbd612'
trello = TrelloApi(api_key, token)
board_id = 'Kdtv941v'


def get_id(name):
    for column in trello.boards.get_list(board_id):
        if column['name'] == name:
            return column['id']

def new_card(text, column):
    return trello.cards.new(text, column)

need_todo_id = get_id('Нужно сделать')
in_process_id = get_id('В процессе')
ready_id = get_id('Готово')

for card in trello.lists.get_card(need_todo_id):
    print('Имя карточки - {}, id карты - {}'.format(card['name'], card['id']))