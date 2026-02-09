#Ejericio trabajador
#Consideraciones: Salario es mensual

Horas_semana = 48
Salario_hora = float(5000)
Horas_mes = Horas_semana*4
Salario_mes = Salario_hora*Horas_mes

Salario_bruto = Salario_mes
Salario_neto = Salario_bruto*0.875
Retefuente = Salario_bruto*0.125

print("El salario bruto mensual del trabajador es: $", Salario_bruto)
print("El salario neto mensual del trabajador es: $", Salario_neto)
print("La retención en la fuente mensual del trabajador es: $", Retefuente)
