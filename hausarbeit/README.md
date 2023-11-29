# Hausarbeit - Passwort Manager

---

## ⚠️ Achtung ⚠️

### Dieser Passwort Manager sollte auf keinen Fall im Alltag verwendet werden, weil dieser nicht sicher ist

In dieser Hausarbeit werdet ihr einen einfachen Passwort Manager programmieren, welcher sich über das Terminal bedienen lässt.
Ihr könnt insgesamt 18 Punkte für die Klausur sammeln mit dieser Hausarbeit. 16 Punkte durch das Erstellen des Codes und 2 Punkte für die Präsentation.
Die Punkte können nur erhalten werden wenn die Präsentation der Hausarbeit gehalten wurde.

Folgende Funktionen sollte er haben:

1. Passwörter in eine Datei abspeichern
2. Passwörter anzeigen
3. Bestimmte Passwörter suchen
4. Programm beenden

In diesem Notebook findet ihr alle Informationen die ihr benötigt um die Hausarbeit erfolgreich fertigzustellen. Viel Spaß! 😄

## Notebooks

### `main.ipynb`

#### In diesem Notebook findet ihr vor der Zelle in der ihr die main() Funktion programmiert 3 Zellen

- `%run Verschluesselung.ipynb` und `%run functions.ipynb`
    Das sind magische Funktionen, die einfach alle Zellen aus den angegebenen Notebooks einmal in diesem Notebook ausführt.

