```mermaid
classDiagram
  Class Player {
    + Name: str ("Hugo Calderano")
    + Age: int (27)
    + Advantage: int (0)
    + Country: str ("Brazil")
    + Hand: str ("Right Hand")
    + Playing Style: str ("Offensive")
    + Grip: str ("Handshake")
    + Sponsor: str ("Xiom")
    ----------------------------------
    + win: bool(True)
    + dopped: bool(False)
  }

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

  Class Racket {}

  Class Blade {
    + Name: str ("Sweden Classic")
    + Style: str ("Neutral")
    + Brand: str("Yasaka")
  }

  Class Rubber {
    + Name: str("Bluefire")
    + Type: str("Inverted")
    + Brand: str("Donic")
    + Boosted: bool("False")
  }

  Class Ball {
    + Brand: str("Raise")
  }

  Match --> Table
  Table --> Player
  Player --> Racket
  Racket --> Blade
  Racket --> Rubber
  Racket --> Ball

```