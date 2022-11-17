# Τεχνολογία Λογισμικού 
## Μαρία Δαραβίγκα 
## Π2015076

| Εβδομάδα | [Όλα τα παραδοτέα βρίσκονται στην ίδια σελίδα της τελικής αναφοράς](https://courses-ionio.github.io/help/deliverables/) με τα προσωπικά στοιχεία σας (Όνομα, ΑΜ, github profile) και μαζί με αυτόν εδώ τον πίνακα περιεχομένων | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | [Eισαγωγή](#1-εισαγωγή)| | |
| 2 | [βιογραφικό και δημιουργία ομάδας](#2-βιογραφικό) | | |
| 3 | Βιβλίο Α παραδοτέο | | |
| 4 | Άσκηση γραμμής εντολών | | |
| 5 | Συμμετοχικό περιεχόμενο A1+A2 | | |
| 6 | Άσκηση γραμμής εντολών | | |
| 7 | βιογραφικό | | |
| 8 | Αίτημα ενσωμάτωσης στην ιστοσελίδα | | |
| 9 | Άσκηση γραμμής εντολών | | |
| 10 | συμμετοχικό περιεχόμενο B1+B2 | | |
| 11 | Άσκηση γραμμής εντολών | | |
| 12 | Τελική αναφορά* | | |

</br> </br>
## 1. Eισαγωγή
  Οι στόχοι μου και οι προσδοκίες μου για το μάθημα τεχνολογιες λογισμικού είναι να εξοικιωθώ πλήρως με το εργαλείο GitHub, να μάθω να γράφω προγράμματα 
σε HTML γλώσσα και να διαχειρίζομαι ευκολότερα Linux. Επίσης θα ήθελα μέσω της ομαδικής εργασίας να αλληλεπιδράσω με τους συναδέλφους μου και να βελτιώσω τις ικανότητες μου στην ανάπτυξη λογισμικών συστημάτων και εφαρμογών λογισμικού. Επιπλέον μέσω από τα εβδομαδιαία βίντεο κουίζ αλλά και από την ίδια την δομή του μαθήματος να αποκτήσω την δυνατότητα να λύνω όσο τον δυνατών περισσότερα προβλήματα και να μπω ακόμα περισσότερο στο τρόπο σκέψης της πληροφορικής.(Δηλαδή στην λογική πως αν σπάσεις ένα πρόβλημα σε μικρότερα υπο-προβλήματα είναι ευκολότερη η επίλυση του.)
</br></br>
## 2. Βιογραφικό
  Σε αυτό το παραδοτέο δημιούργησα το βιογραφικό μου (Html, Css, Javascript).

[Το αποθετήριο του βιογραφικού μου](https://github.com/Mariadar97/mycv/)

[Github pages βιογραφικού](https://mariadar97.github.io/mycv/)

![Screenshot 2022-11-17 at 17 30 00](https://user-images.githubusercontent.com/22714123/202488303-eff2525a-f159-4793-b8ac-c64039ba91f9.png)

[Link Discussions](https://github.com/courses-ionio/help/discussions/1651)
</br></br>

## 3. Κατασκευή Βιβλίου Α Μέρος
  Σε αυτό το παραδοτέο έγιναν οι κατάλληλες μετατροπές στο make-latex.sh και τις κατάλληλες προσθήκες φακέλων ώστε το βιβλίο από .txt μορφή σε πολλά αρχεία να συγχωνευθεί σε ένα τελικό αρχείο pdf, με την χρήση ενός lua filter.
[Repository](https://github.com/Mariadar97/kallipos)
[Picture σημείωσης](https://github.com/Mariadar97/kallipos/blob/master/picture/commentpicture.png)
[make-latex.sh](https://github.com/Mariadar97/kallipos/blob/master/make-latex.sh)
[lua filter](https://github.com/Mariadar97/kallipos/blob/master/comment.lua)
[Link Discussions](https://github.com/courses-ionio/help/discussions/1653)

![commentpicture](https://user-images.githubusercontent.com/22714123/202536849-f30ef4cd-9195-48c2-9770-abd79b6d2da0.png)

</br></br>
## 4. Άσκηση γραμμής εντολών

Για τις ασκήσεις γραμμής εντολών διάλεξα το Distro Artix Linux . Το Artix Linux δημιουργήθηκε όταν τα Arch Linux ξεκίνησαν να χρησιμοποιούν το system-d σαν μία system-d-less εκδοχή των Arch Linux. Επιπλέον κρίσιμο ρόλο σε αυτήν μου την επιλογή έπαιξε και το γεγονός των τεράστιων active community των arch και των artix αντίστοιχα, όπου θα μπορέσω και εγώ να βρω τις κατάλληλες απαντήσεις σε προβλήματα που πιθανώς προκύψουν.
Σε αυτό το παραδοτέο αρχικά δημιουργήθηκε ένα αρχείο linescounter.sh το οποίο μετράει τις γραμμές και των αριθμό λέξεων .txt αρχείων(ως είσοδο δίνεται ένα κεφάλαιο από το βιβλίο από το /kallipos/text) και επιπλέον χρησιμοποιήθηκε το click με σκοπό να μας προβάλει στην οθόνη έναν χαιρετισμό ανάλογα με το όνομα που θα δόσουμε ως είσοδο.( Maria Daravigka p2015076)
</br>
[![asciicast](https://asciinema.org/a/538463.svg)](https://asciinema.org/a/538463)
</br>
[clicktest.py](https://github.com/Mariadar97/paradoteo4/blob/main/clicktest.py)
[linescounter.sh](https://github.com/Mariadar97/paradoteo4/blob/main/linescounter.sh)
[Discussions Link](https://github.com/courses-ionio/help/discussions/1659)
