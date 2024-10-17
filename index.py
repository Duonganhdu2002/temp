s = k = d = e = 0

for i in range(1, 3):
    a = input('Nhập tên học sinh: ')
    x = float(input('Nhập điểm khoa học: '))
    y = float(input('Nhập điểm xã hội: '))
    z = float(input('Nhập điểm kỹ năng mềm: '))

    s = (x + y + z) / 3
    print('Điểm trung bình của', a, 'là:', s)

    if (s >= 8):
        k += 1
        print(a, 'xuất sắc thật')
    elif (s >= 5.5) and (s <= 7.9):
        d += 1
        print(a, 'làm tốt lắm')
    else:
        e += 1
        print(a, 'cố lênnnn')

    print('-' * 10)

print('Có tổng cộng', k, 'HSG')  
print('Có tổng cộng', d, 'HSK') 
print('Có tổng cộng', e, 'HSTB') 
