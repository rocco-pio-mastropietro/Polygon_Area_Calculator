##
#  Questo modulo definisce la super-classe Rettangle e la
#  sotto-classe Square.
#

## E' una super-classe di Square.
class Rectangle:
  ## Quando viene creato un oggetto Rectangle, è
  #  inizializzato con:
  #  @param width attributo larghezza
  #  @param height attributo altezza.
  #
  def __init__(self, width, height):
    self._width = width
    self._height = height
    self._picture_width = ""
    self._picture = ""

  ## @return la rappresentazione in stringa di un'istanza 
  #  di Rectangle.
  #
  def __str__(self):
    return f"Rectangle(width={self._width}, height={self._height})"
  
  ## @param width la larghezza del rettangolo.
  #
  def set_width(self, width):
    self._width = width

  ## @param height l'altezza del rettangolo.
  #
  def set_height(self, height):
     self._height = height

  ## @return l'area del rettangolo.
  #
  def get_area(self):
    return (self._width * self._height)

  ## @return il perimetro del rettangolo.
  #
  def get_perimeter(self):
    return (2 * self._width + 2 * self._height)

  ## @return la diagonale del rettangolo.
  #
  def get_diagonal(self):
    return ((self._width ** 2 + self._height ** 2) ** .5)

  ## @return una stringa che rappresenta la forma del
  #  Rettangolo.
  #
  def get_picture(self):
    self._picture_width = self._width * "*" + "\n"
    self._picture = f"{self._picture_width}" * self._height

    if self._width > 50 or self._height > 50:
      return "Too big for picture."
    else:
      return self._picture

  ## @param Shape un'altra forma (quadrato o rettangolo)
  #  @return il numero di volte che la forma passata
  #  potrebbe adattarsi all'interno della forma (senza
  #  rotazioni).
  #
  def get_amount_inside(self, Shape):
    if Shape._width > self._width or Shape._height > self._height:
      return 0
    else:
      return (self._width // Shape._width) * (self._height // Shape._height)
      
## E' una sotto-classe di Rectangle.
class Square(Rectangle):
  ## Quando viene creato un oggetto Square, viene passata
  #  @param side_lenght la lunghezza di un singolo lato.
  #  
  ## La classe Square è in grado di accedere ai metodi
  #  della classe Rectangle, ma contiene anche un metodo
  #  set_side.
  #
  def __init__(self, side_lenght):
    super().__init__(side_lenght, side_lenght)

  ## @return la rappresentazione in stringa di un'istanza
  #  di Square.
  #
  def __str__(self):
    return f"Square(side={self._width})"

  ## Il metodo sovrascrive le dimensioni del quadrato.
  #  @param side_lenght la lunghezza del lato.
  #
  def set_side(self, side_lenght):
    self._width = side_lenght
    self._height = side_lenght

  ## Il metodo sovrascrive la larghezza del quadrato.
  #  @param side_lenght la lunghezza del lato.
  def set_width(self, side_lenght):
    self._width = side_lenght

  ## Il metodo sovrascrive l'altezza del quadrato.
  #  @param side_lenght la lunghezza del lato.
  def set_height(self, side_lenght):
     self._height = side_lenght
