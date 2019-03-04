## Όνομα: Σπύρος Μπαξεβανάκης

Forked repository: https://github.com/spirosbax/sw

# Bonus CV
Repository: https://github.com/spirosbax/cv  
Link: https://spirosbax.github.io/cv

Έκανα fork το https://github.com/davewhipp/markdown-cv το οποίο είναι δημοφιλές fork του παραδείγματος https://github.com/elipapa/markdown-cv .
Έχω συμπληρώσει το βιογραφικό μου και επίσης χρησιμοποίησα το [Travis CI](https://travis-ci.org/) για να βάλω continuous integration.
Με αυτό τον τρόπο κάθε φορά που γίνεται μία αλλαγή στο βιογραφικό, το travis ακουλουθεί τα βήματα του αρχείου `.travis.yml` και εκτελεί τα
2 bash scripts: `push.sh`, `deploy.sh` ώστε να δημιουργήσει το pdf και να το αποθηκεύσει σε αρχείο με όνομα `cv.pdf` στο αποθετήριο χρησιμοποιόντας Github OΑuth token.
Επίσης πρόσθεσα στο τέλος του βιογραφικού επιλογή ώστε να μπορεί κάποιος να το κατεβάσει σε μορφή pdf.
Τέλος με την εντολή `pandoc https://spirosbax.com/cv -f html-native_divs -o cv.pdf --pdf-engine=xelatex` γίνεται μετατροπή του βιογραφικού σε pdf.
Η ίδια εντολή χρησιμοποιείται και από το `deploy.sh` ώστε να γίνει η μετατροπή σε pdf με την διαφορά ότι στο travis χρησιμοποιείται ρητά `pandoc-2.6`.
