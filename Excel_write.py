import xlwt


class Excel_file(object):
    """
        Работа с Excel файлом
    """
    def __init__(self, filename, stages_number=0):
        self.base_file_name = f'Rocket_{filename}'  # название файла без .txt
        self.stages_number = stages_number
        self.current_stage = None

        self.first_start = 0
        self.rows_pos = 0       # iterable param

        self.workbook_results = None
        self.worksheet_results = None
        self.style_cell = xlwt.easyxf('pattern: pattern none;''alignment: horizontal center')
        self.style_cell_name = xlwt.easyxf('pattern: pattern none;''alignment: horizontal center;''font: bold True')

    def file_settings(self, len_row):
        """
            Настройка ширины столбиков
        """
        for i in range(len_row):
            self.worksheet_results.col(i).width = 4000

    def open_excel(self):
        """
            Создание Excel файла
        """
        self.workbook_results = xlwt.Workbook(f'{self.base_file_name}_results.xlsx')
        self.worksheet_results = self.workbook_results.add_sheet('Расчеты')

    def write_columns_names(self, data_all_dict):
        """
            Заполняем названия столбцов
        """
        for i in range(len(data_all_dict)):
            self.worksheet_results.write(self.rows_pos, i, data_all_dict[i], self.style_cell_name)
        self.rows_pos += 1

    def write_data(self, data_all_dict, stages_number):
        """
            Заполняем строчки
        """
        columns_numbers = len(data_all_dict.keys())
        if self.first_start == 0:
            answer_names_arr = [f'{i}' for i in data_all_dict.keys()]
            self.write_columns_names(answer_names_arr)
            self.file_settings(columns_numbers)
            self.first_start = 1
        answer_arr = [f'{data_all_dict.get(i)}' for i in data_all_dict.keys()]
        if stages_number != self.current_stage:
            self.stages_number = stages_number
            self.worksheet_results.write(self.rows_pos, 0, f"Ступень № {self.stages_number + 1}", self.style_cell_name)
            self.rows_pos += 1
        for i in range(columns_numbers):
            self.worksheet_results.write(self.rows_pos, i, answer_arr[i], self.style_cell)
        self.rows_pos += 1
        self.current_stage = stages_number

    def close_excel(self):
        """
            Закрываем файл
        """
        self.workbook_results.save(f'{self.base_file_name} results.xls')


