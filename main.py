import numpy as np
import matplotlib.pyplot as plt
import Excel_write as xls

"""
Requirements:
    Python libraries:
        - numpy
        - scipy
        - matplotlib
        - xlwt
"""

flag_view_in_details = 0            # Флаг подробного вывода данных на каждой итерации
flag_print_in_cmd = 0               # Флаг вывода результатов в командную строку
flag_write_txt_file = 1             # Флаг записи результатов в текстовый файл
flag_write_excel_file = 1           # Флаг записи результатов в Excel файл
flag_auto_save_png = 1              # Флаг автоматического сохранения графиков в .png
flag_show_graphics = 0              # Флаг вывода графиков на экран при работе программы
flag_write_log_lite = 1             # Флаг записи данных из команднй строки в файл

_your_rocket_name = 'Тополь-М'      # Название вашей ракеты

# _your_rocket_name = 'Minuteman-3'  # Название вашей ракеты

if flag_write_excel_file == 1:
    excel_file = xls.Excel_file(_your_rocket_name)  # Экземпляр класса файл Excel
    excel_file.open_excel()     # Создаем Excel файл

if flag_write_txt_file == 1:
    # Первоначальная запись текста в файл
    filename = 'results.txt'
    file = open(filename, 'w')
    _start_message = 'Start flight:\n'
    file.write(_start_message)

if flag_write_log_lite == 1:
    filename_light_log = 'Краткая сводка из командной строки'
    file_log_lite = open(filename_light_log + '.txt', 'w')

"""Вводимые данные по каждой ракете

km_to_m - перевод из километров в метры
t_to_kg - перевод из тонн в килограммы

rocket_len  - Длина ракеты [м]
rocket_max_diameter  - Максимальный диаметр ракеты [м]

rocket_len_1_stage  - Длина 1 ступени ракеты [м]	!!!
rocket_len_2_stage  - Длина 2 ступени ракеты [м]	!!!
rocket_len_3_stage  - Длина 3 ступени ракеты [м]	!!!

rocket_diameter_1_stage  - Диаметр 1 ступени ракеты [м]	!!!
rocket_diameter_2_stage  - Диаметр 2 ступени ракеты [м]	!!!
rocket_diameter_3_stage  - Диаметр 3 ступени ракеты [м]	!!!

rocket_m_start_with_fuel  - Стартовая масса ракеты с топливом [т]

rocket_m_1_stage_with_fuel  - Масса 1 ступени  ракеты с топливом [т]	!!!
rocket_m_2_stage_with_fuel  - Масса 2 ступени  ракеты с топливом [т]	!!!
rocket_m_3_stage_with_fuel  - Масса 3 ступени  ракеты с топливом [т]	!!!

rocket_m_1_stage_dry  - Сухая масса 1 ступени ракеты [т]	!!!
rocket_m_2_stage_dry  - Сухая масса 2 ступени ракеты [т]	!!!
rocket_m_3_stage_dry  - Сухая масса 3 ступени ракеты [т]	!!!

rocket_m_head_part  - Масса ГЧ ракеты [т]	!!!
rocket_m_cargo_max  - Максимальная забрасываемая масса ракеты [т]	!!!

rocket_distance_max  - Максимальная дистанция ракеты [м]
rocket_stages  - Количество ступеней ракеты [шт]	!!!
rocket_circular_probable_deviation  - КВО (Круговое вероятное отклонение) ракеты [м]
rocket_jet_diameter  - Диаметр сечения сопла ракеты [м]	!!!

rocket_P_vacuum_1_stage  - Пустотная тяга 1 ступени  ракеты [Н]	!!!
rocket_P_vacuum_2_stage  - Пустотная тяга 2 ступени  ракеты [Н]	!!!
rocket_P_vacuum_3_stage  - Пустотная тяга 3 ступени  ракеты [Н]	!!!

rocket_P_earth_1_stage  - Земная тяга 1 ступени  ракеты [Н]	!!!
rocket_P_earth_2_stage  - Земная тяга 2 ступени  ракеты [Н]	!!!
rocket_P_earth_3_stage  - Земная тяга 3 ступени  ракеты [Н]	!!!

rocket_T_1_stage  - Время работы 1 ступени ракеты [сек]	!!!
rocket_T_2_stage  - Время работы 2 ступени ракеты [сек]	!!!
rocket_T_3_stage  - Время работы 3 ступени ракеты [сек]	!!!
"""

# Me
km_to_m = 1000
t_to_Newton = 8896.444

rocket_len = 22.7
rocket_max_diameter = 1.81

rocket_m_cargo_max = 1.2


rocket_len_1_stage = 8.04
rocket_len_2_stage = 6
rocket_len_3_stage = 3.1
rocket_len_stages_arr = [rocket_len_1_stage, rocket_len_2_stage, rocket_len_3_stage]

rocket_diameter_1_stage = 1.81
rocket_diameter_2_stage = 1.61
rocket_diameter_3_stage = 1.58
rocket_diameter_stages_arr = [rocket_diameter_1_stage, rocket_diameter_2_stage, rocket_diameter_3_stage]

rocket_m_start_with_fuel = 47.1

rocket_m_3_stage_with_fuel = 6 + rocket_m_cargo_max
rocket_m_2_stage_with_fuel = 13
rocket_m_1_stage_with_fuel = 28.6

rocket_m_stages_with_fuel_arr = [rocket_m_1_stage_with_fuel, rocket_m_2_stage_with_fuel, rocket_m_3_stage_with_fuel]

rocket_m_3_stage_dry = 1.2
rocket_m_2_stage_dry = 1.5
rocket_m_1_stage_dry = 3

rocket_m_stages_dry_arr = [rocket_m_1_stage_dry + rocket_m_2_stage_dry + rocket_m_3_stage_dry + rocket_m_cargo_max,
            rocket_m_2_stage_dry + rocket_m_3_stage_dry + rocket_m_cargo_max, rocket_m_3_stage_dry + rocket_m_cargo_max]

rocket_m_head_part = 1.2

rocket_distance_max = 11000 * km_to_m
rocket_stages = 3

rocket_circular_probable_deviation = 200

rocket_jet_diameter = 0.76

rocket_P_vacuum_1_stage = 100 * t_to_Newton
rocket_P_vacuum_2_stage = 50 * t_to_Newton
rocket_P_vacuum_3_stage = 25 * t_to_Newton
rocket_P_vacuum_stages_arr = [rocket_P_vacuum_1_stage, rocket_P_vacuum_2_stage, rocket_P_vacuum_3_stage]

rocket_P_earth_1_stage = 92.4 * t_to_Newton
rocket_P_earth_2_stage = 0 * t_to_Newton
rocket_P_earth_3_stage = 0 * t_to_Newton
rocket_P_earth_stages_arr = [rocket_P_earth_1_stage, rocket_P_earth_2_stage, rocket_P_earth_3_stage]

rocket_T_1_stage = 60
rocket_T_2_stage = 64
rocket_T_3_stage = 56
rocket_T_stages_arr = [rocket_T_1_stage, rocket_T_2_stage + rocket_T_1_stage, rocket_T_3_stage + rocket_T_2_stage + rocket_T_1_stage]

rocket_T_stages_arr_for_m = [rocket_T_1_stage, rocket_T_2_stage, rocket_T_3_stage]
rocket_m_stages_dry_arr_m = [rocket_m_1_stage_dry, rocket_m_2_stage_dry, rocket_m_3_stage_dry + rocket_m_cargo_max]

