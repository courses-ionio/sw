
# Οπτικοποίηση Δεδομένων Χορηγιών (UK)

## Χατζόπουλος Παναγιώτης (Π2013127)

### Δήλωση και Δέσμευση Θέματος του μαθήματος "Τεχνολογία Λογισμικού" (24 Φεβρουαρίου)
* Ονοματεπώνυμο Φοιτητή:  **Χατζόπουλος Παναγιώτης**
* Αριθμός Μητρώου: **Π2013127**
* Εξάμηνο Φοίτησης: **Επί Πτυχίω**
* E-mail: **p13chat@ionio.gr**
* Θέμα Εργασίας: **Οπτικοποίηση Δεδομένων Χορηγιών (UK) - Data Visualization**
* Προσωπικό αποθετήριο του κώδικα: [Link Αποθετηρίου του κώδικα](https://github.com/p13chat/D3js-uk-political-donations)
* Link για το εκτελέσιμο: [Link Εκτελέσιμου](https://p13chat.github.io/D3js-uk-political-donations/)
* Link για το αποθετήριο του κώδικα του 1ου Παραδοτέου: [Link 1ου Παραδοτέου](https://github.com/p13chat/D3js-uk-political-donations/tree/Paradoteo-1)
* Link για το αποθετήριο του κώδικα του 2ου Παραδοτέου: [Link 2ου Παραδοτέου](https://github.com/p13chat/D3js-uk-political-donations/tree/Paradoteo-2)
* Link για την Τελική Αναφορά: [Τελική Αναφορά](https://p13chat.github.io/final)

### Παραδοτέο 1: Αρχικό έργο και ενδιάμεση αναφορά προόδου - 25% (4 Μαρτίου)

Η παρούσα εργασία αποτελεί εργασία εξαμήνου στο μάθημα του κ. Χωριανόπουλου, με τίτλο "Τεχνολογία Λογισμικού". Πρόκειται για μία παραλλαγή του [κώδικα](https://github.com/neilhawkins/d3-uk-political-donations) που παρέχεται μέσω του Github από τον Διδάσκοντα του μαθήματος. Σκοπός της εργασίας είναι να ολοκληρωθούν οι επιμέρους στόχοι όπως αναφέρονται στα [Παραδοτέο 1](https://github.com/ioniodi/D3js-uk-political-donations/issues/16) και [Παραδοτέο 2](https://github.com/ioniodi/D3js-uk-political-donations/issues/17), δηλαδή οι διάφορες τροποποιήσεις στον ήδη υπάρχοντα [κώδικα](https://github.com/ioniodi/D3js-uk-political-donations). 

1) Αρχικά αφότου έγινε fork στο αντίστοιχο [αποθετήριο](https://github.com/ioniodi/D3js-uk-political-donations) της εργασίας,  ζητήθηκε να πραγματοποιηθεί η σύνδεση της εφαρμογής με την σελίδα μας. 
2) Έπειτα, ζητήθηκε να πραγματοποιηθούν οι κατάλληλες αλλαγές ώστε το url της εφαρμογής να δείχνει το username μας, δίχως την κατάληξη "full-viz.html". 

*Σχετική εικόνα (2)*

<img src="https://imgur.com/dIWrA2m.png"/>  


3) Στη συνέχεια ζητήθηκε να πραγματοποιηθεί αλλαγή χρωμάτων στις μπάλες με τα δεδομένα, καθώς και στα τρία (3) αντίστοιχα πεδία "Split by party".

*Σχετική εικόνα από το πρίν και το μετά της αλλαγής (3.1)*

<img src="https://imgur.com/AweFzFv.png"/> 


*Σχετική εικόνα από το πρίν και το μετά της αλλαγής στα 3 πεδία "Split by party" (3.2)*

<img src="https://imgur.com/yB3Uscf.png"/> 


4) Έπειτα, ζητήθηκε να ακούγεται ήχος κάθε φορά που επιλέγει μια σελίδα ο χρήστης. Πραγματοποιήθηκε και αυτή η τροποποίηση στον κώδικα, με το αρχείο ήχου "Page turn sound effect.mp3".

5) Στη συνέχεια, ζητήθηκε να γίνουν οι απαραίτητες τροποποιήσεις ώστε, κάθε φορά που θα κάνει κλικ ο χρήστης επάνω σε μία μπάλα, να του βγάζει το αποτέλεσμα της αναζήτησής του, στην μηχανή αναζήτησης της [Google](https://www.google.com).

*Σχετική εικόνα (5)*

<img src="https://imgur.com/0NIdS6Q.png"/>

6) Έπειτα, λόγω του ότι κάποια άτομα ενδεχομένως να έχουν προβλήματα όρασης, ζητήθηκε να γίνουν οι κατάλληλες τροποποιήσεις, ώστε όταν ο χρήστης πηγαίνει πάνω σε κάποια περιοχή της σελίδας με το ποντίκι, να λειτουργεί αυτό ως μεγεθυντικός φακός.  

*Σχετική εικόνα (6)*

<img src="https://imgur.com/5Uk5Eyr.png"/>

7) Επιπροσθέτως, για τον ίδιο λόγο ακριβώς, ζητήθηκε να γίνουν οι απαραίτητες ενέργειες, ώστε να ακούγεται το όνομα του κάθε δωρητή με το ποσό που δώρησε, όταν περνάει με το ποντίκι από πάνω ο χρήστης. Ο στόχος επετεύχθη εφαρμόζοντας τις κατάλληλες συναρτήσεις μέσα στον αντίστοιχο κώδικα.

8) Τέλος, ζητήθηκε να πραγματοποιηθεί άλλη μια επιλογή ομαδοποίησης των δεδομένων ("Split by the amount of the donator") με το αντίστοιχο γράφημα.

