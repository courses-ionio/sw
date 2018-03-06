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
Προκειμένου το κλικ σε κάθε μπάλα να ανοίγει ένα νέο παράθυρο με τα αποτελέσματα της αναζήτησης στο google για τον αντίστοιχο δωρητή, έκανα τις παρακάτω ενέργειες στο αρχείο "chart.js":
1. 
2.
3.
