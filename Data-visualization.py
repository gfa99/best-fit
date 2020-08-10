#-*- coding:utf-8 -*-
#!/usr/bin/env python

def read_and_parse_data(file_path, data_dict):
	"""
	从文件中读取并解析数据
	"""
	pass


from matplotlib.patches import Ellipse, Circle
from matplotlib.lines   import Line2D
import matplotlib.pyplot as plt
import numpy as np
import math

def draw_line(plt=None):
	x = [-43.593586, 33.460638, 38.642593, -14.982494, -13.214993, -34.386358, -24.421168, 10.724942, -24.674256, 11.509581]
	y = [110.862777, 91.411650, 89.936396, 104.124468, 103.054619, 109.025360, 106.492333, 97.730320, 106.453755, 97.499663]

	if plt is None:
		return x, y

	plt.scatter(x,y, label='skitscat', color='r', s=25, marker=".")

	l = np.linspace(-60, 60, 6)
	Or= -0.255306*l + 100.103424
	plt.plot(l, Or, color="red")

	plt.xlabel('x-line')
	plt.ylabel('y-line')


def draw_cricle(plt=None):
	x = [113.298283,  115.874493,  123.921555,  94.405546,   93.672697,   96.108810,   87.103324,   105.505112,  81.919671,   99.116184]
	y = [-178.764956, -181.031497, -207.204071, -224.361744, -223.917429, -224.846684, -221.153975, -175.481420, -182.494772, -224.590517]

	if plt is None:
		return x, y

	plt.scatter(x,y, label='skitscat', color='g', s=25, marker="o")
	plt.scatter(99.914553, -199.887687, label='skitscat', color='g', s=25, marker="*")

	# 圆的基本信息
	# 1.圆半径
	r = 24.955809
	# 2.圆心坐标
	a, b = (99.914553, -199.887687)

	# ==========================================
	# 方法一：参数方程
	theta = np.arange(0, 2*np.pi, 0.01)
	a += r * np.cos(theta)
	b += r * np.sin(theta)
	# cir = Circle(xy = (99.914553, -199.887687), radius=24.955809, color="blue")
	plt.plot(a,b, color="green")

	plt.xlabel('x-cricle')
	plt.ylabel('y-cricle')


def get_ellipse(e_x, e_y, a, b, e_angle):
	"""[summary]
	获取椭圆轨迹
	Args:
		e_x ([type]): [圆心x]
		e_y ([type]): [圆心y]
		a ([type]): [长轴]
		b ([type]): [短轴]
		e_angle ([type]): [旋转角度]]

	Returns:
		[type]: [x，y的轨迹]
	"""
	angles_circle = np.arange(0, 2 * np.pi, 0.01)
	x = []
	y = []
	for angles in angles_circle:
		or_x = a * np.cos(angles)
		or_y = b * np.sin(angles)
		length_or = np.sqrt(or_x * or_x + or_y * or_y)
		or_theta = math.atan2(or_y, or_x)
		new_theta = or_theta + e_angle/180*math.pi
		new_x = e_x + length_or * np.cos(new_theta)
		new_y = e_y + length_or * np.sin(new_theta)
		x.append(new_x)
		y.append(new_y)
	return x,y

def draw_ellipse(plt=None):
	x = [131.249775, 122.817918, 127.574864, 143.237534, 99.856927, 108.873386, 60.335330, 102.140113, 146.293293, 57.054734]
	y = [-180.668477, -177.622758, -220.774265, -212.171155, -175.029140, -224.648693, -185.140892, -175.132549, -209.776645, -212.591938]

	if plt is None:
		return x, y

	plt.scatter(x,y, label='skitscat', color='b', s=25, marker="x")
	plt.scatter(100.171805, -200.034821, label='skitscat', color='b', s=25, marker="+")

	a, b = get_ellipse(100.171805, -200.034821, 49.796104, 24.953340, 0.002091)
	plt.plot(a,b, color="blue")

	plt.xlabel('x-ellipse')
	plt.ylabel('y-ellipse')



def draw_all(plt):
	fig, axe = plt.subplots()

	x, y = draw_line()
	plt.scatter(x,y, label='line', color='r', s=10, marker=".")
	x = np.linspace(-60, 60, 6)
	y = x * -0.255306 + 100.103424
	line = Line2D(x, y, lw=0.1, alpha=0.5)
	axe.add_line(line)

	x, y = draw_cricle()
	plt.scatter(x,y, label='circle', color='g', s=10, marker="o")
	plt.scatter(99.914553, -199.887687, label='point', color='g', s=10, marker="*")
	cir  = Circle(xy = (99.914553, -199.887687), radius=24.955809)
	axe.add_patch(cir)

	x, y = draw_ellipse()
	plt.scatter(x,y, label='ellipse', color='b', s=10, marker="x")
	plt.scatter(100.171805, -200.034821, label='point', color='b', s=10, marker="+")
	ell  = Ellipse(xy = (100.171805, -200.034821), width = 49.796104, height = 24.953340, angle = 0.002091, alpha=0.5)
	axe.add_patch(ell)


def main():
	# draw_line(plt)
	draw_cricle(plt)
	# draw_ellipse(plt)
	# draw_all(plt)

	plt.show()


if __name__ == "__main__":
	main()
