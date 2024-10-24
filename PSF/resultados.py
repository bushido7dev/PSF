def carrera(edad, sexo):
  if edad <= 24 and sexo == "m":
      return "<br>Apto muy Bueno: 9min 22seg<br>Apto: 10min 22seg"
  elif edad <= 24 and sexo == "f":
      return "<br>Apto muy Bueno: 10min 22seg<br>Apto: 11min 37seg"
  elif edad >= 25 and edad <= 29 and sexo == "m":
        return "<br>Apto muy Bueno: 9min 37eg<br>Apto: 10min 41seg"
  elif edad >= 25 and edad <= 29 and sexo == "f":
        return "<br>Apto muy Bueno: 10min 41seg<br>Apto: 11min 58seg"
  elif edad >= 30 and edad <= 34 and sexo == "m":
        return "<br>Apto muy Bueno: 9min 58eg<br>Apto: 10min 58seg"
  elif edad >= 30 and edad <= 34 and sexo == "f":
        return "<br>Apto muy Bueno: 10min 58seg<br>Apto: 12min 19seg"
  elif edad >= 35 and edad <= 39 and sexo == "m":
        return "<br>Apto muy Bueno: 10min 08eg<br>Apto: 11min 18seg"
  elif edad >= 35 and edad <= 39 and sexo == "f":
        return "<br>Apto muy Bueno: 11min 45seg<br>Apto: 11min 18seg"
  elif edad >= 40 and edad <= 44 and sexo == "m":
        return "<br>Apto muy Bueno: 10min 30eg<br>Apto: 11min 42seg"
  elif edad >= 40 and edad <= 44 and sexo == "f":
        return "<br>Apto muy Bueno: 11min 42seg<br>Apto: 13min 06seg"
  elif edad >= 45 and edad <= 49 and sexo == "m":
        return "<br>Apto muy Bueno: 10min 54eg<br>Apto: 12min 06seg"
  elif edad >= 45 and edad <= 49 and sexo == "f":
        return "<br>Apto muy Bueno: 12min 06seg<br>Apto: 13min 36seg"
  elif edad >= 50 and edad <= 54 and sexo == "m":
        return "<br>Apto muy Bueno: 11min 18seg<br>Apto: 12min 36seg"
  elif edad >= 50 and edad <= 54 and sexo == "f":
        return "<br>Apto muy Bueno: 12min 36seg<br>Apto: 14min 12seg"
  elif edad >= 55 and edad <= 59 and sexo == "m":
        return "<br>Apto muy Bueno: 10min 34eg<br>Apto: 11min 45seg"
  elif edad >= 55 and edad <= 59 and sexo == "f":
        return "<br>Apto muy Bueno: 11min 54seg<br>Apto: 15min 00seg"
  elif edad >=60 and sexo == "m":
        return "<br>Apto muy Bueno: 12min 36eg<br>Apto: 14min 04seg"
  elif edad >=60 and sexo == "f":
        return "<br>Apto muy Bueno: 14min 04eg<br>Apto: 15min 52seg"


def abdominales(edad):
  if edad <= 29:
    return "<br>Apto muy Bueno: 51 abdominales<br>Apto: 48 abdominales"
  elif edad >= 30 and edad <= 39:
    return "<br>Apto muy Bueno: 43 abdominales<br>Apto: 39 abdominales"
  elif edad >= 40 and edad <= 49:
    return "<br>Apto muy Bueno: 35 abdominales<br>Apto: 30 abdominales"
  elif edad >= 50 and edad <= 59:
    return "<br>Apto muy Bueno: 31 abdominales<br>Apto: 24 abdominales"
  elif edad > 60:
    return "<br>Apto muy Bueno: 26 abdominales<br>Apto: 21 abdominales"


def barras(edad, sexo):
  if edad <= 29 and sexo =="m":
    return "<br>Apto muy Bueno: 13 barras<br>Apto: 09 barras"
  elif edad >= 30 and edad <= 39 and sexo == "m":
    return "<br>Apto muy Bueno: 11 barras<br>Apto: 08 barras"
  elif edad >= 40 and edad <= 49 and sexo == "m":
    return "<br>Apto muy Bueno: 07 barras<br>Apto: 05 barras"
  elif edad >= 50 and edad <= 59 and sexo == "m":
    return "<br>Apto muy Bueno: 04 barras<br>Apto: 03 barras"
  elif sexo == "f":
    return "No aplica"

def flexionCodoFemenino(edad, sexo):
  if edad <= 29 and sexo == "f":
    return "<br>Apto muy Bueno: 36 flexiones de codo<br>Apto: 30 flexiones de codo"
  elif edad >= 30 and edad <= 39 and sexo == "f":
    return "<br>Apto muy Bueno: 32 flexiones de codo<br>Apto: 27 flexiones de codo"
  elif edad >= 40 and edad <= 49 and sexo == "f":
    return "<br>Apto muy Bueno: 29 flexiones de codo<br>Apto: 24 flexiones de codo"
  elif edad >= 50 and edad <= 59 and sexo == "f":
    return "<br>Apto muy Bueno: 25 flexiones de codo<br>Apto: 21 flexiones de codo"
  elif edad > 60 and sexo == "f":
    return "<br>Apto muy Bueno: 20 flexiones de codo<br>Apto: 17 flexiones de codo"
  else:
    return "No aplica"

def flexionCodoMasculino(edad, sexo):
  if edad >= 45 and edad <= 49 and sexo == "m":
    return "<br>Apto muy Bueno: 30 flexiones de codo<br>Apto: 25 flexiones de codo"
  elif edad >= 50 and edad <= 59 and sexo == "m":
    return "<br>Apto muy Bueno: 25 flexiones de codo<br>Apto: 21 flexiones de codo"
  elif edad > 60 and sexo == "m":
    return "<br>Apto muy Bueno: 22 flexiones de codo<br>Apto: 18 flexiones de codo"
  elif sexo == "f":
    return "No aplica"
