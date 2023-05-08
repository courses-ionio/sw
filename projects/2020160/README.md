# **Τεχνολογία Λογισμικού**

### Ονοματεπώνυμο: Στυλιανή Αδάμ

### Αριθμός Μητρώου: Π2020160

### Github Organization: [lapis-lazuli-ore-block](https://github.com/lapis-lazuli-ore-block)

## Περιεχόμενα

| Εβδομάδα | Παραδοτέα| Σύνδεσμος στην εβδομαδιαία παρουσίαση προόδου στις συζητήσεις | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | Δημιουργία ομάδας, Προσθήκη πίνακα περιεχομένων, Συγγραφή της εισαγωγής | [Παραδοτέο 1](https://github.com/courses-ionio/sw/discussions/1195) | Εντάχθηκα σε ομάδα και έθεσα τους στόχους μου στην εισαγωγή μου, παράλληλα ολοκλήρωσα και το 1ο βίντεο κουίζ |
| 2 | Γραμμή εντολών (systemd) και διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας | [Παραδοτέο 2](https://github.com/courses-ionio/sw/discussions/1294)| |
| 3 | Γραμμή εντολών (no systemd) | [Παραδοτέο 3](https://github.com/courses-ionio/sw/discussions/1349) | |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά) |[Παραδοτέο 4](https://github.com/courses-ionio/sw/discussions/1452) | |
| 5 | Συμμετοχικό περιεχόμενο A1 + A2 |[Παραδοτέο 5](https://github.com/courses-ionio/sw/discussions/1453) | |
| 6 | Γραμμή εντολών (custom static blog generator) |[Παραδοτέο 6](https://github.com/courses-ionio/sw/discussions/1716) | |
| 7 | Συμμετοχικό περιεχόμενο B1 |[Παραδοτεό 7](https://github.com/courses-ionio/sw/discussions/1717) | |
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) |[Παραδοτέο 8](https://github.com/courses-ionio/sw/discussions/1718) | |
| 9 | Συμμετοχικό περιεχόμενο B2 |[Παραδοτέο 9](https://github.com/courses-ionio/sw/discussions/1719) | |
| 10 | Τελική αναφορά |[Παραδοτέο 10](https://github.com/courses-ionio/sw/discussions/1720) | |


## Εισαγωγή

Στο παρόν μάθημα, Τεχνολογία Λογισμικού, αποσκοπώ στην εκμάθηση των πραγμάτων που κρύβονται πίσω από το λογισμικό, δηλαδή για τον σχεδιασμό και την αρχιτεκτονική. Θα ήθελα να αναπτύξω κάποιου είδους διεπαφή με τον χρήστη αλλά και να μάθω πως διατηρούνται και εξελίσσονται οι τεχνολογίες, με στόχο πάντα την επικαιρότητα του λογισμικού.

Συγχρόνως, εκτός από τα βασικά σχετιζόμενα πράγματα με την τεχνολογία λογισμικού και την ανάπτυξή της, θα ήθελα να καταφέρω να συνδυάσω την θεωρία με την πράξη. Οι ασκήσεις γραμμής εντολών (σε system και no systemd) και τα εβδομαδιαία βίντεο κουίζ θα αυξήσουν τους προβληματισμούς μου. 

Σε συνεργατικό επίπεδο, η επαφή με τα υπόλοιπα μέλη της ομάδας μου και τους συμφοιτητές μου γενικότερα, θα ενισχύσουν το ομαδικό πνεύμα και θα καλλιεργήσουν τις ομαδικές μου δεξιότητες έτσι ώστε να αποφευχθούν οι ασάφειες μεταξύ των μελών. Έτσι θα δημιουργηθεί το κατάλληλο κλίμα, το οποίο θα οδηγήσει την ομάδα στην σωστή κατεύθυνση.

Πάντως σε κάθε περίπτωση με την ολοκλήρωση του μαθήματος θα ήθελα να έχω αντιληφθεί την έννοια «Τεχνολογία Λογισμικού» και να μπορώ πρακτικά να έχω τις γνώσεις για τον σχεδιασμό και την ανάπτυξη ενός προγράμματος λογισμικού.   


## Γραμμή εντολών (systemd)

Για το παραδοτέο, επέλεξα να υλοποιήσω τις ασκήσεις γραμμής εντολών στο λειτουργικό σύστημα των Arch Linux. Τα Arch διαθέτουν systemd και υπάρχουν αρκετοί λόγοι για να επιλέξει ένας χρήστης κάτι ανάλογο. Πρώτα απ’ όλα με systemd προσφέρεται μια εύκολη διαχείριση του συστήματος και ο χρόνος εκκίνησης είναι σημαντικά βελτιωμένος ως προς την ταχύτητα, συγκριτικά με ένα παραδοσιακό σύστημα εκκίνησης init. Επίσης το systemd παρέχει χαρακτηριστικά ασφάλειας όπως για παράδειγμα δικαιώματα χρήστη. Συγχρόνως χάρη στο systemd υπάρχει μια ευέλικτη δομή ρύθμισης για να μπορούν οι χρήστες να προσαρμόσουν το σύστημα τους στις ανάγκες τους. Τέλος, η τεράστια δημοτικότητα, συνεπάγεται και την εκτενή τεκμηρίωση για βοήθεια και υποστήριξη.

Με ανάλογο τρόπο σκέψης επέλεξα τα Arch Linux, μιας και τα είχα χρησιμοποιήσει ξανά ως λειτουργικό σύστημα για το μάθημα Επικοινωνία Ανθρώπου Υπολογιστή. Ταυτόχρονα, υπάρχει πληθώρα πληροφοριών και οδηγών για την εγκατάσταση τους και την «επέκταση» τους. Ως πρώτο βήμα, έφτιαξα ένα VM με τα Arch και έπειτα και ένα usb. Μετά από μερικές εβδομάδες αποφάσισα να εγκαταστήσω γραφικό περιβάλλον για να δω και αυτή την διαδικασία. Παρακάτω ακολουθούν τα αντίστοιχα Asciinema.

α) Arch Linux σε VM
 
 Στην αρχή δεν είχα ορίσει όνομα για τον user όπως φαίνεται:

- [Asciinema](https://asciinema.org/a/0zs0f3493LKScO5mxiEF0Day9)

Αλλά στην πορεία πρόσθεσα:
- [Asciinema](https://asciinema.org/a/kBQFGvYdNn5oWPUUBTp3WaAsl)

β) Arch Linux σε USB

- [Asciinema](https://asciinema.org/a/mWGsSMZhJzuokXJCleN3ZAAWf)

Παράλληλα,  υλοποίησα και τις ακόλουθες ασκήσεις γραμμής εντολών. Η πρώτη ήταν το Hyperfine, δηλαδή την παρακολούθηση της απόδοσης ενός κώδικα σε python ( benchmark). Χρησιμοποίησα το αρχείο model.py, ένα αρχείο με κάποιες υλοποιημένες συναρτήσεις ενός δικού μου project.

- [Asciinema](https://asciinema.org/a/CEyyNK5i9SPM9HAdWjHzgJRak)
	
Ως δεύτερη άσκηση, για λίγο παραπάνω εξάσκηση υλοποίησα το ntfy, για να στέλνω ειδοποιήσεις από το laptop στο κινητό όπως φαίνεται στο παρακάτω asciinema και screenshot.

Αντίστοιχα το ακόλουθο link είναι υλοποιημένο προτού προσθέσω user.

- [Asciinema](https://asciinema.org/a/mJZp9x88ryINCItki9qKzIlcw)

Και το αποτέλεσμα απ' το κινητό μου σε screenshot:

![Screenshot](https://github.com/p20adam/sw/blob/2020160/projects/2020160/ntfy-arch.png)

Τέλος υλοποίησα και το wttr για να μπορώ να δω την πρόγνωση του καιρού.

- [Asciinema](https://asciinema.org/a/8M9Iuv2nQvUrDsBr3mJ3BvXSM)

## Γραμμή εντολών (no systemd)

Τα λειτουργικά συστήματα χωρίς το system έχουν ένα διαφορετικό, εναλλακτικό σύστημα διαχείρισης όπως το SysV  init ή το Upstart, βασικές λειτουργίες διαχείρισης των διαδικασιών και της εκκίνησης του συστήματος. Οι προσφερόμενες δυνατότητες δεν είναι τόσο πλούσιες όσο σε ένα Systemd.

Προσωπικά για το μάθημα επέλεξα τα Artix, για να μην απομακρυνθώ πολύ απ’ την νοοτροπία των Arch Linux. Ωστόσο βασικοί λόγοι για να επιλέξει κανείς ένα τέτοιου είδους λειτουργικό σύστημα είναι σίγουρα η ελαφριά δομή τους για τα υπολογιστικά μηχανήματα με περιορισμένους πόρους. Επίσης η ασφάλεια και η αξιοπιστία κατέχουν ύψιστη σημασία και τα Artix μπορούν να την προσφέρουν παρόλο που η αφαίρεση του systemd μειώνει την πολυπλοκότητα και τις πιθανότητες σφαλμάτων. Βέβαια υπάρχει και μια ενεργή κοινότητα που υποστηρίζει τα Artix και μπορεί να παρέχει βοήθεια στους χρήστες αυτού του λειτουργικού συστήματος μέσω forum. Και τέλος τα Artix υποστηρίζουν ελεύθερο και ανοιχτού κώδικα λογισμικό. 

Το λειτουργικό σύστημα που επέλεξα, εγκαταστάθηκε σε usb:

- [Asciinema](https://asciinema.org/a/Dy9KFuyrjin2VkgdU6XwLcrM9)

και μετέπειτα από το ακόλουθο που εγκαταστάθηκε σε VM:

- [Asciinema](https://asciinema.org/a/w5nAuGugpRdL9SxYHJmgtPFG8)
	
Στο λειτουργικό σύστημα αυτό υλοποίησα μια ίδια άσκηση με τα Arch το ntfy, για να στέλνω ειδοποιήσεις από το laptop στο κινητό.

- [Asciinema](https://asciinema.org/a/RlDripLpNLZdynR4LkyLWbL6I)

Screenshot:

![Screenshot](https://github.com/p20adam/sw/blob/2020160/projects/2020160/ntfy-artix.png)

## Κατασκευή Βιβλίου Α2

Στο συγκεκριμένο παραδοτέο, δεν κατάφερα να ξεπεράσω το πρόβλημα που δημιουργήθηκε κατά την δημιουργία του αρχείου pdf. Παρακάτω ακολουθούν τα αρχεία μου και ένα screenshot με το πρόβλημα.

- [make-latex.sh](https://github.com/p20adam/kallipos/blob/master/make-latex.sh)
- [mylua.lua](https://github.com/p20adam/kallipos/blob/master/mylua.lua)
- [note.md](https://github.com/p20adam/kallipos/blob/master/ExtraNote/note.md)
- [Pdf](https://github.com/p20adam/kallipos/blob/master/book.pdf)

![Problem](https://github.com/p20adam/sw/blob/2020160/projects/2020160/Problem.png)

## Συμμετοχικό Περιεχόμενο Α1 και Α2

Για το πρώτο μέρος (Α1) του συμμετοχικού περιεχόμενου χρειάστηκε να προσθέσουμε στο βιβλίο δύο εικόνες με λεζάντα. Οι φωτογραφίες που επέλεξα φαίνονται ακολούθως:

- [Apple-eMate.jpg](https://github.com/p20adam/images/blob/master/apple-eMate.jpg)
- [apple-eMate-thumb.jpg](https://github.com/p20adam/images/blob/master/apple-eMate-thumb.jpg)
- [sony-playstasion.jpg](https://github.com/p20adam/images/blob/master/sony-playstation.jpg)
- [sony-plastasion-thumb.jpg](https://github.com/p20adam/images/blob/master/sony-playstation-thumb.jpg)

Και τα αντίστοιχα αρχεία md είναι:

- [apple-eMate.md](https://github.com/p20adam/_gallery/blob/master/apple-eMate.md)
- [sony-playstation.md](https://github.com/p20adam/_gallery/blob/master/sony-playstation.md)

Οι προσθήκες στο site βρίσκονται παρακάτω:

- [apple-emate](https://elated-hopper-ceabdc.netlify.app/gallery/apple-emate/)
- [sony-playstation](https://elated-hopper-ceabdc.netlify.app/gallery/sony-playstation/)

Για το δεύτερο μέρος (Α2) του συμμετοχικού περιεχόμενου, χρειάστηκε να ασχοληθούμε με το χρονολόγιο και ένα σετ διαφανειών. Αρχικά για το χρονολόγιο, _timeline, πρόσθεσα το apple-eMate στο αρχείο apple.md και το sony-playstation στο αρχείο consoles.md όπως φαίνεται παρακάτω. 

- [apple-eMate](https://github.com/p20adam/site/blob/master/_timeline/apple.md)
- [sony-playstation](https://github.com/p20adam/site/blob/master/_timeline/consoles.md)

Τα αντίστοιχα αποτελέσματα στο site είναι:
- [apple-eMate](https://elated-hopper-ceabdc.netlify.app/timeline/apple/)
- [sony-playstation](https://elated-hopper-ceabdc.netlify.app/timeline/consoles/)

Και έπειτα για το σετ διαφανειών πρόσθεσα το apple-eMate στην κατηγορία "Εκπαιδευτική Τεχνολογία" (learning.md) και το sony-playstation στην κατηγορία "Βιντεοπαιχνίδια" (videogames.md).

- [apple-eMate](https://github.com/p20adam/site/blob/master/_slides/learning.md)
- [sony-playstation](https://github.com/p20adam/site/blob/master/_slides/videogames.md)

Και αντίστοιχα τα αποτελέσματα στο site ακολουθούν:

- [apple-eMate](https://elated-hopper-ceabdc.netlify.app/slides/learning/)
- [sony-playstation](https://elated-hopper-ceabdc.netlify.app/slides/videogames/)

## Γραμμή εντολών (custom static blog generator)

Στην συγκεκριμένη γραμμή εντολών καλούμαστε να φτιάξουμε το δικό μας static blog generator. Στο στιγμιότυπο που ακολουθεί φαίνεται η αρχική σελίδα της ιστοσελίδας μου:


## Συμμετοχικό περιεχόμενο B1

Το δεύτερο σκέλος του Συμμετοχικού περιεχομένου, και συγκεκριμένα το πρώτο ερώτημα, αφορά την μελέτη περίπτωσης. Σύμφωνα με τις οδηγίες το αντικείμενο που θα διαπραγματευτεί πρέπει να σχετίζεται με τις μέχρι τώρα επιλογές μου (όπως βλέπουμε και παραπάνω apple eMate και sony-playstation). Επηρεαζόμενη από την συνήθεια όλων να ασχολούνται με τον τομέα των παιχνιδιών επέλεξα να αναζητήσω περαιτέρω για τις κονσόλες και τα βιντεοπαιχνίδια.

Το αντίστοιχο αρχείο md είναι:

- [consoles-videogames](https://github.com/p20adam/site/blob/master/_case-study/consoles-videogames.md)

Η προσθήκη στο site φαίνεται ακολούθως:

- [consoles-videogames](https://elated-hopper-ceabdc.netlify.app/case-study/consoles-videogames/)

## Κατασκευή του βιβλίου Β2

Στο συγκεκριμένο παραδοτέο, όπως και στο προηγούμενο αντίστοιχο, δεν κατάφερα να ξεπεράσω το πρόβλημα που δημιουργήθηκε κατά την δημιουργία του αρχείου epub.

## Συμμετοχικό περιεχόμενο B2

Σε συνέχεια του δεύτερου σκέλους του Συμμετοχικού Περιεχομένου, και συγκεκριμένα το δεύτερο ερώτημα, καλούμαστε να συντάξουμε μια βιογραφία. Αυτή η νέα βιογραφία πρέπει να σχετίζεται με τις θεματικές ενότητες που αναπτύχθηκαν μέχρι στιγμής. Έτσι το κείμενο αφορά τον κύριο  Jonathan Ive δημιουργό του apple-eMate.

Οι φωτογραφίες που επέλεξα είναι οι εξής:

- [JonathanIve](https://github.com/p20adam/images/blob/master/JonathanIve.jpg)

- [JonathanIve-thumb](https://github.com/p20adam/images/blob/master/JonathanIve-thumb.jpg)

Και το αντίστοιχο αρχείο md είναι:

- [JonathanIve](https://github.com/p20adam/site/blob/master/_biography/JonathanIve.md)

Αντίστοιχα τα αποτελέσματα που προκείπτουν στο Site είναι:

- [JonathanIve](https://elated-hopper-ceabdc.netlify.app/biography/jonathanive/)

## Video

| Τίτλος Βίντεο | Παρακολούθηση | 
| --- | --- |
| Alan Kay at MIT-EECS 1998 Fall Semester Colloquium Series (VPRI 834)| Ναι |
| Ted Nelson -- Computers for Cynics [full version]| Ναι |
|Alan Kay - Could Computing Be Simpler Than It Seems To Be?| Ναι |
| Bret Victor - The Future of Programming| Ναι |
| Alan Kay - Programming Languages & Programming (2013)| Ναι |
| Alan Kay Turing Lecture with dynamic content| Ναι |
| Alan Kay - Programming and Scaling| Ναι |
| Extracting Energy from the Turing Tarpit| Ναι |
| Back to the Future of Software Development 4/23/2003 (VPRI 785)| Ναι |
| VCF East 2019 -- Brian Kernighan interviews Ken Thompson| Ναι |

## Ομαδικότητα
- [link](https://github.com/courses-ionio/sw/pull/1715)
- [link](https://github.com/courses-ionio/sw/pull/1709)
- [link](https://github.com/courses-ionio/sw/discussions/1441)

## Τελική αναφορά 