# константы общие
Radius_earth = 6371000                          # Радиус Земли                                  - м
W_earth = 7.29 * pow(10, -5)                    # Угловая скорость вращения земли               - 1/с
Mu = 3986e11                                    # Гравитационный параметр земли (гравитационная постоянная)
g0 = 9.80665                                    # Ускорение свободного падения                  - м/с^2
P_on_earth = 101325                             # Давление окружающей среды на уровне моря      - Па
m_useful_cargo = rocket_m_cargo_max             # Масса полезного груза                         - кг


# константы ракеты
stage_numbers = rocket_stages                       # Число ступеней - шт
length_rocket = rocket_len                          # Длина ракеты  -м
diameter_max_rocket = rocket_diameter_stages_arr    # Максимальный диаметр РН - м

m_stage_start = rocket_m_stages_with_fuel_arr   # Стартовая масса ракетного блока ступени - т  [1 ст, 2 ст, 3 ст]
m_stage_dry = rocket_m_stages_dry_arr           # Сухая масса ракетного блока ступени - т
P_stage_earth = rocket_P_earth_stages_arr       # Тяга двигателя на уровне моря - кН
P_stage_vacuum = rocket_P_vacuum_stages_arr     # Тяга двигателя в вакууме - кН

time_work_max_stage = rocket_T_stages_arr       # Время работы двигателей - с

C_x_0 = 0.2
C_x = C_x_0
C_ya = 0.5 * length_rocket / diameter_max_rocket[0]


# Ход изменения массы
def m_per_sec(m_start, m_dry, work_time):
    """
    Функция считает расход массы топлива на секунду

    Вход:
            m_start         - Стартовая масса с топливом
            m_dry            - Сухая масса конструкции
            work_time       - Время работы ступени
    Выход:
            fuel_per_sec    - Расход массы за одну секунду
    """
    fuel_per_sec = (m_start - m_dry) / work_time
    # print(f'fuel_per_sec {fuel_per_sec} = (m_start {m_start} - m_dry {m_dry} ) / work_time {work_time}')
    return fuel_per_sec


# Значение модуля радиус вектора от центра СК до РН
def v_full(local_x, local_y):
    """
    Расчет итогового радиуса с учетом координат по осям X и Y

    Вход:
            local_x - координата по X
            local_y - координата по Y
    Выход:
            abs_r   - Итоговый радиус-вектор
    """
    local_abs_r = np.sqrt(pow(local_x, 2) + pow(local_y, 2))
    return local_abs_r


# Значение ускорения свободного падения в данной точки
def g_current_count(local_r):
    """
    Пересчет g (ускорение свободного падения) на каждом новом шаге

    Вход:
            local_r - Текущий радиус
    Выход:
            g_new   - Итоговый радиус-вектор
    """
    g_new = Mu / pow(local_r, 2)
    return g_new


# Значение плотности
def ro_current_count(local_h):
    """
    Пересчет ro (плотности) на каждом новом шаге

        Вход:
                local_h - Текущая высота
        Выход:
                ro_new  - Новое значение плотности
        """
    ro_new = 1.225 * pow(np.e, (-local_h / 7700))
    return ro_new


# Функция с методом Эйлера
def Eiler_func(local_f0, local_f1, local_f2, local_dt):
    """
    Функция производит расчет по методу Эйлера

        Вход:
                local_f0 - текущее значение
                local_f1 - Первая производная
                local_f2 - Вторая производная
                local_dt - шаг
        Выход:
                local_f  - итоговое значение
        """
    local_f = local_f0 + local_f1 * local_dt + local_f2 * pow(local_dt, 2) / 2
    return local_f


# Данные для хранения итоговых результатов
arr_out_abs_r, arr_out_abs_V = [], []
arr_out_X_N, arr_out_Y_N, arr_out_P_N = [], [], []
arr_out_x, arr_out_y = [], []
arr_out_V_x, arr_out_V_y, arr_out_abs_Va = [], [], []
arr_out_a_x, arr_out_a_y = [], []
arr_out_theta, arr_out_phi, arr_out_alpha = [], [], []
arr_out_pitch, arr_out_pitch_a = [], []
arr_out_t_current, arr_out_dt, arr_out_all_flight_time = [], [], []
arr_out_m, arr_out_dm = [], []
arr_out_h = []
arr_out_p_h = []
arr_out_g = []
arr_out_W = []
arr_out_ro = []
arr_out_q = []
arr_out_scatter_mark_stage = []     # Отметка времени(номер итерации), когда произошло отделение ступени
arr_out_THETA_EARTH = []


# String lite out
def slo(data):
    """
    Функция обертка для округления до "num_o" знака после запятой
    """
    num_o = 5
    answer = str(data.__round__(num_o))
    return answer


def str_out(data):
    """
    Функция обертка для отступов между столбиками и округления до "num_o" знака после запятой
    """
    num_o = 5
    _max_len_for_column = 15    # Максимальная ширина столбца в символах
    # Если столбики плывут, поставить значение больше
    answer = str(data.__round__(num_o)).ljust(_max_len_for_column, ' ')
    return answer


def clear_arr():
    pass


def save_data_arr():
    """
    Сохраняем значения на каждм шагу в массив
    """
    global k, arr_out_t_current, arr_out_m, arr_out_h, arr_out_abs_r, arr_out_abs_V, arr_out_g, arr_out_X_N, \
        arr_out_Y_N, arr_out_P_N, arr_out_x, arr_out_y, arr_out_V_x, arr_out_V_y, arr_out_a_x, arr_out_a_y, \
        arr_out_abs_Va, arr_out_theta, arr_out_dm, arr_out_dt, arr_out_pitch, arr_out_pitch_a, arr_out_p_h, arr_out_W, \
        arr_out_ro, arr_out_q, arr_out_phi, arr_out_alpha

    arr_out_t_current.append(t_current)
    arr_out_dt.append(dt)

    arr_out_m.append(m)
    arr_out_dm.append(dm)

    arr_out_g.append(g)
    arr_out_h.append(h)
    arr_out_abs_r.append(abs_r)

    arr_out_abs_V.append(abs_V)
    arr_out_abs_Va.append(abs_Va)

    arr_out_theta.append(theta)
    arr_out_phi.append(phi)
    arr_out_alpha.append(alpha)

    arr_out_V_x.append(V_x)
    arr_out_V_y.append(V_y)
    arr_out_a_x.append(a_x)
    arr_out_a_y.append(a_y)

    arr_out_x.append(x)
    arr_out_y.append(y)

    arr_out_X_N.append(X_N)
    arr_out_Y_N.append(Y_N)
    arr_out_P_N.append(P_N)

    arr_out_pitch.append(pitch)
    arr_out_pitch_a.append(pitch_a)
    arr_out_W.append(W)
    arr_out_p_h.append(p_h)
    arr_out_ro.append(ro)
    arr_out_q.append(q)

    arr_out_THETA_EARTH.append(THETA_EARTH)


