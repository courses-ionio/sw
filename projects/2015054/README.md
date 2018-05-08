# Τεχνολογία Λογισμικού
## Οπτικοποίηση δεδομένων χορηγιών (UK)

#### Στοιχεία φοιτητή
##### Ονοματεπώνυμο: Μαρία-Νεφέλη Νικηφόρου
##### Αριθμός Μητρώου: Π2015054
##### Εξάμηνο φοίτησης: ΣΤ'
##### github username: nefelinikiforou
##### email: p15niki@ionio.gr

#### Σύνδεσμοι
##### Link ιστοσελίδας της εφαρμογής μου: https://nefelinikiforou.github.io/D3js-uk-political-donations/
##### Αποθετήριο του κώδικα της εφαρμογής (master branch) \*: https://github.com/nefelinikiforou/D3js-uk-political-donations
##### Link στο κλαδί του κώδικα που αντιστοιχεί στο Παραδοτέο 1 και στο Παραδοτέο 2 (gh-pages branch) \*: https://github.com/nefelinikiforou/D3js-uk-political-donations/tree/gh-pages
##### Link ιστοσελίδας της Τελικής Αναφοράς μου: https://nefelinikiforou.github.io/SW-Final-Report/
##### Αποθετήριο της Τελικής Αναφοράς μου: https://github.com/nefelinikiforou/SW-Final-Report
***\*** **Σημείωση\:** Παραδοτέο 1 και Παραδοτέο 2: Οι αλλαγές στον κώδικα φαίνονται στο branch [gh-pages](https://github.com/nefelinikiforou/D3js-uk-political-donations/tree/gh-pages) του παραπάνω αποθετηρίου. Το master branch χρησιμοποιήθηκε αποκλειστικά για τα ζητούμενα που απαιτούσαν αλλαγές (pull request) στο κοινό αποθετήριο του κώδικα.*

### Πίνακας Περιεχομένων
  * [Παραδοτέο 1](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%A0%CE%B1%CF%81%CE%B1%CE%B4%CE%BF%CF%84%CE%AD%CE%BF-1)
    * [Σύνδεσμος σελίδας μου με την εφαρμογή](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%A3%CF%8D%CE%BD%CE%B4%CE%B5%CF%83%CE%BC%CE%BF%CF%82-%CF%83%CE%B5%CE%BB%CE%AF%CE%B4%CE%B1%CF%82-%CE%BC%CE%BF%CF%85-%CE%BC%CE%B5-%CF%84%CE%B7%CE%BD-%CE%B5%CF%86%CE%B1%CF%81%CE%BC%CE%BF%CE%B3%CE%AE)
    * [Αλλαγή κατάληξης url](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%91%CE%BB%CE%BB%CE%B1%CE%B3%CE%AE-%CE%BA%CE%B1%CF%84%CE%AC%CE%BB%CE%B7%CE%BE%CE%B7%CF%82-url)
    * [Αλλαγή χρωμάτων στις μπάλες με τα δεδομένα](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%91%CE%BB%CE%BB%CE%B1%CE%B3%CE%AE-%CF%87%CF%81%CF%89%CE%BC%CE%AC%CF%84%CF%89%CE%BD-%CF%83%CF%84%CE%B9%CF%82-%CE%BC%CF%80%CE%AC%CE%BB%CE%B5%CF%82-%CE%BC%CE%B5-%CF%84%CE%B1-%CE%B4%CE%B5%CE%B4%CE%BF%CE%BC%CE%AD%CE%BD%CE%B1)
    * [Αλλαγή χρωμάτων στα 3 πεδία της ομαδοποίησης Split by party](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%91%CE%BB%CE%BB%CE%B1%CE%B3%CE%AE-%CF%87%CF%81%CF%89%CE%BC%CE%AC%CF%84%CF%89%CE%BD-%CF%83%CF%84%CE%B1-3-%CF%80%CE%B5%CE%B4%CE%AF%CE%B1-%CF%84%CE%B7%CF%82-%CE%BF%CE%BC%CE%B1%CE%B4%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7%CF%82-split-by-party)
    * [Ήχος στις επιλογές/κουμπιά ομαδοποίησης των δεδομένων](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%89%CF%87%CE%BF%CF%82-%CF%83%CF%84%CE%B9%CF%82-%CE%B5%CF%80%CE%B9%CE%BB%CE%BF%CE%B3%CE%AD%CF%82%CE%BA%CE%BF%CF%85%CE%BC%CF%80%CE%B9%CE%AC-%CE%BF%CE%BC%CE%B1%CE%B4%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7%CF%82-%CF%84%CF%89%CE%BD-%CE%B4%CE%B5%CE%B4%CE%BF%CE%BC%CE%AD%CE%BD%CF%89%CE%BD-%CE%B5%CE%BD%CE%B5%CF%81%CE%B3%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7-%CE%BC%CE%B5-%CE%BA%CE%BB%CE%B9%CE%BA)
    * [Άνοιγμα νέου παραθύρου με αποτελέσματα αναζήτησης για δωρητή](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%86%CE%BD%CE%BF%CE%B9%CE%B3%CE%BC%CE%B1-%CE%BD%CE%AD%CE%BF%CF%85-%CF%80%CE%B1%CF%81%CE%B1%CE%B8%CF%8D%CF%81%CE%BF%CF%85-%CE%BC%CE%B5-%CE%B1%CF%80%CE%BF%CF%84%CE%B5%CE%BB%CE%AD%CF%83%CE%BC%CE%B1%CF%84%CE%B1-%CE%B1%CE%BD%CE%B1%CE%B6%CE%AE%CF%84%CE%B7%CF%83%CE%B7%CF%82-google-%CE%B3%CE%B9%CE%B1-%CE%B4%CF%89%CF%81%CE%B7%CF%84%CE%AE-%CE%B5%CE%BD%CE%B5%CF%81%CE%B3%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7-%CE%BC%CE%B5-%CE%BA%CE%BB%CE%B9%CE%BA-%CF%83%CE%B5-%CE%BC%CF%80%CE%AC%CE%BB%CE%B1)
    * [Λειτουργία ποντικιού ως μεγεθυντικός φακός του κειμένου](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%9B%CE%B5%CE%B9%CF%84%CE%BF%CF%85%CF%81%CE%B3%CE%AF%CE%B1-%CF%80%CE%BF%CE%BD%CF%84%CE%B9%CE%BA%CE%B9%CE%BF%CF%8D-%CF%89%CF%82-%CE%BC%CE%B5%CE%B3%CE%B5%CE%B8%CF%85%CE%BD%CF%84%CE%B9%CE%BA%CF%8C%CF%82-%CF%86%CE%B1%CE%BA%CF%8C%CF%82-%CF%84%CE%BF%CF%85-%CE%BA%CE%B5%CE%B9%CE%BC%CE%AD%CE%BD%CE%BF%CF%85)
    * [Ήχος για την ονομασία του δωρητή και το ποσό της δωρεάς](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%89%CF%87%CE%BF%CF%82-%CE%B3%CE%B9%CE%B1-%CF%84%CE%B7%CE%BD-%CE%BF%CE%BD%CE%BF%CE%BC%CE%B1%CF%83%CE%AF%CE%B1-%CF%84%CE%BF%CF%85-%CE%B4%CF%89%CF%81%CE%B7%CF%84%CE%AE-%CE%BA%CE%B1%CE%B9-%CF%84%CE%BF-%CF%80%CE%BF%CF%83%CF%8C-%CF%84%CE%B7%CF%82-%CE%B4%CF%89%CF%81%CE%B5%CE%AC%CF%82-%CE%B5%CE%BD%CE%B5%CF%81%CE%B3%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7-%CF%8C%CF%84%CE%B1%CE%BD-%CF%84%CE%BF-%CF%80%CE%BF%CE%BD%CF%84%CE%AF%CE%BA%CE%B9-%CE%B2%CF%81%CE%AF%CF%83%CE%BA%CE%B5%CF%84%CE%B1%CE%B9-%CE%BC%CE%AD%CF%83%CE%B1-%CF%83%CE%B5-%CE%BA%CF%8D%CE%BA%CE%BB%CE%BF-%CE%B4%CF%89%CF%81%CE%B7%CF%84%CE%AE)
    * [Δημιουργία και προσθήκη νέας επιλογής ομαδοποίησης των δεδομένων](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%94%CE%B7%CE%BC%CE%B9%CE%BF%CF%85%CF%81%CE%B3%CE%AF%CE%B1-%CE%BA%CE%B1%CE%B9-%CF%80%CF%81%CE%BF%CF%83%CE%B8%CE%AE%CE%BA%CE%B7-%CE%BD%CE%AD%CE%B1%CF%82-%CE%B5%CF%80%CE%B9%CE%BB%CE%BF%CE%B3%CE%AE%CF%82-%CE%BF%CE%BC%CE%B1%CE%B4%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7%CF%82-%CF%84%CF%89%CE%BD-%CE%B4%CE%B5%CE%B4%CE%BF%CE%BC%CE%AD%CE%BD%CF%89%CE%BD-split-by-the-amount-of-the-donation)
    * [Ζητούμενα που απαιτούν pull request](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%96%CE%B7%CF%84%CE%BF%CF%8D%CE%BC%CE%B5%CE%BD%CE%B1-%CF%80%CE%BF%CF%85-%CE%B1%CF%80%CE%B1%CE%B9%CF%84%CE%BF%CF%8D%CE%BD-pull-request)
    
  * [Παραδοτέο 2](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%A0%CE%B1%CF%81%CE%B1%CE%B4%CE%BF%CF%84%CE%AD%CE%BF-2)
    * [Εμφάνιση και επέκταση σειράς εικόνων δωρητών](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%95%CE%BC%CF%86%CE%AC%CE%BD%CE%B9%CF%83%CE%B7-%CE%BA%CE%B1%CE%B9-%CE%B5%CF%80%CE%AD%CE%BA%CF%84%CE%B1%CF%83%CE%B7-%CF%83%CE%B5%CE%B9%CF%81%CE%AC%CF%82-%CE%B5%CE%B9%CE%BA%CF%8C%CE%BD%CF%89%CE%BD-%CE%B4%CF%89%CF%81%CE%B7%CF%84%CF%8E%CE%BD-%CE%B5%CE%BD%CE%B5%CF%81%CE%B3%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7-%CF%8C%CF%84%CE%B1%CE%BD-%CF%84%CE%BF-%CF%80%CE%BF%CE%BD%CF%84%CE%AF%CE%BA%CE%B9-%CE%B2%CF%81%CE%AF%CF%83%CE%BA%CE%B5%CF%84%CE%B1%CE%B9-%CE%BC%CE%AD%CF%83%CE%B1-%CF%83%CE%B5-%CE%BA%CF%8D%CE%BA%CE%BB%CE%BF-%CE%B4%CF%89%CF%81%CE%B7%CF%84%CE%AE)
    * [Ζητούμενα που απαιτούν pull request](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%96%CE%B7%CF%84%CE%BF%CF%8D%CE%BC%CE%B5%CE%BD%CE%B1-%CF%80%CE%BF%CF%85-%CE%B1%CF%80%CE%B1%CE%B9%CF%84%CE%BF%CF%8D%CE%BD-pull-request-1)
  * [Τελική Αναφορά](https://github.com/nefelinikiforou/sw/blob/2015054/projects/2015054/README.md#%CE%A4%CE%B5%CE%BB%CE%B9%CE%BA%CE%AE-%CE%91%CE%BD%CE%B1%CF%86%CE%BF%CF%81%CE%AC)

## Παραδοτέο 1

#### Σύνδεσμος σελίδας μου με την εφαρμογή
https://nefelinikiforou.github.io/D3js-uk-political-donations/

#### Αλλαγή κατάληξης url
Προκειμένου το url της εφαρμογής μου να μη χρειάζεται να καταλήγει σε "full-viz.html", μετονόμασα το αρχείο "full-viz.html":

![fullviz2](https://user-images.githubusercontent.com/22655733/36723307-8dd50c64-1bb8-11e8-81be-2b093a111543.JPG)

σε "index.html" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/index.html)):

![fullviz1](https://user-images.githubusercontent.com/22655733/36723280-7ea7b0fc-1bb8-11e8-9414-16dc95f95774.JPG)

Με αυτό τον τρόπο, το url άλλαξε από: https://nefelinikiforou.github.io/D3js-uk-political-donations/full-viz.html
σε: https://nefelinikiforou.github.io/D3js-uk-political-donations/.

#### Αλλαγή χρωμάτων στις μπάλες με τα δεδομένα
Για να έχω διαφορετικά χρώματα στις μπάλες με τα δεδομένα, χρειάστηκε να αλλάξω τους κωδικούς των χρωμάτων στο αρχείο "chart.js" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/chart.js)), στο εξής σημείο του κώδικα:

