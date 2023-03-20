# **Τεχνολογία Λογισμικού**

## Ονοματεπώνυμο: Καραστάθης Παναγιώτης

### Αριθμός Μητρώου: Π2020008

## Github Organization: [lapis-lazuli-ore-block](https://github.com/lapis-lazuli-ore-block)

## Περιεχόμενα:

| Εβδομάδα | Παραδοτέα | Σύνδεσμος στην εβδομαδιαία παρουσίαση προόδου στις συζητήσεις | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | Δημιουργία ομάδας, προσθήκη πίνακα περιεχομένων, συγγραφή της εισαγωγής| [Παραδοτέο 1°](https://github.com/courses-ionio/sw/discussions/1194) | Δημιούργησα τα περιεχόμενα και την εισαγωγή της αναφοράς |
| 2 | Γραμμή εντολών (systemd) και διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας |[Παραδοτέο 2°](https://github.com/courses-ionio/sw/discussions/1295) | |
| 3 | Γραμμή εντολών (no systemd) | | |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά) | | |
| 5 | Συμμετοχικό περιεχόμενο A1 + A2 | | |
| 6 | Γραμμή εντολών (custom static blog generator) | | |
| 7 | συμμετοχικό περιεχόμενο B1 | | |
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) | | |
| 9 | Συμμετοχικό περιεχόμενο B2 | | |
| 10 | Τελική αναφορά | | |

## Εισαγωγή:

Στο μάθημα Τεχνολογία Λογισμικού σκοπεύω να αντιληφθώ την σημαντικότητα του όρου και να αποκτήσω γνώσεις σχετικά με το αντικείμενο. Τα εβδομαδιαία παραδοτέα θα με βοηθήσουν να εξασκηθώ και να μελετήσω αλλά και ότι αφορά την ομαδική δουλειά θα είναι μια ενδιαφέρουσα και πολύ σημαντική εμπειρία. 

Τα εβδομαδιαία βίντεο κουίζ θα αποτελέσουν το υπόβαθρο για την αναζήτηση γνώσης και ελπίζω μετά το πέρας του μαθήματος να μπορώ να «στήσω» ένα πρόγραμμα λογισμικού.


## Γραμμή εντολών (systemd)

Αποφάσισα να χρησιμοποιήσω για τις ασκήσεις γραμμής εντολών σε λειτουργικό με system το distribution των Arch Linux. Είναι από τα πιο διαδεδομένα distributions και είχα την ευκαιρία να ασχοληθώ μαζί τους και να τα γνωρίσω από ένα μάθημα της σχολής μου. 

