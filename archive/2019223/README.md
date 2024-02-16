# Τεχνολογία Λογισμικού
### Πετρούλα Στυλιανού Π2019223
#### [Github profile](https://github.com/PetroulaStylianou) 
#### [Η ομάδα μου](https://github.com/IonianUniversity2019)


| Εβδομάδα | Παραδοτέα| [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | Εισαγωγή| <i><a href="https://github.com/courses-ionio/sw/discussions/1170" title="Discussions">Discussions</a></i> | Εμπρόθεσμη παράδοση παραδοτέου με επιτυχή δημιουργία ομάδας, εισαγωγής και αναφοράς των στόχων μου.|
| 2 | Γραμμή εντολών (systemd) και διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας| <i><a href="https://github.com/courses-ionio/sw/discussions/1243" title="Discussions">Discussions</a></i> | Εμπρόθεσμη ολοκλήρωση παραδοτέου. Χρήση του Kali Linux και του Asciinema για ολοκλήρωση της άσκησης.|
| 3 | Γραμμή εντολών (no systemd) |  <i><a href="https://github.com/courses-ionio/sw/discussions/1329" title="Discussions">Discussions</a></i>|Εμπρόθεσμη ολοκλήρωση παραδοτέου. Χρήση του Void Linux και του Asciinema για ολοκλήρωση της άσκησης. |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά)|<i><a href="https://github.com/courses-ionio/sw/discussions/1373" title="Discussions">Discussions</a></i> |Εμπρόθεσμη παράδοση παραδοτέου. Έγιναν οι απαραίτητες αλλαγές αλλά δεν κατάφερα να τα περάσω στο βιβλίο. |
| 5 | Συμμετοχικό περιεχόμενο A1+A2 |<i><a href="https://github.com/courses-ionio/sw/discussions/1400" title="Discussions">Discussions</a></i> |Εμπρόθεσμη παράδοση παραδοτέου. Έγιναν οι απαραίτητες αλλαγές αλλά δεν κατάφερα να τα περάσω στο βιβλίο. |
| 6 | Γραμμή εντολών (no systemd, custom static blog generator)| <i><a href="https://github.com/courses-ionio/sw/discussions/1523">Discussions</a></i> |Δεν ολοκληρώθηκε.|
| 7 | Συμμετοχικό περιεχόμενο B1| <i><a href="https://github.com/courses-ionio/sw/discussions/1524">Discussions</a></i>  |Εμπρόθεσμη παράδοση παραδοτέου. Έγιναν οι απαραίτητες αλλαγές αλλά δεν κατάφερα να τα περάσω στο βιβλίο.  | 
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) | | Δεν ολοκληρώθηκε.|
| 9 | Συμμετοχικό περιεχόμενο B2| <i><a href="https://github.com/courses-ionio/sw/discussions/1531">Discussions</a></i>|Εμπρόθεσμη παράδοση παραδοτέου. Έγιναν οι απαραίτητες αλλαγές αλλά δεν κατάφερα να τα περάσω στο βιβλίο.|
| 10 | Τελική αναφορά*|  <i><a href="https://github.com/courses-ionio/sw/discussions/1654">Discussions</a></i>||
| 11 | Βίντεο Κουίζ| ||


# Εισαγωγή 

Μέσω του μαθήματος Τεχνολογία Λογισμικού αναδεικνύονται τα ζητήματα σχεδιασμού, διαχείρισης ελέγχου και διοίκησης λογισμικού που προκύπτουν κατά την ανάπτυξη έργων λογισμικού.  Ο στόχος μου είναι η εξέλιξη μου μέσα από τις εβδομαδιαίες εργασίες και τα video quiz που θα βοηθήσουν να βελτιωθώ και να αποκτήσω γνώσεις πάνω σε εργαλεία που ίσως χρειαστούν στο μέλλον. Ταυτόχρονα, το κομμάτι της ομαδικότητας θα βοηθήσει σε μελλοντικές συνεργασίες που μπορεί να προκύψουν σε κάποια δουλειά. Ελπίζω, στο τέλος του εξαμήνου και με την ολοκλήρωση του μαθήματος να έχω εκπληρώσει τους στόχους μου.

# Άσκηση Γραμμής Εντολών 

