# Ονοματεπώνυμο: Παναγιωτόπουλος Σωτήρης

# Α.Μ.: Π2017132


## Άσκηση 1η: Choose your stack.

#### Απαιτούμενα της άσκησης: set-up a set of cli tools with minimal dependencies and a software licence that allows commercial use and selling

#### Προαπαιτούμενα:

#### Εγκατάσταση howdoi

pip install howdoi

#### Εγκατάσταση How2

npm install -g how-2

#### Εκτέλεση της άσκησης:

#### Για αρχή θα εκτυπώσουμε την ημερομηνία

printf '%(%Y-%m-%d)T\n' -1  

#### Μετά θα συνεχίσουμε κάνοντας μερικές ερωτήσεις όπως το πως να μετατρέψεις κιλά σε pounds και το πως να αλλάξεις το μεγεθός μιας εικόνας.

howdoi convert kilos into pounds 

howdoi resize a picture      

#### Πως να βρεις ένα αρχείο

howdoi find a file  

sudo find / -name "mi-band.jpg"  

howdoi -l find a file   

howdoi -c find a file     

howdoi -C

howdoi -v  

#### Πως να φτιάξεις ένα persistent usb

howdoi -c make persistent usb    

#### Πως να αλλάξεις το time zone

howdoi -c change time zone 

#### Πως να διαγράψεις έναν φάκελο στο linux, πως να διαγράψεις έναν φάκελο.
howdoi -c delete a folder in linux

howdoi -c delete a folder 


#### Πως να δημιουργήσεις τυχαίους αριθμούς

howdoi -c python create random numbers 

#### Πως να κάνεις unzip
how2 unzip.gz  

#### Πως να φτιάξεις ένα persistent usb αλλά χρησιμοποιόντας το how2
how2 make a persistent usb ubuntu


lynx https://unix.stackexchange.com/questions/16743/github-adding-a-repository-as-a-fork-from-an-existing-clone/16765#16765

### References:

https://www.npmjs.com/package/how-2

https://github.com/gleitz/howdoi

Λινκ του βίντεο: https://asciinema.org/a/JzgXlwW9wqoqHyieSvhASNx3J

## Άσκηση 2η: Try different terminals and shells.
Ζητούμενο της άσκησεις είναι να πειραματιστούμε με διάφορα terminals και shells με σκοπό να δούμε ποιο θα μας βόλευε περισσότερο.

#### Για αρχή κατεβάσαμε το zsh και στην συνέχεια τρέξαμε μερικές βασικές εντολές όπως:
pwd

ll

cd

lspci

lshw

#### Μετά φτιάξαμε ένα txt αρχείο που του βάλαμε μέσα την λέξη Hello και κάνοντας:
echo hello | tee a.txt 

εμφανίσαμε το περιεχόμενο του αρχείου a.txt

#### Μετά περάσαμε στα αρχία a.txt και b.txt το:

Hello people

όπου μετά τρέξαμε τις εντολές:
echo "$(cat a.txt)" 
echo "$(cat b.txt)" 
ξεχωριστά έτσι ώστε να δούμε αν περάστικε και στα 2 αρχεία
η εντολή που δώσαμε.

#### συνεχίσαμε με μερικές εντολές όπως
for i in

βάλαμε την εντολή random για να μας εμφανίσει μερικούς τυχαίους αριθμούς.

#### Μετά συνεχίσαμε με ένα άλλο shell το: csh
#### όπου κι εκεί τρέξαμε μερικές βασικές εντολές:
pwd

ll

cd

lspci

lshw

#### Δοκιμάσαμε στην ακολουθία την εντολή: 
echo

#### και μετά τρέξαμε έναν μικρό αλγόριθμό:
set i = (p 2 0 1 7 1 3 2)                                                                                                                                                         foreach i (p 2 0 1 7 1 3 2)  
? echo $i               
? end
p  
2                                                                                                                                                                               
0                                                                                                                                                                               
1                                                                                                                                                                               
7                                                                                                                                                                               
1                                                                                                                                                                               
3                                                                                                                                                                               
2  

