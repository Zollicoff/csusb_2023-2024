vf = input("What is the final velocity?")
if vf == "/":
 dontuse = "vf"
else:
    vf=float(vf)

vi = str(input("What is the initial velocity?"))
if vi == "/":
  dontuse = "vi"
else:
  vi=float(vi)

a = str(input("What is the acceleration?"))
if a == "/":
  dontuse = "a"
else:
  a=float(a)

t = str(input("What is the time?"))
if t == "/":
  dontuse = "t"
else:
  t=float(t)


def eq1():
    vf = vi + a*t
    print("vf: "+str(vf))
def eq2():
    vi = vf/(a*t)
    print("vi: "+str(vi))
def eq3():
    t = (vf - vi)/a
    print("t: "+str(t))

def eq4():
    a = (vf - vi)/t
    print("a: "+str(a))



if dontuse == "vf":
    eq1()
elif dontuse=='vi':
    eq2()
elif dontuse=='a':
    eq4()
elif dontuse=='t':
    eq3()
else:
    print('All value known')