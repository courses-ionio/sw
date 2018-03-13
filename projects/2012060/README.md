Μαρία Σκαφιδά

Α.Μ.: Π2012060

Εργασία: DATA VISUALIZATION - Οπτικοποίηση δεδομένων χορηγιών (UK)

e-mail: p12skaf@ionio.gr

Link προσωπικού αποθετήριου κώδικα: https://github.com/mskafi28/D3js-uk-political-donations

Link εκτελέσιμου κώδικα: https://mskafi28.github.io/D3js-uk-political-donations/


ΖΗΤΟΥΜΕΝΑ ΠΡΩΤΟΥ ΠΑΡΑΔΟΤΕΟΥ:

1) Ο σύνδεσμος της σελίδας με την εφαρμογή είναι ο παρακάτω: https://mskafi28.github.io/D3js-uk-political-donations/

2) Έκανα μετονομασία του αρχείου full-viz.html σε index.html, για να μη χρειάζεται να καταλήγει το url της εφαρμογής μου σε "full-viz.html".

3) Έγινε αλλαγή των χρωμάτων στις μπάλες με τα δεδομένα σε όλα τα πεδία ομαδοποίησης, με αλλαγή του color scale στο αρχείο chart.js. Επιπλέον, στην κατηγορία Split by party άλλαξα τα χρώματα στα πεδία Conservative Party, Labour Party και Liberal Democrats μέσα από το αρχείο style.css.

4) Στο αρχείο index.html πρόσθεσα την εντολή onmousedown="bs.play()", ώστε να ακούγεται ήχος κάθε φορά που ο χρήστης κάνει κλικ σε κάποιο από τα πεδία ομαδοποίησης των δεδομένων.

5) Στη συνάρτηση start() του αρχείου chart.js προστέθηκε η εντολή .on("click", function(d) { window.open("http://www.google.com/search?q=" + d.donor);});, έτσι ώστε όταν ένας χρήστης κάνει κλικ σε κάποια μπάλα ανοίγει μία καινούρια καρτέλα στο browser με τα αποτελέσματα της αναζήτησης στο google για το δωρητή στον οποίο αντιστοιχεί η μπάλα που πατήθηκε.

6) Στο αρχείο index.html πρόσθεσα σε όλες τις κεφαλίδες των κειμένων το class=zoom, ώστε κάθε φορά που το ποντίκι μεταφέρεται πάνω σε λέξεις του κειμένου, να λειτουργεί και ως μεγεθυντικός φακός. 

7) Στο αρχείο chart.js προστέθηκαν οι εντολές:

    var donatorsname = new SpeechSynthesisUtterance("Donator's name is " + donor + " and the donation amount is " + amount + " pounds");
    
 και 
 
	  window.speechSynthesis.speak(donatorsname);
    
 Με αυτόν τον τρόπο κάθε φορά που ο χρήστης περνάει το ποντίκι από τον κύκλο κάποιου δωρητή, ακούγεται το όνομα του δωρητή αυτού, καθώς επίσης και το συνολικό ποσό της δωρεάς του.
 
8)

Επιπλέον, στο φάκελο participants δημιούργησα ένα αρχείο .csv, το οποίο περιλαμβάνει τα στοιχεία που ζητήθηκαν και στο φάκελο photos επέλεξα και πρόσθεσα πέντε εικόνες δωρητών με μέγεθος 42x42 pixels και κατάληξη .ico.

