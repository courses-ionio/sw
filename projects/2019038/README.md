## ΣΤΟΙΧΕΙΑ : 

### ΑΜ: Π2019038
### Ονοματεπώνυμο: Βασιλική Λώλη 
### Οργανισμός: [modus-vivendi-memento-mori](https://github.com/modus-vivendi-memento-mori)

<br>

| Εβδομάδα | [Όλα τα παραδοτέα βρίσκονται στην ίδια σελίδα της τελικής αναφοράς](https://epidrome.github.io/teaching/deliverables/) με τα προσωπικά στοιχεία σας (Όνομα, ΑΜ, github profile) και μαζί με αυτόν εδώ τον πίνακα περιεχομένων | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | [Δημιουργία ομάδας](https://epidrome.github.io/teaching/team/) + [Φορκ και δημιουργία σελίδας τελικής αναφοράς](https://epidrome.github.io/teaching/guide/), [προσθήκη πίνακα περιεχομένων](https://raw.githubusercontent.com/courses-ionio/sw/master/README.md), [<a href="#Εισαγωγή"><span class="toctext">Εισαγωγή</span></a>](https://epidrome.github.io/teaching/intro/), αποστολή της εισαγωγής [για σχολιασμό στην συζήτηση](https://github.com/courses-ionio/sw/discussions/categories/show-and-tell) και καταγραφή του συνδέσμου συζήτησης δίπλα --> | [Συζήτηση 1](https://github.com/courses-ionio/sw/discussions/1177) | Ολοκλήρωση εντός προθεσμίας |
| 2 | <a href="#Γραμμή Εντολών 1"><span class="toctext">Γραμμή Εντολών 1</span></a> (systemd) και [διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας](https://epidrome.github.io/teaching/team) | [Συζήτηση 2](https://github.com/courses-ionio/sw/discussions/1275) | Ολοκλήρωση εντός προθεσμίας |
| 3 | <a href="#Γραμμή εντολών (no systemd)"><span class="toctext">Γραμμή εντολών (no systemd)</span></a> | [Συζήτηση 3]()  | Ολοκλήρωση εντός προθεσμίας |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά) | | |
| 5 | Συμμετοχικό περιεχόμενο A1 + A2 | | |
| 6 | Γραμμή εντολών (no systemd, custom static blog generator) | | |
| 7 | συμμετοχικό περιεχόμενο B1 | | |
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) | | |
| 9 | συμμετοχικό περιεχόμενο B2 | | |
| 10 | Τελική αναφορά* | | |

<br><br/>

<h2><span id="Εισαγωγή">Εισαγωγή</span></h2>

Μέσω του μαθήματος της Τεχνολογίας Λογισμικού αποσκοπώ στο να εξασκήσω και να μάθω πρακτικές για τη σχεδίαση και την ανάπτυξη λογισμικού, με τη βοήθεια και την 
ολοκλήρωση των εβδομαδιαίων συμμετοχικών και συνεργατικών ασκήσεων και γραμμής εντολών. Επιπλέον, θα μάθω να συνεργάζομαι και με άλλα άτομα με τη δημιουργία ομάδας,
μιας και θα μπορούμε να ανταλλάσσουμε ιδέες και γνώσεις, κάτι που το θεωρώ πολύ σημαντικό στο χώρο της πληροφορικής. Τέλος, ευελπιστώ να καταφέρω να αναπτύξω επιτυχώς όλα τα παραδοτέα στο github, και να γίνω ευέλικτη στο να εκτελώ ασκήσεις γραμμής εντολών σε νέα λειτουργικά συστήματα με τα οποία δεν είμαι εξοικειωμένη, αποκτώντας έτσι σημαντικές γνώσεις και πληροφορίες που θα με βοηθήσουν στη μετέπειτα πορεία μου.
<br><br/>


<h2><span id="Γραμμή Εντολών 1">Γραμμή Εντολών 1</span></h2>

Για την 2η εβδομάδα αποφάσισα να κάνω την άσκηση γραμμής εντολών "Performance monitoring", με τη χρήση του Hyperfine, καθώς δοκιμάζοντας αρχικά το Py-spy αντιμετώπισα ορισμένα προβλήματα τα οποία και δεν κατάφερα να επιλύσω. Έτσι, λοιπόν έκανα install το Hyperfine με την εντολή 'pkg install hyperfine'. Στη συνέχεοα, έφτιαξα ένα τελείως απλό πρόγρμμα σε Python, το οποίο εμφανίζει τα φωνήεντα στα αγγλικά και το ονόμασα vowels.py. Με την εντολή hyperfine --ignore-failure --export-markdown table1 vowels.py έτρεξε το benchmark για το συγκεκριμένο Python script. Η εντολή '--ignore-failure' χρησιμοποιήθηκε, καθώς μου έβγαζε ένα error στην αρχή το οποίο δε μπορούσα να διορθώσω, κι έτσι με αυτό το αγνοεί και εκτελείται κανονικά to benchmark. Με το '--export-markdown' παίρνω ένα αναλυτικότερο πινακάκι των αποτελεσμάτων του benchmark. 

<br/><br>

![vowels](https://user-images.githubusercontent.com/72350646/221419973-5402a8ba-d86f-46c9-8de9-fb152d4093ef.png)

<br/><br>

[-Asciinema Rec Link](https://asciinema.org/a/563027)


<br><br/>

<h2><span id="Γραμμή εντολών (no systemd)">Γραμμή εντολών (no systemd)</span></h2>

Για την 3η εβδομάδα προχώρησα στην εγκατάσταση ενός systemd-free λειτουργικού συστήματος, το Void Linux. Την εγκατάσταση αυτή την πραγματοποιήσα σε εικονική μηχανή και συγκεκριμένα σε Oracle VM VirtualBox. Ως guide για το installation ακολούθησα το [Void Linux Handbook](https://docs.voidlinux.org/installation/live-images/guide.html), αλλά ακολούθησα και την εξής οδηγεία από αυτό το [Guide](https://linuxiac.com/void-linux-installation/#4-10-partition-the-disk), προκειμένου να ενεργοποιήσω το EFI, έτσι ώστε να μη μου εμφανιστεί error κατά τη διάρκεια του install του GRUB bootloader. 

Στό παρακάτω screenshot παραθέτω την εκτέλεση της εντολής Neofetch και το αποτέλεσμα της : 

![Στιγμιότυπο οθόνης (15)](https://user-images.githubusercontent.com/72350646/222903789-e915ac63-b216-42a7-b131-ddaa34ebc9ab.png)

Επίσης, όπως φαίνεται έχω αλλάξει το hostname προκειμένου να φαίνεται το Α.Μ. μου.

[-Asciinema Rec Link](https://asciinema.org/a/564608)