##### Αρχικά:

![chart-js-code-colorballs-1](https://user-images.githubusercontent.com/22655733/36741172-1a9c1938-1bed-11e8-9526-4df6701d8d4e.JPG)

![colorballs1](https://user-images.githubusercontent.com/22655733/36741378-99a373f2-1bed-11e8-8171-3681b75f99b2.JPG)

##### Μετά την αλλαγή:

![chart-js-code-colorballs-2](https://user-images.githubusercontent.com/22655733/36741327-78a919f4-1bed-11e8-9f2f-c8c84a9d3dbf.JPG)

![colorballs2](https://user-images.githubusercontent.com/22655733/36741492-ef804f0c-1bed-11e8-9fa9-08f6e26dc549.JPG)

#### Αλλαγή χρωμάτων στα 3 πεδία της ομαδοποίησης *Split by party*
Για να έχω διαφορετικά χρώματα στα 3 πεδία της ομαδοποίησης *Split by party*, χρειάστηκε να αλλάξω τους κωδικούς των χρωμάτων στο αρχείο "style.css" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/style.css)), στο εξής σημείο του κώδικα:

![style-css-partycolor](https://user-images.githubusercontent.com/22655733/36935875-e8e46b86-1f05-11e8-9eb3-d2e91447b430.JPG)

##### Αρχικά (αριστερά) και μετά την αλλαγή (δεξιά):

![colorparty1](https://user-images.githubusercontent.com/22655733/36935907-79041ec8-1f06-11e8-8e61-451003c04f8f.JPG)
![colorparty2](https://user-images.githubusercontent.com/22655733/36935922-bcb6dbe2-1f06-11e8-9c1f-cbc67d4577f1.JPG)

#### Ήχος στις επιλογές/κουμπιά ομαδοποίησης των δεδομένων (ενεργοποίηση με κλικ)
Για να ακούγεται ήχος κάθε φορά που ο χρήστης της εφαρμογής κάνει κλικ σε μία από τις επιλογές/κουμπιά ομαδοποίησης των δεδομένων, έκανα τις παρακάτω ενέργειες:
1. Βρήκα ([εδώ](http://soundbible.com/)) και ανέβασα στο αποθετήριο της εφαρμογής μου ένα [mp3 αρχείο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/Stapler-SoundBible.com-374581609.mp3).
2. Στο αρχείο "index.html" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/index.html)), έβαλα το script tag:

      ![sound1](https://user-images.githubusercontent.com/22655733/36936649-aeacefaa-1f10-11e8-9238-f31781456b76.JPG)
3. Στο ίδιο αρχείο έβαλα και την ακόλουθη εντολή:

      ![sound2](https://user-images.githubusercontent.com/22655733/36936729-acbc9b90-1f11-11e8-9a4b-022613a8d783.JPG)
   
   στην ετικέτα <a></a> για κάθε λίστα των κουμπιών ομαδοποίησης των δεδομένων, όπως φαίνεται παρακάτω:
   
      ![sound3](https://user-images.githubusercontent.com/22655733/36936799-73156c0e-1f12-11e8-95e5-7b5429fdd520.JPG)

####  Άνοιγμα νέου παραθύρου με αποτελέσματα αναζήτησης (google) για δωρητή (ενεργοποίηση με κλικ σε μπάλα)
Προκειμένου το κλικ σε κάθε μπάλα να ανοίγει ένα νέο παράθυρο με τα αποτελέσματα της αναζήτησης στο google για τον αντίστοιχο δωρητή, έκανα τις παρακάτω ενέργειες στο αρχείο "chart.js" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/chart.js)):
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
1. Στο αρχείο "style.css" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/style.css)), έφτιαξα μια νέα κλάση zoom, η οποία αλλάζει το μέγεθος της γραμματοσειράς (font-size) σε *large* όταν το ποντίκι βρίσκεται πάνω από κείμενο (hover):

   ![zoom-style-css](https://user-images.githubusercontent.com/22655733/37148163-1c413cdc-22d2-11e8-8218-d85951c06dbc.JPG)
2. Στο αρχείο "index.html" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/index.html)), έβαλα το εξής <script>:

   ![zoom-index-html](https://user-images.githubusercontent.com/22655733/37148864-97e63566-22d4-11e8-95d8-fedcfcad942c.JPG)

   Οι εντολές αυτές εντοπίζουν όλες τις ετικέτες (p, h4, h5, nav) στις οποίες θέλουμε να γίνεται η μεγέθυνση κειμένου και προσθέτουν σε αυτές την κλάση zoom. Η μεγέθυνση γίνεται ταυτόχρονα σε όλα τα κουμπιά, ανεξάρτητα από το πάνω σε ποιο ακριβώς από αυτά βρίσκεται το ποντίκι, καθώς θεώρησα ότι ο χρήστης θα θέλει να βλέπει καθαρά το σύνολο των δυνατών επιλογών (κουμπιά) που έχει, ώστε να βρίσκει άμεσα αυτό που θέλει. Επέλεξα να μη γίνεται zoom στις ετικέτες h1, h2 και h3, καθώς το κείμενό τους έχει ήδη αρκετά μεγάλο μέγεθος γραμματοσειράς και είναι bold (Βλ. και σχόλια).   
3. Στο ίδιο αρχείο ("index.html"), πρόσθεσα ετικέτες < p > στα 25k, 50k, 100k, 500k, 1m (value scale), ώστε να μεγεθύνονται, καθώς έχουν αρκετά μικρό μέγεθος γραμματοσειράς και αχνό χρώμα:
      
   ![zoom2-index-html](https://user-images.githubusercontent.com/22655733/37149171-bb396df2-22d5-11e8-928f-17b447482836.JPG)

#### Ήχος για την ονομασία του δωρητή και το ποσό της δωρεάς (ενεργοποίηση όταν το ποντίκι βρίσκεται μέσα σε κύκλο δωρητή)
Ορισμένοι από τους αναγνώστες της εφαρμογής ενδεχομένως να είναι άτομα με περιορισμένη όραση. Για να ακούγεται η ονομασία του δωρητή και το ποσό της δωρεάς του όταν το ποντίκι βρίσκεται μέσα στον κύκλο κάποιου δωρητή, έκανα τις παρακάτω ενέργειες:
1. Στο τέλος του αρχείου "index.html" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/index.html)), δήλωσα την εξωτερική βιβλιοθήκη [responsiveVoice](https://responsivevoice.org/api/) ως εξής:

   ![voice-link-index-html](https://user-images.githubusercontent.com/22655733/37205214-97be952e-239c-11e8-9633-cfa2e5dd4edf.JPG)
2. Στο αρχείο "chart.js" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/chart.js)), πρόσθεσα στη συνάρτηση mouseover(d, i) την εντολή:

   ![voice1-chart-js](https://user-images.githubusercontent.com/22655733/37206273-a843df7c-23a0-11e8-85dc-39ef3c7caf9a.JPG)
   
   Με την εντολή αυτή, ακούγονται οι πληροφορίες του δωρητή για όσο το ποντίκι βρίσκεται εντός του κύκλου του.
3. Στο ίδιο αρχείο ("chart.js"), πρόσθεσα στη συνάρτηση mouseout() την εντολή:

   ![voice2-chart-js](https://user-images.githubusercontent.com/22655733/37206301-c329bf64-23a0-11e8-8324-0d1bcd12df36.JPG)

   ώστε να σταματούν να ακούγονται οι πληροφορίες του δωρητή όταν το ποντίκι δε θα βρίσκεται πλέον μέσα στον κύκλο.

#### Δημιουργία και προσθήκη νέας επιλογής ομαδοποίησης των δεδομένων (Split by the amount of the donation)
Προκειμένου να δημιουργήσω και να προσθέσω μία ακόμα επιλογή ομαδοποίησης των δεδομένων (διαχωρισμός ανάλογα με το ποσό της δωρεάς), έκανα τις παρακάτω ενέργειες:
1. Στο αρχείο "index.html" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/index.html)): 
  * Δημιούργησα το νέο κουμπί (Split by the amount of the donation) κάτω από τα προηγούμενα κουμπιά της λίστας:
      ```
      <li><a href="#" onclick="sound.play()" role="button" class="pure-button switch" id="group-by-donation-amount">Split by the amount of the donation</a></li>
      ```
  * Πρόσθεσα το &lt;div id="view-donation-amount"&gt; κάτω από τα υπόλοιπα &lt;div&gt; ομαδοποίησης:

      ![new-div-index-html](https://user-images.githubusercontent.com/22655733/37247732-86326b82-24c8-11e8-957b-01a014dc99ba.JPG)
2. Στο αρχείο "chart.js" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/chart.js)):
  * Πρόσθεσα στη συνάρτηση transition() μία επιπλέον μετάβαση, η οποία (ενεργοποίηση με κλικ στο κουμπί "Split by the amount of the donation"), φέρνει στο προσκήνιο (fadeIn) το #view-donation-amount (Βλ. και "index.html"), "κρύβει" (fadeOut) όλα τα υπόλοιπα # και επιστρέφει τη συνάρτηση amountsGroup():

      ![new-transition-chart-js](https://user-images.githubusercontent.com/22655733/37259189-d7ed4ee2-258b-11e8-8d62-d007e0942d97.JPG)
   
    Τέλος, έβαλα την εξής εντολή:```$("#view-donation-amount").fadeOut(250);``` σε όλες τις υπόλοιπες μεταβάσεις της transition().
  * Έφτιαξα τη συνάρτηση amountsGroup() έχοντας ως πρότυπο τις υπόλοιπες συναρτήσεις (total(), partyGroup(), donorType(), fundsType()):

      ![func-amounts-group-chart-js](https://user-images.githubusercontent.com/22655733/37259371-f4862874-258d-11e8-8b32-4a4477ac2774.JPG)
   
    Με την εντολή: ```.on("tick", amounts)``` καλείται η συνάρτηση amounts().
  * Έφτιαξα τη συνάρτηση amounts() έχοντας ως πρότυπο τις υπόλοιπες συναρτήσεις (all(), parties(), entities(), types()):

      ![func-amounts-chart-js](https://user-images.githubusercontent.com/22655733/37259414-ab821d58-258e-11e8-9b9c-e7eff6161547.JPG)
  * Δημιούργησα τη συνάρτηση moveToAmounts(alpha), προκειμένου να μετακινηθούν οι κόμβοι στις κατάλληλες θέσεις. Ουσιαστικά, επιλέγεται ένα σταθερό κέντρο για τη θέση Y των κόμβων και, με βάση το value του κάθε κόμβου (το ποσό της δωρεάς), ορίζεται το X σε μία τιμή που αντιστοιχεί στις 6 επιλεγμένες τιμές (Donations over £1m, Donations over £500k, Donations over £100k, Donations over £50k, Donations over £25k, Donations under £25k):

      ![func-movetoamounts-chart-js](https://user-images.githubusercontent.com/22655733/37288197-4f23312e-260f-11e8-84b4-2850a0c94d0e.JPG)
3. Στο αρχείο "style.css" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/style.css)):
  * Επέλεξα να μην εμφανίζονται αρχικά στη σελίδα τα στοιχεία της ```#view-donation-amount```:
  
      ![disappear-view-style-css](https://user-images.githubusercontent.com/22655733/37288507-26379da8-2610-11e8-8430-66c8deea4d6a.JPG)
  * Όρισα τις θέσεις εμφάνισης του τίτλου "Split by the amount of the donation" και των 6 τίτλων των ποσών (Donations over £1m, Donations over £500k, Donations over £100k, Donations over £50k, Donations over £25k, Donations under £25k):
   
      ![labels-style-css-1](https://user-images.githubusercontent.com/22655733/37288301-90a7795c-260f-11e8-9252-cd7175be46ef.JPG)
   
      ![labels-style-css-2](https://user-images.githubusercontent.com/22655733/37288330-aa8320a6-260f-11e8-9b38-e9925255bdb5.JPG)

Για την εύρεση των κατάλληλων pixel, χρησιμοποίησα την επέκταση του Google Chrome, *Page Ruler*:

![pageruler](https://user-images.githubusercontent.com/22655733/37301526-77e6b776-2631-11e8-9680-2884296f53d8.JPG)

#### Ζητούμενα που απαιτούν pull request
1. Δημιούργησα το [αρχείο .csv](https://github.com/ioniodi/D3js-uk-political-donations/blob/master/participants/2015054.csv) με τα στοιχεία μου.
2. Πρόσθεσα τις εξής 5 εικόνες δωρητών στο φάκελο [photos](https://github.com/ioniodi/D3js-uk-political-donations/tree/master/photos): 
  * Bell Pottinger Group (685)
  * Betterworld (785)
  * HCA International (713)
  * Independent Print (808)
  * Seamark (705)
  
## Παραδοτέο 2

#### Εμφάνιση και επέκταση σειράς εικόνων δωρητών (ενεργοποίηση όταν το ποντίκι βρίσκεται μέσα σε κύκλο δωρητή)
Προκειμένου όταν το ποντίκι εισέρχεται σε έναν από τους κύκλους του γραφήματος να εμφανίζεται (και να επεκτείνεται δυναμικά) σε μια ορισμένη περιοχή της ιστοσελίδας του γραφήματος η σειρά των εικόνων με τους δωρητές πάνω από τους οποίους έχει περάσει ο δείκτης του ποντικιού του χρήστη, τροποποίησα τον κώδικα της εφαρμογής μου ως εξής:

1. Στο αρχείο "index.html" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/index.html)), πρόσθεσα ένα νέο &lt;div&gt; tag για τη δημιουργία μιας περιοχής για τις εικόνες των δωρητών, πάνω από τους κύκλους των οποίων έχει περάσει ο δείκτης του ποντικιού του χρήστη:

   ![img_sidebar_html](https://user-images.githubusercontent.com/22655733/39702847-c625c900-520e-11e8-8de7-1d0c9c5b3cd7.JPG)
2. Στο αρχείο "style.css" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/style.css)), πρόσθεσα το εξής πλαίσιο:

   ![img_sidebar_css](https://user-images.githubusercontent.com/22655733/39702982-4a2baba2-520f-11e8-8c0f-621786d98512.JPG)
   
   για να ορίσω το μέγεθος (ύψος: 42 pixels, καθώς οι εικόνες των δωρητών έχουν διαστάσεις 42x42) της περιοχής για τις εικόνες των δωρητών που έχουν προσπελαστεί, καθώς και την τοποθεσία της στην ιστοσελίδα. Με τη βοήθεια της επέκτασης του Google Chrome, *Page Ruler*, εντόπισα τα pixel για τη θέση του πλαισίου στην ιστοσελίδα:
   
   ![pixels_sidebar](https://user-images.githubusercontent.com/22655733/39742854-b438c1ae-52a7-11e8-90b0-5778f4cd379e.JPG)
   
   Χρωμάτισα το πλαίσιο προσωρινά (```background-color: light-blue;```), ώστε να ελέγχω ότι οι εικόνες τοποθετούνται σωστά:
   
   ![sidebar_1st_attempt](https://user-images.githubusercontent.com/22655733/39743105-9027a1da-52a8-11e8-8f98-ebd1602496bd.JPG)
3. Στο αρχείο "chart.js" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/chart.js)):
  * Όρισα μία νέα global μεταβλητή (κενό array) για να μετράω πόσες φορές έχει προσπελαστεί και εμφανιστεί η εικόνα κάθε δωρητή στο πλαίσιο, έτσι ώστε να αποφύγω την πολλαπλή εμφάνιση των ίδιων εικόνων (όταν το ποντίκι ξαναπερνάει πάνω από τον ίδιο κύκλο δωρητή):
  
      ![img_sidebar_js1](https://user-images.githubusercontent.com/22655733/39716346-c7901d84-5238-11e8-8728-79b07cc61c29.JPG)
  * Πρόσθεσα στη συνάρτηση mouseover(d,i) το εξής:

      ![img_sidebar_js2](https://user-images.githubusercontent.com/22655733/39721439-4318e882-5248-11e8-8a2c-64f460b39af2.JPG)
      
    Με τον έλεγχο της επιστρεφόμενης τιμής της συνάρτησης dlist.indexOf(donor) να μην είναι μεγαλύτερη από -1, εξασφαλίζεται ότι θα εμφανιστούν στο πλαίσιο μόνο οι εικόνες των δωρητών που δεν έχουν ξαναεμφανιστεί. Επιπλέον, θέτω τις διαστάσεις όλων των εικόνων στα 42x42 pixels (```element.setAttribute("height", "42"); element.setAttribute("width", "42");```), προκειμένου να εμφανίζονται ομοιόμορφες. Με κάθε νέα εικόνα δωρητή, η σειρά των εικόνων επεκτείνεται δυναμικά (```document.getElementById("images-sidebar").appendChild(element); dlist.push(donor);```)
    
4. Στο αρχείο "style.css" ([Βλ. και αποθετήριο](https://github.com/nefelinikiforou/D3js-uk-political-donations/blob/gh-pages/style.css)), αφαιρώ το περιττό background color του πλαισίου:

   ![img_sidebar_css2](https://user-images.githubusercontent.com/22655733/39724828-820cd030-5252-11e8-94e0-e13b67d8af81.JPG)
   
##### Τελικό αποτέλεσμα:

![final](https://user-images.githubusercontent.com/22655733/39743172-c33be73e-52a8-11e8-8273-f9c5c51c0976.JPG)
      
#### Ζητούμενα που απαιτούν pull request
Προκειμένου να εμφανίζονται τα στοιχεία μου (github username & picture) με κάποια κίνηση στην [ιστοσελίδα](https://ioniodi.github.io/D3js-uk-political-donations/participants/) με τους φοιτητές της άσκησης, έκανα τις παρακάτω ενέργειες:

1. Δήλωσα στο [Issue του Παραδοτέου 2](https://github.com/ioniodi/D3js-uk-political-donations/issues/17) τη δέσμευση της θέσης "Position #014" στον [κώδικα](https://github.com/ioniodi/D3js-uk-political-donations/blob/master/participants/index.html) της ιστοσελίδας:

   ![issue](https://user-images.githubusercontent.com/22655733/39665515-5093f156-509e-11e8-9f47-85944c20c592.JPG)

2. Στο [API του Github](https://api.github.com/users/nefelinikiforou) βρήκα όλες τις πληροφορίες μου σαν χρήστης του Github και, συγκεκριμένα, το url για το avatar μου, το οποίο χρειάζεται ώστε να εμφανίζεται η εικόνα προφίλ μου:

   ![avatar](https://user-images.githubusercontent.com/22655733/39664939-77eeff5c-5094-11e8-8454-dd4436301b35.JPG)

   ![avatar_img](https://user-images.githubusercontent.com/22655733/39664956-c8123bac-5094-11e8-9b5c-7f3486862909.JPG)

3. Στο φάκελο [participants](https://github.com/ioniodi/D3js-uk-political-donations/tree/master/participants) μετέτρεψα το αρχείο [index.html](https://github.com/ioniodi/D3js-uk-political-donations/blob/master/participants/index.html) στη θέση που είχα δεσμεύσει (Position #014), αρχικά ορίζοντας το url για το avatar μου και το username μου και, έπειτα, xρησιμοποιώντας τη [βιβλιοθήκη](https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js) (την οποία εμπεριείχε ήδη το αρχείο) και μετατρέποντας κατάλληλα τον open source [κώδικα](http://tobiasahlin.com/moving-letters/#7) για text animation που βρήκα, ως εξής:

   ![avatar_index_hml_1](https://user-images.githubusercontent.com/22655733/39665012-641b37d8-5095-11e8-8d0e-de162231f886.JPG)

   ![avatar_index_html_2](https://user-images.githubusercontent.com/22655733/39665018-821f5606-5095-11e8-84b0-1143e6fb022e.JPG)

   ![avatar_index_html_3](https://user-images.githubusercontent.com/22655733/39665022-911b8d3c-5095-11e8-93ab-ef605e574eca.JPG)

   
   Με αποτέλεσμα:

   ![anim-pict](https://user-images.githubusercontent.com/22655733/39665455-45b08e1c-509d-11e8-9620-18162508a4c8.JPG)
(Βλ. και [ιστοσελίδα](https://ioniodi.github.io/D3js-uk-political-donations/participants/))

Επιπλέον, ενημέρωσα το [αρχείο .csv](https://github.com/ioniodi/D3js-uk-political-donations/blob/master/participants/2015054.csv) με τα στοιχεία μου προσθέτοντας το δεύτερο παραδοτέο.

## Τελική Αναφορά
Για την Τελική Αναφορά δημιούργησα ξεχωριστό [αποθετήριο](https://github.com/nefelinikiforou/SW-Final-Report) και την έφτιαξα σε μορφή github-pages με ξεχωριστό [link](https://nefelinikiforou.github.io/SW-Final-Report/).
