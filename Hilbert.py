def hilbert(t, len,n):
    if n == 1:
        t.lt(90)
        t.fd(len)
        t.rt(90)
        t.fd(len)
        t.rt(90)
        t.fd(len)
        t.lt(90)
    else:
        t.lt(90)
        hilbert(t, len/3, n - 1)      
        
        t.fd(len*2/3)
        t.rt(90)
        t.fd(len/3)
        
        hilbert(t, len/3, n - 1)
        
        t.fd(len/3)
        
        t.rt(90)
        t.fd(len*2/3)
        
        
        hilbert(t, len/3, n - 1)    

import turtle
t = turtle.Turtle()
hilbert(t, 100, 2)