def pop_data_arr():
    """
    Сохраняем значения на каждм шагу в массив
    """
    global k, arr_out_t_current, arr_out_m, arr_out_h, arr_out_abs_r, arr_out_abs_V, arr_out_g, arr_out_X_N, \
        arr_out_Y_N, arr_out_P_N, arr_out_x, arr_out_y, arr_out_V_x, arr_out_V_y, arr_out_a_x, arr_out_a_y, \
        arr_out_abs_Va, arr_out_theta, arr_out_dm, arr_out_dt, arr_out_pitch, arr_out_pitch_a, arr_out_p_h, arr_out_W, \
        arr_out_ro, arr_out_q, arr_out_phi, arr_out_alpha

    arr_all = arr_out_t_current, arr_out_m, arr_out_h, arr_out_abs_r, arr_out_abs_V, arr_out_g, arr_out_X_N, \
        arr_out_Y_N, arr_out_P_N, arr_out_x, arr_out_y, arr_out_V_x, arr_out_V_y, arr_out_a_x, arr_out_a_y, \
        arr_out_abs_Va, arr_out_theta, arr_out_dm, arr_out_dt, arr_out_pitch, arr_out_pitch_a, arr_out_p_h, arr_out_W, \
        arr_out_ro, arr_out_q, arr_out_phi, arr_out_alpha

    for arr in arr_all:
        arr.pop()


def print_info(start_msg='', n=0):
    """
        Вывод параметров на экран

            start_msg - Возможно добавить стртовое сообщение
            n         - Номер ступени
    """
    local_dict_out = {
        't': f'{str_out(t_current)}',
        'dt': f'{str_out(dt)}',
        'm_current': f'{str_out(m)}',
        'dm': f'{str_out(dm)}',
        'theta': f'{str_out(theta)}',
        'g': f'{str_out(g)}',
        'h': f'{str_out(h)}',
        'r': f'{str_out(abs_r)}',
        'V': f'{str_out(abs_V)}',
        'Va': f'{str_out(abs_Va)}',
        'V_x': f'{str_out(V_x)}',
        'V_y': f'{str_out(V_y)}',
        'a_x': f'{str_out(a_x)}',
        'a_y': f'{str_out(a_y)}',
        'x': f'{str_out(x)}',
        'y': f'{str_out(y)}',
        'phi': f'{str_out(phi)}',
        'alpha': f'{str_out(alpha)}',
        'X_N': f'{str_out(X_N)}',
        'Y_N': f'{str_out(Y_N)}',
        'P_N': f'{str_out(P_N)}',
        'pitch': f'{str_out(pitch)}',
        'pitch_a': f'{str_out(pitch_a)}',
        'W': f'{str_out(W)}',
        'p_h': f'{str_out(p_h)}',
        'ro': f'{str_out(ro)}',
        'q': f'{str_out(q)}',
        'theta_earth': f'{str_out(THETA_EARTH)}'
    }
    answer_arr = [f'  {i}= {local_dict_out.get(i)}' for i in local_dict_out.keys()]
    answer = f"{start_msg}" + ''.join(answer_arr)
    if flag_print_in_cmd == 1:
        print(answer)
    if flag_write_txt_file == 1:
        file.write(answer + '\n')
    if flag_write_excel_file == 1:
       excel_file.write_data(local_dict_out, n)


def view_in_details(string='', end_iter=0):
    """
        Подробный вывод данных на каждом шаге
    """
    global flag_view_in_details
    if flag_view_in_details == 1:
        print(string)
        if end_iter == 1:
            print('-' * 200)
        elif end_iter == -1:
            input('\nНажмите ENTER чтобы перейти к следующей итерации\n')


def init_start_values():
    # Начальные условия при t = 0
    local_latitude_start = np.deg2rad(np.pi / 2)    # Широта старта (0, старт с экватора)   - рад
    local_longitude_start = np.deg2rad(np.pi / 2)   # Долгота старта (0, старт с экватора)  - рад

    # Начальные условия для инерциальной системы координат, где Y - направленна от центра Земли к точки пересечения
    # плоскости экватара и широты стартовго комплекса
    local_x_0 = 0.01            # - м
    local_y_0 = Radius_earth    # Координата Y в описанной СК   - м

    local_W_0 = W_earth * Radius_earth

    local_V_x_0 = W_earth*Radius_earth             # Скорости в момент времени t=0 - м/с
    local_V_y_0 = 0             # Скорости в момент времени t=0 - м/с
    local_V_ax_0 = local_W_0    # Скорости в момент времени t=0 - м/с
    local_V_ay_0 = 0            # Скорости в момент времени t=0 - м/с
    local_a_x_0 = 0             # Ускорения в момент времени t=0 - м/с^2
    local_a_y_0 = 0             # Ускорения в момент времени t=0 - м/с^2
    local_h = 0                 # Высота относительно метсного горизонта - м

    local_theta_0 = 0       # Значение угла в момент времени t=0 - рад      pi/2    - рад
    local_pitch_0 = np.pi / 2       # Значение тангжа       pi/2    - рад
    local_pitch_a_0 = np.pi / 2     # Значение тангжа A     pi/2    - рад
    local_phi_0 = 0                 # - рад
    return local_x_0, local_y_0, local_V_x_0, local_V_y_0, local_V_ax_0, local_V_ay_0, local_a_x_0, local_a_y_0, \
           local_W_0, local_theta_0, local_phi_0, local_pitch_0, local_pitch_a_0, local_h, \
           local_latitude_start, local_longitude_start


# Пишем стартовые параметры в стартовые глобальные переменные
x_0, y_0, V_x_0, V_y_0, V_ax_0, V_ay_0, a_x_0, a_y_0, W_0, \
theta_0, phi_0, pitch_0, pitch_a_0, h_0, latitude_start, longitude_start = init_start_values()

# MAIN функция
# Текущее значении координат, скоростей и ускорений объекта
#       c - стартовая СК

"""
x       - Координата X      - м
y       - Координата Y      - м
V_x     - Скорость          - м/с
V_y     - Скорость          - м/с
V_ax    - Скорость          - м/с
V_ay    - Скорость          - м/с
a_x     - Ускорение         - м/с^2
a_y     - Ускорение         - м/с^2
W       - Скорость ветра    - м/с

theta   - Угол траектории   - рад
phi     - Угол              - рад
pitch   - Значение тангжа   - рад
pitch_a - Значение тангжа A - рад

m = 0       - Полная масса блоков РН    - т
Sm          - Площадь сечения РН        - м^2
t_current   - Время работы              - с
dt          - Шаг изменения времени     - с
dm          - Шаг изменения массы       - т/c

alpha           -                       - рад
sin_alpha       -                       - рад    

sin_pitch_phi   -                       - рад        
cos_pitch_phi   -                       - рад        

sin_pitch_a_phi -                       - рад        
cos_pitch_a_phi -                       - рад        

sin_phi         -                       - рад
cos_phi         -                       - рад

abs_r       - Радиус полный             - м
abs_V       - Скорость полная           - м/с
abs_Va      - Скорость А полная         - м/с

P_N         - Тяга                      - 
X_N         -                           - 
Y_N         -                           - 

Cx          -                           - 
Cy          -                           - 

ro          - Плотность атмосферы       - 
p_h         - Давление на высоте        - 
q           - Воздушны   поток          - 
g           - Ускорение на земле        - м/с^2

n           - Текущая ступень           - 

Sc          - Площадь сечения сопла ДУ  - м^2
"""