Τερματίζοντας έτσι την επίδειξη με τα shells.

### Όλα τα προηγούμενα βρίσκονται στο εξής βίντεο: https://asciinema.org/a/cCi8cyTDbSQA9dgMOwmwNzIOJ

## Άσκηση 3η: Performance Monitoring.

#### Ζητούμενο της άσκησης είναι τα δείξουμε κάποιους τρόπους που μπορούμε να απεικονίσουμε την απόδοση εκτέλεσης κάποιων συγκεκριμένων αλγορίθμων. H οπτικοποίηση των δεδομένων κάνει πολύ καλύτερη την κατανόησή τους.

#### Πρωτού τρέξουμε την άσκηση θα χρείαστούμε μερικά εργαλεία:

#### i) Να κατεβάσουμε το εργαλείο hyperfine.

wget https://github.com/sharkdp/hyperfine/releases/download/v1.9.0/hyperfine_1.9.0_amd64.deb

#### ii) Να εγκαταστήσουμε το εργαλείο hyperfine.

sudo dpkg -i hyperfine_1.9.0_amd64.deb

#### iii) Να φτιάξουμε μερικά αρχεία αλγορίθμων έτσι ώστε να τα συγκρίνουμε. Τα αρχεία που χρησιμοποίησα θα τα βρείτε εδώ: https://github.com/Sotiris132/My-scripts


#### iv) Οι αλγόριθμοι μας θα πρέπει να έχουν τον ίδιο αριθμό στοιχείων και τους ίδιους ακριβώς αριθμούς να ταξινομήσουν.


### Εκτέλεση της άσκησης:

#### 1) πρέπει να εκτελέσουμε το πρώτο μας αρχείο, εγώ έβαλα το bubblesort100random.py

#### 2) Μετά εκτέλεσα το δεύτερο αρχείο, το quicksort100random.py

#### 3) Αφού εκτελέσουμε και τα δύο αρχεία, τότε κάνουμε warmup ή αλλιώς w, ώστε τα δεδομένα να είναι φορτωμένα στην cashe memory πριν ξεκινήσει το test, έτσι ώστε να μην επηρεαστούν τα αποτελέσματα μας.

hyperfine -w 3 'python bubblesort100random.py'

#### 4) Ακολουθούμε την ίδια διαδικασία και για την quicksort100random.py

hyperfine -w 3 'python quicksort100random.py'

#### 5) Και για τέλος θα εκτελέσουμε ταυτόχρονα και τα δύο python scripts για να δούμε τις διαφορές τους.

hyperfine -w 3 'python quicksort100random.py' 'python bubblesort100random.py'

#### Αποτελέσματα: 

Ο αλγόριθμος quicksort έτρεξε 1.31 φορές πιο γρήγορα από την bubblesort.


Summary                                                                                                                                                                                                     
  'python quicksort100random.py' ran                                                                                                                                                                        
    1.31 ± 0.23 times faster than 'python bubblesort100random.py' 
    

### Το ακόλουθο βίντεο δείχνει την όλη διαδικασία που μόλις διαβάσατε: https://asciinema.org/a/333472

## Άσκηση 4η: Send notifications to your desktop-mobile

### Σκοπός της άσκησης είναι μέσω του εργαλείου ntfy να στείλουμε ειδοποίηση στο κινητό μας όταν τελειώσει μια εντολή που η εκτέλεση της πήρε παραπάνω από 10 δευτερόλεπτα.

#### 1) Για αρχή εγκατέστησα το εργαλείο ntfy εκτελόντας την εξής εντολή:

sudo pip install ntfy

#### 2) Μετά έπαιξα λίγο με αυτό εκτελόντας μερικές εντολές για να δω πως λειτουργεί

ntfy send test (Για να μου εμφανίσει την ειδοποίηση στην οθόνη μου)