Σε αυτό το παραδοτέο μας ζητήθηκε να κάνουμε μία άσκηση γραμμής εντολών. Η άσκηση που επέλεξα να κάνω είναι η άσκηση performance monitoring από τις ασκήσεις software. Σε αυτή την άσκηση έπρεπε να δούμε τις επιδόσεις της python που έχουμε στο λογισμικό και να της οπτικοποιήσουμε με χρώματα ή γραμμές για να φανεί η διαδικασία. 
Η άσκηση πραγματοποιήθηκε σε λογισμικό kali linux.

Εγκατέστησα το hyperfine με την εντολή <kbd>xbps-install -S hyperfine</kbd>.

- Για εκτέλεση αναφοράς χρησιμοποίησα την εντολή <kbd>hyperfine ‘sleep 0.3’</kbd>

- Για αυτόματο καθορισμό αριθμού εκτελέσεων κάθε εντολής από προεπιλογή και εκτέλεση 10 εκτελέσεις συγκριτικής αξιολόγησης, χρησιμοποίησα την εντολή <kbd>hyperfine —runs 5 ’sleep 0.3’</kbd>

- Για έλεγχο μεγέθους βήματος, χρησιμοποίησα την εντολή <kbd>hyperfine —parameter-scan delay 0.3 0.7 -D 0.2 ‘sleep {delay}’</kbd>

