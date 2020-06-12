# Lösen eines Differentialgleichungssystems in Simulink

## Aufgabestellung

Nachdem Sie Ihr letztes offenes Ticket fertig bearbeitet haben und das Review positiv verlief, schauen Sie sich nach einem neuem Ticket im Backlog des aktuellen Sprints um. Dabei entdecken Sie das Ticket `VMC-667` mit dem Titel **Implementation of a feedforward for the Vehicle Motion Controller (VMC)**.

Laut der Beschreibung des Tickets soll der aktuelle `VMC` um eine Vorsteuerung für die Querführung erweitert werden, um so die Performanz (Minimierung der Querablage) für Querbeschleunigungen bis $a_y = 4\ \frac{m}{s^2}$ zu erhöhen.

Aufgrund früherer Tätigkeiten sind Sie selbstbewusst genug und weisen sich das Ticket zur Bearbeitung zu. Nach einer kurzen Recherche (falls Sie Fahrzeugtechniker sind, haben Sie sofort das richtige Buch aufgeschlagen) haben Sie das lineare Einspurmodell zur Beschreibung der Fahrzeugbewegung vor sich liegen.

Im Folgenden finden Sie zwei unterschiedliche Darstellungsformen des linearen Einspurmodells.

### Differentialgleichungen

$\dot\beta = - \frac{c_v + c_h}{m \cdot v} \cdot \beta + \frac{m \cdot v^2 - (c_h \cdot l_h - c_v \cdot l_v)}{m \cdot v^2} \cdot \dot\psi - \frac{c_v}{m \cdot v} \cdot \frac{\delta_H}{i_S}$

$\ddot\psi = - \frac{c_h \cdot l_h - c_v \cdot l_v}{\Theta} \cdot \beta - \frac{c_h \cdot {l_h}^2 + c_v \cdot {l_v}^2}{\Theta \cdot v} \cdot \dot\psi + \frac{c_v \cdot l_v}{\Theta} \cdot \frac{\delta_H}{i_S}$

### Zustandsraum

$\underline{\underline{A}} = \begin{bmatrix}- \frac{c_v + c_h}{m \cdot v} & \frac{m \cdot v^2 - (c_h \cdot l_h - c_v \cdot l_v)}{m \cdot v^2}\\\ - \frac{c_h \cdot l_h - c_v \cdot l_v}{\Theta} & - \frac{c_h \cdot {l_h}^2 + c_v \cdot {l_v}^2}{\Theta \cdot v}\end{bmatrix}, \underline{B} = \begin{bmatrix}- \frac{c_v}{m \cdot v} \\\ \frac{c_v \cdot l_v}{\Theta}\end{bmatrix}, \underline{x} = \begin{bmatrix}\beta \\\ \dot\psi \end{bmatrix}, u = \frac{\delta_H}{i_S}$

$\underline{\dot x} = \underline{\underline{A}} \cdot \underline{x} + \underline{B} \cdot u$

Bevor Sie sich an die eigentliche Aufgabe des Tickets machen, möchten Sie kurz überprüfen, ob das Modell, welches Sie gefunden haben, plausibel ist.

`AUFGABE:`

1. Simulieren Sie die Bewegung eines Fahrzeuges während eines *Lenkradwinkelsprungs* mit Hilfe des linearen Einspurmodells in Simulink. Das Manöver *Lenkradwinkelsprung* stellt nach einer anfänglichen Geradeausfahrt ab dem Zeitpunkt $t_{trig}$ einen Ziellenkradwinkel $\delta_{H, max}$ mit dem Gradienten $\dot\delta_{H}$ ein und hält diesen.

2. Stellen Sie die Verläufe des Schwimmwinkels $\beta$, der Gierrate $\dot \psi$ und des Lenkradwinkels $\delta_{H}$ für die gesamte Simulationszeit grafisch dar.

---

Simulationsparameter | Wert
--- | ---
Simulationzeit | $t = 5s$
Schrittweite | $d_t = 0.001s$
Solver | diskret

---

Manöverparameter | Wert
--- | ---
Fahrzeuggeschwindigkeit | $v=70\ \frac{km}{h}$
Manöverbeginn | $t_{trig}=1\ s$
max. Lenkradwinkel | $\delta_{H, max} = 100^\circ$
Lenkradwinkelgradient | $\dot \delta_H = 200\ \frac{^\circ}{s}$

---

Fahrzeugparameter | Wert
--- | ---
Lenkübersetzung | $i_S = 15$
Fahrzeugmasse | $m = 1500\ kg$
Schwerpunktlage vorne | $l_v = 1.2\ m$
Schwerpunktlage hinten | $l_h = 1.4\ m$
Schräglaufsteifigkeit vorne | $c_v = 70000\ \frac{N}{rad}$
Schräglaufsteifigkeit hinten | $c_h = 85000\ \frac{N}{rad}$
Gierträgheit | $\theta = 2520\ kgm^2$

---

Die Bearbeitungszeit beträt 90 Minuten.

Viel Erfolg.
