# Τεχνολογία Λογισμικού 

### Ονοματεπώνυμο: Καλαθάς Αλέξανδρος
### Αριθμός Μητρώου: Π2019017
### [github profile](https://github.com/p19kala)

## Πίνακας Περιεχομένων:
| Εβδομάδα | Παραδοτεά | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | [Εισαγωγή](#Εισαγωγή)| https://github.com/courses-ionio/help/discussions/79 | Έκανα ο,τι απαιτείται για το παραδοτέο 1. |
| 2 | [βιογραφικό και δημιουργία ομάδας](#Ιστοσελίδα-βιογραφικού-και-ένταξη-σε-ομάδα) | https://github.com/courses-ionio/help/discussions/230 | Ακολούθησα τα κριτήρια για την άριστη βαθμολόγηση, αλλά κατά τη γνώμη μου υπάρχει πολύ χώρος για βελτίωση. Έχω ιδέες, άλλα όχι χρόνο προς το παρών. Θα το επεξεργαστώ περαιτέρω στη πορεία.|
| 3 | [Αίτημα ενσωμάτωσης στην ιστοσελίδα](#Pull-Request)| https://github.com/courses-ionio/help/discussions/326 | Ακολούθησα τις οδηγίες και βγήκε άριστη. |
| 4 | [Άσκηση γραμμής εντολών](#Ασκηση-Γραμμης-Εντολων) | https://github.com/courses-ionio/help/discussions/363 | Ακολούθησα τις οδηγίες και βγήκε άριστη. |
| 5 | [Συμμετοχικό περιεχόμενο A1+A2](#Συμμετοχικο-1) | https://github.com/courses-ionio/help/discussions/428 | Ακολούθησα τις οδηγίες και βγήκε άριστη. |
| 6 | Άσκηση γραμμής εντολών | | |
| 7 | βιογραφικό | | |
| 8 | Αίτημα ενσωμάτωσης στην ιστοσελίδα | | |
| 9 | Άσκηση γραμμής εντολών | | |
| 10 | συμμετοχικό περιεχόμενο B1+B2 | | |
| 11 | Άσκηση γραμμής εντολών | | |
| 12 | Τελική αναφορά* | | |

## Εισαγωγή
Αποσκοπώ να αντλήσω όση πληροφορία γίνεται μέσα από τα πληροφοριακά βίντεο και να εξετάσω τον εαυτό μου σε υλικό του Linux μέσα από τα εβδομαδιαία παραδοτέα. Έχω παρατηρήσει ότι η πλειοψηφία προγραμματιστών στο κόσμο χρησιμοποιεί (και προτιμάει) ένα περιβάλλον Linux για ανάπτυξη και χρησιμοποίηση εφαρμογών, οπότε σκέφτηκα ότι θα ήταν καλό να επεκτείνω τις γνώσεις και δεξιότητές μου κάποια στιγμή και αυτό το μάθημα είναι ιδανικό. Μέσα από τις ομάδες του μαθήματος ευελπιστώ να μάθω να συνεργάζομαι σε μια ομάδα για επίλυση προβλημάτων και έπειτα να χρησιμοποιήσω την εμπειρία αυτή για την ομαλή και επαγγελματική συνεργασία με άλλους πάνω σε συστήματα ασφάλειας δικτύων.

## Ιστοσελίδα βιογραφικού και ένταξη σε ομάδα
Σύνδεσμοι στο [αποθετήριο](https://github.com/p19kala/online-cv/tree/gh-pages) του κώδικα της ιστοσελίδας, στην [ομάδα](https://github.com/Git-s-PopTeamEpic) και το [webring](https://git-team-epic-webring.netlify.app/) της. Το βιογραφικό μου: https://p19kala.github.io/online-cv/

Συμπλήρωσα το βιογραφικό βάση του template και προσθεσα τα εξης:
- Αλλαξα το χρωμα του θεματος jekyll στην ιστοσελιδα
- Προσθεσα επιπλεον ενοτητα "Programs & Proficiency" κατω απο τα "skills & proficiency" για να δειξω ποια προγραμματα γνωριζω και ποσο. Για να το κανω αυτο, αντεγραψα τον φακελο skills.html και δημιουργησα τον programs.html, αλλαζωντας ολα τα αντικειμενα "skills" με "programs". Επειτα πηγα στο index.html και προσθεσα τη γραμμη `{% include programs.html %}`.
- Περασα την ενοτητα "graduation" απο το sidebar στο body της ιστοσελιδας για να φαινεται πιο εμπλουτισμενη καθως δεν ειχα δεξιοτητες να γραψω (και ετσι φαινονται τα details του education)
- Προς το παρων xρησιμοποιωντας το raw content ενος pdf αρχειου που δημιουργησα, ο χρηστης πατωντας στο λινκ μπορει να κατεβασει το βιογραφικο μου σε pdf μορφη.
- Asciinema: https://asciinema.org/a/nfULxsiwhCHFN4VbcVqvPqMAD

## Pull Request
Σύνδεσμος στο [issue](https://github.com/ioniodi/sitegr/issues/237) και στο [pull request](https://github.com/ioniodi/all_collections/pull/22). Πρόσθεσα ένα μάθημα στο Ζ' εξάμηνο στις Σπουδές στο φάκελο [\_courses](https://github.com/p19kala/all_collections/tree/2019017/_courses), το οποίο είναι η "Πτυχιακή Εργασία" όπως φαίνεται στο live demo μου [εδώ](https://p19kalasw.netlify.app/courses/thesis/). 
- Αποθετήριο του sitegr και του all_collections με branch το ΑΜ μου: [sitegr](https://github.com/p19kala/sitegr/tree/2019017), [all_collections](https://github.com/p19kala/all_collections/tree/2019017)
- Asciinema: https://asciinema.org/a/Lcb6l2CcGAastdRxuYVKVwrLu

## Ασκηση Γραμμης Εντολων
Εκανα εγκατασταση FreeBSD, αλλαξα το shell και το prompt μου: 
![image](https://user-images.githubusercontent.com/72458452/158074687-40428982-ff05-4054-95f8-d39e3a8bbea4.png)


Για την ασκηση γραμμης εντολων επελεξα να στειλω ενα desktop notification μετα απο download, με τη χρηση του εργαλειου [ntfy](https://github.com/dschep/ntfy). Χρησιμοποιησα το [youtube-dl](https://github.com/ytdl-org/youtube-dl) για να κατεβασω ενα βιντεο, με τη χρηση του `--no-check-certificate` καθως πετουσε SSL certificate error. Η καταγραφη εγινε με το εργαλειο kazam, καθως το notification ειναι εκτος του terminal και επειτα μετατροπη σε gif. Σταματησα το recording λιγο μετα την εναρξη του download γιατι εδειχνε πως θα παρει 1 λεπτο, ετσι ωστε το βιντεο να μην ειναι πολυ μεγαλο χωρις καμια ουσιωδες αλλαγη στο περιεχομενο. Στο μελλον θα κανω την ασκηση στο FreeBSD.

![AltText](https://i.imgur.com/rBVf9cJ.gif)

## Συμμετοχικο 1
Για το συμμετοχικο περιεχομενο Α1 και Α2 επελεξα να ασχοληθω με συγκεντρωση πληροφοριας πανω σε systemd-less λειτουργικα. Για αυτο διαλεξα τα freebsd και void.

Συνδεσμοι στα αποθετηρια μου οπου ειναι οι αλλαγες μου: [slides](https://github.com/p19kala/site/blob/P2019017_sw/_slides/operating-systems.md), [timeline](https://github.com/p19kala/site/blob/P2019017_sw/_timeline/os-apps.md), images για [freebsd](https://github.com/p19kala/images/commit/3032511d4febe27fdeb1f439921d6cdbacd58b65) και [void](https://github.com/p19kala/images/commit/c89d4d7aa0b9d8f61594a1c627a2bb9d2ee5fe52), gallery για [freebsd](https://github.com/p19kala/_gallery/blob/P2019017/freebsd.md) και [void](https://github.com/p19kala/_gallery/blob/P2019017/voidlinux.md).

Live demo changes: [slides](https://p19kala-pibook.netlify.app/slides/operating-systems/), [timeline](https://p19kala-pibook.netlify.app/timeline/os-apps/), gallery για [freebsd](https://p19kala-pibook.netlify.app/gallery/freebsd/) και [Void](https://p19kala-pibook.netlify.app/gallery/voidlinux/).<br>
Issue πριν κανω pull request στο organization: https://github.com/Git-s-PopTeamEpic/site/issues/2 <br>
Pull requests στο organization: [site](https://github.com/Git-s-PopTeamEpic/site/pull/3), [images](https://github.com/Git-s-PopTeamEpic/images/pull/1), [gallery](https://github.com/Git-s-PopTeamEpic/_gallery/pull/1).

## Links ομαδικότητας και συμμετοχής:
Βοήθεια σε issue για το 1o pull request: https://github.com/ioniodi/sitegr/issues/281#issuecomment-1059838232

Αξιολόγηση issue του συνεργάτη μου: https://github.com/ioniodi/sitegr/issues/230#issuecomment-1059802447

Απαντηση σε ερωτηση στα discussions του sitegr: https://github.com/ioniodi/sitegr/discussions/229#discussioncomment-2295458

Δημιουργια guide στα discussions του sitegr για Ruby version management: https://github.com/courses-ionio/help/discussions/200

Βοηθεια σε προβλημα στα discussions του help: https://github.com/courses-ionio/help/discussions/304#discussioncomment-2301642

Βοηθεια σε guide στα discussions του help: https://github.com/courses-ionio/help/discussions/344#discussioncomment-2342616