[Asciinema](https://asciinema.org/a/561732)

# Άσκηση Γραμμής Εντολών 

Στο τρίτο παραδοτέο μας ζητήθηκε η εγκατάσταση ενός λογισμικού χωρίς systemd. Για το σκοπό αυτό επέλεξα την χρήση του void linux με το οποίο πραγματοποίησα την άσκηση γραμμής εντολών που εκτέλεσα και στο προηγούμενο παραδοτέο.

[Asciinema](https://asciinema.org/a/561001)

# Κατασκευή βιβλίου Α2

Στο παραδοτέο αυτό αποφάσισα να ασχοληθώ με την προσθήκη μιας παραγράφου στο κεφάλαιο 8 του βιβλίου σας. Το κομμάτι παραγράφου που πρόσθεσα αφορά τον υπολογιστή Xerox Alto.

Σύνδεσμοι:

- [media.md](https://github.com/PetroulaStylianou/kallipos/blob/master/P2019223/media.md)
- [media.lua](https://github.com/PetroulaStylianou/kallipos/blob/master/media.lua)
- [make-latex.sh](https://github.com/PetroulaStylianou/kallipos/blob/master/make-latex.sh)
- [asciinema](https://asciinema.org/a/j48D7EjFyDWH2ndL43GFfHpVi)


# Συμμετοχικό περιεχόμενο A1+A2

Πρώτη εργασία για συμμετοχικό περιεχόμενο Α1+Α2 αποφάσισα να κάνω για την γλώσσα προγραμματισμού Javascript και για το λογισμικό OpenBsd.

## Συμμετοχικό περιεχόμενο A1
|gallery | images|
| --- | --- | 
|[JavaScript.md](https://github.com/PetroulaStylianou/_gallery/blob/master/JavaScript.md)|[JavaSxcript](https://github.com/PetroulaStylianou/images_/blob/master/JavaScript.png) / [JavaSxcript-thumb](https://github.com/PetroulaStylianou/images_/blob/master/JavaScript-%20thumb.png)
|[OpenBsd.md](https://github.com/PetroulaStylianou/_gallery/blob/master/OpenBsb.md)|[OpenBsd](https://github.com/PetroulaStylianou/images_/blob/master/OpenBsd.png) / [OpenBsd-thumb](https://github.com/PetroulaStylianou/images_/blob/master/OpenBsd-%20thumb.png)

## Συμμετοχικό περιεχόμενο A2
|timeline| slides|
| --- | --- | 
|[Programming](https://github.com/PetroulaStylianou/site/blob/master/_timeline/programming.md)|[programming](https://github.com/PetroulaStylianou/site/blob/master/_slides/programming.md)
|[Systems](https://github.com/PetroulaStylianou/site/blob/master/_timeline/systems.md)|[archetypes](https://github.com/PetroulaStylianou/site/blob/master/_slides/archetypes.md)

# Συμμετοχικό περιεχόμενο Β1

Σε αυτό το παραδοτέο μας ζητήθηκε μία νέα έρευνα με παρόμοια περίπτωση με τις θεματικές που διαλέξαμε στο 5ο παραδοτέο. Γι' αυτό, επέλεξα να ασχοληθώ με το λογισμικό OpenBsd και να ψάξω περισσότερες λεπτομέρειες.

|_case-study| _includes|images|
| --- | --- | --- |
|[OpenBsd](https://github.com/PetroulaStylianou/site/blob/master/_case-study/OpenBsd.md)|[cs- OpenBsd](https://github.com/PetroulaStylianou/site/blob/master/_includes/cs-%20OpenBsd.md)| [OpenBsd](https://github.com/PetroulaStylianou/images_/blob/master/OpenBsd.png) / [OpenBsd-thumb](https://github.com/PetroulaStylianou/images_/blob/master/OpenBsd-%20thumb.png)|

# Συμμετοχικό περιεχόμενο Β2

Στο συγκεκριμένο παραδοτέο εν συνεχεία του συμμετοχικού περιεχομένου Β1, ζητήθηκε η δημιουργία μιας βιογραφίας. Γιαυτό τον λόγο αποφάσισα να ασχοληθώ με την βιογραφία του δημιουργού του OpenBsd, theo de Raadt.

|_biography|images|
| --- | --- |
|[Theo de Raadt.md](https://github.com/PetroulaStylianou/site/blob/master/_biography/Theo%20de%20Raadt.md)/[bio-Theo de Raadt.md](https://github.com/PetroulaStylianou/site/blob/master/_biography/bio-Theo%20de%20Raadt.md)| [Theo de Raadt](https://github.com/PetroulaStylianou/images_/blob/master/Theo%20de%20Raadt%20.jpeg) / [Theo de Raadt-thumb](https://github.com/PetroulaStylianou/images_/blob/master/Theo%20de%20Raadt-thumb.jpeg)|

# Τελική αναφορά

Φτάνοντας στο τέλος του εξαμήνου και ολοκληρώνοντας την αναφορά της εργασίας μου, θα ήθελα να αναφέρω τις γνώσεις και τις εμπειρίες που κέρδισα από το συγκεκριμένο μάθημα. Όπως είχα αναφέρει και στους στόχους μου, η τεχνολογία λογισμικού κατάφερε να με εξοπλίσει με τις κατάλληλες δεξιότητες πάνω στα λειτουργικά συστήματα. Ειδικότερα έκανα χρήση των συστημάτων Kali και Void Linux, συστήματα με και χωρίς systemd και αρκετά άγνωστα σε εμένα, με τα οποία πέτυχα να ολοκληρώσω τις ασκήσεις γραμμής εντολών που απαιτούνταν. Επιπλέον, μέσα από τα εβδομαδιαία κουίζ κατανόησα καλύτερα τον τρόπο με τον οποίο δουλεύουν τα λειτουργικά συστήματα και την επίδραση που έχουν στην καθημερινή και κοινωνική ζωή. Όσον αφορά την ομαδικότητα εν μέρει επιτεύχθηκε, καθώς υπήρχε επικοινωνία με τους συμφοιτητές μου μέσω των discussions, με τον σχολιασμό παραδοτέων.

Η εξέταση μου πραγματοποιήθηκε από τον κ. Αριστείδη Βραχάτη ο οποίος μου επισήμαινε κάποιες αλλαγές που έπρεπε να γίνουν στην αναφορά, όπως είναι η βελτίωση της αυτοαξιολόγησης. Απαιτούνταν πιο λεπτομερής περιγραφή στο συγκεκριμένο κομμάτι. Επίσης, μου επισήμαινε ότι είναι σημαντικό να προστεθούν οι αλλαγές στο βιβλίο κάτι το οποίο τελικά δεν κατάφερα να υλοποιήσω. 

# Σχόλια σε αναφορές
- [Σχόλιο 1](https://github.com/courses-ionio/sw/pull/1712#issuecomment-1556186584)
- [Σχόλιο 2](https://github.com/courses-ionio/sw/pull/1662#issuecomment-1556188675)

# Βίντεο Κουίζ
|Βίντεο Κουίζ|Ολοκλήρωση|
| --- | --- |
|Alan Kay at MIT-EECS 1998 Fall Semester Colloquium Series|✔️|
|Ted Nelson -- Computers for Cynics|✔️|
|Alan Kay - Could Computing Be Simpler Than It Seems To Be?|✔️|
|Bret Victor - The Future of Programming|✔️|
|Alan Kay - Programming Languages & Programming (2013)|✔️|
|Alan Kay Turing Lecture with dynamic content|✔️|
|Alan Kay - Programming and Scaling|✔️|
|Extracting Energy from the Turing Tarpit|✔️|
|Back to the Future of Software Development 4/23/2003 (VPRI 785)|✔️|
|VCF East 2019 -- Brian Kernighan interviews Ken Thompson|✔️|







