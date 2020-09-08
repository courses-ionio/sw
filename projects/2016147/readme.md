
# Μάθημα: Τεχνολογία Λογισμικού
#
## Προσωπικά Στοιχεία:
#### A.M: Π2016147
#### Όνομα: Δημήτριος
#### Επώνυμο: Σιδηρόπουλος
#
### Προαπαιτούμενα: 
##### α) Εγκατάσταση Ubuntu σε Virtual Machine
#
##### β)Εγκατάσταση Python
###### sudo apt-get update
###### sudo apt install python
#
##### γ) Αλλαγή του .bashrc ώστε το Terminal να εμφανίζει το ΑΜ
###### cd ~
###### nano .bashrc
###### Πρόσθεση της εντολής  export PS1='P2016147:\w$ ' στο τέλος και CTRL+O για αποθήκευση
#
##### δ) Δημιουργία λογαριασμού στο Asciinema και εγκατάσταση του εργαλείου με την εντολή:
###### sudo apt-get install asciinema
#
## ΑΣΚΗΣΗ 1
### Τίτλος: Choose your stack
#
Για την άσκηση αυτή απαραίτητη είναι η εγκατάσταση του howdoi με την εντολή sudo apt-get install howdoi. Το howdoi είναι ενα command line tool το οποίο παρέχει άμεσα απαντήσεις για το θέμα που ρωτάει ο χρήστης. Έχει την δυνατότητα να να λαμβάνει δεδομένα από όποια μηχανή αναζήτησης επιθυμεί ο χρήστης και πρόκειται για ένα χρήσιμο εργαλείο ειδικά για τους προγραμματιστές γιατί τους δίνει απαντήσεις στα ερωτήματά τους χωρίς τον κίνδυνο κάτι άλλο να τους αποσπάσει την προσοχή

###### howdoi -a create an array java //-a για πλήρη προβολή του κειμένου
###### howdoi -n 3 free memory in c //-n NUM_ANSWERS προβολή NUM_ANSWERS απαντήσεων
###### howdoi -c allocate memory in c //Προβολή απαντήσεων από το duckduckgo


#### Asciinema link:

[Choose your stack](https://asciinema.org/a/4hR2ZfdsFa1Tq8xxCuVHe4ulM)
#
## ΑΣΚΗΣΗ 2
### Τίτλος: send notifications to your desktop-mobile
#### Εγκατάσταση ntfy
###### sudo pip install ntfy
#### Εκτέλεση
###### ntfy send test
###### ntfy -t 'ntfy' send "Here's a custom notification title!" //Custom Tittles
###### ntfy done firefox // Ειδοποίηση αφού κλείσει ο browser
###### ntfy done git clone https://github.com/dschep/ntfy.git
![image](https://github.com/p16sidi/sw/blob/2016147/projects/2016147/scr1.png)
#### Asciinema link:
#### [send notifications to your desktop-mobile](https://asciinema.org/a/vhgH0ttCoBi9G83ybDR7unCHa)
#
### Άσκηση 3(performance monitoring)
#### 3.1 Κατέβασμα Hyperfine
###### wget https://github.com/sharkdp/hyperfine/releases/download/v1.9.0/hyperfine_1.9.0_amd64.deb
#### Εγκατάσταση Hyperfine
###### sudo dpkg -i hyperfine_1.9.0_amd64.deb
##### Τα scripts που θα χρησιμοποιηθούν για σύγκριση είναι τα [script1]() και [script2]() τα οποία τροποποιήκαν για να ταξινομούν την ίδια λίστα.
#### Εκτέλεση
###### hyperfine --warmup 3 'python3 bubblesort.py' 'python3 selectionsort.py'
#### Παράμετροι
###### hyperfine -m 8 'python3 bubblesort.py' 'python3 selectionsort.py' //-m παράμετρος για εκτέλεση συγκεκριμένων επαναλήψεων του κώδικα
###### hyperfine --export-markdown results.txt 'python3 bubblesort.py' 'python3 selectionsort.py' //Export των αποτελεσμάτων
###### hyperfine -i 'python3 bubblesort.py' 'python3 selectionsort.py' //Αγνόηση σφαλμάτων
#### Αποτελέσματα
##### Μετά την εκτέλεση των Benchmarks με το Hyperfine είναι φανερός πως ο αλγόριθμος ταξινόμησης Selection Sort πρόκειται για ένα πιο γρήγορο αλγόριθμο καθώς σύμφωνα με το εργαλείο εκτελείται περίπου 2 φορες πιο γρήγορα από τον Bubble Sort. Αυτό φαίνεται και στην πολυπλοκότητα των αλγορίθμων αφού ο Selection Sort έχει Complexity O(n) ενώ ο Bubble Sort O(n2).
#### [Link3 για Asciinema]()
#### 3.2 Κατέβασμα py-spy
###### sudo pip install py-spy
#### Τρέξιμο
###### py-spy record -o results.svg -- python selectionsort.py //Γραφική αναπαράσταση του προγράμματος και αποθήκευση του Output στον φάκελο results.svg
###### py-spy record -o results.svg --pid PID //Δυνατότητα εκτέλεσης με το ID της διεργασίας
###### py-spy dump --pid 12345 //Παρουσίαση του τρέχων Call Stack του κάθε Thread
#
### Άσκηση 4(try different terminals and shells)
##### a) Fish
##### b) Terminator
#### Εγκατάσταση fish
###### sudo apt-get install fish
#### Το Fish πρόκειται για ένα Shell όπου σου προσφέρει διάφορες διευκολύνσεις όπως η πρόβλεψη της εντολής που πληκτρολογείς. Για την εκτέλεση της άσκησης δημιουργώ πρόγραμμα σε Python όπου εκτυπώνει το "Hello World" 10 φορές.
#### [Link4 για Asciinema]()
#
#### Εγκατάσταση Terminator
###### sudo apt-get install terminator
#### Terminator Customisation
###### terminator -m //Maximized
###### terminator -b//Bordless
###### Split terminals horizontally: Ctrl + Shift + O.
###### Split terminals vertically: Ctrl + Shift + E.
###### Close current Panel: Ctrl + Shift + W.
###### Open new tab: Ctrl + Shift + T.
![image]()
#
#### Άσκηση 5(send notifications to your desktop-mobile)
#### Εγκατάσταση ntfy
###### sudo pip install ntfy
#### Εκτέλεση
###### ntfy send test
###### ntfy -t 'ntfy' send "Here's a custom notification title!" //Custom Tittles
###### ntfy done hyperfine --warmup 3 'python3 bubblesort.py' 'python3 selectionsort.py' // Ειδοποίηση αφού ολοκληρωθεί το Benchmarks
###### ntfy done git clone https://github.com/dschep/ntfy.git
##### Μπορεί να χρησιμοποιηθεί επίσης η παράμετρος --pid όπου η ειδοποίηση εμφανίζεται αφού τερματιστεί η διαδικασία με το αντίστοιχο Process ID e.g.(ntfy done --pid 4829)
![image]()
#### [Link5 για Asciinema]()
#
#### Άσκηση 6(Use the terminal as an IDE)
#### Εγκατάσταση vim
###### sudo apt install vim
#### Εκτέλεση Vim
###### vim onoma_arxeiou
###### vim -h //Εμφάνιση όλων των διαθέσιμων παραμέτρων κατά την εκτέλεση
###### h - μετακίνηση κέρσορα αριστερά
###### l - μετακίνηση κέρσορα δεξιά
###### re - αντικατάτασταση χαρακτήρα
###### u - Undo
###### S - διαγραφή μιας γραμμής
###### Η - μετακίνηση στην αρχή του κειμμένου
#### [Link6 για Asciinema]()
#
### Συμμετοχικό εκπαιδευτικό υλικό 
##### To προσωπικό αποθετήριο της ιστοσελίδας του μαθήματος είναι στο παρακάτω [link](https://github.com/p16sidi/gr).
##### H προσωπική ιστοσελίδα βιβλίου του μαθήματος είναι στο παρακάτω [link](https://p16sidi.github.io/gr/).
#
#### Συμμετοχικό περιεχόμενο
##### Δύο νέες εικόνες [ενότητα](https://p16sidi.github.io/gr/gallery/) την [εικόνα 1](https://p16sidi.github.io/gr/gallery/Spacex/) και την [εικόνα 2](https://p16sidi.github.io/gr/gallery/paypal/).
##### Η βιογραφία βρίσκεται στο [Link](https://p16sidi.github.io/gr/biography/Jeff%20Bezos/)
##### Διαδραστικό παράδειγμα στο [Link](https://p16sidi.github.io/gr/remix/illusion/)








 