- Die 3. Zelle wird verwendet um Libraries in das Notebook zu importieren.
    Achtet darauf, falls ihr weitere Libraries verwenden müsst, dass es sich ausschließlich um Libraries aus der Python Standardbibliothek handelt:
    [Python Standardbibliothek](https://docs.python.org/3/library/index.html)

#### Der Passwort Manager soll insgesamt vier Optionen bieten

- Passwort anlegen
- Passwörter anzeigen
- Passwort finden
- Beenden

Die Bearbeitung dieses Notebooks gibt einen Punkt.

---

### `functions.ipynb`

#### Diese Datei beinhaltet folgende Funktionen

- **add_password()**
    Diese Funktion soll ein von dem Benutzer eingegebenes Passwort abspeichern. Außerdem sollen noch Name des Benutzers und die Plattform abgespeichert werden. Die Passwörter sollen nur im verschlüsselten Zustand abgespeichert werden. Um diese wieder zu entschlüsseln, könnt ihr den Key zusätzlich abspeichern (deshalb nicht sicher!).
- **display_passwords()**
    Diese Funktion soll alle Passwörter ausgeben, die mit einer bestimmten Verschlüsselungsmethode hinterlegt sind.
- **decrypt_password()**
    Diese Funktion dient dazu, verschlüsselte Passwörter zu entschlüsseln. Das ist wichtig, um die gespeicherten und verschlüsselten Passwörter zu entschlüsseln, damit sie korrekt im Terminal ausgegeben werden.
- **find_password()**
    Diese Funktion soll ein bestimmtes Passwort finden können, wenn der Benutzer seinen Namen, die Plattform und die Verschlüsselungsmethode in das Terminal eingibt

---

### `Verschluesselung.ipynb`

#### Diese Datei enthält für die 4 Verschlüsselungsmethoden die programmiert werden jeweils die Verschlüsselungs- und die Entschlüsselungsmethode

##### 1. Cäsar-Verschlüsselung

Die Cäsar-Verschlüsselung, auch bekannt als Verschiebechiffre, ist eine einfache Form der Verschlüsselung, die auf einer Verschiebung des Alphabets basiert.

Beispiel mit Verschiebung um +3:
A wird zu D
B wird zu E
C wird zu F
Z wird zu C

Um wieder zu entschlüsseln, brauchen wir die Verschiebung als Schlüssel, um die Buchstaben wieder korrekt zurück zu verschieben.
Beispiel: "hallo" mit Verschiebung 3 wird zu "kdoor", und mit Verschiebung -3 wird es wieder zu "hallo".

[Mehr Infos zur Cäsar-Verschlüsselung](https://de.serlo.org/informatik/48121/caesar-verschl%C3%BCsselung)

##### 2. Vernam-Verschlüsselung (One Time Pad - Verschlüsselung)

Die Vernam-Verschlüsselung ist eine symmetrische Verschlüsselungsmethode, die auf der Verwendung eines zufälligen Schlüssels basiert.
Der Schlüssel muss genau so lange sein wie der zu verschlüsselnde Text.
Bei der Verschlüsselung wird jedes Bit oder Buchstabe der Nachricht mit dem entsprechenden Bit oder Buchstaben des zufälligen Schlüssels XOR (ausschließendes Oder) verknüpft.
Bei der Entschlüsselung wird das verschlüsselte Passwort erneut mit dem gleichen Schlüssel XOR verknüpft, sodass das originale Passwort wiederhergestellt wird.
Bei der Verschlüsselungsmethode besteht die Schwierigkeit darin, dass durch die XOR-Verknüpfung von zwei Buchstaben sehr ungewöhnliche Zeichen entstehen können.

[Mehr Infos zum One Time Pad](https://www.youtube.com/watch?v=nKEKDS0epKw)

##### 3. Substitutions-Verschlüsselung

Die Substitutionsverschlüsselung ist eine Methode der Verschlüsselung, bei der einzelne Elemente der Klartextnachricht durch andere Elemente ersetzt werden.
Es wird ein Schlüssel erstellt, der wie ein Wörterbuch funktioniert. In diesem Schlüssel werden die Elemente als Keys abgespeichert und die Zeichen, die diese ersetzen sollen, als Value.
Bei der Verschlüsselung werden die Elemente dann einfach gemäß des Übersetzungswörterbuchs ausgetauscht.
Bei der Entschlüsselung benötigen wir das Wörterbuch, um die Entschlüsselung korrekt durchzuführen.
Bei dieser Verschlüsselung besteht die Schwierigkeit darin, sich zu überlegen, wie man das Wörterbuch abspeichert und bei der Entschlüsselung abruft.

[Mehr Infos zur Substitution](https://norbert-pohlmann.com/glossar-cyber-sicherheit/monoalphabetische-substitution)

##### 4. Morse-Codierung

Bei dieser Codierung wird ein Morse-Alphabet angelegt, welches bestimmt, wie die einzelnen Buchstaben und Zeichen codiert werden.
Das funktioniert ähnlich wie die Substitutionsverschlüsselung.
Da das Morse-Alphabet nicht zwischen Groß- und Kleinbuchstaben unterscheidet, nehmen wir die Limitation in Kauf, dass man entweder auf Groß- oder Kleinbuchstaben begrenzt ist.

[Mehr Infos zur Morse-Codierung](https://kryptografie.de/kryptografie/chiffre/morse.htm)

---

## Anmerkungen

- Ihr müsst nicht die ganze Hausarbeit bearbeiten, sondern habt die Möglichkeit auch nur einzelne Funktionen zu bearbeiten. Für jede erfolgreich bearbeitete Funktion gibt es am Ende einen Punkt.
- Um die Punkte zu bekommen werden wir Termine einrichten (im Neujahr irgendwann) bei dem wir uns gegenseitig kurz unsere Ergebnisse vorstellen. Für die Präsentation gibt es 2 Punkte.
- Falls ihr etwas anders umsetzen wollt wie vorgegeben, könnt ihr das gerne machen das macht die ganze Sache etwas flexibler. Die Grundfunktion muss allerding erfüllt werden.
- Die Hausarbeit wird als ZIP-Archiv auf Ilias abgegeben. 

Links die man im zusammenhang mit der Hausarbeit durchlesen kann:

- Dateien lesen mit `with open`: <https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/>
- Dateipfade: <https://www.cip.ifi.lmu.de/~laskh/Python/dateien/Pfadangaben.pdf> (Seite 8-10)
- ASCII: <https://www.ascii-code.com/de>
- Anonyme Funktion Lambda: <https://www.w3schools.com/python/python_lambda.asp>
- String Methoden: <https://www.w3schools.com/python/python_ref_string.asp>
- <https://www.w3schools.com/python/python_ref_keywords.asp>
