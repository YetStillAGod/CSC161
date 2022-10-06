from graphics import *

def main():
	'''
	win = GraphWin("face", 500, 500)
	p = Polygon(Point(200, 100), Point(300, 100), Point(350,250), Point(300, 400), Point(200, 400), Point(150,250))
	e1 = Point(200, 150)
	e2 = Point(300, 150)
	E1 = Circle(e1, 10)
	E2 = Circle(e2, 10)
	l1 = Line(Point(250, 160), Point(250, 250))
	l2 = Line(Point(200, 300), Point(300, 300))
	p.draw(win)
	e1.draw(win)
	e2.draw(win)
	E1.draw(win)
	E2.draw(win)
	l1.draw(win)
	l2.draw(win)
	win.getMouse()
	win.close()
	'''
	'''
	win = GraphWin()
	p1 = Point(130,130)
	p2 = win.getMouse()
	l = Line(p1, p2)
	l.draw(win)
	l.move(p2.getX()-p1.getX(), p2.getY()-p1.getY())z
	win.getMouse()
	win.close()
	'''
	win = GraphWin()
	e_p = Point(100, 100)
	e = Entry(e_p, 20)
	e.setText("Enter something")
	e.draw(win)
	print(e.getText())
	win.getMouse()
	win.close()


if __name__ == '__main__':
	main()