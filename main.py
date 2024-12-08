import matplotlib.pyplot as plt
import numpy as np


def graph(voice, pressure, temperature, volume, x1_coordinate, y1_coordinate, rectilinear, axes):
    x = [0, 0]
    y = [0, 0]
    cir = 0
    if voice == 1:
        axes.set_ylabel('P')
        axes.set_xlabel('V')
        if 'const' in pressure:
            if 'up' in temperature and 'up' in volume:
                x = [x1_coordinate, x1_coordinate + 1.5]
                y = [y1_coordinate, y1_coordinate]
                x1_coordinate += 1.5
            elif 'down' in temperature and 'down' in volume:
                x = [x1_coordinate, x1_coordinate - 1.5]
                y = [y1_coordinate, y1_coordinate]
                x1_coordinate -= 1.5
        elif 'up' in pressure:
            if 'up' in temperature and 'const' in volume:
                x = [x1_coordinate, x1_coordinate]
                y = [y1_coordinate, y1_coordinate + 1.5]
                y1_coordinate += 1.5
            elif 'const' in temperature and 'down' in volume:
                cir = 1
                x = np.linspace(0.5, 2, 100)
                y = 1 / x
                x1_coordinate -= 1.5
                y1_coordinate += 1.5
        elif 'down' in pressure:
            if 'down' in temperature and 'const' in volume:
                x = [x1_coordinate, x1_coordinate]
                y = [y1_coordinate, y1_coordinate - 1.5]
                y1_coordinate -= 1.5
            elif 'const' in temperature and 'up' in volume:
                cir = 1
                x = np.linspace(0.5, 2, 100)
                y = 1 / x
                x1_coordinate += 1.5
                y1_coordinate -= 1.5
    if voice == 2:
        axes.set_ylabel('P')
        axes.set_xlabel('T')
        if 'const' in pressure:
            if 'up' in temperature and 'up' in volume:
                x = [x1_coordinate, x1_coordinate + 1.5]
                y = [y1_coordinate, y1_coordinate]
                x1_coordinate += 1.5
            elif 'down' in temperature and 'down' in volume:
                x = [x1_coordinate, x1_coordinate - 1.5]
                y = [y1_coordinate, y1_coordinate]
                x1_coordinate -= 1.5
        elif 'up' in pressure:
            if 'up' in temperature and 'const' in volume:
                x = [x1_coordinate, x1_coordinate + 1.5]
                y = [y1_coordinate, y1_coordinate + 1.5]
                x1_coordinate += 1.5
                y1_coordinate += 1.5
            elif 'const' in temperature and 'down' in volume:
                x = [x1_coordinate, x1_coordinate]
                y = [y1_coordinate, y1_coordinate + 1.5]
                y1_coordinate += 1.5
        elif 'down' in pressure:
            if 'down' in temperature == 'down' and 'const' in volume:
                x = [x1_coordinate, x1_coordinate - 1.5]
                y = [y1_coordinate, y1_coordinate - 1.5]
                x1_coordinate -= 1.5
                y1_coordinate -= 1.5
            elif 'const' in temperature and 'up' in volume:
                x = [x1_coordinate, x1_coordinate]
                y = [y1_coordinate, y1_coordinate - 1.5]
                y1_coordinate -= 1.5
    if voice == 3:
        axes.set_ylabel('V')
        axes.set_xlabel('T')
        if 'const' in pressure:
            if 'up' in temperature and 'up' in volume:
                x = [x1_coordinate, x1_coordinate + 1.5]
                y = [y1_coordinate, y1_coordinate + 1.5]
                x1_coordinate += 1.5
                y1_coordinate += 1.5
            elif 'down' in temperature and 'down' in volume:
                x = [x1_coordinate, x1_coordinate - 1.5]
                y = [y1_coordinate, y1_coordinate - 1.5]
                x1_coordinate -= 1.5
                y1_coordinate -= 1.5
        elif 'up' in pressure:
            if 'up' in temperature and 'const' in volume:
                x = [x1_coordinate, x1_coordinate + 1.5]
                y = [y1_coordinate, y1_coordinate]
                x1_coordinate += 1.5
            elif 'const' in temperature and 'down' in volume:
                x = [x1_coordinate, x1_coordinate]
                y = [y1_coordinate, y1_coordinate - 1.5]
                y1_coordinate -= 1.5
        elif 'down' in pressure:
            if 'down' in temperature and 'const' in volume:
                x = [x1_coordinate, x1_coordinate - 1.5]
                y = [y1_coordinate, y1_coordinate]
                x1_coordinate -= 1.5
            elif 'const' in temperature and 'up' in volume:
                x = [x1_coordinate, x1_coordinate]
                y = [y1_coordinate, y1_coordinate + 1.5]
                y1_coordinate += 1.5
    if cir != 0:
        if 'down' in P:
            axes.plot(x + x1_coordinate - 2, y + y1_coordinate - 0.5)
        elif 'up' in P:
            axes.plot(x + x1_coordinate - 0.5, y + y1_coordinate - 2)
    else:
        axes.plot(x, y)
    ins = {'x': x1_coordinate, 'y': y1_coordinate}
    rectilinear.append(ins)


