m=int(input("Ievadi no kuras pakāpes jāapreķina: "))
N = int(input("IEvadi līdZ kurai pakāpei jāapreķīna: "))
for i in range(m, N+1):
  n = pow(2, i)
  print(n)