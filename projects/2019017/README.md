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
| 4 | [Άσκηση γραμμής εντολών 1](#Ασκηση-Γραμμης-Εντολων-1) | https://github.com/courses-ionio/help/discussions/363 | Η ασκηση γραμμης εντολων δεν εγινε σε συστημα χωρις systemd και το custom λειτουργικο συστημα ηταν το FreeBSD. Θα τη βελτιωσω στο μελλον και μαλλον θα βαλω Void Linux. |
| 5 | [Συμμετοχικό περιεχόμενο A1+A2](#Συμμετοχικο-1) | https://github.com/courses-ionio/help/discussions/428 | Ακολούθησα τις οδηγίες και βγήκε άριστη. |
| 6 | [Άσκηση γραμμής εντολών 2](#Ασκηση-Γραμμης-Εντολων-2) | https://github.com/courses-ionio/help/discussions/474 | Εκανα εγκατασταση το void linux σε VM απο iso image. Ηταν σχετικα ευκολη διαδικασια, αλλα κολλαει αρκετα στο terminal οποτε η εμπειρια εκει ηταν κουραστικη. |
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

## Ασκηση Γραμμης Εντολων 1
Εκανα εγκατασταση FreeBSD, αλλαξα το shell και το prompt μου: 
![image](https://user-images.githubusercontent.com/72458452/158074687-40428982-ff05-4054-95f8-d39e3a8bbea4.png)<br>
Neofetch: https://asciinema.org/a/rCovVT5nKbeXB1hmV1VmL6XBI


Για την ασκηση γραμμης εντολων επελεξα να στειλω ενα desktop notification μετα απο download, με τη χρηση του εργαλειου [ntfy](https://github.com/dschep/ntfy). Χρησιμοποιησα το [youtube-dl](https://github.com/ytdl-org/youtube-dl) για να κατεβασω ενα βιντεο, με τη χρηση του `--no-check-certificate` καθως πετουσε SSL certificate error. Η καταγραφη εγινε με το εργαλειο kazam, καθως το notification ειναι εκτος του terminal και επειτα μετατροπη σε gif. Σταματησα το recording λιγο μετα την εναρξη του download γιατι εδειχνε πως θα παρει 1 λεπτο, ετσι ωστε το βιντεο να μην ειναι πολυ μεγαλο χωρις καμια ουσιωδες αλλαγη στο περιεχομενο. Στο μελλον θα κανω την ασκηση στο FreeBSD.

![AltText](https://i.imgur.com/rBVf9cJ.gif)

## Συμμετοχικο 1
Για το συμμετοχικο περιεχομενο Α1 και Α2 επελεξα να ασχοληθω με συγκεντρωση πληροφοριας πανω σε systemd-less λειτουργικα. Για αυτο διαλεξα τα freebsd και void.

Συνδεσμοι στα αποθετηρια μου οπου ειναι οι αλλαγες μου: [slides](https://github.com/p19kala/site/blob/P2019017_sw/_slides/operating-systems.md), [timeline](https://github.com/p19kala/site/blob/P2019017_sw/_timeline/os-apps.md), images για [freebsd](https://github.com/p19kala/images/commit/3032511d4febe27fdeb1f439921d6cdbacd58b65) και [void](https://github.com/p19kala/images/commit/c89d4d7aa0b9d8f61594a1c627a2bb9d2ee5fe52), gallery για [freebsd](https://github.com/p19kala/_gallery/blob/P2019017/freebsd.md) και [void](https://github.com/p19kala/_gallery/blob/P2019017/voidlinux.md).

Live demo changes: [slides](https://p19kala-pibook.netlify.app/slides/operating-systems/), [timeline](https://p19kala-pibook.netlify.app/timeline/os-apps/), gallery για [freebsd](https://p19kala-pibook.netlify.app/gallery/freebsd/) και [Void](https://p19kala-pibook.netlify.app/gallery/voidlinux/).<br>
Site του οργανισμου με τις αλλαγες μου: [slides](https://gits-team-epic-pibook.netlify.app/slides/operating-systems/), [timeline](https://gits-team-epic-pibook.netlify.app/timeline/os-apps/), gallery για [freebsd](https://gits-team-epic-pibook.netlify.app/gallery/freebsd/) και [Void](https://gits-team-epic-pibook.netlify.app/gallery/voidlinux/).<br>
Issue πριν κανω pull request στο organization: https://github.com/Git-s-PopTeamEpic/site/issues/2 <br>
Pull requests στο organization: [site](https://github.com/Git-s-PopTeamEpic/site/pull/3), [images](https://github.com/Git-s-PopTeamEpic/images/pull/1), [gallery](https://github.com/Git-s-PopTeamEpic/_gallery/pull/1).

## Ασκηση Γραμμης Εντολων 2
Για αυτη την εβδομαδα στην ασκηση γραμμης εντολων εγκατεστησα το void linux στο virtualbox. Εκανα neofetch και dmesg και χρησιμοποιησα το εργαλειο ntfy οπως στην ασκηση 1 (ωστε αυτη τη φορα να μετρησει στο βαθμο, καθως ειναι σε systemd-less OS). 
Χρησιμοποιησα ενα recording application για να δειξω το desktop notification που εμφανιστηκε μετα το download (καθως το asciinema δεν μπορει να το δειξει):<br>
![image](https://user-images.githubusercontent.com/72458452/160300105-4cfe2aed-af6f-45c1-8499-89d6e66bea97.gif)<br>
Επιπλεον, εγκατεστησα την εφαρμογη "pushbullet" σε android simulator και εγραψα το αρχειο `~/.ntfy.yml`ωστε να εχει ως backends το pushbullet και να μπορει να στειλει ειδοποιησεις στο "κινητο" μου. Ετσι, οποιαδηποτε εντολη κανω και διαρκεσει παραπανω απο 10 δευτερολεπτα (default setting), οταν τελειωσει θα σταλθει ειδοποιηση _και_ στο "κινητο" μου _και_ στο desktop του Void.<br>
![ezgif com-gif-maker (9)](https://user-images.githubusercontent.com/72458452/160302752-3c10e38f-5241-470d-a06b-69419020abdf.gif)


Προσπαθησα επισης να δουλεψω με το εργαλειο [huginn](https://github.com/huginn/huginn), το οποιο φαινεται να ειναι παρατημενο απο τον ιδιοκτητη του repo για να δημιουργησω εναν agent που θα "τραβαει" τα τελευταια news απο [αυτη την ιστοσελιδα](https://m.naftemporiki.gr/liveblog/1835606#top) την οποια ακολουθω, αλλα υπηρξε προβλημα στο bundle και θα χρειαστω χρονο να το λυσω.
<br>Asciinema: https://asciinema.org/a/M2Mr7PfLmd4XkLkQvuvwTjwrb <br>

## Links ομαδικότητας και συμμετοχής:
Βοήθεια σε issue για το 1o pull request: https://github.com/ioniodi/sitegr/issues/281#issuecomment-1059838232

Αξιολόγηση issue του συνεργάτη μου: https://github.com/ioniodi/sitegr/issues/230#issuecomment-1059802447

Απαντηση σε ερωτηση στα discussions του sitegr: https://github.com/ioniodi/sitegr/discussions/229#discussioncomment-2295458

Δημιουργια guide στα discussions του sitegr για Ruby version management: https://github.com/courses-ionio/help/discussions/200

Βοηθεια σε προβλημα στα discussions του help: https://github.com/courses-ionio/help/discussions/304#discussioncomment-2301642

Βοηθεια σε guide στα discussions του help: https://github.com/courses-ionio/help/discussions/344#discussioncomment-2342616

Βοηθεια σε ερωτηση στα discussions του help: https://github.com/courses-ionio/help/discussions/406#discussioncomment-2394513