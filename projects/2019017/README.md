# Τεχνολογία Λογισμικού 

### Ονοματεπώνυμο: Καλαθάς Αλέξανδρος
### Αριθμός Μητρώου: Π2019017
### [github profile](https://github.com/p19kala)
### edpuzzle name: p19kala P2019017

[Μεταβαση στην ενοτητα "Ομαδικοτητα και συνεργασια"](#Links-ομαδικότητας-και-συμμετοχής).

## Πίνακας Περιεχομένων:
| Εβδομάδα | Παραδοτεά | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | [Εισαγωγή](#Εισαγωγή)| https://github.com/courses-ionio/help/discussions/79 | Έκανα ο,τι απαιτείται για το παραδοτέο 1. |
| 2 | [βιογραφικό και δημιουργία ομάδας](#Ιστοσελίδα-βιογραφικού-και-ένταξη-σε-ομάδα) | https://github.com/courses-ionio/help/discussions/230 | Ακολούθησα τα κριτήρια για την άριστη βαθμολόγηση, αλλά κατά τη γνώμη μου υπάρχει πολύ χώρος για βελτίωση. Έχω ιδέες, άλλα όχι χρόνο προς το παρών. Θα το επεξεργαστώ περαιτέρω στη πορεία.|
| 3 | [Αίτημα ενσωμάτωσης στην ιστοσελίδα](#Pull-Request-1)| https://github.com/courses-ionio/help/discussions/326 | Ακολούθησα τις οδηγίες και βγήκε άριστη. |
| 4 | [Άσκηση γραμμής εντολών 1](#Ασκηση-Γραμμης-Εντολων-1) | https://github.com/courses-ionio/help/discussions/363 | Η ασκηση γραμμης εντολων δεν εγινε σε συστημα χωρις systemd και το custom λειτουργικο συστημα ηταν το FreeBSD. Θα τη βελτιωσω στο μελλον και μαλλον θα βαλω Void Linux. |
| 5 | [Συμμετοχικό περιεχόμενο A1+A2](#Συμμετοχικο-1) | https://github.com/courses-ionio/help/discussions/428 | Ακολούθησα τις οδηγίες και βγήκε άριστη. |
| 6 | [Άσκηση γραμμής εντολών 2](#Ασκηση-Γραμμης-Εντολων-2) | https://github.com/courses-ionio/help/discussions/474 | Εκανα εγκατασταση το void linux σε VM απο iso image. Ηταν σχετικα ευκολη διαδικασια, αλλα κολλαει αρκετα στο terminal οποτε η εμπειρια εκει ηταν κουραστικη. |
| 7 | [Βιογραφικό](#Βιογραφικό) | https://github.com/courses-ionio/help/discussions/519  | Γρηγορη και ευκολη διαδικασια. Χρηση pandoc, latex, git hooks.  |
| 8 | [Αίτημα ενσωμάτωσης στην ιστοσελίδα](#Pull-Request-2) | https://github.com/courses-ionio/help/discussions/549 | Δυσκολη διαδικασια παρολο που ηταν μονο 3 γραμμες, αλλα φοβερη εξασκηση σε html/css/javascript και πως να δουλευω με το inspect του chrome, το οποιο με βοηθησε αργοτερα σε αλλες δουλειες. |
| 9 | [Άσκηση γραμμής εντολών](#Ασκηση-Γραμμης-Εντολων-3) | | |
| 10 | [Συμμετοχικό περιεχόμενο B1+B2](#Συμμετοχικο-2-με-αλλαγες-στο-συμμετοχικο-1)| | |
| 11 | [Άσκηση γραμμής εντολών](#Ασκηση-Γραμμης-Εντολων-4) | | |
| 12 | Τελική αναφορά* | | |

## Εισαγωγή
Καθως το ενδιαφερον μου ειναι για την ασφαλεια, για αρχη εβαλα το ntfy να με ειδοποιει στο κινητο οταν το τερματικο στο λινουξ μου τρεχει μια εντολη. Ειτε ειναι με τον φυσικο υπολογιστη μου, ειτε καποιος επιτιθεμενος με ενα κακοβουλο λογισμικο, θα γνωριζω ποτε εκτελει εντολες, ποιες εντολες και ποση διαρκεια ειχαν. Οταν ηρθε η ωρα να διαλεξω ενα λειτουργικο χωρις systemd, επελεξα το Void Linux OS, καθως διαβασα οτι υποσχοταν γρηγορο boot με το δικο του init συστημα. Πιστευω οτι το systemd παιρνει τον ελεγχο ενος μερος του συστηματος απο τον χρηστη για διευκολυνση στο φορτο εργασιας, αλλα αυτο δεν συμφερει εμενα. Για αυτο αποφασισα να ερευνησω αυτο το εξαμηνο λειτουργικα χωρις systemd ως το init τους, ωστε να δω τι εναλλακτικες υπαρχουν. Συγκεκριμενα, διαλεξα το init του Void, runit, που μπορει να δουλεψει *και* ως init, αλλα *και* ως διαχειριστης υπηρεσιων το οποιο αφηνει να δουλεψει αρμονικα μαζι με αλλες init διεργασιες (περισσοτερα στο συνδεσμο της ιστοσελιδας στην αντιστοιχη ενοτητα παρακατω).

## Ιστοσελίδα βιογραφικού και ένταξη σε ομάδα
Σύνδεσμοι στο [αποθετήριο](https://github.com/p19kala/online-cv/tree/gh-pages) του κώδικα της ιστοσελίδας, στην [ομάδα](https://github.com/Git-s-PopTeamEpic) και το [webring](https://git-team-epic-webring.netlify.app/) της. Το βιογραφικό μου: https://p19kala.github.io/online-cv/

Συμπλήρωσα το βιογραφικό βάση του template και προσθεσα τα εξης:
- Αλλαξα το χρωμα του θεματος jekyll στην ιστοσελιδα
- Προσθεσα επιπλεον ενοτητα "Programs & Proficiency" κατω απο τα "skills & proficiency" για να δειξω ποια προγραμματα γνωριζω και ποσο. Για να το κανω αυτο, αντεγραψα τον φακελο skills.html και δημιουργησα τον programs.html, αλλαζωντας ολα τα αντικειμενα "skills" με "programs". Επειτα πηγα στο index.html και προσθεσα τη γραμμη `{% include programs.html %}`.
- Περασα την ενοτητα "graduation" απο το sidebar στο body της ιστοσελιδας για να φαινεται πιο εμπλουτισμενη καθως δεν ειχα δεξιοτητες να γραψω (και ετσι φαινονται τα details του education)
- Προς το παρων xρησιμοποιωντας το raw content ενος pdf αρχειου που δημιουργησα, ο χρηστης πατωντας στο λινκ μπορει να κατεβασει το βιογραφικο μου σε pdf μορφη.
- Asciinema: https://asciinema.org/a/nfULxsiwhCHFN4VbcVqvPqMAD

## Pull Request 1
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
Για αυτη την εβδομαδα στην ασκηση γραμμης εντολων εγκατεστησα το void linux στο virtualbox. Εκανα neofetch και dmesg και χρησιμοποιησα το εργαλειο [ntfy](https://github.com/dschep/ntfy) οπως στην ασκηση 1 (ωστε αυτη τη φορα να μετρησει στο βαθμο, καθως ειναι σε systemd-less OS). 
Asciinema: https://asciinema.org/a/M2Mr7PfLmd4XkLkQvuvwTjwrb <br>

Χρησιμοποιησα ενα recording application για να δειξω το desktop notification που εμφανιστηκε μετα το download (καθως το asciinema δεν μπορει να το δειξει):<br>
![image](https://user-images.githubusercontent.com/72458452/160300105-4cfe2aed-af6f-45c1-8499-89d6e66bea97.gif)<br>

Επιπλεον, εγκατεστησα την εφαρμογη "pushbullet" σε android emulator και εγραψα το αρχειο `~/.ntfy.yml`ωστε να εχει ως backends το pushbullet και να μπορει να στειλει ειδοποιησεις στο "κινητο" μου. Ετσι, οποιαδηποτε εντολη κανω και διαρκεσει παραπανω απο 10 δευτερολεπτα (default setting), οταν τελειωσει θα σταλθει ειδοποιηση _και_ στο "κινητο" μου _και_ στο desktop του Void.<br>
![ezgif com-gif-maker (9)](https://user-images.githubusercontent.com/72458452/160302752-3c10e38f-5241-470d-a06b-69419020abdf.gif)


Προσπαθησα επισης να δουλεψω με το εργαλειο [huginn](https://github.com/huginn/huginn) για να δημιουργησω εναν agent που θα "τραβαει" τα τελευταια news απο [αυτη την ιστοσελιδα](https://m.naftemporiki.gr/liveblog/1835606#top) την οποια ακολουθω, αλλα υπηρξε προβλημα στο bundle και θα χρειαστω χρονο να το λυσω.
<br>

## Βιογραφικό
Δημιουργησα [αλλο ενα pdf αρχειο](https://github.com/p19kala/online-cv/blob/gh-pages/assets/pdf/cv.pdf) με το pandoc και το latex. Η εντολη `pandoc https://p19kala.github.io/online-cv/ -o cv.tex -s` παιρνει τη σελιδα και τη μετατρεπει σε .tex αρχειο. Επειτα χρησιμοποιωντας την εντολη `pdflatex cv.tex`, δημιουργειται το pdf αρχειο με το εργαλειο latex. Πηγα στον φακελο \_includes και πειραξα το αρχειο [contact.html](https://github.com/p19kala/online-cv/blob/gh-pages/_includes/contact.html#:~:text=%3Ca%20href%3D%22%7B%7B%20sidebar.pdf2%20%7D%7D%22%20target%3D%22_blank%22%3EResume%20(LaTeX)%20PDF%3C/a%3E) ωστε να εχω [2 ξεχωριστους downloadable συνδεσμους](https://github.com/p19kala/online-cv/blob/gh-pages/_data/data.yml#:~:text=pdf2%3A%20https%3A//raw.githubusercontent.com/p19kala/online%2Dcv/gh%2Dpages/assets/pdf/cv.pdf) για τα pdf μου. Επιπλεον, εφτιαξα 2 αρχεια pre-commit και post-commit στο path ".git/hooks" τα οποια διαχειριζονται τη συνεχή ενσωμάτωση του pdf. Δημιουργει καινουργιο pdf απο τη τροποποιημενη σελιδα, ωστε να ειναι παντα ενημερωμενο.

Asciinema: https://asciinema.org/a/bZVTBuvyCW8J2vL6l8NUpkhrV

Επισης βελτιωσα λιγο παραπανω την ιστοσελιδα. Εβαλα τα ποσοστα σε text μορφη κατω απο τα sliders στις [Skills](https://github.com/p19kala/online-cv/blob/gh-pages/_includes/skills.html#:~:text=div%3E%3C!%2D%2D//level%2Dbar%2D%2D%3E-,%7B%7B%20skill.level%20%7D%7D,-%3C/div%3E%3C!%2D%2D//item%2D%2D%3E) / [Programs](https://github.com/p19kala/online-cv/blob/gh-pages/_includes/programs.html#:~:text=div%3E%3C!%2D%2D//level%2Dbar%2D%2D%3E-,%7B%7B%20skill.level%20%7D%7D,-%3C/div%3E%3C!%2D%2D//item%2D%2D%3E) ενοτητες μου.

Asciinema: https://asciinema.org/a/m0qVjqPG8RDhnlze7shhsjIpG

**Προβληματα που αντιμετωπισα:**
- Δεν ηταν εγκατεστημενο ενα πακετο με διαφορα fonts. Μου εβγαζε καποια errors οταν εκανα την εντολη `pdflatex` και δημιουργουσε ενα missfont.log αρχειο το οποιο περιειχε το ονομα του error. Συγκεκριμενα, το error ηταν "mktextfm ecrm1000" και το διορθωσα με την εντολη `sudo apt-get install texlive-fonts-recommended`, η οποια κατεβαζει καποια προτεινομενα fonts για το texlive.

## Pull Request 2
Αρχικα προσπαθησα να κανω την ιστοσελιδα να αναγνωριζει ποτε ο τυπος συσκευης του χρηστη ειναι κινητο, για να φτιαξω το βιντεο στην αρχικη σελιδα και να ελεγξω αν το layout προσαρμοζεται σωστα σε μικροτερες οθονες. Δεν καταφερα να το υλοποιησω.

Σημειωση: Η αλλαγη αυτη ειναι στο path assets/css/main.scss του αποθετηριου minimal-ionio.
Υλοποιησα μια λειτουργια να μενει το navigation bar menu στο πανω μερος της σελιδας, οταν ο χρηστης κανει scroll προς τα κατω. Ετσι, δεν χρειαζεται να επιστρεψει πανω για να περιηγηθει σε αλλη σελιδα. Αυτο θα βοηθησει ιδιαιτερα στις σελιδες που ειναι πολυ μεγαλες (σελιδες "Σπουδες", "Προσωπικο"). Η ιδεα της υλοποιησης ηρθε μετα απο δικια μου αναγκη οταν επισκεπτομουν συχνα τη σελιδα "Σπουδες" και ηθελα να μπορω να αλλαζω γρηγορα σε αλλη σελιδα.<br>
Σχετικο issue: https://github.com/ioniodi/sitegr/issues/382 <br>
Συνδεσμος στο αρχειο με τις αλλαγες: [γραμμες 12 με 15, η κλαση .masthead](https://github.com/p19kala/minimal-ionio/blob/demo-branch/assets/css/main.scss) <br>
Συνδεσμος στο demo: https://p19kalasw.netlify.app/ <br>
Συνδεσμος σε παλιο issue που πηρε το οκ απο τον καθηγητη αλλα αυτος που ανοιξε το issue τελικα δεν το εκανε PR: https://github.com/ioniodi/sitegr/issues/206#issuecomment-825857093
Εχω λυσει το προβλημα που αναφερθηκε εδω: https://github.com/ioniodi/sitegr/issues/206#issuecomment-822429411. Χρειαζεται το z-index να ειναι πιο υψηλο απο το z-index καθε αλλου αντικειμενου, οποτε το εβαλα μια ακραια τιμη.

## Ασκηση Γραμμης Εντολων 3

## Συμμετοχικο 2 με αλλαγες στο συμμετοχικο 1
Πραγματοποιησα αλλαγες στην προσθηκη μου Void Linux. Αντι να λεω γενικα πραγματα για το Void, εγραψα συγκεκριμενα για το [runit](https://github.com/p19kala/_gallery/blob/P2019017/runit.md) init συστημα που χρησιμοποιει το Void και το πλεονέκτημά του ειναι να κανει boot πιο γρηγορα το λειτουργικο χαρη σε μια λειτουργια του (παραλληλισμος των υπηρεσιων εκκινησης). Ενω κανει boot, ταυτοχρονα τρεχει startup services για να γλιτωσει χρονο. Εκανα screenshot το boot του runit και το εβαλα στη θεση του Void logo που ειχα προηγουμενως. [Full image](https://github.com/p19kala/images/commit/b58fb2ef11b26b1d27760efa0c398e730a86cbc7) and [thumbnail](https://github.com/p19kala/images/commit/349ee52589d570c8b75cf6d86ea94539dde73265).<br>
Revised Gallery (demo): https://p19kala-pibook.netlify.app/gallery/runit <br>
Slide: [pibook](https://p19kala-pibook.netlify.app/slides/service-manage/), [github](https://github.com/p19kala/site/blob/livedemo/_slides/service-manage.md) <br>
Timeline: [pibook](https://p19kala-pibook.netlify.app/timeline/os-apps/), [github](https://github.com/p19kala/site/blob/livedemo/_timeline/os-apps.md)

Αντικατασταση της εγγραφης για το FreeBSD με το XBPS package manager του Void. Δημιουργηθηκε απο το μηδεν απο την ομαδα του Void και συντηρειται μεχρι σημερα. Υλοποιηθηκε για πρωτη φορα στο λειτουργικο του Void, το οποιο με τη σειρα του δημιουργηθηκε αποκλειστικα ως testing grounds για το XBPS. Ο κωδικας βρισκεται στο [github](https://github.com/void-linux/xbps). Περισσοτερα εδω:<br>
Εικονα με λεζαντα: https://p19kala-pibook.netlify.app/gallery/void-xbps/ <br>
Εικονα [full](https://github.com/p19kala/images/commit/dcd60635e92d270f8ee43408fa52a01e0b35bfb4) και [thumbnail](https://github.com/p19kala/images/commit/6096a01c608b82c0e88b48e9cf44bc319aa9890a). <br>
Slide: [pibook](https://p19kala-pibook.netlify.app/slides/service-managers/), [github](https://github.com/p19kala/site/blob/livedemo/_slides/service-managers.md) <br>
Timeline: [pibook](https://p19kala-pibook.netlify.app/timeline/os-apps/), [github](https://github.com/p19kala/site/blob/livedemo/_timeline/os-apps.md)

More to be added...

## Ασκηση Γραμμης Εντολων 4

## Links ομαδικότητας και συμμετοχής
Δημιουργια guide στα discussions του sitegr για Ruby version management: https://github.com/courses-ionio/help/discussions/200

Βοήθεια σε issue για το 1o pull request: https://github.com/ioniodi/sitegr/issues/281#issuecomment-1059838232

Αξιολόγηση issue ενός άλλου συνεργάτη για το 1ο αιτημα: https://github.com/ioniodi/sitegr/issues/230#issuecomment-1059802447

Αξιολογηση issue ενός συνεργάτη για το 2ο αιτημα: https://github.com/ioniodi/sitegr/issues/386#issuecomment-1092695663

Απαντηση σε ερωτηση στα discussions του sitegr: https://github.com/ioniodi/sitegr/discussions/229#discussioncomment-2295458

Βοηθεια σε προβλημα στα discussions του help: https://github.com/courses-ionio/help/discussions/304#discussioncomment-2301642

Βοηθεια σε guide στα discussions του help: https://github.com/courses-ionio/help/discussions/344#discussioncomment-2342616

Βοηθεια σε ερωτησεις στα discussions του help: https://github.com/courses-ionio/help/discussions/406#discussioncomment-2394513, https://github.com/courses-ionio/help/discussions/576#discussioncomment-2685800
