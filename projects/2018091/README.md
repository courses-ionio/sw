# Μάθημα: Τεχνολογία Λογισμικού

### Ονοματεπώνυμο: Καλερίδης Ηλίας
  
### Αριθμός Μητρώου: Π2018091

### e-mail: p18kale@ionio.gr

## Σύνοψη

| Εβδομάδα* | Παραδοτέο | Ημερομηνία |
| --- | --- | --- |
| 1 | [Φορκ του αποθετηρίου και δημιουργία της σελίδας της αναφοράς με τα προσωπικά στοιχεία σας, της σύνοψης με αυτόν τον πίνακα περιεχομένων, και συγγραφή της εισαγωγής με περιγραφή των αναγκών και των στόχων σας για το αντίστοιχο μάθημα*](#Εβδομάδα-1) | 20/2 |
| 2 | [βιογραφικό](#Εβδομάδα-2) | 28/2 |
| 3 | [Αίτημα ενσωμάτωσης στην ιστοσελίδα](#Εβδομάδα-3) ([Προσθήκη ανακοίνωησης](https://github.com/ioniodi/sitegr/pull/143)) | 9/3 |
| 4 | [Άσκηση γραμμής εντολών](#Εβδομάδα-4) (ntfy)| 15/3 |
| 5 | [Συμμετοχικό περιεχόμενο](#Εβδομάδα-5) | 21/3 |
| 6 | [Άσκηση γραμμής εντολών](#Eβδομάδα-6) (mqttwarn) | 28/3 |
| 7 | [βιογραφικό](#Εβδομάδα-7) | 4/4 |
| 8 | Αίτημα ενσωμάτωσης στην ιστοσελίδα | - |
| 9 | [Άσκηση γραμμής εντολών](#Εβδομάδα-9) (py-spy, hyperfine) | 25/4 |
| 10 | [συμμετοχικό περιεχόμενο](#Εβδομάδα-10) | 20/5 |
| 11 | [Άσκηση γραμμής εντολών](#Εβδομάδα-11) (huginn) |  23/5 |
| 12 | [Τελική αναφορά*](#Εβδομάδα-12) |

Καθ' όλη την διάρκεια του εξαμήνου η ενασχόληση μου με το τερματικό και τις ανάγκες του μαθήματος γενικότερα ήταν αρκετά συνεπής και συνεχής. Στα πλαίσια της ενασχόλησης αυτής έκανα τα παραδοτέα του μαθήματος, συμμετήχα στα Discussions ([#940](https://github.com/courses-ionio/sw/discussions/940), [#938](https://github.com/courses-ionio/sw/discussions/938), [#934](https://github.com/courses-ionio/sw/discussions/934)) και προσπαθούσα να βοηθάω τους συναδέλφους όπου μπορούσα. Για τις ασκήσεις γραμμής εντολών δεν έκανα πολλά περισσότερα από ένα απλό ντέμο. Για το βιογραφικό επέλεξα να μην κάνω fork κάποιο έτοιμο, αλλά να κάνω το δικό μου από την αρχή (εκτός του θέματος που είναι του Git Hub Pages). Αξίζει να σημειωθεί πως ταυτόχρονα αυτή ήταν και η πρώττη μου επαγή με html καθώς η σχολή μέχρι τώρα δεν προσφέρει κάποιο σχετικό μάθημα και προσωπικά έχω επιλέξει να ασχοληθώ με διαφορετικά πράγματα που με ενδιαφέρουν περισσότερο. Για το δεύτερο αίτημα ενσωμάτωσης λόγω έλειψης γνώσεων στο web development δεν κατάφερα να συνησφέρω σε κάτι λειτουργικό της ιστοσελίδας. Αξίζει να σημειωθεί μια μικρή συνησφορά στο documentation του wiki [Discussion #940](https://github.com/courses-ionio/sw/discussions/940), [Issue #209](https://github.com/ioniodi/sitegr/issues/209). 

## Εβδομάδα 1

### Εισαγωγή
Στόχοι του μαθήματος είναι, στο τέλος του ο φοιτητής να έχει μάθει για την διαδικασία ανάπτηξης και συντήρησης λογισμικού, καθώς και το πως να δουλεύει συνεργατικά σε αυτές τις διαδικασίες. Στο μάθημα επιπλέον, χρησιμοποιείτε η πλατφόρμα GitHub, που προσφέρει υπηρεσίες συνεργατικής ανάπτηξης κώδικα, μεταξύ άλλων συνεργατικών λειτουργιών. Έτσι ταυτόχρονα με τις γνώσεις πάνω στο βασικό θέμα του μαθήματος αποκτούμε εμπειρία και στην χρήση του GitHub και το GitHub Workflow, ένα από τα σημαντικότερα εργαλεία στην αγορά εργασίας. Επίσης το μάθημα αποσκοπεί σε εξοικείωση των φοιτητών με την γραμμή εντολών, αλλά και τους παροτρύνει να χρησιμοποιούν εργαλεία τα οποία προσφέρουν ελευθερία αλλά και προσαρμόζονται με βάσει τις ανάγκες του χρήστη. Αναγκαίες είναι προαπαιτούμενες γνώσεις προγραμματισμού, δικτύων και δομών δεδομένων. Οι γνώσεις σε αυτούς τους τομείς είναι αναγκαίες καθώς είναι πολύ βασικές και αποτελούν τα "θεμέλια" της επιστήμης της Πληροφορικής.


## Εβδομάδα 2

### Βιογραφικό
Για το πρώτο παραδοτέο του βιογραφικού μας ζητήθηκε να δημιουργήσουμε απλά μια σελίδα με την χρήση του εργαλείου [Jekyll](https://jekyllrb.com/). Η σελίδα μου βρίσκεται [εδώ](https://elias2500.github.io/cv-1/). Η πληροφορίες, το θέμα και η μορφή είναι τελείως προσωρινά και υπόκεινται όλα σε αλλαγές. Η σελίδα βασίσεται σε αυτό το [Repository](https://github.com/elias2500/cv-1) του GitHub. Η τωρινή μορφή είναι κάπως έτσι:![cv-1](https://user-images.githubusercontent.com/44614923/113521412-01a89c80-95a2-11eb-9af8-7898d48206e2.png)

## Εβδομάδα 3

### Αίτημα ενσωμάτωσης στην ιστοσελίδα του τμήματος
Για την τρίτη εβδομάδα το ζητούμενο ήταν να κάνουμε μια συνεισφορά στην [ανεπίσημη ιστοσελίδα του τμήματος](https://epic-hamilton-da9ac8.netlify.app/). Εγώ, λόγω της μικρής εμπειρίας που έχω πάνω σε θέματα web, αποφάσησα, για την πρώτη συνεισφορά, απλός να προσθέσω μια [ανακοίνωση](https://epic-hamilton-da9ac8.netlify.app/posts/2021/02/19/ekdilosi-provolis-kai-enimerosis-sto-plaisio-tou-ergou-trumpet/), που έλειπε από την ανεπίσημη ιστοσελίδα. Η διαδικασία ήθελε να ανοίξουμε ένα [issue](https://github.com/ioniodi/sitegr/issues/119), στο οποίο θα έπρεπε πρώτα να πάρουμε την ετικέτα green light και μετά να προχωρήσουμε σε ένα [pull request](https://github.com/ioniodi/sitegr/pull/143). Όσο περίμενα για την ετικέτα, έκανα build την [δική μου έκδοση της σελίδας](https://amazing-brattain-89cab3.netlify.app/), χρησιμοποιώντας το [Netlify](https://www.netlify.com/), για να ελέγξω αν υπάρχει κάποιο πρόβλημα με την προσθήκη που έκανα. Για την δημιουργία του [branch](https://github.com/elias2500/sitegr/tree/demo-branch), αλλά και του [σχετικού αρχείου](https://github.com/elias2500/sitegr/blob/demo-branch/all_collections/_posts/2021-02-19-ekdilosi-provolis-kai-enimerosis-sto-plaisio-tou-ergou-TRUMPET.md), εργάστηκα τοπικά χρησιμοποιώντας ένα docker container και Git, από το οποίο έκανα push τις αλλαγές στο GitHub. Έχω καταγράψει και ανεβάσει την σχετική διαδικασία στο [Asciinema](https://asciinema.org/), στο παρακάτω [link](https://asciinema.org/a/397278).![Screenshot 2021-03-09 225824](https://user-images.githubusercontent.com/44614923/110537169-fee59380-812a-11eb-8954-d4d8409d5197.png)

## Εβδομάδα 4

### Άσκηση γραμμής ενοτλών
Για την 4η εβδομάδα το ζητούμενο ήταν να κάνουμε μια άσκηση γραμμής εντολών. Εγώ επέλεξα να ασxοληθώ με το [ntfy](https://github.com/dschep/ntfy). Το ntfy είναι ένα εργαλείο που επιτρέπει την αποστολή notification όταν τελειώνει μια εργασία στο terminal, όπως θα δείτε και στο [βίντεο](https://www.youtube.com/watch?v=fNVhC6bTTB8). Λόγω των αναγκών του βίντεο, αυτό δεν είναι φτιαγμένο με το [Asciinema](https://github.com/dschep/ntfy), αλλά με το [OBS](https://obsproject.com/) και το [Openshot](https://www.openshot.org/). To link του βίντεο οδηγεί σε upload στο [YouTube](https://www.youtube.com/). Στο βίντεο βλέπετε τις ειδοποιήσεις στο ίδιο το σύστημα, αλλά και ειδοποιήσεις προς το κινητό με την χρήση του [Pushover](https://pushover.net/).

## Εβδομάδα 5

### Συμμετοχικό περιεχόμενο
Για την 5η εβδομάδατο ζητούμενο ήταν να προσθέσουμε δύο νέες φωτογραφίες με λεζάντα και με ελεύθερα πνευματικά δικαιόματα στο βιβλίο [pibook](https://github.com/pibook) και να εντάξουμε αυτές τις εικόνες σε ένα σετ διαφανειών και ένα χρονολόγιο. Εγώ πρόσθεσα εικόνες για το [Arduino IDE](https://github.com/elias2500/images/blob/f77858b48b92c4cc160d1367f3f68a0872182dcf/arduino-ide.png) και για το [Tennis For Two](https://github.com/elias2500/images/blob/f77858b48b92c4cc160d1367f3f68a0872182dcf/tennis-for-two.jpg), και τα αντίστοιχα thumbnail: [Arduino-IDE-thumb](https://github.com/elias2500/images/blob/f77858b48b92c4cc160d1367f3f68a0872182dcf/arduino-ide-thumb.png), [Tennis-For-Two-thumb](https://github.com/elias2500/images/blob/f77858b48b92c4cc160d1367f3f68a0872182dcf/tennis-for-two-thumb.jpg). Επίσης έφτιαξα δύο νέα .md αρχέια για κάθε μία από τις προσθήκες μου [arduino-ide.md](https://github.com/elias2500/_gallery/blob/c66ffe4fce304f08b647a52616c9e5aecaad135f/arduino-ide.md), [tennis-for-two.md](https://github.com/elias2500/_gallery/blob/c66ffe4fce304f08b647a52616c9e5aecaad135f/tennis-for-two.md). Tέλος τροποποίησα τα αρχεία [_slides/preface.md](https://github.com/elias2500/site/blob/master/_slides/preface.md) και [_slides/videogames.md](https://github.com/elias2500/site/blob/master/_slides/videogames.md) για να προσθέσω τις εικόνες σε σετ διαφανειών, αλλά και τα [_timeline/micros](https://github.com/elias2500/site/blob/master/_timeline/micros.md), [_timeline/videogames](https://github.com/elias2500/site/blob/master/_timeline/videogames.md) για να προσθέσω τις εικόνες σε χρονολόγιο. Όλη η διαδικασία είναι καταγεγραμμένη στο παρακάτω [Asciinema Link](https://asciinema.org/a/401042). To instalation του Netlify βρίσκεται [εδώ](https://adoring-hugle-45db8e.netlify.app/). Τα αρχεία στο github δεν θα συμφωνούν με τα αρχεία στο Asciinema, καθώς χρειάστηκαν αρκετές αλλαγές για το Netlify. Αυτές έγιναν σε πολλά διαφορετικά sessions, οπότε και δεν είναι εφικτό και αποδοτικό να καταγραφούν. Η γενική διαδικασία που ακολούθησα, όμως, είναι αυτή του παραπάνω βίντεο. Παράδειγμα πρόσθεσης σε χρονολόγιο:![tennis](https://user-images.githubusercontent.com/44614923/112877315-48445580-90cf-11eb-9ece-52b29daa69b0.png)

#### [Arduino IDE Galery](https://60a57c50dda17200e096c71a--adoring-hugle-45db8e.netlify.app//gallery/arduino-ide/) | [Διαφάνειες](https://60a57c50dda17200e096c71a--adoring-hugle-45db8e.netlify.app//slides/preface/) | [Χονολόγιο](https://60a57c50dda17200e096c71a--adoring-hugle-45db8e.netlify.app//timeline/micros/)
#### [Tennis for Two Galery](https://adoring-hugle-45db8e.netlify.app/gallery/tennis-for-two/) | [Διαφάνειες](https://adoring-hugle-45db8e.netlify.app/slides/videogames/) | [Χρονολόγιο](https://adoring-hugle-45db8e.netlify.app/timeline/videogames/)

## Eβδομάδα 6

### Άσκηση γραμμής εντολών
Για την 6η εβδομάδα το ζητούμενο ήταν να κάνουμε μια άσκηση γραμμής εντολών. Επέλεξα να ασχοληθώ με το mqttwarn. Την εργασία μου, λόγω των αναγκών κατέγραψα με το [OBS](https://obsproject.com/) και επεξεργάστηκα με το [Openshot](https://www.openshot.org/). Το βίντεο έχει ανέβει στο [YouTube](https://www.youtube.com/) στο παρακάτω [λινκ](https://www.youtube.com/watch?v=sRq9zGL1MUY).

## Εβδομάδα 7
### PDF Βιογραφικού
Για την 7η εβδομάδα το ζητούμενο ήταν να δημιουργήσουμε ένα PDF του βιογραφικού μας χρησιμοποιόντας [Pandoc](https://pandoc.org/) και [LaTeX](https://www.latex-project.org/). Ταυτόχρονα έπρεπε να στήσουμε CI που εγώ έκανα μέσω [Git Hooks](https://www.atlassian.com/git/tutorials/git-hooks). Στο script του Git Hook, στην αρχή μετατρέπω την live σελίδα του CV σε LaTex και στην συνέχεια από LaTeX σε pdf με χρήση του pdflatex. Η διαδικασία είναι καταγεγραμμένη στο [Asciinema](https://asciinema.org/) στο παρακάτω [link](https://asciinema.org/a/405112). H σελίδα του CV βρίσκεται [εδώ](https://elias2500.github.io/cv-1/)(μέσω GitHub Pages) και [εδώ](https://elias2500-cv.netlify.app/)(μέσω Netlify) και [εδώ](https://github.com/elias2500/cv-1)(repo). Λόγω της μετατροπής από την live ιστοσελίδα του CV σε LaTeX το pdf μένει μια "έκδοση" πίσω. Έχω σκεφτεί κάποιες πιθανές λύσεις τις οποίες θα δοκιμάσω. (Always a work in progress :P). Το πρόβλημα με τις "εκδόσεις" έχει λυθεί και η αλλαγές φαίνονται [εδώ](https://asciinema.org/a/405203). Η τωρινή μορφή από GitHub Pages:![cv-1](https://user-images.githubusercontent.com/44614923/113521293-3bc56e80-95a1-11eb-8288-dfdd5427cfde.png)

## Εβδομάδα 9 
### Άσκηση γραμμής ενολών
Για την 8η εβδομάδα το ζητούμενο ήταν να κάνουμε μία άσκηση γραμμής εντολών από τις [διαθέσιμες](https://github.com/epidrome/dokey#software). Εγώ ασχολήθηκα με το [py-spy](https://github.com/benfred/py-spy) και το [hyperfine](https://github.com/sharkdp/hyperfine). Για να δείξω την λειτουργία τους έτρεξα ένα script που κάνει bubble sort σε ένα αρχείο με 10000000 random ints. Το asciinema για το py-spy βρίσκεται [εδώ](https://asciinema.org/a/409884), ενώ για το hyperfine, [εδώ](https://asciinema.org/a/409875). To flamegraph που παράγει το py-spy (στο βίντεο το profile1.svg):
![profile1](https://user-images.githubusercontent.com/44614923/116007842-5b890900-a61a-11eb-9101-2fc5ee6cee8a.jpg)

## Εβδομάδα 10
### Συμμετοχικό περιεχόμενο
H 10η εβδομάδα ήταν το δεύτερο παραδοτέο του συμμετοχικού περιεχομένου, όπου έπρεπε να κάνουμε μία νέα [βιογραφία](https://github.com/pibook/site/tree/master/_biography) και μία νέα [μελέτη περίπτωσης](https://github.com/pibook/site/tree/master/_case-study). Εγώ έκανα την βιογραφία του Ralph Baer, "πατέρα" των βίντεο-παιχνιδιών και μελέτη περίπτωσης του Tennis for Two, ενός από τα πρώτα βίντεο-παιχνίδια. Το instalation του Netlify βρίσκεται [εδώ](https://adoring-hugle-45db8e.netlify.app/), ενώ η βιογραφία [εδώ](https://adoring-hugle-45db8e.netlify.app/biography/ralph-baer/) και η μελέτη περίπτωσης [εδώ](https://adoring-hugle-45db8e.netlify.app/case-study/tennis-for-two-cs/).

#### [Ralph Baer Image](https://github.com/elias2500/images/blob/a8bb11801535959eca920c02ef7c5b9e3fe50dac/ralph.jpg) | [Ralph Baer thumb](https://github.com/elias2500/images/blob/a8bb11801535959eca920c02ef7c5b9e3fe50dac/ralph-thumb.jpg) | [Ralph Baer Bio md](https://github.com/elias2500/site/blob/master/_biography/ralph-baer.md) | [Ralph Baer Bio include](https://github.com/elias2500/extras/blob/f0cf315f408f1416049eafe6948b20decb7a569f/bio-baer.md)
#### [Tennis for Two Image](https://github.com/elias2500/images/blob/a8bb11801535959eca920c02ef7c5b9e3fe50dac/tennis-for-two.jpg) | [Tennis for Two Image thumb](https://github.com/elias2500/images/blob/a8bb11801535959eca920c02ef7c5b9e3fe50dac/tennis-for-two-thumb.jpg) | [Tennis for Two cs md](https://github.com/elias2500/site/blob/master/_case-study/tennis-for-two-cs.md) | [Tennis for Two cs include](https://github.com/elias2500/extras/blob/f0cf315f408f1416049eafe6948b20decb7a569f/cs-tennis-for-two.md)

#### Πηγές Ralph Baer: [Wiki](https://en.wikipedia.org/wiki/Ralph_H._Baer), [Article](https://www.baesystems.com/en/feature/father-of-video-games), [Video](https://www.youtube.com/watch?v=83ThW_HjtBg&t=760s)
#### Πηγές Tennis for Two: [Wiki](https://en.wikipedia.org/wiki/Tennis_for_Two)

## Εβδομάδα 11
###  Άσκηση γραμμής εντολών 
Για την 11η εβδομάδα το εργαλείο με το οποίο ασχολήθηκα ήταν το [Huggin](https://github.com/huginn/huginn).![huginn login](https://user-images.githubusercontent.com/44614923/119268090-054bbd80-bbfa-11eb-9935-982776228612.png)
Το Huginn είναι ένα εργαλείο που επιτρέπει την δημιουργία "bot" που κάνουν αυτοματοποιημένες εργασίες online. Εγώ έφτιαξα έναν agent ο οποίος κάνει scrapping για τον τίτλο και το λινκ των [ανακοινώσεων του site της σχολής](https://di.ionio.gr/gr/news/all-news/).![di ionio  announcements](https://user-images.githubusercontent.com/44614923/119268336-24971a80-bbfb-11eb-9dcd-696c0f730a9f.png)
Τα αποτελέσματα είναι κάπως έτσι στο UI του Huginn:![results](https://user-images.githubusercontent.com/44614923/119268466-d0406a80-bbfb-11eb-981f-4872f8e24e2f.png)
και κάπως έτσι στο τερματικό:![results terminal](https://user-images.githubusercontent.com/44614923/119268515-08e04400-bbfc-11eb-9c21-2f9fd11e4b8b.png)
Επίσης ένωσα το Huginn με το [Slack](https://slack.com/intl/en-gr/) μου μέσω ενός post agend, για να λαμβάνω ειδοποιήσεις κάθε φορά που υπάρχει ένα νέο άρθρο.
Ο post agent:![post agent](https://user-images.githubusercontent.com/44614923/119269233-45fa0580-bbff-11eb-973f-dacb04c9fb05.png)
Οι ειδοποιήσεις στο slack:![slack](https://user-images.githubusercontent.com/44614923/119269243-514d3100-bbff-11eb-99e2-4c229be386db.png)

## Εβδομάδα 12
### Συμπεράσματα

Το μάθημα αυτό για εμένα ήταν σαν μια περιπέτεια με αρχή, μέση και τέλος. Ξεκίνησα στην αρχή του εξαμήνου με αυτό το "βουνό" μπροστά μου καθώς ήμουν μέτρια εξοικειωμένος με το Git Hub, καθόλου με το Git και ήξερα βασικές εντολές του τερματικού. Οι κυριότερες εξελήξεις μου επίσης, βρίσκονται σε αυτά τα τρία εργαλεία, καθώς, με τον καιρό, εξοικηωνόμουν περισσότερο με το Git και Git Hub και τον συνδιασμό τους, σε σημείο που πλέον αισθάνομαι άνετα να κάνω αυτά που θέλω. Όσο για το τερματικό, νομίζω πως είχα την μεγαλύτερη εξέληξη καθώς, πέρα απο καινούρια εργαλεία που χρησιμοποιούνται μέσω αυτού, άλλαξα από bash σε zsh που είναι πιο βολικό για git και έχει πολλά plug-in για παραμετροποίηση. Με το τέλος αυτού του μαθήματος αισθάνομαι πως έχω αποκτήσει χρήσιμη εμπειρία για το πώς είναι το workflow της ομαδικής ανάπτηξης κώδικα, πως είναι να εργάζεσαι δηλαδή, σε ένα περιβάλλον "εταιρείας". Με βοήθησε επίσης να καταλάβω πόσο μαρέσει να εργάζομαι σε μία ομάδα, να προσφέρω βοήθεια, αλλά και να μπορώ να βρω βοήθεια όποτε την χρειάζομαι. Μπορώ να πω πως ξεπέρασα κατά πολύ τους στόχος που είχα στην αρχή του εξαμήνου, καθώς περίμενα απλός να εξοικηωθώ περισσότερο με το Git και Git Hub. Δεν περίμενα όμως, όπως προείπα, να έχω αυτή την εξέληξη σε ότι αφορά το τερματικό, αλλά κυρίως δεν είχα καταλάβει πως το μάθημα είναι μια πολύ καλή προσομοίωση του εργασιακού περιβάλλοντος και πως θα μου έδεινε ανεκτίμητη εμπειρία.
