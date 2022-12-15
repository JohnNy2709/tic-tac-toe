field = [
    [' ', 1, 2 , 3],
    [1, '-', '-', '-'],
    [2, '-', '-', '-'],
    [3, '-', '-', '-'],
]
def display_field():
    for row in field:
        print('\t', *row)
    print('\n')

def user_move(row_index, column_index, x_or_o):
    field[row_index][column_index] = x_or_o

def check_if_win():
    win = False
    #проверка, победил ли игрок после своего хода
    #победил, если 3 символа подряд в:
        # -строке
        # -стоблце
        # -диагонали
    matrix_to_check = [x[1:] for x in field[1:]]
    #проверям диагонали:
    if matrix_to_check[0][0] == matrix_to_check[1][1] and matrix_to_check[1][1] == matrix_to_check[2][2] and matrix_to_check[0][0] != '-':
        win = True
        return win
    if matrix_to_check[0][2] == matrix_to_check[1][1] and matrix_to_check[0][2] == matrix_to_check[2][0] and matrix_to_check[0][2] != '-':
        win = True
        return win
    #проверяем строки:
    for row in matrix_to_check:
        if row[0] == row[1] and row[0] == row[2] and row[0] != '-':
            win = True
            return win
    #проверяем столбцы:
    
    #Продолжить здесь
    
    print(matrix_to_check)
    return win

def print_hi_words():
    print('''
    Добро пожаловать в игру "Крестики-Нолики"!
    Первые начинают "Крестики".
    Ходы чередуются автоматически.
    Для того, чтобы сделать ход, поочередно введите номер строки и номер столбца
''')

def define_current_player(move):
    if move % 2 == 0: return 'o'
    else: return 'x'

def get_checked_user_input(player):
    def if_input_correct(text):
        correct = text.isdigit() and len(text) == 1
        if correct:
            num = int(text)
            if num in [1, 2, 3]: return True
        return False
    player = 'Крестики' if player == 'x' else 'Нолики'
    row_ind, col_ind = 0, 0
    #Выйдем из цикла тогда, когда получим корректный input, а также проверим, что такой ход возможен
    while True:
        row_ind = input(f'\tВведите номер строки, чтобы сделать ход ({player}):')
        correct = if_input_correct(row_ind)
        while not correct:
            row_ind = input(f'\tЧто-то пошло не так, введите только одну цифру от 1 до 3({player}):')
            correct = if_input_correct(row_ind)
            
        col_ind = input(f'\tВведите номер столбца, чтобы сделать ход ({player}):')
        correct = if_input_correct(col_ind)
        while not correct:
            col_ind = input(f'\tЧто-то пошло не так, введите только одну цифру от 1 до 3({player}):')
            correct = if_input_correct(col_ind)

        row_ind, col_ind = int(row_ind), int(col_ind)
        if field[row_ind][col_ind] == '-': break
        else:
            print('\t Такой ход сделать невозможно, клетка занята')
    return row_ind, col_ind

def make_move(row_num, col_num, x_or_o):
    field[row_num][col_num] = x_or_o



print_hi_words()
move_number = 0
win = False

while not win:
    move_number+=1

    display_field()
    player = define_current_player(move_number)
    row, col = get_checked_user_input(player)
    make_move(row, col, player)
    win = check_if_win()

display_field()
print(f'\'{player}\' выигрывают за {move_number} ходов!')
input('Нажмите Enter, чтобы выйти')