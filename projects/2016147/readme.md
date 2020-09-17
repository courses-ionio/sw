
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
## ΑΣΚΗΣΗ 3
### Τίτλος: performance monitoring
#### 3.1 Κατέβασμα Hyperfine
###### wget https://github.com/sharkdp/hyperfine/releases/download/v1.9.0/hyperfine_1.9.0_amd64.deb
#### Εγκατάσταση Hyperfine
###### sudo dpkg -i hyperfine_1.9.0_amd64.deb
#### Με το hyperfine μπόρεσα να ελέγξω το χρόνο εκτέλεσης 2 προγραμμάτων python. Επιπλέον έβαλα warmup και πόσες φόρες να τρέξουν τα προγράμματα.

```
hyperfine 'python3 python1.py' 'python3 python2.py' --warmup 40 --min-runs 40

```
Τα δύο αρχεία python ήταν 2 Hello World όπου στο ένα εκτυπωνόταν δέκα φορές ενώ στο άλλο μία, για αυτόν το λόγο το ένα τρέχει και πιο γρήγορα από το άλλο. 

#### Asciinema link:

#### [performance monitoring](https://asciinema.org/a/FPxdM4s1mGuFBUuPM0tO9mN0O)
#### 3.2 Κατέβασμα py-spy
###### sudo pip install py-spy
#### Τρέξιμο
###### py-spy record -o results.svg -- python python1.py //Γραφική αναπαράσταση του προγράμματος και αποθήκευση του Output στον φάκελο results.svg
###### py-spy record -o results.svg --pid PID //Δυνατότητα εκτέλεσης με το ID της διεργασίας
###### py-spy dump --pid 12345 //Παρουσίαση του τρέχων Call Stack του κάθε Thread
#
## ΑΣΚΗΣΗ 4
### Τίτλος: set-up a system for python development
```
pip install virtualenv
```

### Δημιουργία νέου enviroment.

```
mkdir project
cd project
virtualenv Enviroment
```

### Ενεργοποίηση enviroment
```
source Enviroment/bin/activate
```
### Τέλος έτρεξα το νέο μου πρόγραμμά και εφόσον δεν έβγαλε πρόβλημα τότε το virtual enviroment λειτουργεί κανονικά.
```
pipenv run python main.py
```

### Απενεργοποίηση του enviroment.
```
deactivate
```
#### Asciinema link:

#### [set-up a system for python development](https://asciinema.org/a/2hmG3AFWITn5HyNO8od1vruAr)
#
## ΑΣΚΗΣΗ 5
### Τίτλος: Try different terminals and shells
#### Εγκατάσταση zsh

```
sudo apt install zsh
```
Για την άσκηση χρησιμοποίησα το zsh για την εκτέλεση του send notifications to your desktop-mobile

```
zsh

ntfy send test
```


#### Asciinema link:

#### [Try different terminals and shells](https://asciinema.org/a/V2E22TpHyp7C6nHMw7zeOan62)
#
## ΑΣΚΗΣΗ 6
### Τίτλος: Use the terminal as an IDE
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
#### [Try different terminals and shells](https://asciinema.org/a/TtuR66USdtTBdqhxflS4Sqcby)
#
### Συμμετοχικό εκπαιδευτικό υλικό 
##### To προσωπικό αποθετήριο της ιστοσελίδας του μαθήματος είναι στο παρακάτω [link](https://github.com/p16sidi/gr).
##### H προσωπική ιστοσελίδα βιβλίου του μαθήματος είναι στο παρακάτω [link](https://p16sidi.github.io/gr/).
#
#### Συμμετοχικό περιεχόμενο
##### Δύο νέες εικόνες [ενότητα](https://p16sidi.github.io/gr/gallery/) την [εικόνα 1](https://p16sidi.github.io/gr/gallery/Spacex/) και την [εικόνα 2](https://p16sidi.github.io/gr/gallery/paypal/).
##### Η βιογραφία βρίσκεται στο [Link](https://p16sidi.github.io/gr/biography/Jeff%20Bezos/)
##### Διαδραστικό παράδειγμα στο [Link](https://p16sidi.github.io/gr/remix/illusion/)








 
