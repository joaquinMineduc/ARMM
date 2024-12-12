from .static_data import regiones


def classificator_by_reg(CR, arg):
  num_cr = CR.split(arg)
  num_cr = int(num_cr[1])
  for index, region in enumerate(regiones, start = 1):
    if index == num_cr:
      return region