def restart_values_to_start():
    global x, y, V_x, V_y, V_ax, V_ay, a_x, a_y, W, theta, phi, pitch, pitch_a, h, latitude, longitude, t_current,\
           t_stage_already_fly, Sm, i, count, num, k, dm, flag_integrate_step, sin_pitch_phi, cos_pitch_phi,\
           sin_pitch_a_phi, cos_pitch_a_phi, sin_alpha, alpha, sin_phi, cos_phi, abs_r, abs_V, abs_Va,X_N, \
           Y_N, P_N, Cx, Cy, ro, p_h, g, q, local_additional_len, THETA_EARTH
    # Пишем стартовые параметры в общие глобальные переменные
    x, y, V_x, V_y, V_ax, V_ay, a_x, a_y, W, theta, phi, pitch, pitch_a, h, latitude, longitude = init_start_values()
    t_current = 0  # Стартовое время равно нулю
    t_stage_already_fly = 0  # Время, которое ракета уже пролетела
    Sm = np.pi / 4 * pow(diameter_max_rocket[0], 2)  # Площадь сечения РН    - м^2

    i, count, num = 0, 0, 0  # Интерация цикла
    k = 0  # Счеткик
    dm = None  # Шаг изменения массы - т/c
    flag_integrate_step = False  # Флаг одноразового разрещение смены шага интегрирования

    # Переменные углов
    sin_pitch_phi, cos_pitch_phi = None, None
    sin_pitch_a_phi, cos_pitch_a_phi = None, None
    sin_alpha, alpha = None, None
    sin_phi, cos_phi = None, None

    # Модули радиус-вектора и скорости
    abs_r = None
    abs_V = None
    abs_Va = None

    # Силы воздействующие на объект
    X_N, Y_N, P_N = None, None, None
    Cx, Cy = None, None

    # Иные переменные
    ro = None
    p_h = None
    q = None
    g = None

    local_additional_len = 0  # Объявление и инициализация переменной добавочного общего времени

    THETA_EARTH = 0
    # k = 0


flag_k1, flag_k2, flag_k3 = False, False, False

# my 1 var
"""
1:
theta normal = 0.5398 rad  ~ 30.9307°
theta earth= 0.7843 rad  ~ 44.937°
phi= 0.0063 rad  ~ 0.3635°
h= 18139.0698 m  ~ 18.1391 км
pitch = 0.7898 rad  ~ 45.25°
alpha = 0.0005 rad  ~ 0.0288°

2:
theta normal = 0.3352 rad  ~ 19.2045°
theta earth= 0.396 rad  ~ 22.6874°
phi= 0.0252 rad  ~ 1.4433°
h= 78067.197 m  ~ 78.0672 км
pitch = 0.3553 rad  ~ 20.3547°
alpha = -0.0624 rad  ~ -3.5754°

3:
theta normal = 0.0926 rad  ~ 5.306°
theta earth= 0.1061 rad  ~ 6.0805°
phi= 0.0601 rad  ~ 3.4458°
h= 147189.9497 m  ~ 147.1899 км
pitch = 0.0082 rad  ~ 0.4675°
alpha = -0.1534 rad  ~ -8.7864°
"""
# k_1 = 0.5
# k_2 = 360
# k_3 = 0.006

# ----------------------------------------
"""
1:
theta normal = 0.7903 rad  ~ 45.2794°
theta earth= 1.1505 rad  ~ 65.9189°
phi= 0.0054 rad  ~ 0.309°
h= 20395.73 m  ~ 20.3957 км
pitch = 1.1531 rad  ~ 66.0681°
alpha = -0.0022 rad  ~ -0.1234°

2:
theta normal = 0.758 rad  ~ 43.4288°
theta earth= 0.8911 rad  ~ 51.0556°
phi= 0.0182 rad  ~ 1.0439°
h= 105939.4608 m  ~ 105.9395 км
pitch = 0.8712 rad  ~ 49.9147°
alpha = -0.0363 rad  ~ -2.081°

3:
theta normal = 0.6274 rad  ~ 35.9494°
theta earth= 0.6883 rad  ~ 39.4391°
phi= 0.0419 rad  ~ 2.4006°
h= 250726.8794 m  ~ 250.7269 км
pitch = 0.6411 rad  ~ 36.7338°
alpha = -0.0864 rad  ~ -4.9481°
"""
# k_1 = 0.22
# k_2 = 360
# k_3 = 0.004

# ----------------------------------------
"""
1:
theta normal = 0.6853 rad  ~ 39.2653°
theta earth= 0.9997 rad  ~ 57.281°
phi= 0.0058 rad  ~ 0.3301°
h= 19657.433 m  ~ 19.6574 км
pitch = 0.9987 rad  ~ 57.2237°
alpha = -0.0059 rad  ~ -0.3357°

2:
theta normal = 0.5561 rad  ~ 31.8633°
theta earth= 0.6562 rad  ~ 37.5965°
phi= 0.0213 rad  ~ 1.223°
h= 95270.8428 m  ~ 95.2708 км
pitch = 0.6113 rad  ~ 35.0227°
alpha = -0.0636 rad  ~ -3.6465°

3:
theta normal = 0.351 rad  ~ 20.1086°
theta earth= 0.3879 rad  ~ 22.2237°
phi= 0.0509 rad  ~ 2.9183°
h= 206638.9304 m  ~ 206.6389 км
pitch = 0.295 rad  ~ 16.9007°
alpha = -0.1399 rad  ~ -8.0179°

"""

# k_1 = 0.3
# k_2 = 360
# k_3 = 0.0055

# ----------------------------------------
"""
1:
theta normal = 0.6606 rad  ~ 37.8482°
theta earth= 0.9652 rad  ~ 55.3018°
phi= 0.0058 rad  ~ 0.3332°
h= 19379.764 m  ~ 19.3798 км
pitch = 0.9686 rad  ~ 55.4991°
alpha = -0.0014 rad  ~ -0.0786°

2:
theta normal = 0.5663 rad  ~ 32.4449°
theta earth= 0.6675 rad  ~ 38.2444°
phi= 0.0216 rad  ~ 1.2392°
h= 94328.7367 m  ~ 94.3287 км
pitch = 0.6922 rad  ~ 39.6614°
alpha = 0.0059 rad  ~ 0.3361°

3:
theta normal = 0.4376 rad  ~ 25.0717°
theta earth= 0.4817 rad  ~ 27.5997°
phi= 0.0504 rad  ~ 2.8896°
h= 214596.3361 m  ~ 214.5963 км
pitch = 0.5058 rad  ~ 28.979°
alpha = -0.0225 rad  ~ -1.2885°

"""

# k_1 = 0.55
# k_2 = 760
# k_3 = 0.003

# ----------------------------------------
"""
1:
theta normal = 0.5972 rad  ~ 34.2178°
theta earth= 0.8628 rad  ~ 49.4372°
phi= 0.0063 rad  ~ 0.3626°
h= 18667.9296 m  ~ 18.6679 км
pitch = 0.9065 rad  ~ 51.9407°
alpha = 0.0389 rad  ~ 2.23°

2:
theta normal = 0.5504 rad  ~ 31.538°
theta earth= 0.6468 rad  ~ 37.057°
phi= 0.0232 rad  ~ 1.3285°
h= 92845.3789 m  ~ 92.8454 км
pitch = 0.739 rad  ~ 42.343°
alpha = 0.0721 rad  ~ 4.1335°

3:
theta normal = 0.4726 rad  ~ 27.0787°
theta earth= 0.5191 rad  ~ 29.7447°
phi= 0.0523 rad  ~ 2.9945°
h= 217681.8042 m  ~ 217.6818 км
pitch = 0.6196 rad  ~ 35.5007°
alpha = 0.0522 rad  ~ 2.9912°

"""

# k_1 = 0.5
# k_2 = 300
# k_3 = 0.002

