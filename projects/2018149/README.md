# Μάθημα: Τεχνολογία Λογισμικού

**Ονοματεπώνυμο: Δημήτρης Πραματευτάκης** | **ΑΜ: Π2018149** | **Link αποθετηρίων μου: [[dimpram/sw](https://github.com/dimpram/sw)]**

## Σύνοψη

| Εβδομάδα* | Παραδοτέο |
| --- | --- |
| 1 | [Φορκ του αποθετηρίου και δημιουργία της σελίδας της αναφοράς με τα προσωπικά στοιχεία σας, της σύνοψης με αυτόν τον πίνακα περιεχομένων, και συγγραφή της εισαγωγής με περιγραφή των αναγκών και των στόχων σας για το αντίστοιχο μάθημα*](#1-εισαγωγή) |
| 2 | [βιογραφικό](#2-βιογραφικό) |
| 3 | [Αίτημα ενσωμάτωσης στην ιστοσελίδα](#3-αίτημα-ενσωμάτωσης-στην-ιστοσελίδα) |
| 4 | [Άσκηση γραμμής εντολών](#4-άσκηση-γραμμής-εντολών) |
| 5 | [Συμμετοχικό περιεχόμενο](#5-συμμετοχικό-περιεχόμενο) |
| 6 | [Άσκηση γραμμής εντολών](#6-άσκηση-γραμμής-εντολών) |
| 7 | [βιογραφικό](#7-βιογραφικό) |
| 8 | [Αίτημα ενσωμάτωσης στην ιστοσελίδα](#8-αίτημα-ενσωμάτωσης-στην-ιστοσελίδα) |
| 9 | [Άσκηση γραμμής εντολών](#9-άσκηση-γραμμής-εντολών) |
| 10 | συμμετοχικό περιεχόμενο |
| 11 | Άσκηση γραμμής εντολών |
| 12 | Τελική αναφορά* |

Το παρόν αρχείο αποτελεί την αναφορά μου για το μάθημα **Τεχνολογία λογισμικού** και περιέχει περιγραφές για κάθε εργασία που υλοποίηθηκε κατά την διάρκεια της ολοκλήρωσης του μαθήματος.

## 1. Εισαγωγή

Για το μάθημα **Τεχνολογία λογισμικού**, στόχος μου αποτελεί η κατανόηση και η εφαρμογή τεχνικών ανάπτυξης λογισμικού μέσα από την πρακτική εξάσκηση που παρέχουν εργασίες οι οποίες θα υλοποιηθούν στα προσεχώς παραδοτέα. Ανάγκες όπως η απόκτηση πρακτικής εμπειρίας ανάπτυξης εφαρμογών πέρα από την κατανόηση της θεωρίας είναι κάτι για το οποίο όχι μόνο δίνω μεγάλη βαρύτητα αλλά αποτέλει και κίνητρο για την βαθύτερη ενασχόληση με το αντικείμενο του μαθήματος και την ποιοτική ικανοποίηση των στόχων του. 

## 2. Βιογραφικό
Για αυτήν την βδομάδα στόχος του παραδοτέου ήταν η δημιουργία του βιογραφικού μας με την μορφή μιας ιστοσελίδας το οποίο αποτελεί το πρώτο μέρος του συνολικού παραδοτέου που αφορά το βιογραφικό. Αρxικά, έφτιαξα από την αρχή ένα δικό μου jekyll theme gem το οποίο το άνεβασα στο [rubygems.org](https://rubygems.org/) με βάση το επίσημο [jekyll theme gem documentation](https://jekyllrb.com/docs/themes/#creating-a-gem-based-theme) και το χρησιμοποιώ από το αποθετήριο του βιογραφικού μου. Όπως περιγράφοουν και οι οδηγίες του παραδοτέου, το theme που έφτιαξα περιέχει ένα κεντρικό αρχείο `cv.yml` στο οποίο βρίσκονται όλες οι πληροφορίες για την κατασκευή του βιογραφικού. Τέλος, το βιογραφικό μου ακολουθεί ακαδημαική δομή και στυλ και είναι προσαρμοσμένο στο να εκτυπώνεται ορθά σε μια σελίδα Α4 και μπορεί να προβληθεί στο προσωπικό μου domain `cv.dimitrisprama.com`

**Σύνδεσμοοι**

- [[dimpram/cv](https://github.com/dimpram/cv)]
- [[dimpram/academic-cv-jekyll](https://github.com/dimpram/academic-cv-jekyll)]
- http://cv.dimitrisprama.com


Για το δεύτερο μέρος του παραδοτέου μου απομένουν
1. Continuous Integration
2. Παραγωγή PDF μέσω του command line εργαλείου `pandoc`

[![asciicast](https://asciinema.org/a/qdHu1taXRKKSqr9LCG6m6Fy0O.svg)](https://asciinema.org/a/qdHu1taXRKKSqr9LCG6m6Fy0O)

## 3. Αίτημα ενσωμάτωσης στην ιστοσελίδα

Η δική μου συνεισφορά στην σελίδα ήταν η διόρθωση του reponsiveness στο footer. Πιο συγκεκριμένα, αυτό αφορούσε ένα include στο αποθετήριο του θέματος δηλαδή στο minmal-ionio και χρειάστηκε να γίνει ένα rewrite στην CSS που χρησιμοποιούσε καθώς και να αφαιρεθούν κάποια άχρηστα html tags. Για αυτό δημιούργησα ένα νέο minimal-ionio scss αρχείο για την προσθήκη νέας CSS χωρίς να εμπλέκεται με την κεντρική CSS του θέματος. Έτσι το minmal mistakes δεν θα επιρεαστεί μελλοντικά από αυτήν την αλλαγή όταν θα γίνει το επόμενο update στο θέμα. Επίσης, αυτό το στήσιμο αποτελεί ένας κομψός τρόπος συγγραφής των CSS styles με κλάσεις και όχι με inline styling που συνέβαινε εως τώρα στις προσθήκες που αφορούσαν το minimal-ionio. 

![comparison](https://user-images.githubusercontent.com/44473195/110768095-93511280-825f-11eb-9282-3ff372c70a9e.png)

*Σύγκριση πριν την αλλαγή(αριστερά) και μετά την αλλαγή(δεξιά)*


Για την υλοποίηση αυτών τον αλλαγών χρησιμοποίησα τα δικά μου forks των αποθετήριων sitegr και minimal-ionio και αξιοποιόντας το workflow ["Αλλαγή και στα 2 αποθετήρια"](https://github.com/ioniodi/sitegr/wiki/Workflow#%CE%91%CE%BB%CE%BB%CE%B1%CE%B3%CE%AE-%CE%BA%CE%B1%CE%B9-%CF%83%CF%84%CE%B1-%CE%B4%CF%8D%CE%BF-%CE%B1%CF%80%CE%BF%CE%B8%CE%B5%CF%84%CE%AE%CF%81%CE%B9%CE%B1) έκανα όλες μου τις δοκιμές αλλαγές τοπικά σε νέο branch στο minmal-ionio. Έπειτα, έφτιαξα ένα καινούριο deploy στο netlify που χρησιμοποιούσε το καινούριο branch που είχα στο minimal-ionio και χρησιμοποίησα αυτό το deploy ως preview για το pull request μου.

**Links**

- [Pull Request](https://github.com/ioniodi/minimal-ionio/pull/39)
- [Issue](https://github.com/ioniodi/sitegr/issues/109)
- [[dimpram/sitegr](https://github.com/dimpram/sitegr)]
- [[dimpram/minimal-ionio](https://github.com/dimpram/minimal-ionio/tree/fix-footer-responsiveness)]


Παράλληλα εκείνη την χρονική περίοδο πραγματοποίσα μερικά Pull request reviews από συνεισφορές συναδέλφων από τα οποία μερικά κατάφερα να τα κάνω και merge στο κεντρικό αποθετήριο.Επιπλέον έδωσα συμβουλές ακόμα και σε περιπτώσεις που δεν μου ζητήθηκε ευθέως. Παρακάτω φαίνεται όλη η συνεργατική δραστηριότητα μου:

- [Προσθήκη Ανακοίνωσης "Εκδήλωση Παρουσιάσεων Ατομικών Εργασιών Φοιτητών ΠΜΣ “Ψηφιακές Εφαρμογές και Καινοτομία” 2020-2021" #127](https://github.com/ioniodi/sitegr/pull/127)
- [Adding course "Graph Theory and Applications" in the 6th semester #112](https://github.com/ioniodi/sitegr/pull/112#pullrequestreview-608424712)
- [Προσθήκη ανακοίνωσης "15ο Διεθνές Εργαστήριο Σημασιολογικής και Κοινωνικής Μέσης Προσαρμογής & Εξατομίκευσης «SMAP 2020» (ONLINE)"#106](https://github.com/ioniodi/sitegr/pull/106)
- [Προσθήκη Πρακτικής Άσκησης #103](https://github.com/ioniodi/sitegr/pull/103#event-4423730770)
- [Προσθήκη ανακοίνωσης "Ανακοίνωση δήλωση θέματος και τριμελούς πτυχιακής Φεβρουάριος - Μάρτιος 2021" #135](https://github.com/ioniodi/sitegr/pull/135)
- [Αλλαγές στο μάθημα «Έξυπνα Περιβάλλοντα και Εφαρμογές» #153](https://github.com/ioniodi/sitegr/pull/153)
- [Προσθήκη Ανακοίνωσης:"Διεθνές Συνέδριο Sunbelt XXVII" #154](https://github.com/ioniodi/sitegr/pull/154)
- [Προσθήκη ΕΔΙΠ Προσωπικού : Σωτηροπούλου Άννα](https://github.com/ioniodi/sitegr/pull/108)
- [Add course "Distributed Network Systems" #113](https://github.com/ioniodi/sitegr/pull/113)
- [Μεταφορά-μετατροπή της σελίδας εράσμους σε ανακοίνωση #161](https://github.com/ioniodi/sitegr/pull/161)
- [Προσθήκη ανακοίνωσης "Διαβούλευση για το Σχέδιο του Εσωτερικού Κανονισμού του Ιονίου Πανεπιστημίου" #98](https://github.com/ioniodi/sitegr/pull/98)
- [Προσθήκη Ανακοίνωσης "Πρόσκληση εκδήλωσης ενδιαφέροντος για εγγραφή στο Μητρώο Φοιτητών της Εθνικής Αρχής Ανώτατης Εκπαίδευσης (ΕΘΑΑΕ)" #116](https://github.com/ioniodi/sitegr/pull/116)
- [Προσθήκη ανακοίνωσης #129](https://github.com/ioniodi/sitegr/pull/129)
- [2018171 add multimedia details #130](https://github.com/ioniodi/sitegr/pull/130/)
- [Προσθήκη των πληροφοριών του μαθήματος “Ελεύθερη Επιλογή” #132](https://github.com/ioniodi/sitegr/pull/132)
- [Προσθήκη της ανακοίνωσης "Κυκλοφόρησε το πρώτο τεύχος του ηλεκτρονικού ενημερωτικού δελτίου ionio" που δημοσιεύτηκε στις 09-02-2021 ώρα 10:52 #156](https://github.com/ioniodi/sitegr/pull/156)
- [Προσθήκη μαθήματος "Εφαρμοσμένος Προγραμματισμός με Python" #126](https://github.com/ioniodi/sitegr/pull/126)
- [Βελτιστοποίηση της SCSS του footer #177](https://github.com/ioniodi/sitegr/issues/177)
- [Δημιουργία δυνατότητας προσθήκης zoom link στα profile κάθε εκπαιδευτικού της σχολής #181](https://github.com/ioniodi/sitegr/issues/181)
- [Προσθήκη "Back to Top" Button #188](https://github.com/ioniodi/sitegr/issues/188)
- [Διόρθωση εμφάνισης των link "Learn More" στην βασική σελίδα μέσω οθόνης κινητού. #194](https://github.com/ioniodi/sitegr/issues/194)
- [Διαγραφή των κουμπιών "Learn more" και προσθήκη λινκ στους τίτλους. #42](https://github.com/ioniodi/minimal-ionio/pull/42#pullrequestreview-653615950)

## 4. Άσκηση γραμμής εντολών

***Εκφώνηση: "set-up continuous integration"***

Σε αυτήν την άσκηση ασχολήθηκα με τα Github actions αντί για το Travis CI. Δημιούργησα ένα action για το βιογραφικό μου το οποίο με το που γίνεται ένα commit στο main branch του αποθετηρίου μου κάνει αυτόματα build οτι αλλαγές έγιναν στο cv.yml, σε pdf μέσω του pandoc. Και όλα αυτα παράλληλα με το build του jekyll site που γίνεται από το netlify. Εν ολίγης, πλέον όλα είναι αυτοματοποιημένα στο αποθετήριο του βιογραφικό μου.

![1assignment](https://user-images.githubusercontent.com/44473195/111388914-cd377400-86b8-11eb-8817-73f97b069d39.gif)

## 5. Συμμετοχικό περιεχόμενο

Το πρώτο μέρος της συνεισφοράς μου στα πλαίσια της άσκησης συμμετοχικού περιεχόμενου.

**Αποθετήρια**

- [[dimpram/site](https://github.com/dimpram/site)]
- [[dimpram/images](https://github.com/dimpram/images)]
- [[dimpram/_gallery](https://github.com/dimpram/_gallery)]

**Ζήτημα Α1**

| Θέμα                 | Εικόνα                                                                                             | Thumbnail                                                                                                      | Markdown                                                                                                                   |
|----------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Mouse pointing stick | [mouse-pointing-stick.jpg](https://github.com/dimpram/images/blob/master/mouse-pointing-stick.jpg) | [mouse-pointing-stick-thumb.jpg](https://github.com/dimpram/images/blob/master/mouse-pointing-stick-thumb.jpg) | [mouse-poiting-stick.md](https://github.com/dimpram/_gallery/blob/master/mouse-pointing-stick.md)                          |
| Streaming media      | [streaming-media.png](streaming-media.png)                                                         | [streaming-media-thumb.png](streaming-media-thumb.png)                                                         | [streaming-media.md](https://github.com/dimpram/_gallery/blob/fa23654965079f282cd16e510478b911a81924b4/streaming-media.md) |

**Ζήτημα Α2**

| Περιεχόμενο           	| Σύνδεσμος                                                                           	|
|------------------------	|-------------------------------------------------------------------------------------	|
| Χρονοδιάγραμμα         	| [multimedia.md](https://github.com/dimpram/site/blob/master/_timeline/multimedia.m) 	|
|   Θεματικές διαφάνειες 	| [pointer.md](https://github.com/dimpram/site/blob/master/_slides/pointer.md)        	|

Link του deployment μου: https://dimpram-pibook.netlify.app/


## 6. Άσκηση γραμμής εντολών

***Εκφώνηση: "create your own static site and blog generator"***

Ως παραδοτέο αυτής της άσκησης απόφασισα να υλοποιήσω ένα δικό μου static site generator σε nodejs το οποίο να λειτουργεί με markdown αρχεία και να υποστηρίζει posts, pages και templates. Χρησιμοποιήθηκε η [handlebars](https://handlebarsjs.com/) βιβλιοθήκη που παρέχει μια templating γλώσσα παρόμοια με αυτή του jekyll. Στο παρακάτω asciinema φαίνεται ένα site παράδειγμα το οποίο έφτιξα για να παρουσιάσω την λειτουργία του static site generator το οποίο εντέλει το ονόμασα s3g.js (Simple Static Site Generator).

Συνοπτικά χρειάζεται μια συγκεκριμένη οργάνωση των αρχείων όπως αντίστοιχα και στο jekyll και έπειτα μέσω της εντολής `npm run build` παράγεται ο φάκελος `dist` που περιέχει το τελικό site το οποίο μπορεί να γίνει deploy σε μέρη όπως το netlify κτλ.

Αποθετήριο κώδικα: [[dimpram/s3g.js](https://github.com/dimpram/s3g.js)]

[![asciicast](https://asciinema.org/a/8lbsqVHMd8sZTssTR9UrDOm08.svg)](https://asciinema.org/a/8lbsqVHMd8sZTssTR9UrDOm08)

## 7. Βιογραφικό

Με αφορμή μια [άσκηση γραμμής εντολών](#4-άσκηση-γραμμής-εντολών) που χρειάστηκε να ολοκληρώσω ως παραδοτέο της 4η βδομάδας, τα ζητήματα που αφορούσαν το Continuous Integration και την παραγωγή του βιογραφικού με την βοήθεια του εργαλείου pandoc έχουν ήδη υλοποιηθεί. Οπότε ως παραδοτέο αυτής της βδομάδας αποφάσισα να συμπληρώσω κάποιες λεπτομέρειες όπως ένα κουμπί για να μπορεί να προβληθεί το pdf και μερικές διορθώσεις στο κείμενο. Πλέον αυτό το βιογραφικό αποτελεί το επίσημο βιογραφικό μου.

![View pdf button](https://user-images.githubusercontent.com/44473195/114185332-4b9cd400-994e-11eb-97cc-7f3ea987193e.png)

- [[dimpram/cv](https://github.com/dimpram/cv)]
- [[dimpram/academic-cv-jekyll](https://github.com/dimpram/academic-cv-jekyll)]
- http://cv.dimitrisprama.com


## 8. Αίτημα ενσωμάτωσης στην ιστοσελίδα

Ως δεύτερη συνεισφορά στην σελίδα ήταν η διόρθωση της θέσης εμφάνισης των περιγραφών των μαθημάτων. Όσα μαθήματα είχαν κείμενο πέρα από την μεταβλητή excerpt, εμφανιζόντουσαν κάτω από την βιβλιογραφία πράγμα που ήταν μη ορθο. Έτσι με την διόρθωση του κώδικα το αποτέλεσμα ήταν πλέον το επιθυμητό. Παρακάτω φαίνεται η σύγκριση πριν (αριστερά) και μετά (δεξιά) μετά την συνεισφορά.

<p align="center">
  <img align="left" src="https://user-images.githubusercontent.com/44473195/110914149-a971d800-831e-11eb-85ae-40d9154c0415.png" width="460" height="460">
  <img align="right" src="https://user-images.githubusercontent.com/44473195/111343371-09041680-8684-11eb-992b-018c052a6bb8.png" width="460" height="460">
</p>


Για την υλοποίηση αυτών τον αλλαγών χρησιμοποίησα το δικο μου fork του αποθετηρίου minimal-ionio και αξιοποιόντας το workflow ["Αλλαγή στο minimal-ionio"](https://github.com/ioniodi/sitegr/wiki/Workflow#%CE%91%CE%BB%CE%BB%CE%B1%CE%B3%CE%AE-%CF%83%CF%84%CE%BF-minimal-ionio) έκανα όλες μου τις δοκιμές αλλαγές τοπικά σε νέο branch στο minmal-ionio. Έπειτα, έφτιαξα ένα καινούριο deploy στο netlify που χρησιμοποιούσε το καινούριο branch που είχα στο minimal-ionio και χρησιμοποίησα αυτό το deploy ως preview για το pull request μου.

**Links**

- [Pull Request](https://github.com/ioniodi/minimal-ionio/pull/40)
- [Issue](https://github.com/ioniodi/sitegr/issues/155)
- [[dimpram/sitegr](https://github.com/dimpram/sitegr)]
- [[dimpram/minimal-ionio](https://github.com/dimpram/minimal-ionio/tree/fix-footer-responsiveness)]


## 9. Άσκηση γραμμής εντολών

***Εκφώνηση: "test an alternative stack of tools"***

Για αυτό το παραδοτέο αποφάσισα να κάνω εγκαταστήσω το FreeBSD λειτουργικό σύστημα σε ένα virtual box και να εγκαταστήσω τα απατραίτητα dependencies ωστε να μπορώ να αναπτύξω λογισμικό σε python. Αρχικά εγκατέστησα εργαλία όπως το `vim` και το `git` και έπειτα έκανα `git clone` ένα δικό μου python script που είχα ανεβάσει στο github λογαριασμό μου. Στην συνέχεια το έκανα edit και το έτρεξα με την freeBSD εκδοση της python.

To python script που χρησιμοποιήθηκε υπολογίζει την εντροπία ενός κειμένου. Περισσότερες λεπτομέρειες μπορούν να βρεθούν [εδώ](https://github.com/dimpram/entropy-calculator)

[![asciicast](https://asciinema.org/a/vFRIQGcqCorIwbH55j8jRr6Kv.svg)](https://asciinema.org/a/vFRIQGcqCorIwbH55j8jRr6Kv)
