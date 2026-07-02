import math
an = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print ('O ângulo de {} tem o COSSENO de {:.2f}, o SENO de {:.2f} e a TANGENTE de {:.2f}'.format(an, co, seno, tan))