*Σχετικές εικόνες (8)*

<img src="https://imgur.com/rVrJ7Ds.png"/>


<img src="https://imgur.com/xKL9qc2.png"/>


9) Στο κεντρικό αποθετήριο της εργασίας στον φάκελο [participants](https://github.com/ioniodi/D3js-uk-political-donations/tree/master/participants), δημιούργησα ένα .csv αρχείο με τίτλο "2013127.csv" στο οποίο περιέχει τα στοιχεία μου.

10) Επίσης στον φάκελο [photos](https://github.com/ioniodi/D3js-uk-political-donations/tree/master/photos), τοποθέτησα 5 εικόνες δωρητών με το λογότυπο της κάθε εταιρίας (αν πρόκειται για εταιρία) και με το πρόσωπο του κάθε δωρητή (αν πρόκειται για φυσικό πρόσωπο). Οι φωτογραφίες με τα logo που ανέβασα είναι αρχεία τύπου .ico με διαστάσεις 42x42. Οι δωρητές τους οποίους διάλεξα είναι οι εξής:
* Magna Carta Club 
* Bristol Labour Group 
* David Rowland
* Neil Goulden
* Bestway


### Παραδοτέο 2: Tελικό έργο και [Τελική Αναφορά](https://p13chat.github.io/final) - 25% (9 Μαϊου)

Για το δεύτερο παραδοτέο, πραγματοποίησα 3 από τα 5 ζητούμενα της εργασίας.

1) Αρχικά ζητήθηκε να εμφανίζεται (και να επεκτείνεται δυναμικά) η σειρά των εικόνων με τους δωρητές πάνω από τους οποίους πέρασε ο δείκτης του ποντικιού στο γράφημα.Ουσιαστικά πρόκειται για ένα ιστορικό σχετικά με το από ποιους δωρητές έκανε mouseover ο χρήστης.

*Σχετική Εικόνα (1)*

<img src="https://imgur.com/1LCDVLW.png"/>


2) Έπειτα ζητήθηκε η Δημιουργία του ίδιου D3 γραφήματος οπτικοποίησης με νέα ανοικτά δεδομένα από επίσημη Στατιστική Αρχή. Στο συγκεκριμένο ερώτημα τα [νέα δεδομένα](http://www.sharecsv.com/s/41ac20b6c978af0ce092ac5247af66db/WATER_ABSTRACT.csv), αφορούν την κατανάλωση νερού (για υδατοκαλλιεργειες και δημοσια χρηση) κατά τα έτη 2014-2015-2016 σε χώρες της ΕΕ. Τα στοιχεία τα άντλησα από τον [Organisation for Economic Co-operation and Development (OCED](https://data.oecd.org/water/water-withdrawals.htm). 
Για την υλοποίηση με το ίδιο d3 διάγραμμα, έγιναν οι κατάλληλες τροποποιήσεις στα αρχεία [newdata.html](https://github.com/p13chat/D3js-uk-political-donations/blob/gh-pages/newdata.html) , [chart3.js](https://github.com/p13chat/D3js-uk-political-donations/blob/gh-pages/chart3.js) και [new_style.css](https://github.com/p13chat/D3js-uk-political-donations/blob/gh-pages/new_style.css). Επίσης, δημιουργήθηκε και ένα νέο button στο αρχείο [index.html](https://github.com/p13chat/D3js-uk-political-donations/blob/gh-pages/index.html) (του 1ου παραδοτέου) το οποίο μας οδηγεί στο [Παραδοτέο 2](https://p13chat.github.io/D3js-uk-political-donations/newdata.html) με τα νέα δεδομένα.

*Σχετική Εικόνα αρχικής σελίδας των νέων δεδομένων (2)*

<img src="https://imgur.com/Zg8ub8g.png"/>

Ο διαχωρισμός (split) που έγινε για τα νέα δεδομένα είναι:
- Συνολικά
- Κατά ετός (2014-2015-2016)
- Κατά τύπο (Δημόσια χρήση - Υδατοκαλλιέργειες)

*Σχετική εικόνα για τον πρώτο διαχωρισμό (2.1)*

<img src="https://imgur.com/Zg8ub8g.png"/>

*Σχετική εικόνα για τον δεύτερο διαχωρισμό (2.2)*

<img src="https://imgur.com/TLxpN5N.png"/>

*Σχετική εικόνα για τον τρίτο διαχωρισμό (2.3)*

3) Τέλος, το τελευταίο ζητούμενο που υλοποίησα ήταν αυτό με τα [credits](https://ioniodi.github.io/D3js-uk-political-donations/participants/), για το οποίο έπρεπε στον φάκελο [participants] (https://github.com/ioniodi/D3js-uk-political-donations/tree/master/participants) να γράψω τον κατάλληλο κώδικα στο [index](https://github.com/ioniodi/D3js-uk-political-donations/blob/master/participants/index.html) αρχειο, προκειμένου να εμφανίζονται τα στοιχεία μου (github username & picture) με κάποια κίνηση. Δεύσμευσα την περιοχη "position #001" και πραγματοποιήθηκαν οι κατάλληλες αλλαγές στον κώδικα ώστε να πραγματοποιηθεί το ζητούμενο.

*Σχετική οθόνη για τα credit (3)*

<img src="https://media.giphy.com/media/2dmXIquWqBPpEAwBF8/giphy.gif"/>


## Η τελική αναφορά της εργασίας βρίσκεται [εδώ](https://p13chat.github.io/final) 
