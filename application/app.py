from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QRadioButton, QButtonGroup
from PyQt5.QtGui import QFont


def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('Фильтрация')
    window.resize(300, 300)

    h_layout1 = QHBoxLayout()
    h_layout2 = QHBoxLayout()
    h_layout3 = QHBoxLayout()
    v_layout = QVBoxLayout()

    font1 = QFont("Arial", 12, QFont.Normal)
    font2 = QFont("Arial", 10, QFont.Normal)

    filter_price = QLabel('Фильтр цены:')
    from_price = QLabel('от')
    before_price = QLabel('до')
    filter_count_rooms = QLabel('Выбрать кол-во комнат:')
    filter_floor = QLabel('Выбрать этаж:')
    floor = QLabel('Этаж:')
    count_floors = QLabel('Кол-во этажей:')

    filter_price.setFont(font1)
    filter_count_rooms.setFont(font1)
    filter_floor.setFont(font1)

    in_from_price = QLineEdit()
    in_before_price = QLineEdit()
    input_count_rooms = QLineEdit()
    input_floor = QLineEdit()
    in_count_floors = QLineEdit()

    input_count_rooms.setFont(font1)
    input_floor.setFont(font2)

    rbtn1 = QRadioButton('1')
    rbtn2 = QRadioButton('2')
    rbtn3 = QRadioButton('3')
    rbtn4 = QRadioButton('4')
    rbtn5 = QRadioButton('5')

    # radio_group = QButtonGroup()
    # radio_group.addButton(rbtn1)
    # radio_group.addButton(rbtn2)
    # radio_group.addButton(rbtn3)
    # radio_group.addButton(rbtn4)
    # radio_group.addButton(rbtn5)

    # radio_group.setExclusive(False)    
    # rbtn1.setChecked(False)
    # rbtn2.setChecked(False)
    # rbtn3.setChecked(False)
    # rbtn4.setChecked(False)
    # rbtn5.setChecked(False)
    # radio_group.setExclusive(True) 

    apply_filter = QPushButton('применить')
    apply_filter.setFont(font2)

    v_layout.addWidget(filter_price)
    h_layout1.addWidget(from_price)
    h_layout1.addWidget(in_from_price)
    h_layout1.addWidget(before_price)
    h_layout1.addWidget(in_before_price)
    v_layout.addLayout(h_layout1)

    v_layout.addWidget(filter_count_rooms)
    h_layout2.addWidget(rbtn1)
    h_layout2.addWidget(rbtn2)
    h_layout2.addWidget(rbtn3)
    h_layout2.addWidget(rbtn4)
    h_layout2.addWidget(rbtn5)
    v_layout.addLayout(h_layout2)

    v_layout.addWidget(filter_floor)
    h_layout3.addWidget(floor)
    h_layout3.addWidget(input_floor)
    h_layout3.addWidget(count_floors)
    h_layout3.addWidget(in_count_floors)
    v_layout.addLayout(h_layout3)
    v_layout.addWidget(apply_filter)

    window.setLayout(v_layout)

    data = []

    def get_data():
        global data
        from_price = int(in_from_price.text())
        before_price = int(in_before_price.text())
        for btn in [rbtn1, rbtn2, rbtn3, rbtn4, rbtn5]: 
            if btn.isChecked():
                count_rooms = int(btn.text())
                break
        floor = input_floor.text()
        count_floors = in_count_floors.text()

        # data = coordinates_flats.apply_filter(from_price, before_price, count_rooms, floor, count_floors, db)

        with open(r'data.txt', 'w') as file:
            file.write(f'{from_price} {before_price} {count_rooms} {floor} {count_floors}')
       
    apply_filter.clicked.connect(get_data)

    window.show()
    app.exec_()
    