# ----------------------------------------
"""
1:
theta normal = 0.5972 rad  ~ 34.2178°
theta earth= 0.8628 rad  ~ 49.4372°
phi= 0.0063 rad  ~ 0.3626°
h= 18667.9296 m  ~ 18.6679 км
pitch = 0.9065 rad  ~ 51.9407°
alpha = 0.0389 rad  ~ 2.23°

2:
theta normal = 0.5504 rad  ~ 31.538°
theta earth= 0.6468 rad  ~ 37.057°
phi= 0.0232 rad  ~ 1.3285°
h= 92845.3789 m  ~ 92.8454 км
pitch = 0.739 rad  ~ 42.343°
alpha = 0.0721 rad  ~ 4.1335°

3:
theta normal = 0.4726 rad  ~ 27.0787°
theta earth= 0.5191 rad  ~ 29.7447°
phi= 0.0523 rad  ~ 2.9945°
h= 217681.8042 m  ~ 217.6818 км
pitch = 0.6196 rad  ~ 35.5007°
alpha = 0.0522 rad  ~ 2.9912°

"""

k_1 = 0.5
k_2 = 300
k_3 = 0.002

# ----------------------------------------


def check_K_values():
    global k_1, k_2, k_3, flag_k1, flag_k2, flag_k3
    if flag_k2 is False:
        flag_k2 = np.abs(alpha) < 0.05
    elif flag_k1 is False:
        flag_k1 = np.abs(alpha) < 0.1
    elif flag_k3 is False:
        flag_k3 = np.abs(alpha) < 0.003


def check_K_flags():
    global flag_k1, flag_k2, flag_k3, k_1, k_2, k_3
    # Если все коэффициенты К подобраны, то выдаем разрешение на запись данных в массивы
    if (flag_k1 and flag_k2 and flag_k3) is True:
        flag_k1, flag_k2, flag_k3 = True, True, True
        return True
    else:
        # Если не все К подобраны, то доподбираем оставшиеся
        check_K_values()
        if flag_k2 is False:    # Если К_2 не подорбран, ищем его
            k_2 += 0.01
            return False
        else:
            flag_k2 = True
        if flag_k1 is False:    # Если К_1 не подорбран, ищем его
            k_1 += 0.01
            return False
        else:
            flag_k1 = True
        if flag_k3 is False:    # Если К_3 не подорбран, ищем его
            k_3 += 0.01
            return False
        else:
            flag_k3 = True


# Пишем стартовые параметры в общие глобальные переменные
x, y, V_x, V_y, V_ax, V_ay, a_x, a_y, W, theta, phi, pitch, pitch_a, h, latitude, longitude = init_start_values()
t_current = 0               # Стартовое время равно нулю
t_stage_already_fly = 0     # Время, которое ракета уже пролетела
Sm = np.pi / 4 * pow(diameter_max_rocket[0], 2)    # Площадь сечения РН    - м^2

i, count, num = 0, 0, 0             # Интерация цикла
k = 0                               # Счеткик
dm = None                           # Шаг изменения массы - т/c
flag_integrate_step = False         # Флаг одноразового разрещение смены шага интегрирования

# Переменные углов
sin_pitch_phi, cos_pitch_phi = None, None
sin_pitch_a_phi, cos_pitch_a_phi = None, None
sin_alpha, alpha = None, None
sin_phi, cos_phi = None, None

# Модули радиус-вектора и скорости
abs_r = None
abs_V = None
abs_Va = None

# Силы воздействующие на объект
X_N, Y_N, P_N = None, None, None
Cx, Cy = None, None

# Иные переменные
ro = None
p_h = None
q = None
g = None

local_additional_len = 0        # Объявление и инициализация переменной добавочного общего времени

THETA_EARTH = 0

try_number = 0  # Номер попытки


def print_str_msg(try_num_in, result_in, n_in):
    if result_in is True:
        _Stage_message = f'\n\nВыполняется прогон ступени № {n_in + 1}:\n'
        if flag_write_log_lite == 1:
            file_log_lite.write(_Stage_message)
        file.write(_Stage_message)
    else:
        _Stage_message = f'\n\nВыполняется прогон № {try_num_in} ступени № {n_in + 1}:\n'
    print(_Stage_message)


def get_stage_m(n_now_in):
    global m
    arr_m_data = np.array([m_stage_start[i] for i in range(n_now_in, stage_numbers)], dtype='float32')
    # print(arr_m_data.sum())
    m = arr_m_data.sum()
    view_in_details(f'm [{slo(m)}] = {[f"m_stage_start[{n_now_in + i}] [{slo(m_stage_start[n_now_in + i])}] + " for i in range(stage_numbers - n_now_in)]}')


def get_Sc_current(n_now_in):
    global Sc
    Sc = (P_stage_vacuum[n_now_in] - P_stage_earth[n_now_in]) / P_on_earth  # Площадь сечения сопла ДУ - м^2
    view_in_details(f'Sc [{slo(n_now_in)}] =  (P_stage_vacuum[n] [{slo(P_stage_vacuum[n_now_in])}] - '
                    f'P_stage_earth[n] [{slo(P_stage_earth[n_now_in])}]) / P_on_earth [{slo(P_on_earth)}]')


def get_m_current(n_now_in):
    global dm
    # Изменение массы для работы текущей ступени
    dm = m_per_sec(m_stage_start[n_now_in], rocket_m_stages_dry_arr_m[n_now_in], rocket_T_stages_arr_for_m[n_now_in])
    view_in_details(f'dm [{slo(dm)}] = m_per_sec(m_stage_start[n] [{slo(rocket_m_stages_dry_arr_m[n_now_in])}], '
                    f'm_stage_dry[n] [{slo(m_stage_dry[n_now_in])}], '
                    f'time_work_max_stage[n] [{slo(rocket_T_stages_arr_for_m[n_now_in])}])')


def get_time_data():
    global t_current, dt
    # Текущее значение времени - c
    t_current = t_stage_already_fly
    # t_current = 0  # Время работы - с
    dt = 0.1  # Шаг изменения времени - с
    view_in_details(f't_current= {slo(t_current)}, dt= {slo(dt)}')


def get_abs_data():
    global abs_V, abs_Va, abs_r
    # Амплитуды скоростей
    abs_V = v_full(V_x, V_y)        #
    abs_r = v_full(x, y)            # Вычисление модуля радиус-вектора
    abs_Va = v_full(V_ax, V_ay)     # ???
    view_in_details(f'abs_V= {slo(abs_V)}, abs_r= {slo(abs_r)}, abs_Va= {slo(abs_Va)}')


def count_stage_data(n_in):
    view_in_details(f'n= {n_in}')
    print_str_msg(try_number, True, n_in)
    get_stage_m(n_in)
    get_Sc_current(n_in)
    get_m_current(n_in)
    get_time_data()
    get_abs_data()


def get_pitch():
    global pitch
    pitch = pitch_0 - (k_1 * t_current * t_current + k_3 * pow(t_current, 3)) / (k_2 + pow(t_current, 2))
    view_in_details(f'pitch [{slo(pitch)}] = pitch_0 [{slo(pitch_0)}] - k_1 [{slo(k_1)}] * '
                    f't_current [{slo(t_current)}] / (k_2 [{slo(k_2)}] + pow(t_current [{slo(t_current)}], 2))')


def get_alpha():
    global alpha
    alpha = pitch - pitch_a
    if alpha > 3:
        alpha = 0
    view_in_details(f'alpha [{slo(alpha)}] = pitch [{slo(pitch)}] - pitch_a [{slo(pitch_a)}]')


