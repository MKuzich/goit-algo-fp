import turtle

def pifagor_tree(t, branch_len, order):
    if order == 0:
        return

    t.forward(branch_len)
    t.right(45)
    pifagor_tree(t, branch_len * 0.7, order - 1)
    t.left(90)
    pifagor_tree(t, branch_len * 0.7, order - 1)
    t.right(45)
    t.backward(branch_len)

def draw_pifagor_tree(order):
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Піфагорове дерево")
    
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.color("white")

    pifagor_tree(t, 200, order)

    window.mainloop()

def main():
    order = int(input("Введіть глибину рекурсії: "))

    draw_pifagor_tree(order)

if __name__ == "__main__":
    main()