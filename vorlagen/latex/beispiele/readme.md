# Warum LaTeX
LaTeX erlaubt das Erstellen von sorgfältig gesetzten Textdokumenten. Das besondere an LaTeX ist, dass man sich um die Gestaltung nicht kümmern muss – lediglich die Textstruktur wird vorgegeben ("Auszeichnungssprache"), um die tatsächliche Gestaltung kümmert sich LaTeX selbst. In die Textstatz-Algorithmen von LaTeX (das auf TeX basiert) sind viele Jahre Erfahrung eingeflossen, daher kann man sich fast immer darauf verlassen, dass die Gestaltung sehr gut ist.

# Voraussetzungen 
Du brauchst eine LaTeX-Distribution auf deinem Computer. Wenn du noch keine hast, kannst du hier nachlesen, wie du eine installieren kannst:
[unter Windows](#latex-unter-window-installieren), [unter Linux](#latex-unter-linux-installieren) und [unter MacOS](#latex-unter-macos-installieren)

# Minimales LaTex-Template für BwInf-Zwecke
Dieses Dokument zeigt die Grundstruktur eines LaTeX-Dokuments. Der eigentliche Inhalt muss zwischen `\begin{document}` und `\end{document}` stehen. Weiter unten findet sich noch ein etwas umfangreicheres Template, das die meisten Pakete, die man für eine BwInf-Einsendung wahrscheinlich braucht schon beinhaltet.

```latex
\documentclass[a4paper,10pt]{scrartcl}
\usepackage[ngerman]{babel}
\usepackage[T1]{fontenc}
\usepackage[utf8x]{inputenc}

% Hier mehr Pakete laden. Z. B.: Mathe-Modus, Quellcode-Umgebung

\title{Aufgabe 0: \LaTeX-Dokument}
\author{Max Mustermännchen}

\begin{document}
\maketitle

\section{Lösungsidee}
Die Idee der Lösung sollte hieraus vollkommen ersichtlich werden, ohne das auf
die eigentliche Implementation Bezug genommen wird.

\section{Umsetzung}
Hier wird kurz erläutert, wie die Lösungsidee im Programm tatsächlich umgesetzt
wurde. Hier können auch Implementierungsdetails erwähnt werden.

\section{Beispiele}
Genügend Beispiele einbinden! Eigene Beispiele sind sehr gut! Und die Beispiele
sollte diskutiert werden.

\section{Quellcode (ausschnittsweise)}
Unwichtige Teile des Programms sollen hier nicht abgedruckt werden.

\end{document}
```

# Erklärung der wichtigsten LaTeX-Kommandos
## Textstrukturierung
Ein Einfacher Absatz wird durch eine leere Zeile erzeugt.

`\section{Überschrift}`, `\subsection{Überschrift}`, `\subsubsection{Überschrift}` und `\paragraph{Überschrift}` erzeugen Überschriften und Unterüberschriften. Mit `\tableofcontents` lässt sich ein Inhaltsverzeichnis erzeugen.

`maketitle` erzeugt die Titelseite. Mit `\newpage` lässt sich ein Seitenumbruch erzwingen.

## Textauszeichung
 * mit `\emph{Wort}` lassen sich Wörter hervorheben,
 * mit `\underline{Wort}` unterstreichen,
 * mit `\textbf{Wort}` fett drucken,
 * mit `\texttt{Wort}` in Monospace-Schrift schreiben,
 * mit `{\large Wort}` etwas größer,
 * mit `{\small Wort}` etwas kleiner,
 * mit `\footnote{Text}` eine Fußnote

## Aufzählungen

Unnummerierte Liste: `\begin{itemize} … \end{itemize}`
Nummerierte Aufzählung: `\begin{enumerate} … \end{enumerate}`
Beschreibungen: `\begin{description} … \end{description}`

Dazwischen jeweils die Aufzählungspunkte als `\item Text`, in Beschreibung als `\item[Wort] Beschreibung`.

Beispiel
```latex
\begin{enumerate}
  \item Das ist der erste Punkt
  \item und das hier der zweite.
\end{enumerate}
```
```latex
\begin{description}
  \item[Begriff1] Beschreibung von Begriff1
  \item[Begriff2] Beschreibung von Begriff2
\end{description}
```

## Tabellen
Tabellen werden mit `\begin{tabular}{lll} … \end{tabular}` umschlossen, wobei `{lll}` die Anzahl und Ausrichtung der Spalten beschreibt: je ein `l`: linksbündig, `r`: rechtsbündig, `c`: zentriert.

Neue Zeilen werden mit `\\` eingeleitet, die nächste Spalte mit `&`. Mit `|` und `\hline` lassen sich Tabellen mit Linien/Rahmen versehen.

Ohne Linien:
```latex
\begin{tabular}{lll}
   & Kirschen & Birnen \\
  Farbe: & rot & gelb  \\
  Kern:  & ja  & nein
\end{tabular}
```
Mit Linien:
```latex
\begin{tabular}{r||c|l}
   & Kirschen & Birnen \\
  \hline \hline
  Farbe: & rot & gelb  \\
  Kern:  & ja  & nein
\end{tabular}
```

## Formeln und Mathemodus
Formeln lassen sich in LaTeX nur im Mathe-Modus verwenden. Dafür gibt es zwei Möglichkeiten:
* Inline-Mathe: Wird durch Dollarzeichen begrenzt: z.B. `$a=7$`. Eignet sich für kurze Formeln.
* Align-Umgebung: Steht im Text hervor. `\\` macht einen Zeilenumbruch, `&` sorgt für die Ausrichtung der Zeilen.

```latex
\begin{align}
  f &= \sum_{a=1}^{20}\frac{1}{a+1}  \\
  &= b+12
\end{align}
```

### Befehle im Mathemodus
* `+`, `-`, `\cdot`, `/`: Grundrechenarten
* `^{a}`: Hochgestellt (Potenz)
* `_{a}`: Tiefgestellt (Index)
* `\sum_{}^{}`: Summenzeichen, ggf. mit Über- und Untertext
* `\prod_{}^{}`: Produktzeichen, ggf. mit Über- und Untertext
* `\frac{a}{b}`: Bruch a/b
* `\sqrt{a}`: Wurzel, `\sqrt[n]{a}`: n-te Wurzel
*  `=`, `<`, `>`, `\leq`, `\geq`, `\neq`: Gleichungen und Ungleichungen: = < > ≤ ≥ ≠
* `\propto`: proportional, `\in`: Element, `\forall`: ∀, `\exists`: ∃
* `\mathcal{O}`: Großes O für Groß-O-Notation


## Zusätzliche Pakete
### Bilder
Paket `graphicx` (`\usepackage{graphicx}`).

Bild einfügen mit
```latex
\begin{figure}
  \begin{center}
    \includegraphics{bild.jpg}
    \caption{Bildunterschrift}
  \end{center}
\end{figure}
```

Hinweis: So eingebundene Bilder erscheinen nicht unbedingt an der Stelle, wo sie eingebunden wurden, sondern meistens am Anfang oder Ende einer Seite. Das ist Absicht, und dient dazu, den Lesefluss nicht zu stören!

Müssen Bilder unbedingt an der Stelle stehen, wo sie eingebunden werden, so kann man sie mit dem folgenden Code einbinden.
```latex
\begin{center}
  \includegraphics{bild.jpg}
\end{center}
```
So eingebunden können Bilder aber keine Bildunterschrift haben. Prinzipiell ist die erste Variante zu bevorzugen!

### Quellcode
Paket `listings` (`\usepackage{listings}`).

Verwendung und Einstellungen siehe: https://en.wikibooks.org/wiki/LaTeX/Source_Code_Listings

### Algorithmen
Paket `algorithmicx` (`\usepackage{algorithmicx}`).

Beispiel:
```latex
\begin{algorithmic}
\If {$i\geq maxval$}
    \State $i\gets 0$
\Else
    \If {$i+k\leq maxval$}
        \State $i\gets i+k$
    \EndIf
\EndIf
\end{algorithmic}
```

https://en.wikibooks.org/wiki/LaTeX/Algorithms#Typesetting_using_the_algorithmicx_package

## Weiterführendes
### Tics
Graphik-Paket: Erlaubt das beschreiben von Graphiken direkt in LaTeX. https://en.wikibooks.org/wiki/LaTeX/PGF/TikZ

### Beamer
Folienpräsentationen in LaTeX schreiben. https://en.wikibooks.org/wiki/LaTeX/Presentations

# LaTeX installieren
## LaTex unter Linux installieren
Mit der Paketverwaltung sollte ein TeX-Live-Paket installiert werden. Z.B texlive-latex-base und texlive-latex-extra. Mit dem Kommando `pdflatex` lassen sich dann LaTeX-Dateien (`.tex`) zu PDFs übersetzen. Oder man verwendet einen LaTeX-Editor wie `kile`.

## LaTex unter Window installieren
Es sollte eine LaTeX-Distribution und ein LaTeX-Editor installiert werden. Manche Pakete bieten auch beides gebündelt an.

Ich empfehle die Verwendung von [miktex](https://miktex.org/) (Distribution) zusammen mit [texniccenter](http://www.texniccenter.org/) (Editor).

Alternativen sind die Distribution [TeX Live](http://www.tug.org/texlive/) (Distribution) und die Editoren [texstudio](http://texstudio.sourceforge.net/)  oder [texworks](http://www.tug.org/texworks/). Alle sind natürlich frei miteinander kombinierbar …

https://de.wikibooks.org/wiki/LaTeX-Kompendium:_Schnellkurs:_Die_Installation_unter_Windows

## LaTex unter MacOS installieren
https://de.wikibooks.org/wiki/LaTeX-Kompendium:_Schnellkurs:_Die_Installation_unter_Mac_OS_X


# Ausführlicheres LaTeX-Dokument mit viele Beispielen und Hinweisen

Diese Beispieldokument soll die meisten Befehle noch einmal veranschaulichen. Darunter findet sich auch noch ein Template zur eigenen Verwendung für BwInf-Einsendungen.

 * Mit Beispielaufgabe 
 * erläuterndem Text zu
    * Aufgabeinhalt
    * LaTeX-Verwendung
 * sollte alle oben auftauchende Befehle mal benutzen
 * Hinweis, dass man nicht alles können muss, um sehr gute BwInf-Einsendungen zu erzeugen (z.B. O-Notation)


# LaTex-Template für BwInf-Zwecke

```latex
\documentclass[a4paper,10pt,ngerman]{scrartcl}
\usepackage{babel}
\usepackage[T1]{fontenc}
\usepackage[utf8x]{inputenc}
\usepackage[a4paper,margin=2.5cm]{geometry}

% Die nächsten drei Felder bitte anpassen:
\newcommand{\Name}{Team: ??? / Name} % Teamname oder eigenen Namen angeben
\newcommand{\TeamId}{???}
\newcommand{\Aufgabe}{Aufgabe 1: \LaTeX-Dokument}

% Kopf- und Fußzeilen
\usepackage{scrlayer-scrpage}
\setkomafont{pageheadfoot}{\textrm}
\ifoot{\Name}
\cfoot{\thepage}
\chead{\Aufgabe}
\ofoot{Team-ID: \TeamId}

% Für mathematische Befehle und Symbole
\usepackage{amsmath}
\usepackage{amssymb}

% Für Bilder
\usepackage{graphicx}

% Für Algorithmen
\usepackage{algpseudocode}

% Für Quelltext
\usepackage{listings}
\usepackage{color}
\definecolor{mygreen}{rgb}{0,0.6,0}
\definecolor{mygray}{rgb}{0.5,0.5,0.5}
\definecolor{mymauve}{rgb}{0.58,0,0.82}
\lstset{
  keywordstyle=\color{blue},commentstyle=\color{mygreen},
  stringstyle=\color{mymauve},rulecolor=\color{black},
  basicstyle=\footnotesize\ttfamily,numberstyle=\tiny\color{mygray},
  captionpos=b, % sets the caption-position to bottom
  keepspaces=true, % keeps spaces in text
  numbers=left, numbersep=5pt, showspaces=false,showstringspaces=true,
  showtabs=false, stepnumber=2, tabsize=2, title=\lstname
}
\lstdefinelanguage{JavaScript}{ % JavaScript ist als einzige Sprache noch nicht vordefiniert
  keywords={break, case, catch, continue, debugger, default, delete, do, else, finally, for, function, if, in, instanceof, new, return, switch, this, throw, try, typeof, var, void, while, with},
  morecomment=[l]{//},
  morecomment=[s]{/*}{*/},
  morestring=[b]',
  morestring=[b]",
  sensitive=true
}

% Diese beiden Pakete müssen als letztes geladen werden
%\usepackage{hyperref} % Anklickbare Links im Dokument
\usepackage{cleveref}

% Daten für die Titelseite
\title{\Aufgabe}
\author{\Name\\Team-ID: \TeamId}
\date{\today}

\begin{document}

\maketitle
\tableofcontents


% Hier kommt der Inhalt hin!


\end{document}
```