def get_sin_cos_data():
    global sin_phi, cos_phi, sin_pitch_phi, cos_pitch_phi, sin_pitch_a_phi, cos_pitch_a_phi, sin_alpha
    # Вычисление значение синусов и косинусов необходимых углов
    sin_phi = np.sin(phi)
    cos_phi = np.cos(phi)
    sin_pitch_phi = np.sin(pitch - phi)
    cos_pitch_phi = np.cos(pitch - phi)
    sin_pitch_a_phi = np.sin(pitch_a - phi)
    cos_pitch_a_phi = np.cos(pitch_a - phi)
    sin_alpha = np.sin(alpha)
    view_in_details(
        f'sin_phi [{slo(sin_phi)}] = np.sin(phi [{slo(phi)}]), cos_phi [{slo(cos_phi)}] = np.cos(phi [{slo(phi)}])\n'
        f'sin_pitch_phi [{slo(sin_pitch_phi)}] = np.sin(pitch [{slo(pitch)}] - phi [{slo(phi)}])\n'
        f'cos_pitch_phi [{slo(cos_pitch_phi)}] = np.sin(pitch [{slo(pitch)}] - phi [{slo(phi)}])\n'
        f'sin_pitch_a_phi [{slo(sin_pitch_a_phi)}] = np.sin(pitch_a [{slo(pitch_a)}] - phi [{slo(phi)}])\n'
        f'cos_pitch_a_phi [{slo(cos_pitch_a_phi)}] = np.sin(pitch_a [{slo(pitch_a)}] - phi [{slo(phi)}])\n'
        f'sin_alpha [{slo(sin_alpha)}] = np.sin(alpha [{slo(alpha)}])')


def get_h_g_ro_q_():
    global h, g, ro, q
    #  Необходимые вычисления
    h = np.abs(abs_r - Radius_earth)    # Высота относительно перепендикуляра опущенного на поверхность Земли
    g = g_current_count(abs_r)          # Вычисление ускорение свободного падения в данной точке
    ro = ro_current_count(h)            # Значение плотности
    view_in_details(f'h [{slo(h)}] = np.abs(abs_r [{slo(abs_r)}] - Radius_earth [{slo(Radius_earth)}])\n'
                    f'g [{slo(g)}] = g_current_count(abs_r [{slo(abs_r)}])\n'
                    f'ro [{slo(ro)}] = ro_current_count(h [{slo(h)}])')
    # Определение лобового сопротивления
    q = ro * pow(abs_Va, 2) / 2
    if t_current == 0:
        q = 0
    view_in_details(f'q [{slo(q)}]= ro [{slo(ro)}] * pow(abs_Va [{slo(abs_Va)}], 2) / 2')


def get_C_xy():
    global Cx, Cy
    # Опредлеление коэфициентов лобового сопротивления и подъемной силы
    Cx = C_x_0 + C_ya * pow(sin_alpha, 2)
    Cy = C_ya * sin_alpha
    view_in_details(
        f'Cx [{slo(Cx)}] = C_x_0 [{slo(C_x_0)}] + C_ya [{slo(C_ya)}] * pow(sin_alpha [{slo(sin_alpha)}], 2)\n'
        f'Cy [{slo(Cy)}] = C_ya [{slo(C_ya)}] * sin_alpha [{slo(sin_alpha)}]')


def get_XY_n_Ph_Pn():
    global X_N, Y_N, p_h, P_N
    # Опредлелени силы подъемной и силы сопротивления
    X_N = q * Sm * Cx               # function X
    if t_current == 0:
        X_N = 0
    Y_N = q * Sm * Cy               # function Y
    p_h = P_on_earth * ro / 1.225   # Давление
    view_in_details(f'X_N [{slo(X_N)}] = q [{slo(q)}] * Sm [{slo(Sm)}] * Cx [{slo(Cx)}]\n'
                    f'Y_N [{slo(Y_N)}] = q [{slo(q)}] * Sm [{slo(Sm)}]* Cy [{slo(Cy)}]\n'
                    f'p_h [{slo(p_h)}] = P_on_earth [{slo(P_on_earth)}] * ro [{slo(ro)}] / 1.225')
    # Опредление модуля тяги
    P_N = P_stage_vacuum[n] - Sc * p_h
    view_in_details(
        f'P_N [{slo(P_N)}] = P_stage_vacuum[n] [{slo(P_stage_vacuum[n])}] - Sc [{slo(Sc)}] * p_h [{slo(p_h)}]\n')


def count_each_step_flight_1():
    view_in_details('', 1)

    get_pitch()
    get_alpha()
    get_sin_cos_data()
    get_h_g_ro_q_()
    get_C_xy()
    get_XY_n_Ph_Pn()

    get_abs_V_ampl()
    get_phi()
    get_V_xg_Theta_earth()
    get_theta()
    get_W()
    get_V_abs_axy()
    get_pitch_a()


def save_if_True(flag_in):
    if flag_in is True:
        save_data_arr()     # Сохраняем все переменные в массивы для последующей работы
        print_info('', n)   # Вывод данных на экран и запись в файл
        view_in_details('\n' + '*' * 50 + " " * 10 + 'ПРОИЗВОДИМ ИЗМЕНЕНИЯ ПАРАМЕТРОВ' + " " * 10 + '*' * 50)
    else:
        print('Continue searching k coef')


def get_a_v_cord_xy_derivative():
    global a_x, a_y, V_x, V_y, x, y
    # Уравнение производной скорости по оси X
    a_x = -g * sin_phi + (P_N / (m * 1000)) * cos_pitch_phi + (X_N / (m * 1000)) * cos_pitch_a_phi - (
                Y_N / (m * 1000)) * sin_pitch_a_phi
    # Уравнение производной скорости по оси Y
    a_y = -g * cos_phi + (P_N / (m * 1000)) * sin_pitch_phi + (X_N / (m * 1000)) * sin_pitch_a_phi + (
                Y_N / (m * 1000)) * sin_pitch_a_phi

    # Переменные для метода Эйлера
    f_0Vx = V_x  # for eiler f_p
    f_0Vy = V_y  # for eiler f_p
    f_0ax = a_x  # for eiler f_p
    f_0ay = a_y  # for eiler f_p

    view_in_details(f'a_x [{slo(a_x)}] = -g [{slo(-g)}] * sin_phi [{slo(sin_phi)}] + (P_N [{slo(P_N)}] / (m [{slo(m)}] * 1000)) * '
                    f'cos_pitch_phi [{slo(cos_pitch_phi)}] + (X_N [{slo(X_N)}] / (m [{slo(m)}] * 1000)) * '
                    f'cos_pitch_a_phi [{slo(cos_pitch_a_phi)}] - (Y_N [{slo(Y_N)}] / (m [{slo(m)}] * 1000)) * '
                    f'sin_pitch_a_phi [{slo(sin_pitch_a_phi)}]\n'
                    f''
                    f'a_y [{slo(a_y)}] = -g [{slo(-g)}] * cos_phi [{slo(cos_phi)}] + (P_N [{slo(P_N)}] / (m [{slo(m)}] * 1000)) * '
                    f'sin_pitch_phi [{slo(sin_pitch_phi)}] + (X_N [{slo(X_N)}] / (m [{slo(m)}] * 1000)) * '
                    f'cos_pitch_a_phi [{slo(cos_pitch_a_phi)}] - (Y_N [{slo(Y_N)}] / (m [{slo(m)}] * 1000)) * '
                    f'cos_pitch_a_phi [{slo(cos_pitch_a_phi)}]')

    # Метод Эйлера
    V_x = Eiler_func(f_0Vx, f_0ax, (a_x - f_0ax) / dt, dt)  # for Vx
    V_y = Eiler_func(f_0Vy, f_0ay, (a_y - f_0ay) / dt, dt)  # for Vy

    view_in_details(
        f'V_x [{slo(V_x)}] = Eiler_func(f_0Vx [{slo(f_0Vx)}], f_0ax [{slo(f_0ax)}], (a_x [{slo(a_x)}] - f_0ax [{slo(f_0ax)}]) / dt [{slo(dt)}], '
        f'dt [{slo(dt)}])\n'
        f'V_y [{slo(V_y)}] = Eiler_func(f_0Vx [{slo(f_0Vx)}], f_0ay [{slo(f_0ay)}], (a_y [{slo(a_y)}] - f_0ay [{slo(f_0ay)}]) / dt [{slo(dt)}], '
        f'dt [{slo(dt)}])')

    x = Eiler_func(x, f_0Vx, f_0ax, dt)  # for x
    y = Eiler_func(y, f_0Vy, f_0ay, dt)  # for

    view_in_details(
        f'x [{slo(x)}] = Eiler_func(x [{slo(x)}], f_0Vx [{slo(f_0Vx)}], f_0ax [{slo(f_0ax)}], dt [{slo(dt)}])\n'
        f'y [{slo(y)}] = Eiler_func(y [{slo(y)}], f_0Vy [{slo(f_0Vy)}], f_0ay [{slo(f_0ay)}], dt [{slo(dt)}])')
    # Конец метода Эйлера


