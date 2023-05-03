# Τεχνολογία Λογισμικού 

#### Ονοματεπώνυμο: Ελένη Τηλαβερίδου

#### ΑΜ: Π2019061

#### e-mail: p19tila@ionio.gr

#### Github: [Tilav](https://github.com/tilav)

#### Ομάδα: [Ranger-Power](https://github.com/Ranger-Power)



| Εβδομάδα | [Όλα τα παραδοτέα βρίσκονται στην ίδια σελίδα της τελικής αναφοράς](https://epidrome.github.io/teaching/deliverables/) με τα προσωπικά στοιχεία σας (Όνομα, ΑΜ, github profile) και μαζί με αυτόν εδώ τον πίνακα περιεχομένων | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | [Δημιουργία ομάδας](https://epidrome.github.io/teaching/team/) + [Φορκ και δημιουργία σελίδας τελικής αναφοράς](https://epidrome.github.io/teaching/guide/), [προσθήκη πίνακα περιεχομένων](https://raw.githubusercontent.com/courses-ionio/sw/master/README.md), [συγγραφή της εισαγωγής](https://epidrome.github.io/teaching/intro/), αποστολή της εισαγωγής [για σχολιασμό στην συζήτηση](https://github.com/courses-ionio/sw/discussions/categories/show-and-tell) και καταγραφή του συνδέσμου συζήτησης δίπλα --> | [Discussion link](https://github.com/courses-ionio/sw/discussions/1174) | |
| 2 | [Γραμμή εντολών](https://epidrome.github.io/teaching/cli) (systemd) και [διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας](https://epidrome.github.io/teaching/team) | [Discussion link](https://github.com/courses-ionio/sw/discussions/1259) | |
| 3 | Γραμμή εντολών (no systemd) | [Discussion link](https://github.com/courses-ionio/sw/discussions/1315) | |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά) | | |
| 5 | Συμμετοχικό περιεχόμενο A1 + A2 | [Discussion link](https://github.com/courses-ionio/sw/discussions/1439) | |
| 6 | Γραμμή εντολών (no systemd, custom static blog generator) | [Discussion link](https://github.com/courses-ionio/sw/discussions/1483) | |
| 7 | συμμετοχικό περιεχόμενο B1 | [Discussion link](https://github.com/courses-ionio/sw/discussions/1626) | |
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) | | |
| 9 | συμμετοχικό περιεχόμενο B2 | [Discussion link](https://github.com/courses-ionio/sw/discussions/1627) | |
| 10 | Τελική αναφορά* | | |



## 1. Εισαγωγή

Στο μάθημα "Τεχνολογίες Διαδικτύου" ευελπιστώ να συμπληρώσω τις γνώσεις και τις δεξιότητες που απέκτησα από το μάθημα "Επικοινωνία Ανθρώπου-Υπολογιστή". Σκοπεύω να βελτιωθώ στη χρήση του GitHub, των συστημάτων UNIX, της γραμμής εντολών και να ολοκληρώσω τελικά την αναφορά μου με επιτυχία. Η ενασχόλησή μου με τη Yoga, με ώθησε να επιλέξω ως θέμα της αναφορά μου, την άσκηση και την βελτίωσή της μέσω διαδραστικής τεχνολογίας και εφαρμογών. Στην ολοκλήρωση των παραδοτέων, θα συνεισφέρει σίγουρα η ομάδα μου, με συζήτηση και ανταλλαγή γνώσεων.


## 2. Γραμμή εντολών (systemd)

Για το παραδοτέο της 2ης εβδομάδας εγκατέστησα τα Arch Linux σε usb.

[![asciicast](https://asciinema.org/a/rrzuF7GYGr1L1dZXMbjO3Xo4c.svg)](https://asciinema.org/a/rrzuF7GYGr1L1dZXMbjO3Xo4c)

Επίσης, υλοποίησα την άσκηση γραμμής εντολών: "Send notifications to your desktop-mobile". Με τη χρήση του ntfy και του Visual Studio Code, έγραψα ένα python script, το οποίο επιλέγει μέσα από μια λίστα, ένα τυχαίο motivation quote και το στέλνει στο κινητό τηλέφωνο του χρήστη.
Σκοπός του python κωδικά μου είναι η αποστολή μηνυμάτων στον χρήστη αφού έχει τελειώσει με επιτυχία το workout του σε μια fitness εφαρμογή. Με τη σύνδεση του script με μια τέτοια εφαρμογή, η αποστολη θα γίνεται πατώντας το κουμπί "Workout Done".

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![IMG_8354(5)(3)](https://user-images.githubusercontent.com/72463627/221252040-816225e5-89b1-470e-8af5-4ac292af5298.jpg)

## 3. Γραμμή εντολών (no systemd)

Για το 3ο παραδοτέο εγκατέστησα το Alpine Linux, το οποίο δεν χρησιμοποιεί το systemd ως προεπιλεγμένο σύστημα διαχείρησης εκκίνησης και υπηρεσιών, αλλά το OpenRC, ένα εναλλακτικό σύστημα που παρέχει παρόμοια χαρακτηριστικά με το systemd. Βασική διαφορά του με το systemd είναι ότι το δεύτερο χρησιμοποιεί έναν κεντρικό daemon για τη διαχείριση όλων αυτών των υπηρεσιών και λειτουργιών ενώ το openRC χρησιμοποιεί αυτόνομους deamons.
Κάποιες επιπλέον πληροφορίες σχετικά με το Alpine Linux:
* Έχει πολύ μικρό μέγεθος εγκατάστασης και απαιτεί λιγότερη μνήμη και αποθηκευτικό χώρο από άλλες διανομές Linux.
* Λόγω χαμηλής ζήτησης του συγκεκριμένου linux και της χρήσης της musl ως βιβλιοθήκη C, θεωρείται πιο ασφαλές και ανθεκτικό σε επιθέσεις.
* Είναι λιγότερο πιθανό να παρουσιάσει προβλήματα στο μέλλον λόγω της απλότητας του συστήματος.

[![asciicast](https://asciinema.org/a/iKem3vMVbeeCiTnXIxhp9Fq5e.svg)](https://asciinema.org/a/iKem3vMVbeeCiTnXIxhp9Fq5e)

## 4. Κατασκευή του βιβλίου Α2 (συνεργατικά)

#### ! Στο συγκεκριμένο παραδοτέο αντιμετωπίζω το error "pandoc-fignos: Bad reference: fig <όνομα εικόνας>" για το οποίο δεν έχω βρει λύση ακόμα. Η προσθήκη μου θα γίνει στο Κεφάλαιο 8: "Τεχνολογία" και το αρχείο md είναι το παρακάτω:


title: Αθλητισμός και Βιντεοπαιχνίδια
caption: 'Οι αθλητικές δραστηριότητες είναι μια "ασφαλής" ιδέα για βιντεοπαιχνίδι, αφού ο αθλητισμός αποτελεί μεγάλο ψυχαγωγικό μέσο για πολλούς ανθρώπους. Τα πρώτα βιντεοπαιχνίδια αφορούσαν το τένις και το ping pong, τα οποία λόγω της ταυτόχρονης αλληλεπίδρασης με το παιχνίδι μέχρι δύο χρηστών, μπορούσαν να οπτικοποιηθούν με ευκολότερο τρόπο. Ανάλογα με τον τρόπο οπτικοποίησης, ο χρήστης αλληλεπιδρά διαφορετικά με το παιχνίδι-υπολογιστή. Χρησιμοποιεί με διαφορετικό τρόπο τα κουμπιά, πλήκτρα, analog sticks κ.α. όχι μόνο λόγω της διαφορετικής κατασκευής του κάθε παιχνιδιού αλλά και λόγω της ανάγκης για όσο το δυνατόν πιο ρεαλιστικής αίσθησης του αθλήματος, ανάλογα με την εικόνα που βλέπει. Με άλλα λόγια, ένα βιντεοπαιχνίδι αθλητικού περιεχομένου δημιουργεί άλλη εντύπωση στον χρήστη, ανάλογα με την γωνία της κάμερας (first-person, second-person, third-person, top-down/isometric etc.)'
name: Ελένη Τηλαβερίδου
id: Π2019061 


## 5. Συμμετοχικό περιεχόμενο A1 + A2

Στο συγκεκριμένο παραδοτέο πρόσθεσα το Lifecycle stationary bike και το Peloton bike στα [images](https://github.com/tilav/images), gallery: [Lifecycle](https://github.com/tilav/_gallery/blob/master/lifecyclebike.md) + [Peloton](https://github.com/tilav/_gallery/blob/master/pelotonbike.md), χρονολόγιο: [Lifecycle](https://github.com/tilav/site/blob/2019061/_timeline/prototypes.md) + [Peloton](https://github.com/tilav/site/blob/2019061/_timeline/systems.md) και τις διαφάνειες: [Lifecycle](https://github.com/tilav/site/blob/2019061/_slides/styles.md) + [Peloton](https://github.com/tilav/site/blob/2019061/_slides/hypermedia.md).

Οι προσθήκες μου: 

### Lifecycle stationary bike (1968)

![lifecyclebike](https://user-images.githubusercontent.com/72463627/226211998-dcf53595-34ba-4c65-b4c6-c4f62cd7b56e.png)

### Peloton bike (2013)

![pelotonbike](https://user-images.githubusercontent.com/72463627/226212008-ef073558-ee2d-4a80-bd9b-4ab412627998.jpg)

### Οι προσθήκες μου στην ιστοσελίδα μου:

* [Στατικό ποδήλατο Lifecycle](https://tilav-sw.netlify.app//gallery/lifecyclebike/)
* [Ποδήλατο Peloton](https://tilav-sw.netlify.app//gallery/pelotonbike/)
* Χρονολόγιο: [Lifecycle stationary bike](https://tilav-sw.netlify.app//timeline/prototypes/) - [Peloton bike](https://tilav-sw.netlify.app//timeline/systems/)
* Διαφάνειες: [Lifecycle stationary bike](https://tilav-sw.netlify.app//slides/styles/) - [Peloton bike](https://tilav-sw.netlify.app//slides/hypermedia/)

### Οι προσθήκες μου στην [ιστοσελίδα της ομάδας μου](https://ranger-power.netlify.app/):

* [Στατικό ποδήλατο Lifecycle](https://ranger-power.netlify.app//gallery/lifecyclebike/)
* [Ποδήλατο Peloton](https://ranger-power.netlify.app//gallery/pelotonbike/)
* Χρονολόγιο: [Lifecycle stationary bike](https://ranger-power.netlify.app//timeline/prototypes/) - [Peloton bike](https://ranger-power.netlify.app//timeline/systems/)
* Διαφάνειες: [Lifecycle stationary bike](https://ranger-power.netlify.app//slides/styles/) - [Peloton bike](https://ranger-power.netlify.app//slides/hypermedia/)

### Τα Pull Request στην ομάδα μου:

* images: [Pull Request](https://github.com/Ranger-Power/images/pull/2)
* _gallery: [Pull Request](https://github.com/Ranger-Power/_gallery/pull/2)
* site: [Pull Request](https://github.com/Ranger-Power/site/pull/2)

## 6. Γραμμή εντολών (no systemd, custom static blog generator)

Σε αυτό το παραδοτέο έφτιαξα μια ιστοσελίδα-blog σχετική με το θέμα της αναφοράς μου, χρησιμοποιώντας το jekyll.

* [Το blog μου](https://tilav.github.io/mysite/)
* [Το αποθετήριο του blog μου](https://github.com/tilav/mysite)

![static site](https://user-images.githubusercontent.com/72463627/235916836-abc70d4c-3a86-4787-a93f-05537d4d5cc9.gif)

## 7. συμμετοχικό περιεχόμενο B1

Στο συμμετοχικό περιεχόμενο Β1 αποφάσισα να προσθέσω ως μελέτη περίπτωσης το Virtual Tennis
* [Η μελέτη περίπτωσης που πρόσθεσα](https://ranger-power.netlify.app/case-study/virtual-tennis/)
* [Το pull request στην ιστοσελίδα της ομάδας μου](https://github.com/Ranger-Power/site/pull/5)
* [Το pull request στα images](https://github.com/Ranger-Power/images/pull/5)

![vt1](https://user-images.githubusercontent.com/72463627/235810908-c765d005-e390-48d4-b0e7-99c086b19513.jpg)

## 9. συμμετοχικό περιεχόμενο B2

Στο συμμετοχικό περιεχόμενο Β2 αποφάσισα να προσθέσω την βιογραφία του James Park
* [Η βιογραφία που πρόσθεσα](https://ranger-power.netlify.app/biography/james-park/)
* [Το pull request στην ιστοσελίδα της ομάδας μου](https://github.com/Ranger-Power/site/pull/5)
* [Το pull request στα images](https://github.com/Ranger-Power/images/pull/5)

![jamespark](https://user-images.githubusercontent.com/72463627/235810932-d9316f6b-a425-483f-bf66-bc28d921592c.jpeg)

## 10. Τελική αναφορά

## Βίντεο Κουίζ

|Χ| Τίτλος | Πραγματοποιήθηκαν | Εμπρόθεσμα |
| ---- | ---- | ---- | ---- |
| 1 | Alan Kay at MIT-EECS 1998 Fall Semester Colloquium Series (VPRI 834) |<p align = "center">:heavy_check_mark:</p>|<p align = "center">:heavy_check_mark:</p>|
| 2 | Ted Nelson -- Computers for Cynics [full version]  |<p align = "center">:heavy_check_mark:</p>|<p align = "center">:heavy_check_mark:</p>|
| 3 | Alan Kay - Could Computing Be Simpler Than It Seems To Be? |<p align = "center">:heavy_check_mark:</p>|<p align = "center">:heavy_check_mark:</p>|
| 4 | Bret Victor - The Future of Programming |<p align = "center">:heavy_check_mark:</p>|<p align = "center">:heavy_check_mark:</p>|
| 5 | Alan Kay - Programming Languages & Programming (2013) |<p align = "center">:heavy_check_mark:</p>|<p align = "center">:heavy_check_mark:</p>|
| 6 | Extracting Energy from the Turing Tarpit |<p align = "center">:heavy_check_mark:</p>|<p align = "center">:heavy_check_mark:</p>|
