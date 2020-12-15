import copy
import math
import turtle


def create_h_matr(n):
    h_matr = []
    for i in range(n):
        row = []
        for j in range(n):
            element = math.cos((2 * math.pi * i * j) / 16) + math.sin((2 * math.pi * i * j) / 16)
            element = round(element, 2)
            element = float('{:.2f}'.format(element))
            row.append(element)
        h_matr.append(row)
    return h_matr


def create_g_v(h_matr, row):
    g_x = []

    for elem in h_matr:
        summ = 0
        for x in range(len(row)):
            summ += elem[x] * row[x]
        summ = round(summ, 2)
        summ = float('{:.2f}'.format(summ))
        g_x.append(summ)
        #print(summ),
    #print(" ")
    return g_x


def create_g_n(h_matr, row):
    g_x = []

    for line in range(len(h_matr)):
        summ = 0
        for x in range(len(row)):
            summ += h_matr[x][line] * row[x]
        summ /= len(row)
        summ = round(summ, 2)
        summ = float('{:.2f}'.format(summ))
        g_x.append(summ)
        print(summ)
    print(" ")
    return g_x


def filter_matr(matr, var):
    for i in range(len(matr)):
        if abs(matr[i]) < var:
            matr[i] = 0
        #print(matr[i])
    #print(" ")
    return matr


def draw_picture(x_point, y_point, color):
    k = 20  # коэффициент учеличения изображения для наглядности
    turtle.hideturtle()
    turtle.penup()
    turtle.pencolor(color)
    first_point = (x_point[0] * k, y_point[0] * k)
    x_point.append(x_point[0])
    y_point.append(y_point[0])
    turtle.goto(first_point)
    turtle.pendown()

    for i in range(1, len(x_point)):
        point = (x_point[i] * k, y_point[i] * k)
        turtle.goto(point)


def find_error(x, y, g_n_x, g_n_y):
    result = 0
    for i in range(len(x)):
        result += math.pow((round(g_n_x[i]) - x[i]), 2) + math.pow((round(g_n_y[i]) - y[i]), 2)

    result = math.sqrt(result / (2 * 16))
    result = round(result, 5)
    result = float('{:.5f}'.format(result))
    return result


def run():
    h_matr = create_h_matr(16)

    x = [1, 1, 2, 3, 5, 6, 6, 7, 8, 7, 6, 6, 5, 4, 2, 1]
    y = [5, 10, 11, 11, 11, 10, 8, 8, 6, 6, 6, 5, 5, 5, 5, 5]

    draw_picture(copy.deepcopy(x), copy.deepcopy(y), "black")

    # расссчёт значений по второй формуле для x
    g_v_x_kr = create_g_v(h_matr, x)
    # расссчёт значений по второй формуле для y
    g_v_y_kr = create_g_v(h_matr, y)

    # фильтрация значений по модулю меньше 5
    g_v_x_kr_f1 = filter_matr(g_v_x_kr, 5)
    # расссчёт значений по третьей формуле для x
    g_n_x = create_g_n(h_matr, g_v_x_kr_f1)

    # фильтрация значений по модулю меньше 5
    g_v_y_kr_f1 = filter_matr(g_v_y_kr, 5)
    # расссчёт значений по третьей формуле для y
    g_n_y = create_g_n(h_matr, g_v_y_kr_f1)

    print("Для 5: " + str(find_error(x, y, g_n_x, g_n_y)))
    draw_picture(g_n_x, g_n_y, "red")

    # фильтрация значений по модулю меньше 10
    g_v_x_kr_f1 = filter_matr(g_v_x_kr, 20)
    # расссчёт значений по третьей формуле для x
    g_n_x = create_g_n(h_matr, g_v_x_kr_f1)

    # фильтрация значений по модулю меньше 10
    g_v_y_kr_f1 = filter_matr(g_v_y_kr, 20)
    # расссчёт значений по третьей формуле для y
    g_n_y = create_g_n(h_matr, g_v_y_kr_f1)

    print("Для 20: " + str(find_error(x, y, g_n_x, g_n_y)))
    draw_picture(g_n_x, g_n_y, "purple")

    # фильтрация значений по модулю меньше 15
    g_v_x_kr_f1 = filter_matr(g_v_x_kr, 25)
    # расссчёт значений по третьей формуле для x
    g_n_x = create_g_n(h_matr, g_v_x_kr_f1)

    # фильтрация значений по модулю меньше 15
    g_v_y_kr_f1 = filter_matr(g_v_y_kr, 25)
    # расссчёт значений по третьей формуле для y
    g_n_y = create_g_n(h_matr, g_v_y_kr_f1)

    print("Для 25: " + str(find_error(x, y, g_n_x, g_n_y)))
    draw_picture(g_n_x, g_n_y, "brown")

    turtle.mainloop()


if __name__ == '__main__':
    run()
