#Valores booleanos (Booleans) (George Bool)
# Los bools poseen solo dos valores
# True o False (ojo, nada de true o false). COMO AMO A MI NOVIA BELLA :)
#Los booleanos nos sirven para decir si algo es verdero o falso.
cielo_es_azul=  True
valery_es_increiblemente_Hermosa = True
valery_es_muy_Fea = False
pasto_no_existe = False

#Uso de operadores booleanos

#USO DE 'AND' (multiplicacion boolena)
afirmacion = cielo_es_azul and valery_es_increiblemente_Hermosa
print(afirmacion) # imprime : True


afirmacion2 = cielo_es_azul and valery_es_muy_Fea
print(afirmacion2) #imprime : False

afirmacion_compuesta = cielo_es_azul and valery_es_increiblemente_Hermosa and valery_es_muy_Fea
print(afirmacion_compuesta) #imprime : False


#USO DEL 'OR' (suma booleana)
af = cielo_es_azul or valery_es_increiblemente_Hermosa
print (af)

af1 = cielo_es_azul or valery_es_muy_Fea # 1 or 0
print(af1)

af2 = pasto_no_existe or valery_es_muy_Fea
print(af2)

#Operador 'not'
valery_tiene_el_pelo_rosado_fuego = False
af3 = not valery_tiene_el_pelo_rosado_fuego
print(af3)