- [Asciinema](https://asciinema.org/a/w5Lmo1RcUVwJM3AfeDgfN4xdQ)

Επέλεξα για άσκηση γραμμής εντολών να υλοποιήσω το hyperfine από την κατηγορία software. Αρχικά με την εντολή `sudo pacman -S hyperfine` εγκατέστησα το hyperfine. Στην συνέχεια με την εντολή `hyperfine -i tictactoe.py` μέτρησα τον χρόνο εκτέλεσης του κώδικα μου σε python  για tic-tac-toe.

- [Asciinema](https://asciinema.org/a/eloFbEeGKO3Ft0Vom4zzcLzSu)

## Γραμμή εντολών (no systemd)

Για το παραδοτέο χωρίς system αποφάσισα να χρησιμοποιήσω τα Artix Linux που χρησιμοποιούν OpenRC. Τα Artix είναι βασισμένα στο distribution των Arch linux με τη μεγάλη διαφορά ότι δε χρησιμοποιεί Systemd. Διάλεξα αυτό το distribution επειδή είναι αρκετά όμοια με τα Arch τα οποία μου έχουν ζητηθεί να χρησιμοποιήσω και να μάθω σε αυτά αλλά και για το γεγονός ότι έχουν όπως και τα Arch μία μεγάλη και ενεργή κοινότητα διατεθειμένη να βοηθήσουν σε τυχών προβλήματα.

Παρακάτω φαίνετε το asciinema από το neofetech από το distribution των Artix Linux. Ακόμα φαίνετε το asciinema από την αλλαγή του hostname από "panagiotis-zenbookux425eaux425ea" σε "P2020008" με την εντολή `nmtui`
 
- [Asciinema](https://asciinema.org/a/nDJJ7jLIyUbXnlWoDvTdXBFY2)
- [Asciinema](https://asciinema.org/a/uZO04nwIvdHL8LBIJgjHQE4tv)

## Κατασκευή Βιβλίου Α2

Στη κατασκευή βιβλίου αντιμετώπισα πρόβλημα στη δημιουργία του pdf. Ακολούθως είναι τα αρχεία που χρησιμοποίησα καθώς και η προσωπική μου σημείωση.

- [make-latex.sh](https://github.com/p20kara/kallipos/blob/master/make-latex.sh)
- [mylua.lua](https://github.com/p20kara/kallipos/blob/master/mylua.lua)
- [Note.md]()
- [Pdf](https://github.com/p20kara/kallipos/blob/master/book.pdf)

Το πρόβλημα είναι στη δημιουργία του αρχείου pdf.

![Error](https://github.com/p20kara/sw/blob/2020008/projects/2020008/%CE%A3%CF%84%CE%B9%CE%B3%CE%BC%CE%B9%CF%8C%CF%84%CF%85%CF%80%CE%BF%20%CE%BF%CE%B8%CF%8C%CE%BD%CE%B7%CF%82%20(283).png)


## Συμμετοχικό Περιεχόμενο Α1 & Α2

Για το συμμετοχικό περιεχόμενο αποφάσισα να προσθέσω τις δύο ακόλουθες φωτογραφίες, οι οποίες ακολοθούν μαζί με τα αρχεία .md που αντιπροσωπεύουν τη κάθε μία. 

[aibo-photo1-full.md](https://github.com/p20kara/_gallery/blob/master/aibo-photo1-full.md)
- [aibo-photo1-full.jpg](https://github.com/p20kara/images/blob/master/aibo-photo1-full.jpg)
- [aibo-photo1-full-thumb.png](https://github.com/p20kara/images/blob/master/aibo-photo1-full-thumb.png)

[Apple_Newton_and_iPhone.md](https://github.com/p20kara/_gallery/blob/master/Apple_Newton_and_iPhone.md)
- [Apple_Newton_and_iPhone.jpg](https://github.com/p20kara/images/blob/master/Apple_Newton_and_iPhone.jpg)
- [Apple_Newton_and_iPhone-thumb.png](https://github.com/p20kara/images/blob/master/Apple_Newton_and_iPhone-thumb.png)

Οι προσθήκες φαίνονται και στο site στα ακόλουθα link.

- [Sony aibo](https://p20kara.netlify.app/gallery/aibo-photo1-full/)
- [Apple Newton MessagePad](https://p20kara.netlify.app/gallery/apple_newton_and_iphone/)

Ακόμα έχουν προστεθεί στο timeline του βιβλιού στις κατηγορίες `prototypes` και `apple` αντίστοιχα.

- [Sony aibo](https://p20kara.netlify.app/timeline/prototypes/)
  - [Sony aibo (github)](https://github.com/p20kara/site/blob/master/_timeline/prototypes.md)
- [Apple Newton MessagePad](https://p20kara.netlify.app/timeline/apple/)
  - [Apple Newron MessagePad (GitHub)](https://github.com/p20kara/site/blob/master/_timeline/apple.md)
  
Έπειτα ακολουθεί η προσθήκη των εικόνων στο σετ διαφανειών. Όπου έχουν προστεθεί και τα δύο στη κατηγορία `technology`.

- [GitHub](https://github.com/p20kara/site/blob/master/_slides/technology.md)
- [pibook](https://p20kara.netlify.app/slides/technology/)
