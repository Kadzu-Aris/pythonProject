import turtle
a = list(map(int,input().split()))
print(a)
_max=0
for i in a:
    if a>0:
        _max=a
    turtle.circle(i)

turtle.exitonclick()