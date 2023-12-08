class Nomina:

#METODO AFP
 def Afp (self, sb):

    return sb * 0.07

#METODO ARS
def Ars (self, sb):

    return sb * 0.02

# METODO SUENDO NETO
def SueldoNeto (self, sb, td):

    return sb - td

# METODO TOTAL DESCUENTO
def TotalDesc (self, afp, ars):

    return afp + ars

# EJEMPLO NOMINA
n = Nomina()
sueldo = float(input("Entre Sueldo Base:"))
afp = n.Afp (sueldo)
ars = n.Ars (sueldo)
descuentos = n.Totaldescuento (afp, ars)
sn = n.sueldoneto (sueldo, descuentos)

print ("Afp             :{:0.2f}".format(afp))
print ("Ars             :{:0.2f}".format(ars))
print ("Descuento       :{:0.2f}".format(descuentos))
print ("Sueldo Neto     :{:0.2f}".format(sn))