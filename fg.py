import turtle
a = list(map(int,input().split()))
print(a)
for i in a:
    turtle.circle(i)

turtle.exitonclick()