def change_current_m():
    global m
    m = m - dm * dt             # Уравнение изменения массы
    view_in_details(f'm [{slo(m)}]= m [{slo(m - dm * dt)}] - dm [{slo(dm)}] * dt [{slo(dt)}]')


def get_abs_V_ampl():
    global abs_V, abs_r
    # Амплитуды скоростей
    abs_V = v_full(V_x, V_y)
    abs_r = v_full(x, y)        # Вычисление модуля радиус-вектора
    view_in_details(f'abs_V [{slo(abs_V)}] = v_full(V_x [{slo(V_x)}], V_y [{slo(V_y)}])\n'
                    f'abs_r [{slo(abs_r)}] = v_full(x [{slo(x)}] , y [{slo(y)}])')


def get_phi():
    global phi
    phi = 2 * np.arctan(x / (y + abs_r))
    view_in_details(f'phi [{slo(phi)}] = 2 * np.arctan(x [{slo(x)}] / (y [{slo(y)}] + abs_r [{slo(abs_r)}]))')


def get_V_xg_Theta_earth():
    global Vxg, vg, THETA_EARTH
    Vxg = V_x - W_earth * abs_r
    vg = np.sqrt(Vxg * Vxg + V_y * V_y)
    THETA_EARTH = 2 * np.arctan(V_y / (vg + Vxg)) - phi
    # print(THETA_EARTH)


def get_theta():
    global theta
    theta = 2 * np.arctan(V_y / (V_x + abs_V)) - phi
    view_in_details(f'theta [{slo(theta)}] = 2 * np.arctan(V_x [{slo(V_x)}] / (V_y [{slo(V_y)}] + abs_V [{slo(abs_V)}] )) + phi [{slo(phi)}]')


def get_W():
    global W
    W = abs_r * W_earth
    view_in_details(f'W [{slo(W)}] = abs_r [{slo(abs_r)}] * W_earth [{slo(W_earth)}]')


def get_V_abs_axy():
    global V_ax, V_ay, abs_Va
    V_ax = abs_V * np.cos(theta) - W
    V_ay = abs_V * np.sin(theta)
    view_in_details(f'V_ax [{slo(V_ax)}] = abs_V [{slo(abs_V)}] * np.cos(theta [{slo(theta)}]) - W [{slo(W)}]\n'
                    f'V_ay [{slo(V_ay)}] = abs_V [{slo(abs_V)}] * np.sin(theta [{slo(theta)}])')

    abs_Va = v_full(V_ax, V_ay)
    view_in_details(f'abs_Va  [{slo(abs_Va)}] = v_full(V_ax [{slo(V_ax)}], V_ay [{slo(V_ay)}])')


def get_pitch_a():
    global pitch_a
    pitch_a = 2 * np.arctan(V_ay / (V_ax + abs_Va)) + phi
    view_in_details(f'pitch_a [{slo(pitch_a)}] = 2 * np.arctan(V_ax [{slo(V_ax)}] / (V_ay [{slo(V_ay)}] + abs_Va [{slo(abs_Va)}])) + phi [{slo(phi)}]')


def get_t_current():
    global t_current
    t_current += dt
    view_in_details(f't_current [{slo(t_current)}] = t_current [{slo(t_current - dt)}] + dt [{slo(dt)}]')


def count_each_step_flight_2():
    get_a_v_cord_xy_derivative()
    change_current_m()
    # get_abs_V_ampl()
    # get_phi()
    # get_V_xg_Theta_earth()
    # get_theta()
    # get_W()
    # get_V_abs_axy()
    # get_pitch_a()
    get_t_current()
    view_in_details('', -1)


flag = True
# while check_K_flags() is False:
while True:
    # Цикл for от 0 до макс числа ступеней
    for n in range(stage_numbers):
        count_stage_data(n)
        # ЦИКЛ
        while t_current <= time_work_max_stage[n]:
            count_each_step_flight_1()
            save_if_True(flag)
            count_each_step_flight_2()

        if flag is True:
            # Пройдясь по массиву с текущим временем работы добавим все значения времени в глобальный массив,
            # где хранятся все данные по времени
            for i_local in arr_out_t_current:
                arr_out_all_flight_time.append(i_local)     # + t_stage_already_fly)
            # Запись номера итерации. на которой происходит отделение ступени
            arr_out_scatter_mark_stage.append(len(arr_out_t_current) + local_additional_len)
            # Добавочная длина равна последнему значению времени на прогоне
            local_additional_len = arr_out_scatter_mark_stage[-1]

            # Если хотим продолжить считать другие ступени, то ставим True. Иначе должен стоять False
            _1_stage = [False, False]               # Вывод графиков только первой ступени ракеты
            _2_stages = [True, False]               # Вывод графиков только первой и второй ступени ракеты
            _3_stages = [True, True, True]          # Вывод графиков трех ступеней ракеты
            _model_behaviour = [_1_stage, _2_stages, _3_stages]     # Модели поведения вывода графиков

            """                 МЕНЯТЬ СТУПЕНИ ЗДЕСЬ                 """
            # Выбрать модель вывода графиков 0 - 1 ступень, 1 - вторая ступень, 2 - 3 ступень
            next_stage = _model_behaviour[2]
            if next_stage[n] is True:
                # Чистим массив с текущем временем, чтобы набрать новый набор значений
                arr_out_t_current.clear()
                # На сколько мы будем смещать наши данные по времени для след ступеней
                t_stage_already_fly = t_current
            else:
                break
            num_r = 4
            msg_out = f'theta normal = {theta.__round__(num_r)} rad  ~ {np.rad2deg(theta).__round__(num_r)}°\n'\
                  f'theta earth= {THETA_EARTH.__round__(num_r)} rad  ~ {np.rad2deg(THETA_EARTH).__round__(num_r)}°\n'\
                  f'phi= {phi.__round__(num_r)} rad  ~ {np.rad2deg(phi).__round__(num_r)}°\n'\
                  f'h= {h.__round__(num_r)} m  ~ {(h / 1000).__round__(num_r)} км\n'\
                  f'pitch = {pitch.__round__(num_r)} rad  ~ {np.rad2deg(pitch).__round__(num_r)}°\n'\
                  f'alpha = {alpha.__round__(num_r)} rad  ~ {np.rad2deg(alpha).__round__(num_r)}°'
            print(msg_out)
            if flag_write_log_lite == 1:
                file_log_lite.write(msg_out)
    break


