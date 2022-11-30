# Minesweeper
Schreibe ein Programm, das zu einem Minesweeper Spielfeld einen Mogelzettel erstellt.

Minesweeper ist ein Spiel, das bei einigen Windows Versionen mitgeliefert wurde. Die Herausforderung besteht darin, Spielfelder aufzudecken, unter denen Minen liegen können. Wenn ein Feld aufgedeckt wird, unter dem sich eine Mine befindet, ist das Spiel verloren. Aufgedeckte Felder werden mit Ziffern markiert, die angeben, wie viele Minen an das Feld angrenzen.

Aufgabe des zu erstellenden Programms „Mogelzettel“ ist es, einen Mogelzettel zu erstellen, aus dem die Anzahl der angrenzenden Minen zu jedem Feld ersichtlich ist.

Eine Eingabedatei für das Programm sieht wie folgt aus:
```
*...
.... 
.*.. 
....
``` 
Das Programm wird darauf wie folgt aufgerufen:

`C:> mogelzettel feld1.txt feld1mogel.txt`\
Ergebnis ist die Datei feld1mogel.txt mit folgendem Inhalt:
```
*100
2210
1*10
1110
```
Weitere Beispiele für Eingaben und Ausgaben des Programms:
```
**...     **100
.....     33200
.*...     1*100
```
Die Spielfeldgröße kann sowohl in der Anzahl der Zeilen als auch Spalten variieren. Die Eingabedateien sind allerdings immer korrekt aufgebaut, eine Fehlerbehandlung ist nicht erforderlich.