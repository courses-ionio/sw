Ονοματεπόνυμο: ΓΙΩΡΓΟΣ ΜΠΑΣΙΑΡΗΣ

Αριθμός Μητρώου: Π2018120

Github link: https://github.com/paranaloma

Οργανισμός: is_init_right?


# Τεχνολογία Λογισμικού


| Εβδομάδα | [Όλα τα παραδοτέα βρίσκονται στην ίδια σελίδα της τελικής αναφοράς](https://epidrome.github.io/teaching/deliverables/) με τα προσωπικά στοιχεία σας (Όνομα, ΑΜ, github profile) και μαζί με αυτόν εδώ τον πίνακα περιεχομένων | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | [Δημιουργία ομάδας](https://epidrome.github.io/teaching/team/) + [Φορκ και δημιουργία σελίδας τελικής αναφοράς](https://epidrome.github.io/teaching/guide/), [προσθήκη πίνακα περιεχομένων](https://raw.githubusercontent.com/courses-ionio/sw/master/README.md), [συγγραφή της εισαγωγής](https://epidrome.github.io/teaching/intro/), αποστολή της εισαγωγής [για σχολιασμό στην συζήτηση](https://github.com/courses-ionio/sw/discussions/categories/show-and-tell) και καταγραφή του συνδέσμου συζήτησης δίπλα --> |https://github.com/courses-ionio/sw/discussions/1190 | |
| 2 | [Γραμμή εντολών](https://epidrome.github.io/teaching/cli) (systemd) και [διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας](https://epidrome.github.io/teaching/team) |https://github.com/courses-ionio/sw/discussions/1312 | |
| 3 | Γραμμή εντολών (no systemd) |https://github.com/courses-ionio/sw/discussions/1318 |  |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά) |https://github.com/courses-ionio/sw/discussions/1388 | |
| 5 | Συμμετοχικό περιεχόμενο A1 + A2 |https://github.com/courses-ionio/sw/discussions/1396 | |
| 6 | Γραμμή εντολών (no systemd, custom static blog generator) |https://github.com/courses-ionio/sw/discussions/1596 | |
| 7 | συμμετοχικό περιεχόμενο B1 |https://github.com/courses-ionio/sw/discussions/1597 | |
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) |https://github.com/courses-ionio/sw/discussions/1598 | |
| 9 | συμμετοχικό περιεχόμενο B2 |https://github.com/courses-ionio/sw/discussions/1599 | |
| 10 | Τελική αναφορά* |https://github.com/courses-ionio/sw/discussions/1599| |

# Εισαγωγή - Εβδομάδα 1
Το μάθημα τεχνολογία λογισμικού πιστεύω ότι θα με βοηθήσει στην κατανόηση του τρόπου λειτουργίας των λειτουργικών συστημάτων, όπως το τι είναι το systemd και το πως εποπτέυει τις υπόλοιπες διεργασίες σαν daemon καθώς και εναλλακτικές του. Επιπλέον θεωρώ ότι τα εβδομαδιαία βίντεο κουίζ θα με βοηθήσουν στο να καταλάβω τους προβληματισμούς και την ιστορία της ανάπτυξης λογισμικού από μεγάλους επιστήμονες της Πληροφοριής. Πιστεύω πώς το συνεργατικό κομματί του μαθήματος θα με βοηθήσει στο να μάθω να συνεργάζομαι με τους υπόλοιπους συμφοιτητές μου και να μάθουμε μαζί. Τέλος η γραμμή εντολών θα με βοηθήσει στο να μάθω να έχω πλήρη ελευθερία πάνω στον τρόπο λειτουργίας του συστήματος μιας και η γραμμή εντολών σου δίνει μια ελευθερία που η κλασική διάδραση όχι.

# Άσκηση γραμμής εντολών 1 - Εβδομάδα 2
Δημιουργήθηκε ένα αρχείο checkweather.sh που κάθε φορά που εκτελείται μου στέλνει τον καιρό στο Telegram χρησιμοποιώντας το curl στο wttr.in.
Για να πραγματοποιηθεί με επιτυχία πρέπει να υπάρχει εγκατεστημένα τα python, python-pip, ntfy, ntfy[telegram], curl.
```sh
#!/bin/bash

# City name for Corfu, Greece
CITY_NAME="Corfu,Kerkyra,Greece"

# URL to get the weather data for Corfu
URL="https://wttr.in/${CITY_NAME}?format=%C:%t,%f"

# Get the weather data using curl
WEATHER=$(curl -s "${URL}")

# Send notification using ntfy
ntfy -b telegram send "${WEATHER}"
```


![asciicast](https://asciinema.org/a/563907.svg)](https://asciinema.org/a/563907)


![prntscrn](https://user-images.githubusercontent.com/56626790/222225366-c0520312-975d-4ca2-84a2-a6de39c11a9e.png)



# Άσκηση γραμμής εντολών 2 - Εβδομάδα 3
Δημιουργήθηκε ένα αρχείο [autobench.sh](https://github.com/paranaloma/shellscripting/commit/795389ee6f346f24caac16ca4acc49224da017e5),απαρτίζεται από ένα Menu με τρεις διαφορετικές επιλογές το οποίο κάνει 3 διαφορετικά benchmark και αποθηκεύει τα αποτελέσματα σε ανάλογο αρχείο (π.χ για το standard_benchmark -> standard_benchmark_results.json) 

[![asciicast](https://asciinema.org/a/c4uxlSI9m7ZmDYWX0HWQ5Yzc9.svg)](https://asciinema.org/a/c4uxlSI9m7ZmDYWX0HWQ5Yzc9)

# Κατασκευή του Βιβλίου 1 - Εβδομάδα 4
Δημιουργήθηκε το βιβλίο του μαθήματος σε μορφή PDF μέσω του [filter.lua](https://github.com/paranaloma/kallipos/blob/master/comment.lua), [make-latex.sh](https://github.com/paranaloma/kallipos/blob/master/make-latex.sh), [comment.md](https://github.com/paranaloma/kallipos/blob/master/comment.lua).
[kallipos](https://github.com/paranaloma/kallipos). Επιπρόσθετα έγινε προσθήκη σχολίου με πληροφορίες σχετικά με το Raspberry Pi.

![letsgo](https://user-images.githubusercontent.com/56626790/224571178-f7534b95-e6a8-405c-a94e-ad96447d139e.png)

# Συμμετοχικό Περιεχόμενο Α1 + Α2 ([site](https://github.com/paranaloma/site)) - Εβδομάδα 5
Δημιουργήθηκαν τα κατάλληλα αρχεία md ώστε να πραγματοποιηθούν τα παραδοτέα Α1,Α2. Πιο συγκεκριμένα στο submodule _gallery έγιναν οι προσθήκες της Pascal και τις C, στο images 4 εικόνες και τέλος στο _slides και στο _timeline συνδέθηκαν οι παραπάνω εικόνες με θέμα Δομημένος Προγραμματισμός.
- [pascal.md](https://github.com/paranaloma/_gallery/blob/090127de0a9dad501897c28990a4cbb73b417b77/pascal.md)
- [c-language.md](https://github.com/paranaloma/_gallery/blob/090127de0a9dad501897c28990a4cbb73b417b77/c-language.md)
- [_slides md](https://github.com/paranaloma/site/blob/master/_slides/structuredprogram.md)
- [_timeline md](https://github.com/paranaloma/site/blob/master/_timeline/structuredprog.md)
- [Pascal Picture](https://github.com/paranaloma/images/blob/2f01f03836ce7adea12c90ddd63c97d7dfc49416/pascal.jpg)
- [Pascal Picture thumb](https://github.com/paranaloma/images/blob/2f01f03836ce7adea12c90ddd63c97d7dfc49416/pascal-thumb.jpg)
- [C picture](https://github.com/paranaloma/images/blob/2f01f03836ce7adea12c90ddd63c97d7dfc49416/c-language.jpg)
- [C picture thumb](https://github.com/paranaloma/images/blob/2f01f03836ce7adea12c90ddd63c97d7dfc49416/c-language-thumb.jpg)
- [Netlify pascal](https://dancing-churros-ac3101.netlify.app/gallery/pascal/)
- [Netlify C](https://dancing-churros-ac3101.netlify.app/gallery/c-language/)
- [Netlify slides](https://dancing-churros-ac3101.netlify.app//slides/structuredprogram/)
- [Netlify timeline](https://dancing-churros-ac3101.netlify.app//timeline/structuredprog/)

# Κατασκευή Blog - Εβδομάδα 6
Κατασκεύασα χρησιμοποιώντας το [bashblog](https://github.com/cfenollosa/bashblog) το δικό μου blog, το οποίο γίνεται hosted μέσω του [Github Pages](https://paranaloma.github.io/treeblog/).

![Screenshot 2023-04-25 at 02 48 03](https://user-images.githubusercontent.com/56626790/234139507-8e7d8fe7-960c-42aa-a60d-641e0bb0a229.png)

[Repository](https://github.com/paranaloma/treeblog)

# Συμμετοχικό περιεχόμενο B1 - Εβδομάδα 7
Για το συμμετοχικό περιεχόμενο Β1 πραγματοποιήθηκε μελέτη περίπτωσης αναφορικά με τον δομημένο προγραμματισμό δηλαδή την φιλοσοφία πως για να λύσουμε κάποιο πρόβλημα θα πρέπει να χρησιμοποιούμε την λογική, αυστηρά και καθορισμένα βήματα, να διαχωρίζουμε το αρχικό πρόβλημα σε απλούστερα υποπροβλήματα (συναρτήσεις ή υπορουτίνες).

![screenshot](https://user-images.githubusercontent.com/56626790/234142071-249134a9-a912-444b-9e53-627d26caa27b.png)

- [Netlify](https://dancing-churros-ac3101.netlify.app//case-study/scructured/)
- [structured.md](https://github.com/paranaloma/site/blob/master/_case-study/scructured.md)
- [cs-structured.md](https://github.com/paranaloma/site/blob/master/_includes/cs-structured.md)

## Κατασκευή βιβλίου Β2 - Εβδομάδα 8
Για αυτό το παραδοτέο χρησιμοποίησα το makepollen.sh προκειμένου να υλοποιήσω το βιβλίο του μαθήματος σε μορφή pollen.

[kallipos repo](https://github.com/paranaloma/kallipos)

[makepollen.sh](https://github.com/paranaloma/kallipos/blob/master/makepollen.sh)

![screenshot 3](https://user-images.githubusercontent.com/56626790/234149565-964d661e-23b2-4b19-8c09-37fe4cecaad9.png)


## Συμμετοχικό περιεχόμενο Β2 - Εβδομάδα 9
Για το συμμετοχικό περιεχόμενο Β2 αναρτήθηκε στο site η βιογραφία του Edsger Dijkstra ένας άνθρωπος γνωστός για τις σημαντικές συνεισφορές του στη θεωρία των αλγορίθμων, τον σχεδιασμό και την ανάλυση αλγορίθμων, και την προώθηση των αρχών του δομημένου προγραμματισμού.

![screenshot 2](https://user-images.githubusercontent.com/56626790/234144466-7b355432-3d75-4fe6-a20d-5c885afd1aba.png)

## Τελική αναφορά 
Στο μάθημα τεχνολογίας λογισμικού έμαθα πως Edsger Dijkstra ήταν ένας από τους πιο επιδραστικούς υπολογιστικούς επιστήμονες όλων των εποχών. Ο Dijkstra ήταν ο πρωτοπόρος στον δομημένο προγραμματισμό και ανέπτυξε αλγόριθμους που χρησιμοποιούνται ακόμα και σήμερα. Ακόμη έμαθα πως το systemd είναι ένα σύστημα διαχείρισης εκκίνησης και διαχείρισης διαδικασιών που χρησιμοποιείται στις περισσότερες σύγχρονες διανομές Linux. Τέλος έμαθα πως οργανώνεται και συντηρείται το λογισμικό παρακολουθώντας την δομή, τα προβλήματα που αντιμετωπίζουν (issues) και τον τρόπο αντιμετώπισης αυτών μέ
σω της πλατφόρμας του Github.
