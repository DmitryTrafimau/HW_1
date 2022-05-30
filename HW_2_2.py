print('### Расчет необходимого количества рулонов обоев для поклейки ###')
room_length = float(input('Введите длину комнаты в м - '))
room_width = float(input('Введите ширину комнаты в м - '))
room_height = float(input('Введите высоту комнаты в м - '))
wallpaper_width = float(input('Введите ширину рулона обоев в м - '))
wallpaper_lenth = float(input('Введите длину рулона обоев в м - '))
import math
number_of_rolls = math.ceil((room_length + room_width) * 2 * room_height / wallpaper_width / wallpaper_lenth)
print('Необходимое количество рулонов размером', wallpaper_width, 'м на', wallpaper_lenth, 'м - ', number_of_rolls, 'шт.')