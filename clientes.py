import pandas as pd
from faker import Faker

fake = Faker('es_CL')

def generar_cliente():
  nombre = fake.name()
  correo = fake.email()
  telefono = fake.phone_number()
  company = fake.company()
  ciudad = fake.city()
  region = fake.state()

  return {"Nombre": nombre, "Correo": correo, "Telefono": telefono,"Nombre de la empresa": company, "region": region}