ntfy done sleep 10 (Για να μου εμφανίσει την ειδοποίηση στην οθόνη μου αφού περάσουν 10 δευτερόλεπτα)

#### 3) Μετά έπρεπε κάπως να συνδέσω τον υπολογιστή με το κινητό μου για να λαμβάνω εκεί τις ειδοποιήσεις, οπότε εγκατέστησα στο κινητό μου την εφαρμογή Pushover και έφτιαξα λογαρισμό.

#### 4) Αφού βρήκα πως θα στείλω στο κινητό μου ειδοποίηση έπρεπε να βρω τι θα βάλω στον υπολογιστή να τρέξει και σκέφτηκα να του βάλω να παίξει ένα τραγούδι, όμως για να το κάνω αυτό χρειάστηκα το εργαλείο SoX (Sound eXchange) που το εγκατέστησα με την ακόλουθη εντολή:

sudo apt-get install sox

#### 5) Βρήκαμε πως θα στείλουμε ειδοποίηση στο κινητό, βρήκαμε τι θα βάλουμε στον υπολογιστή να τρέξει, ήρθε η ώρα να δούμε αμα θα λειτουργήσει η ιδέα, και έτρεξα την εξής εντολή:

ntfy -b pushover -o user_key t0k3n done play s0n9.mp3

#### 6) Αντικατέστησα όπου t0k3n το user key του κινητού μου και όπου s0n9 ένα τραγούδι που έχω στον υπολογιστή και αυτά είναι τα αποτελέσματα:

![image](https://github.com/Sotiris132/MyPhotos/blob/master/Screenshot%20from%202020-07-04%2022-05-58.png)

![image](https://github.com/Sotiris132/MyPhotos/blob/master/Screenshot%20from%202020-07-04%2022-13-10.png)

![image](https://github.com/Sotiris132/MyPhotos/blob/master/107221906_626149364922719_1603728382767791829_n.png)

Λινκ του βίντεο: https://asciinema.org/a/HM6fXV6o7sWauSFlc5W2EWKQ0

## Συμμετοχικό Υλικό - Α' Παραδοτέο
Link του βιβλίου: https://www.mibook.org/ 

Link του αντιγράφου του αποθετηρίου του βιβλίου: https://github.com/Sotiris132/gr/tree/master

Link της Σελίδας μου: https://sotiris132.github.io/gr/

Link πρώτης Εικόνας/Google Maps: https://sotiris132.github.io/gr/gallery/google-maps/

Link δεύτερης Εικόνας/Xiaomi Mi Band: https://sotiris132.github.io/gr/gallery/mi-band/

## Συμμετοχικό Υλικό - Β' Παραδοτέο
Link του βιβλίου: https://www.mibook.org/

Link του αντιγράφου του αποθετηρίου του βιβλίου: https://github.com/Sotiris132/gr/tree/master

Link της Σελίδας μου: https://sotiris132.github.io/gr/

Link διαδραστικού παραδείγματος: https://sotiris132.github.io/gr/remix/Xterm/

Το διαδραστικό παράδειγμα αυτό απεικονίζει ένα τερματικό χωρίς επιπτώσεις (σε περίπτωση που ο χρήστης θα έδινε πολύπλοκες εντολές
ή εντολές που θα προκαλούσαν πρόβλημα στο σύστημα) με σκοπό την εξοικείωση του χρήστη με το τερματικό.

## Πρόσθετες Εργασίες αντί για Τελική εξέταση

Εργασία συμμετοχικού περιεχομένου: https://sotiris132.github.io/gr/remix/Home%20portal%20app/

Αυτό το διαδραστικό παράδειγμα δείχνει μία επιφάνεια εργασίας όπου απεικονίζει τα στοιχεία της ώρας και μέρας, καθώς του έχει και τις εφαρμογές για: τον καιρό, το ημερολόγιο,
χάρτες, τις λίστες καθηκόντων, σύνδεση στο ίντερνετ.
