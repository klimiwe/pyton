from logger import *
import user_view
from calc_rational import *
from calc_complex import calc_c
def calculate():
    print('Введите выражение для вычисления рациональных и комплексных чисел')
    print('В случае комплексных чисел используйте "j" как мнимую единицу')
    try:
        stroka = user_view.get_string()
        if 'j' in stroka:
            result = calc_c(stroka)
        else:
            result = so_skobkami(stroka)
        user_view.result_view(result, stroka)
        log_true(stroka, result)
    except: 
        user_view.error()
        log_error(stroka)

calculate()