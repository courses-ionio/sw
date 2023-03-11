# Τεχνολογία Λογισμικού
### Πετρούλα Στυλιανού 
### ΑΜ: Π2019223
#### [Github profile](https://github.com/PetroulaStylianou)
#### [Η ομάδα μου](https://github.com/IonianUniversity2019)


| Εβδομάδα | Παραδοτέα| [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | <li><a href="#Εισαγωγή"></span> <span class="toctext">Εισαγωγή</span></a> | <i><a href="https://github.com/courses-ionio/sw/discussions/1170" title="Discussions">Discussions</a></i> | Εμπρόθεσμη παράδοση παραδοτέου με επιτυχή δημιουργία ομάδας, εισαγωγής και αναφοράς των στόχων μου.|
| 2 | <li><a href="#Γραμμή εντολών (systemd) και διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας"></span> <span class="toctext">Γραμμή εντολών (systemd) και διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας</span></a> | <i><a href="https://github.com/courses-ionio/sw/discussions/1243" title="Discussions">Discussions</a></i> | Εμπρόθεσμη ολοκλήρωση παραδοτέου. Χρήση του Kali Linux και του Asciinema για ολοκλήρωση της άσκησης.|
| 3 | <li><a href="#Γραμμή εντολών (no systemd)"></span> <span class="toctext">Γραμμή εντολών (no systemd)</span></a>  |  <i><a href="https://github.com/courses-ionio/sw/discussions/1329" title="Discussions">Discussions</a></i>|Εμπρόθεσμη ολοκλήρωση παραδοτέου. Χρήση του Void Linux και του Asciinema για ολοκλήρωση της άσκησης. |
| 4 | <li><a href="#Κατασκευή του βιβλίου Α2 (συνεργατικά)"></span> <span class="toctext">Κατασκευή του βιβλίου Α2 (συνεργατικά)</span></a>|<i><a href="https://github.com/courses-ionio/sw/discussions/1373" title="Discussions">Discussions</a></i> |Εμπρόθεσμη παράδοση παραδοτέου |
| 5 | <li><a href="#Συμμετοχικό περιεχόμενο A1+A2"></span> <span class="toctext">Συμμετοχικό περιεχόμενο A1+A2</span></a> | | |
| 6 |  <li><a href="#Γραμμή εντολών (no systemd, custom static blog generator)"></span> <span class="toctext">Γραμμή εντολών (no systemd, custom static blog generator)</span></a>| | |
| 7 | <li><a href="#συμμετοχικό περιεχόμενο B1"></span> <span class="toctext">συμμετοχικό περιεχόμενο B1</span></a>| | | 
| 8 | <li><a href="#Κατασκευή του βιβλίου Β2 (συνεργατικά)"></span> <span class="toctext">Κατασκευή του βιβλίου Β2 (συνεργατικά)</span></a> | ||
| 9 | <li><a href="#συμμετοχικό περιεχόμενο B2"></span> <span class="toctext">συμμετοχικό περιεχόμενο B2</span></a> | ||
| 10 | <li><a href="#Τελική αναφορά*"></span> <span class="toctext">Τελική αναφορά*</span></a> | | |


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

