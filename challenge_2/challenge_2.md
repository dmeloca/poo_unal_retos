```mermaid
classDiagram
  Match <|---- Player
  Player <|---- Table;
  Player <|---- Racket;
  Racket <|---- Blade;
  Racket <|---- Rubber;
  Player <|---- Ball;
  Class Match {
    + Location: str("Busan")
    + Date: int (16)
    + Type: str("Teams")
    + Sets: int(5)
    }

  Class Table {
    + Brand: str("DHS")
    + Number: int(1)
  }
  class Player {
    + Name: str ("Hugo Calderano")
    + Age: int (27)
    + Advantage: int (0)
    + Country: str ("Brazil")
    + Hand: str ("Right Hand")
    + Playing Style: str ("Offensive")
    + Grip: str ("Handshake")
    + Sponsor: str ("Xiom")
    + win: bool(True)
    + dopped: bool(False)
  }


  class Table {
    + Brand: str("DHS")
    + Number: int(1)
  }

  class Racket {}

  class Blade {
    + Name: str ("Sweden Classic")
    + Style: str ("Neutral")
    + Brand: str("Yasaka")
  }

  class Rubber {
    + Name: str("Bluefire")
    + Type: str("Inverted")
    + Brand: str("Donic")
    + Boosted: bool("False")
  }

  class Ball {
    + Brand: str("Raise")
  }


```
