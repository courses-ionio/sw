# ΤΕΧΝΟΛΟΓΙΑ ΛΟΓΙΣΜΙΚΟΥ
## ΕΡΓΑΣΙΑ : BONUS 

### Καθηγητής : ΧΩΡΙΑΝΟΠΟΥΛΟΣ
### ΦΟΙΤΗΤΡΙΑ : ΠΑΠΑΠΟΣΤΟΛΟΥ ΜΥΡΤΩ
### Α.Μ. : Π2016030

link : https://myrtop.github.io/online-cv/ 

### Α-Β ΠΑΡΑΔΟΤΕΟ & ΤΕΛΙΚΗ ΑΝΑΦΟΡΑ
Σε αυτό το μπόνους ζητήται να η δημιουργία ιστοσελίδας του προσωπικού βιογραφικού 
των φοιτητών με την χρήση αρχείου δεδομένων μορφής YAML. 
Αρχικά, έγινε fork του πρώτου παραδείγματος από τον χρήστη "sharu725", https://github.com/sharu725/online-cv  και η ονομασία του αποθετηρίου είναι "online-cv".
Έγινε συμπλήρωση των προσωπικών δεδομένων στο data.yml αρχείο και έπειτα έγιναν αλλαγές στην εικόνα του βιογραφικού.
Για την αλλαγή της εμφάνισης του βιογραφικού (πήγα την στήλη αριστερά, άλλαξα το χρώμα, και έβαλα σκιά) έγιναν αλλαγές στο
css αρχείο , στον φάκελο https://github.com/MyrtoP/online-cv/blob/master/_sass/_base.scss , όπου οι αλλαγές είναι σε σχόλια.
Το χρώμα το έβαλα να είναι berry, την στήλη με την φωτογραφία και τα στοιχεία επικοινωνίας την τοποθέτησα αριστερά,
τις υπόλοιπες πληροφορίες της έβαλα να εμφανίζονται στο κέντρο της σελίδας, πρόσθεσα σκιά και τέλος άλλαξα το footer.
Για το δεύτερο μέρος της εργασίας έγινε η δημιουργία ενός pdf. Για την δημιουργία του έγινε αρχικά η εγκατάσταση 
του pandoc και του latex τοπικά στον υπολογιστή και έπειτα η δημιουργία ενός template.tex και με ένα license αρχείο και 
με την εντολή "pandoc details.yml -o cv.pdf --template=template.tex --pdf-engine=xelatex" στο τερματικό δημιουργήθηκε το pdf. 
Στη συνέχεια ζητήθηκε η αυτόματη τοποθέτηση του pdf στην ιστοσελίδα με Continuous Integration με το Travis CI. 
Δυστηχώς δεν κατάφερα να βρώ κάποια λύση για το error του  Travis εξού και δεν ολοκληρώθηκε το παραδοτέο.

Αρχικό,
<img src="https://github.com/MyrtoP/online-cv/blob/master/assets/images/initial.png" width="300"/>
Τελικό,
<img src="https://github.com/MyrtoP/online-cv/blob/master/assets/images/final.png" width="300"/> 

το footer,
<img src="https://github.com/MyrtoP/online-cv/blob/master/assets/images/footer.png" width="300"/>

το pdf, 
<img src="https://github.com/MyrtoP/online-cv/blob/master/assets/images/pdf.png" width="300"/>

