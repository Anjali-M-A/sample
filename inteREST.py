def smpInt():
      p,r,t=10000,5.5,5
      SI=p*t*r/100
      print("simple interest is ",SI)
smpInt()
def cmpInt():
      p,r,t=10000, 10.25, 5
      a=p*(pow((1+r/100),t))
      CI=a-p
      print("compound interest is",CI)
cmpInt()

