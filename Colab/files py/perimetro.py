def perimetro():
  try:
    print("Defina o comprimento e largura para definir o perímetro du uma determinada área.\nCasas decimais devem ser representadas com .:")
    comp = float(input("Defina o comprimento em metros: "))
    larg = float(input("Defina o comprimento em metros: "))
    perim = 2 * (comp + larg)
    print( f"A soma entre o comprimento {comp:.2f}m e a largura {larg:.2f}m dá o perímetro de {perim:.2f}m²")
  except ValueError:
    print("Por favor, certifique-se de que introduziu os valores corretos. Caracteres especiais, texto e virgulas não são reconhecidos.")

perimetro()