if flag_write_excel_file == 1:
    excel_file.close_excel()
if flag_write_txt_file == 1:
    file.close()
if flag_write_log_lite == 1:
    file_log_lite.close()

colors_graph = ['red', 'blue', 'violet', 'green', 'black', 'brown', 'yellow', 'orange', 'purple', 'pink',
                'red', 'blue', 'violet', 'green', 'black', 'brown', 'yellow', 'orange', 'purple', 'pink',
                'red', 'blue', 'violet', 'green', 'black', 'brown', 'yellow', 'orange', 'purple', 'pink']


def make_graph(title, data_time, data_DATA, colors, labels, all_stages=0):
    """
    Функция создает на выходе график с кривыми

        на вход:
            Parameters
            ----------

            title:      название,

            data_time:  массив[время графика 1, время графика 2, ...],

            data_DATA:  массив[информация график 1, итнформация график 2, ...],

            colors:     цвета графиков,

            labels:     названия кривых

            all_stages: флаг указания точек, где происходит разделение ступеней
            """
    plt.cla()
    plt.title(title)
    data_number = len(data_DATA)
    for i in range(data_number):
        plt.plot(data_time[i], data_DATA[i], color=colors[i], label=labels[i])
    # Если стоит флаг показывать точки разделения ступеней
    if all_stages == 1:
        # Проходим по каждой кривой
        for i_i in range(len(data_DATA)):
            # Ставим все точки на кривой
            for i in range(len(arr_out_scatter_mark_stage)):
                local_data_time = data_time[i_i].copy()     # Локальная переменная массива с исх данными
                local_data_DATA = data_DATA[i_i].copy()     # Локальная переменная массива с исх данными
                local_position = arr_out_scatter_mark_stage[i] - 1  # Позиция точки где разделяются ступени
                style = dict(size=10, color='black')        # Размер и цвет шрифта текста
                # Смещение текста на несколько px
                few_px_upper = (local_data_DATA[local_position] - local_data_DATA[local_position - 1])
                # Рисуем точку, в которой происходит разделение ступпеней
                plt.scatter(local_data_time[local_position], local_data_DATA[local_position], color=colors[i_i])
                # Рисуем надпись над точкой
                plt.text(local_data_time[local_position], local_data_DATA[local_position] + few_px_upper,
                         f'Отделение \nступени № {i + 1}', ha='right', **style)
    plt.legend()
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel('Data')
    if flag_auto_save_png == 1:
        plt.savefig(title)
    if flag_show_graphics == 1:
        plt.show()


time = arr_out_all_flight_time  # массив времени

dict_graphs = {
    'alpha': {
        'title': 'alpha',
        'time': [time],
        'data': [arr_out_alpha],
        'labels': ['alpha'],
        'spec': 1
    },
    'theta': {
        'title': 'theta',
        'time': [time],
        'data': [arr_out_theta],
        'labels': ['theta'],
        'spec': 1
    },
    'THETA_EARTH': {
        'title': 'THETA_EARTH',
        'time': [time],
        'data': [arr_out_THETA_EARTH],
        'labels': ['THETA_EARTH'],
        'spec': 1
    },
    'pitch': {
        'title': 'pitch',
        'time': [time],
        'data': [arr_out_pitch],
        'labels': ['pitch'],
        'spec': 1
    },
    'plot V': {
        'title': 'plot V',
        'time': [time for i in range(len(np.array([arr_out_V_x, arr_out_V_y, arr_out_abs_V], dtype='float32')))],
        'data': np.array([arr_out_V_x, arr_out_V_y, arr_out_abs_V], dtype='float32'),
        'labels': ['V_x', 'V_y', 'abs_V'],
        'spec': 1
    },
    'h': {
        'title': 'plot h',
        'time': [time for i in range(len(np.array([arr_out_h], dtype='float32')))],
        'data': np.array([arr_out_h], dtype='float32'),
        'labels': ['h', 'x_pos', 'y_pos'],
        'spec': 1
    },
    'V(r)': {
        'title': 'V от  R',
        'time': [time for i in range(len(np.array([arr_out_abs_V, arr_out_h], dtype='float32')))],
        'data': np.array([arr_out_abs_V, arr_out_h], dtype='float32'),
        'labels': ['V по Y', 'R по X'],
        'spec': 1
    },
    'X_N': {
        'title': 'X_N',
        'time': [time],
        'data': [arr_out_X_N],
        'labels': [''],
        'spec': 1
    },
    'Y_N': {
        'title': 'Y_N',
        'time': [time],
        'data': [arr_out_Y_N],
        'labels': [''],
        'spec': 1
    },
    'm': {
        'title': 'Масса ракеты',
        'time': [time],
        'data': [arr_out_m],
        'labels': [''],
        'spec': 1
    },
    'x': {
        'title': 'x coord',
        'time': [time],
        'data': [arr_out_x],
        'labels': [''],
        'spec': 1
    },
    'y': {
        'title': 'y coord',
        'time': [time],
        'data': [arr_out_y],
        'labels': [''],
        'spec': 1
    },
    'ro': {
        'title': 'ro',
        'time': [time],
        'data': [arr_out_ro],
        'labels': [''],
        'spec': 1
    },
    'q': {
        'title': 'q',
        'time': [time],
        'data': [arr_out_q],
        'labels': [''],
        'spec': 1
    },
    'phi': {
        'title': 'phi',
        'time': [time],
        'data': [arr_out_phi],
        'labels': [''],
        'spec': 1
    },
    # 'test': {
    #     'title': 'name_test',
    #     'time': [time],
    #     'data': [arr_out_],
    #     'labels': ['label_test'],
    #     'spec': 1
    # },
}


graphs_out = ['alpha', 'theta', 'THETA_EARTH', 'pitch', 'plot V', 'h', 'V(r)', 'X_N', 'Y_N', 'm', 'phi', 'ro', 'q']

for i in graphs_out:
    print(i)
    make_graph(dict_graphs[i].get('title'), dict_graphs[i].get('time'), dict_graphs[i].get('data'), colors_graph,
               dict_graphs[i].get('labels'), dict_graphs[i].get('spec'))

input('\n\n\nНажмите любую клавишу для завершения программы')

"""
Массивы, в которых хранятся данные. Их можно выбирать для визуализации

arr_out_all_flight_time  -   
arr_out_t_current  -   
arr_out_dt         -  

arr_out_m          -  
arr_out_dm         -  

arr_out_h          - 
arr_out_g          -  

arr_out_abs_r      -      
arr_out_abs_V      -     
arr_out_abs_Va     -    

arr_out_x          -  
arr_out_y          - 

arr_out_V_x        -  
arr_out_V_y        -  
arr_out_a_x        -  
arr_out_a_y        -  

arr_out_X_N        -  
arr_out_Y_N        -  
arr_out_P_N        -  

arr_out_theta      -      
arr_out_alpha      - 
arr_out_phi        -  

arr_out_pitch      -      
arr_out_pitch_a    -      

arr_out_p_h        -  
arr_out_W          -  
arr_out_ro         -  
arr_out_q          -  


 """