def data(pressure, temperature, volume, rectilinear):
    cur = {'P': pressure, 'T': temperature, 'V': volume}
    rectilinear.append(cur)


def spot(x_coordinate, y_coordinate, dot, axes):
    if x_coordinate != x1 or y_coordinate != y1:
        axes.plot(x_coordinate, y_coordinate, marker='o')
        axes.text(x_coordinate, y_coordinate, dot, fontsize=16)


def subscribe(pressure, temperature, volume):
    if pressure == 'const':
        return "Изобарный процесс"
    elif temperature == 'const':
        return "Изотермический процесс"
    elif volume == 'const':
        return "Изохорный процесс"


def conclusion():
    direct = 0
    for j in data_line:
        direct += 1
        print(f"Линия {direct}")
        print(f"P - {j['P']}, T - {j['T']}, V - {j['V']}. {subscribe(j['P'], j['T'], j['V'])}", end="\n")


fig, (ax1, ax2, ax3) = plt.subplots(
    nrows=1, ncols=3,
    figsize=(15, 5)
)
ax1.grid()
ax2.grid()
ax3.grid()
ax1.set_xlim((0, 10))
ax1.set_ylim((0, 10))
ax2.set_xlim((0, 10))
ax2.set_ylim((0, 10))
ax3.set_xlim((0, 10))
ax3.set_ylim((0, 10))
fig.suptitle("Уравнение Менделеева-Клапейрона")
print("Параметры линии графика")
print("P - давление")
print("T - температура")
print("v - объём")
print("Параметры принимают значения, которые указаны ниже")
print("up - возрастает; Пример: P = up - давление возрастает")
print("down - уменьшается; Пример: P = down - давление уменьшается")
print("const - постоянно; Пример P = const - давление остается постоянным")
n = int(input("Количество линий, которое вы хотите построить = "))
print("Вводите данные графика")
count = 0
x1 = 5
y1 = 5
point = 1
ax1.plot(x1, y1, marker='o')
ax2.plot(x1, y1, marker='o')
ax3.plot(x1, y1, marker='o')
ax1.text(x1, y1, point, fontsize=16)
ax2.text(x1, y1, point, fontsize=16)
ax3.text(x1, y1, point, fontsize=16)
point += 1
line = 0
data_line = []
data_coordinate1 = []
data_coordinate2 = []
data_coordinate3 = []
launch = {'x': x1, 'y': y1}
data_coordinate1.append(launch)
data_coordinate2.append(launch)
data_coordinate3.append(launch)
for i in range(n):
    print(f"Параметры {i + 1} линии")
    P = str(input("P = ")).lower()
    T = str(input("T = ")).lower()
    V = str(input("V = ")).lower()
    graph(1, P, T, V, data_coordinate1[i]['x'], data_coordinate1[i]['y'], data_coordinate1, ax1)
    spot(data_coordinate1[i + 1]['x'], data_coordinate1[i + 1]['y'], point, ax1)
    data(P, T, V, data_line)
    point += 1
    line += 1
addition = str(input("Хотите построннию линию? "))
if addition == "yes" or addition == "да":
    n += 1
    P = str(input("P = ")).lower()
    T = str(input("T = ")).lower()
    V = str(input("V = ")).lower()
    graph(1, P, T, V, x1, y1, data_coordinate1, ax1)
    spot(data_coordinate1[n]['x'], data_coordinate1[n]['y'], point, ax1)
    point += 1
    line += 1
    data(P, T, V, data_line)
point = 2
for i in range(n):
    if addition == "yes" and i == n - 1:
        graph(2, data_line[i]['P'], data_line[i]['T'], data_line[i]['V'], x1, y1, data_coordinate2, ax2)
        spot(data_coordinate2[i + 1]['x'], data_coordinate2[i + 1]['y'], point, ax2)
    else:
        graph(2, data_line[i]['P'], data_line[i]['T'], data_line[i]['V'], data_coordinate2[i]['x'],
              data_coordinate2[i]['y'], data_coordinate2, ax2)
        spot(data_coordinate2[i + 1]['x'], data_coordinate2[i + 1]['y'], point, ax2)
    point += 1
point = 2
for i in range(n):
    if addition == 'yes' and i == n - 1:
        graph(3, data_line[i]['P'], data_line[i]['T'], data_line[i]['V'], x1, y1, data_coordinate3, ax3)
        spot(data_coordinate3[i + 1]['x'], data_coordinate3[i + 1]['y'], point, ax3)
    else:
        graph(3, data_line[i]['P'], data_line[i]['T'], data_line[i]['V'], data_coordinate3[i]['x'],
              data_coordinate3[i]['y'], data_coordinate3, ax3)
        spot(data_coordinate3[i + 1]['x'], data_coordinate3[i + 1]['y'], point, ax3)
    point += 1
conclusion()
plt.show()
