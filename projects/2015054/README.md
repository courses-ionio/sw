## Τεχνολογία Λογισμικού
### Οπτικοποίηση δεδομένων χορηγιών (UK)

#### Στοιχεία φοιτητή
##### Ονοματεπώνυμο: Μαρία-Νεφέλη Νικηφόρου
##### Αριθμός Μητρώου: Π2015054
##### Εξάμηνο φοίτησης: ΣΤ'
##### email: p15niki@ionio.gr

#### Σύνδεσμοι
##### Link ιστοσελίδας της εφαρμογής μου: https://nefelinikiforou.github.io/D3js-uk-political-donations/
##### Αποθετήριο του κώδικα της εφαρμογής: https://github.com/nefelinikiforou/D3js-uk-political-donations

### Παραδοτέο 1

#### Σύνδεσμος σελίδας μου με την εφαρμογή
https://nefelinikiforou.github.io/D3js-uk-political-donations/

#### Αλλαγή κατάληξης url
Προκειμένου το url της εφαρμογής μου να μη χρειάζεται να καταλήγει σε "full-viz.html", μετονόμασα το αρχείο "full-viz.html":

![fullviz2](https://user-images.githubusercontent.com/22655733/36723307-8dd50c64-1bb8-11e8-81be-2b093a111543.JPG)

σε "index.html" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/tree/gh-pages)):

![fullviz1](https://user-images.githubusercontent.com/22655733/36723280-7ea7b0fc-1bb8-11e8-9414-16dc95f95774.JPG)

Με αυτό τον τρόπο, το url άλλαξε από: https://nefelinikiforou.github.io/D3js-uk-political-donations/full-viz.html
σε: https://nefelinikiforou.github.io/D3js-uk-political-donations/.

#### Αλλαγή χρωμάτων στις μπάλες με τα δεδομένα
Για να έχω διαφορετικά χρώματα στις μπάλες με τα δεδομένα, χρειάστηκε να αλλάξω τους κωδικούς των χρωμάτων στο αρχείο "chart.js" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/tree/gh-pages)), στο εξής σημείο του κώδικα:

##### Αρχικά:

![chart-js-code-colorballs-1](https://user-images.githubusercontent.com/22655733/36741172-1a9c1938-1bed-11e8-9526-4df6701d8d4e.JPG)

![colorballs1](https://user-images.githubusercontent.com/22655733/36741378-99a373f2-1bed-11e8-8171-3681b75f99b2.JPG)

##### Μετά την αλλαγή:

![chart-js-code-colorballs-2](https://user-images.githubusercontent.com/22655733/36741327-78a919f4-1bed-11e8-9f2f-c8c84a9d3dbf.JPG)

![colorballs2](https://user-images.githubusercontent.com/22655733/36741492-ef804f0c-1bed-11e8-9fa9-08f6e26dc549.JPG)

#### Αλλαγή χρωμάτων στα 3 πεδία της ομαδοποίησης *Split by party*
Για να έχω διαφορετικά χρώματα στα 3 πεδία της ομαδοποίησης *Split by party*, χρειάστηκε να αλλάξω τους κωδικούς των χρωμάτων στο αρχείο "style.css" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/tree/gh-pages)), στο εξής σημείο του κώδικα:

![style-css-partycolor](https://user-images.githubusercontent.com/22655733/36935875-e8e46b86-1f05-11e8-9eb3-d2e91447b430.JPG)

##### Αρχικά (αριστερά) και μετά την αλλαγή (δεξιά):

![colorparty1](https://user-images.githubusercontent.com/22655733/36935907-79041ec8-1f06-11e8-8e61-451003c04f8f.JPG)
![colorparty2](https://user-images.githubusercontent.com/22655733/36935922-bcb6dbe2-1f06-11e8-9c1f-cbc67d4577f1.JPG)

#### Ήχος στις επιλογές/κουμπιά ομαδοποίησης των δεδομένων (ενεργοποίηση με κλικ)
Για να ακούγεται ήχος κάθε φορά που ο χρήστης της εφαρμογής κάνει κλικ σε μία από τις επιλογές/κουμπιά ομαδοποίησης των δεδομένων, έκανα τις παρακάτω ενέργειες:
1. Βρήκα ([εδώ](http://soundbible.com/)) και ανέβασα στο αποθετήριο της εφαρμογής μου ένα [mp3 αρχείο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/Stapler-SoundBible.com-374581609.mp3).
2. Στο αρχείο "index.html" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/tree/gh-pages)), έβαλα το script tag:

      ![sound1](https://user-images.githubusercontent.com/22655733/36936649-aeacefaa-1f10-11e8-9238-f31781456b76.JPG)
3. Στο ίδιο αρχείο έβαλα και την ακόλουθη εντολή:

      ![sound2](https://user-images.githubusercontent.com/22655733/36936729-acbc9b90-1f11-11e8-9a4b-022613a8d783.JPG)
   
   στην ετικέτα <a></a> για κάθε λίστα των κουμπιών ομαδοποίησης των δεδομένων, όπως φαίνεται παρακάτω:
   
      ![sound3](https://user-images.githubusercontent.com/22655733/36936799-73156c0e-1f12-11e8-95e5-7b5429fdd520.JPG)

####  Άνοιγμα νέου παραθύρου με αποτελέσματα αναζήτησης (google) για δωρητή (ενεργοποίηση με κλικ σε μπάλα)
Προκειμένου το κλικ σε κάθε μπάλα να ανοίγει ένα νέο παράθυρο με τα αποτελέσματα της αναζήτησης στο google για τον αντίστοιχο δωρητή, έκανα τις παρακάτω ενέργειες στο αρχείο "chart.js" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/tree/gh-pages)):
1. Δημιούργησα τη συνάρτηση googleSearch(d), που έχει σαν όρισμα τα δεδομένα της εκάστοτε μπάλας (όνομα δωρητή) και με την εντολή window.open() ανοίγει ένα νέο παράθυρο με τα αποτελέσματα της αναζήτησης google για τον αντίστοιχο δωρητή:
   
   ![char-js-gsearch-funct](https://user-images.githubusercontent.com/22655733/37045497-c0958956-216e-11e8-9eed-ae070741eb7c.JPG)
2. Συνδυάζοντας τη συνάρτηση on μαζί με τη συνάρτηση googleSearch(d), έβαλα την εξής εντολή μέσα στη συνάρτηση start():

   ![c2](https://user-images.githubusercontent.com/22655733/37046876-0d447e6c-2172-11e8-950a-6b5bebe4f353.JPG)
   
   έτσι ώστε να ενεργοποιείται η αναζήτηση όταν γίνεται κλικ σε κάποια μπάλα.
3. Πρόσθεσα στη συνάρτηση mouseover(d, i) την εντολή:

   ![chart-js-cursor1](https://user-images.githubusercontent.com/22655733/37048053-6a7dadbc-2175-11e8-8f09-60aba3ab418d.JPG)
     
      και στη συνάρτηση mouseout() την εντολή:
      
   ![chart-js-cursor2](https://user-images.githubusercontent.com/22655733/37048165-ba8c7978-2175-11e8-81e6-38965b221d98.JPG)

   Η πρώτη εντολή μετατρέπει τον κέρσορα σε χεράκι που δείχνει (pointer) κάθε φορά που εκείνος μετακινείται πάνω από κάποια μπάλα, έτσι ώστε να φαίνεται ότι εκεί υπάρχει υπερσύνδεσμος. Η δεύτερη εντολή μετατρέπει τον κέρσορα στη default εμφάνισή του, όταν εκείνος δεν μετακινείται πάνω από κάποια μπάλα.

#### Λειτουργία ποντικιού ως μεγεθυντικός φακός του κειμένου
Ορισμένοι από τους αναγνώστες της εφαρμογής ενδεχομένως να είναι άτομα με περιορισμένη όραση. Προκειμένου το ποντίκι να λειτουργεί και ως μεγεθυντικός φακός όταν μεταφέρεται επάνω από τις λέξεις του κειμένου (αύξηση μεγέθους γραμματοσειράς), έκανα τις παρακάτω ενέργειες:
1. Στο αρχείο "style.css" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/tree/gh-pages)), έφτιαξα μια νέα κλάση zoom, η οποία αλλάζει το μέγεθος της γραμματοσειράς (font-size) σε *large* όταν το ποντίκι βρίσκεται πάνω από κείμενο (hover):

   ![zoom-style-css](https://user-images.githubusercontent.com/22655733/37148163-1c413cdc-22d2-11e8-8218-d85951c06dbc.JPG)
2. Στο αρχείο "index.html" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/tree/gh-pages)), έβαλα το εξής <script>:

   ![zoom-index-html](https://user-images.githubusercontent.com/22655733/37148864-97e63566-22d4-11e8-95d8-fedcfcad942c.JPG)

   Οι εντολές αυτές εντοπίζουν όλες τις ετικέτες (p, h4, h5, nav) στις οποίες θέλουμε να γίνεται η μεγέθυνση κειμένου και προσθέτουν σε αυτές την κλάση zoom. Επέλεξα να μη γίνεται zoom στις ετικέτες h1, h2 και h3, καθώς το κείμενό τους έχει ήδη αρκετά μεγάλο μέγεθος γραμματοσειράς και είναι bold (Βλ. και σχόλια).   
3. Στο ίδιο αρχείο ("index.html"), πρόσθεσα ετικέτες < p > στα 25k, 50k, 100k, 500k, 1m (value scale), ώστε να μεγενθύνονται, καθώς έχουν αρκετά μικρό μέγεθος γραμματοσειράς και αχνό χρώμα:
      
   ![zoom2-index-html](https://user-images.githubusercontent.com/22655733/37149171-bb396df2-22d5-11e8-928f-17b447482836.JPG)
