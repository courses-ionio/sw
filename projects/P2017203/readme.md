# Μάθημα: Τεχνολογία Λογισμικού
#
## Προσωπικά Στοιχεία:
#### A.M.: Π2017203
#### Όνομα: Ανδρέας
#### Επώνυμο: Καγκελάρης
#
### Άσκηση 1
##### Τίτλος: performance monitoring
##### Ζητούμενα: monitor the performance of your python scripts and visualize them with colors and/or spark lines
#
##### Προαπαιτούμενα: 
##### α) Download hyperfine
###### wget https://github.com/sharkdp/hyperfine/releases/download/v1.9.0/hyperfine_1.9.0_amd64.deb
##### β) Εγκατάσταση hyperfine
###### sudo dpkg -i hyperfine_1.9.0_amd64.deb
##### γ) Δημιουργία python script το οποίο δημιουργεί αρχεία .txt με πλήθος αριθμών το οποίο και καθορίζεται κατά την εκτέλεση του script. Το script είναι διαθέσιμο [εδώ](https://github.com/p17kagk/myfiles/blob/master/rand.py.tar.gz)
##### δ) Εκτέλεση του python script, ώστε να δημιουργήσουμε αρχεία με τυχαίους αριθμούς, πλήθους 10,100,1000,10000,100000 αντίστοιχα. Θα χρειαστούν στην συνέχεια για την εξαγωγή συμπερασμάτων.
###### python rand.py 10 && python rand.py 100 && python rand.py 1000 && python rand.py 10000 && python rand.py 100000
##### ε) Δημιουργία 3 python scripts τα οποία θα διαβάζουν ένα .txt αρχείο με τυχαίους αριθμούς, και θα κάνουν ταξινόμηση με χρήση αλγορίθμου i)bubblesort ii)heapsort iii)mergesort. Τα 3 scripts είναι διαθέσιμα [εδώ](https://github.com/p17kagk/myfiles/blob/master/sorting_scripts.tar.gz)
##### στ) Εγκατάσταση asciinema, και δημιουργία λογαριασμού σε αυτό.
###### sudo apt-get install asciinema
##### ζ) Τροποποίηση του .bashrc έτσι ώστε το shell prompt να δείχνει τον Α.Μ. μας.
###### cd ~
###### vi .bashrc
###### export PS1='Π2017203:\w$ ' //add this line in the end of file
###### source .bashrc //execute this command so as to reload new .bashrc
#
##### Εκτέλεση Άσκησης
##### α) Εκτέλεση του benchmark με 1 εντολή, αρχείο 1000 αριθμών 
###### hyperfine 'python heapsort.py 1000'
##### β) Εκτέλεση του benchmark με 1 εντολή, αρχείο 1000 αριθμών, αφού προηγουμένως κάνουμε warmup, ώστε τα δεδομένα να είναι φορτωμένα στην cashe memory πριν ξεκινήσει το test, και έτσι να μην επιρρεαστεί το αποτέλεσμα απο την ταχύτητα I/O του μέσου ανάγνωσης.
###### hyperfine --warmup 3 'python heapsort.py 1000'
##### γ) Εκτέλεση του benchmark με αρχείο 1000 αριθμών, 3 φορές, μία για κάθε αλγόριθμο, ώστε να συγκρίνουμε την απόδοση των 3 διαφορετικών αλγορίθμων. Θα κάνουμε και εδώ χρήση του warmup.
###### hyperfine --warmup 3 'python heapsort.py 1000' 'python mergesort.py 1000' 'python bubblesort.py 1000'
##### δ) Εκτέλεση του benchmark με 1 εντολή, αρχείο 1000 αριθμών, αφού προηγουμένως κάνουμε prepare, ώστε να καθαρίσουμε την  cashe memory πριν ξεκινήσει το test, και έτσι τα αποτελέσματα του test να συμπεριλαμβάνουν και την ταχύτητα I/O του μέσου ανάγνωσης.
###### 












#### 1) search, download and play (with the terminal) your favorite song of the month from youtube
#
#### Για την εκπόνηση της άσκησης, ακολουθήσαμε τα εξής βήματα:
##### α) Εγκατάσταση του S/W 'asciinema', ώστε να γίνει καταγραφή του terminal (χρήση flag -i=0.2 για την αποφυγή καταγραφής κενών διαστημάτων). Για την σκοπό της άσκησης δημιουργήσαμε και λογαριασμό στο www.asciinema.org
###### sudo apt-get install asciinema
##### β) Τροποποίηση του .bashrc, ώστε το bash prompt να δείχνει τον Α.Μ. μας.
###### vi .bashrc
##### γ) Εγκατάσταση του S/W 'youtube-dl' ώστε να κάνουμε download το επιθυμητό link με την χρήση terminal. Η εγκατάσταση του πακέτου έγινε απο την σελίδα του δημιουργού και όχι απο τον Ubuntu server, λόγω γνωστού προβλήματος στην έκδοση του Ubuntu Server https://github.com/ytdl-org/youtube-dl/issues/21952. 
###### sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
###### sudo chmod a+rx /usr/local/bin/youtube-dl
##### δ) Εγκατάσταση του front end 'mps-youtube', ώστε να κάνουμε search και download το αρχείο που θέλουμε.
###### sudo apt install mps-youtube
##### ε) Εκτέλεση του mpsyt. Download το βέλτιστο audio αρχείο (και όχι video για οικονομία χρόνου). 
##### στ) Εγκατάσταση του πακέτου 'ffmpeg', ώστε να μετατρέψουμε το αρχείο που κατεβάσαμε (.m4a) σε μορφή .mp3.
###### sudo apt-get install ffmpeg
##### ζ) Μετατροπή του αρχείου σε .mp3
###### ffmpeg -i 'Dmitri Shostakovich -  Waltz No. 2.m4a' -acodec libmp3lame -aq 2 'Dmitri Shostakovich -  Waltz No. 2.mp3'
##### η) Εγκατάσταση του S/W 'mpv', ώστε να γίνει απο εκεί η αναπαραγωγή του .mp3 αρχείου.
###### sudo apt-get install mpvsudo apt-get install mpv
##### θ) Αναπαραγωγή του .mp3 αρχείου απο terminal. Η αναπαραγωγή τερματίστηκε μετά απο λίγα δευτερόλεπτα, για οικονομία χρόνου.
###### mpv 'Dmitri Shostakovich -  Waltz No. 2.mp3'
##### Σημ 1.: Στην καταγραφή του asciinema δεν ακούγεται η αναπαραγωγή του ήχου, αλλά μπορεί κανείς να το καταλάβει απο την έξοδο του terminal. Επίσης αν κάποιος ακολουθήσει τα βήματα, θα πετύχει το αποτέλεσμα.
#
#### όλα τα παραπάνω βήματα φαίνονται αναλυτικά στο [link](https://asciinema.org/a/275789) 
#
#### [link](https://github.com/p17kagk/mm/tree/master) στο αποθετήριο του κώδικα:
#### [link](https://github.com/p17kagk/mm/tree/P2017203) στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
#### [link](https://asciinema.org/a/275789) στο εκτελέσιμο:
#
## Άσκηση 2
#### Τίτλος: download a torrent
#
##### Σημ 1.: Επιλέξαμε να πραγματοποιήσουμε απο το τερματικό (σαν παραπάνω βήμα )όχι μόνο το downloading του torrent, αλλά και την αναζήτηση του torrent αρχείου. Σε αυτό το βήμα συναντήσαμε τις παρακάτω δυσκολίες:
##### Σημ 2.: Διαπιστώθηκε οτι ένας μεγάλος αριθμός απο τα γνωστά cli torrent search λογισμικά (torrench, we-get, rtorrent) έχει σταματήσει να αναπτύσσεται και να υποστηρίζεται απο τα τέλη περίπου του 2017, όπου δηλαδή η πληθώρα των torrent trackers μετέβη σε 'https'. Για τον λόγο αυτό, το κομμάτι της άσκησης που αφορά την αναζήτηση αρχείου δεν υλοποιήθηκε με κάποιο απο αυτα τα εργαλεία, αλλά με την χρήση python script.
##### Σημ 3.: Επιλέξαμε η αναζήτηση να "τρέξει" μέσα σε συγκεκριμένο torrent tracker και όχι στο διαδίκτυο γενικά (Δηλαδή το search να μην γίνει κάνοντας χρήση μηχανής αναζήτησης, αλλά μέσα στην αναζήτηση ενός torrent tracker).
#### Για την εκπόνηση της άσκησης, ακολουθήσαμε τα εξής βήματα:
##### α) Εγκατάσταση του S/W 'asciinema', ώστε να γίνει καταγραφή του terminal (χρήση flag -i=0.2 για την αποφυγή καταγραφής κενών διαστημάτων). Για την σκοπό της άσκησης δημιουργήσαμε και λογαριασμό στο www.asciinema.org
###### sudo apt-get install asciinema
##### β) Τροποποίηση του .bashrc, ώστε το bash prompt να δείχνει τον Α.Μ. μας.
###### vi .bashrc
##### γ) Εγκατάσταση  'terminaltables' packet απο πακέτο pip3. Χρειάζεται για την σωστή απεικόνιση των αποτελεσμάτων του παρακάτω script.
###### pip3 install terminaltables
##### δ) Δημιουργία python script με όνομα 'torrent_search', που θα εκτελείται απο κονσόλα, κάνει αναζήτηση σε torrent server και θα επιστρέφει τα αποτελέσματα στο τερματικό. Ο κώδικας προέρχεται απο αναζήτηση στον διαδίκτυο.
###### vi torrent_search 
##### Για ευκολία του αναγνώστη, το script βρίσκεται [εδω](https://github.com/p17kagk/myfiles/blob/master/torrent_search.py.gz)
##### Για να μην χρειάζεται κάθε φορά να καλούμε το script μέσα απο το full path της python, δίνουμε το χαρακτηριστικό python στο script, προσθέτοντας στην πρώτη γραμμή του αρχείου το shebang:
###### #!/usr/bin/env python3
##### ε) Μετατροπή του αρχείου σε εκτελέσιμο. 
###### chmod +χ torrent_search
##### H σύνταξη για την εκτέλεση είναι:
###### ./torrent_search name
##### στ) Εγκατάσταση του cli torrent client "transmission "repository
###### sudo add-apt-repository ppa:transmissionbt/ppa 
##### Ενημέρωση των πακέτων αναζήτησης (στην ουσία προσθέτω το repository που μόλις έβαλα)
###### sudo apt-get update
##### εγκατάσταση των πακέτων που θα χρειαστω: transmission-cli, transmission-common, tranmission-daemon.
###### sudo apt-get install transmission-cli transmission-common tranmission-daemon
##### ζ) Σταματάω τον daemon και προσθέτω τον Ubuntu user μου (andreas) στους Authenticated χρήστες του Transmission. Στην συνέχεια ξαναξεκινώ τον daemon
###### sudo service transmission -daemon stop
###### sudo usermode -a -G debian-transmission andreas
###### sudo service transmission -daemon start
##### η) Κάνω την αναζήτησή μου (keyword="wind")
###### ./torrent_search wind
##### Επιλέγω  ένα απο τα αποτελέσματα, και παίρνω απο εκει το magnetic link. Στην συνέχεια το βάζω στον torrent client
###### transmission-remote -a "magnetic link"
##### και στην συνέχεια βλέπω οτι όντως προστέθηκε:
###### transmission-remote -l
##### Για να δείξουμε οτι τα παραπάνω δεν δουλεύουν μόνο για magnetic links, αλλά και για αρχεία torrents, εκτελούμε την ίδια εντολή και για ένα αρχείο .torrent που έχουμε κατεβάσει απο το διαδίκτυο.
###### transmission-remote -a ".torrent file"
##### Eπιβεβαίωση
###### transmission-remote -l
##### και τέλος μεταβαίνουμε στο download path και επιβεβαιώνουμε την ύπαρξη των των αρχείων:
###### cd /var/lib/transmission-daemon/downloads
###### ls 
#
#### όλα τα παραπάνω βήματα φαίνονται αναλυτικά στο [link](https://asciinema.org/a/277131 )
#
#### [link](https://github.com/p17kagk/mm/tree/master) στο αποθετήριο του κώδικα:
#### [link](https://github.com/p17kagk/mm/tree/P2017203) στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
#### [link](https://asciinema.org/a/277131) στο εκτελέσιμο:
#
## Συμμετοχικό εκπαιδευτικό υλικό - 1
#
#### [Link](https://mibook.org/) του mibook.org
#### [Link](https://github.com/p17kagk/gr) του προσωπικού αποθετηρίου του βιβλίου
#
#### Αναρτήσεις του περιεχομένου του mibook.org/gr/ με τρόπο εκπαιδευτικό και ευχάριστο! 
#### Για τις αναρτήσεις έγινε χρήση των κοινωνικών δικτύων facebook και tweeter.
#
#### [Ανάρτηση 1](https://www.facebook.com/andreas.kagkelaris/posts/10156381743652414)
#### [Ανάρτηση 2](https://www.facebook.com/andreas.kagkelaris/videos/10156381702157414/)
#### [Ανάρτηση 3](https://www.facebook.com/andreas.kagkelaris/videos/10156381718967414/)
#### [Ανάρτηση 4](https://www.facebook.com/andreas.kagkelaris/videos/10156381756957414/)
#### [Ανάρτηση 5](https://www.facebook.com/andreas.kagkelaris/videos/10156381726337414/)
#### [Ανάρτηση 6](https://twitter.com/kagelaris3/status/1192932196157468673)
#### [Ανάρτηση 7](https://twitter.com/kagelaris3/status/1192930702200889344)
#### [Ανάρτηση 8](https://twitter.com/kagelaris3/status/1192929617251840005)
#### [Ανάρτηση 9](https://twitter.com/kagelaris3/status/1192928238240194563)
#### [Ανάρτηση 10](https://twitter.com/kagelaris3/status/1192927744604196864)
#### [Ανάρτηση 11](https://twitter.com/kagelaris3/status/1192925222904705026)
#
## Άσκηση 3
#### Τίτλος: edit a spreadsheet
#### Ζητούμενα: 
#### 1) edit values and formulas
#
#### Για την εκπόνηση της άσκησης, ακολουθήσαμε τα εξής βήματα:
##### α) Εγκατάσταση του S/W 'asciinema', ώστε να γίνει καταγραφή του terminal (χρήση flag -i=0.2 για την αποφυγή καταγραφής κενών διαστημάτων). Για την σκοπό της άσκησης δημιουργήσαμε και λογαριασμό στο www.asciinema.org
###### sudo apt-get install asciinema
##### β) Τροποποίηση του .bashrc, ώστε το bash prompt να δείχνει τον Α.Μ. μας.
###### vi .bashrc
##### γ) Εγκατάσταση του S/W 'sc' ώστε να επεξεργαστούμε ένα spreadsheed. 
###### sudo apt install sc
##### δ) Εκκίνηση του επεξεργαστή 'sc'. Πραγματοποιήθηκαν οι παρακάτω λειτουργίες:
###### hjkl — keys motion
###### gX00 - go to cell
###### ir — insert row
###### dr — delete row
###### = — enter a numeric value
###### = (@sum(A2:A145)) enter a formula
###### e — edit a numeric value
###### e — edit a formula
###### P<ΜΜ.sc> — write an .sc file
###### q=quite
#
#### όλα τα παραπάνω βήματα φαίνονται αναλυτικά στο [link](https://asciinema.org/a/281721)
#
#### [link](https://github.com/p17kagk/mm/tree/master) στο αποθετήριο του κώδικα:
#### [link](https://github.com/p17kagk/mm/tree/P2017203) στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
#### [link](https://asciinema.org/a/281721) στο εκτελέσιμο:
#
## Άσκηση 4
#### Τίτλος: watch video
#### Ζητούμενα: youtube video streaming with asciiart
#
#### Για την εκπόνηση της άσκησης, ακολουθήσαμε τα εξής βήματα:
##### α) Εγκατάσταση του S/W 'asciinema', ώστε να γίνει καταγραφή του terminal (χρήση flag -i=0.2 για την αποφυγή καταγραφής κενών διαστημάτων). Για την σκοπό της άσκησης δημιουργήσαμε και λογαριασμό στο www.asciinema.org
###### sudo apt-get install asciinema
##### β) Τροποποίηση του .bashrc, ώστε το bash prompt να δείχνει τον Α.Μ. μας.
###### vi .bashrc
##### γ) Εγκατάσταση του S/W 'youtube-dl' ώστε να κάνουμε download το επιθυμητό link με την χρήση terminal. Η εγκατάσταση του πακέτου έγινε απο την σελίδα του δημιουργού και όχι απο τον Ubuntu server, λόγω γνωστού προβλήματος στην έκδοση του Ubuntu Server https://github.com/ytdl-org/youtube-dl/issues/21952. 
###### sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
###### sudo chmod a+rx /usr/local/bin/youtube-dl
##### δ) Εγκατάσταση των βιβλιοθηκών [libcaca](https://launchpad.net/ubuntu/+source/libcaca) και [AAlib](https://launchpad.net/ubuntu/+source/aalib). Η βιβλιοθήκη AAlib μετατρέπει την έξοδο του σήματος που δέχεται απο pixels σε ασπρόμαυρους ASCII χαρακτήρες. Αντίστοιχα, η βιβλιοθήκη libcaca μετατρέπει την έξοδο του σήματος που δέχεται απο pixels σε έγχρωμους ASCII χαρακτήρες. Και οι 2 βιβλιοθήκες εγκαταστάθηκαν κάνοντας build και install στο τερματικό μας:
##### Για ευκολία του αναγνώστη, το lib ΑΑlib έχει ανέβει [εδώ](https://github.com/p17kagk/myfiles/blob/master/aalib-1.4rc4.tar.gz)
##### και το lib libcaca [εδώ](https://github.com/p17kagk/myfiles/blob/master/libcaca-0.99.beta19.tar.gz)
##### Για να κάνω build και install (και τις 2 βιβλιοθήκες) εκτελώ:
###### ./configure && make && sudo make install
##### ε) εκτέλεση της εντολής:
###### mplayer -really-quiet -vo aa:driver=curses -cookies -cookies-file /tmp/cookie.txt $(youtube-dl -g -f best --cookies /tmp/cookie.txt "https://www.youtube.com/watch?v=EKkzbbLYPuI")
##### (επιλέξαμε να γίνει video streaming και όχι download το αρχείο, και απο εκεί εκτέλεση)
##### όπου:
##### mplayer: o player που χρησιμοποιούμε
##### -really-quite: Make console output less verbose. Particularly useful on slow terminals
##### -vo: για να οδηγήσουμε την έξοδο σε περιβάλλον X11 (παράθυρο)
##### aa:driver=curses: για να μετατρέψουμε τα pixels σε ASCII χαρακτήρες. Οδηγώ την έξοδο στο παρόν bash.
##### -cookies -cookies-file /tmp/cookie.txt: για να δηλώσουμε οτι θα χρησιμοποιήσουμε cookies (απαραίτητα για την λειτουργία του youtube). τα οποία και θα βρίσκονται στο δηλωθέν path.
##### $(youtube-dl): η είσοδος του mplayer θα είναι η έξοδος απο την εκτέλεση του youtube-dl
##### youtube-dl -g: για να κανουμε real time streaming και όχι download.
##### -f best: επιλέγουμε βέλτιστη ανάλυση
##### --cookies /tmp/cookie.txt: χρήση cookies
##### "https://www.youtube.com/watch?v=EKkzbbLYPuI": το url μας.
#
##### στ) Θα επαναλάβουμε το ίδιο βήμα, αυτήν την φορά όμως η έξοδός μας θα είναι με έγχρωμους ascii. Για να το πετύχουμε αυτό θα κάνουμε χρήση της 'libcaca' αντί της 'AAlib'.
##### Αυτή τη φορά, για να οδηγήσουμε την έξοδο στο παρόν τερματικό, θα χρησιμοποιήσουμε πρώτα την εντολη:
###### export CACA_DRIVER=ncurses
##### ώστε να ρυθμίσουμε την libcaca να χρησιμοποιήσει την ncurses (a library of functions that manages an application's display on character-cell terminals) σαν driver εξόδου.
##### και στη συνέχεια:
###### mplayer -really-quiet -vo caca -cookies -cookies-file /tmp/cookie.txt $(youtube-dl -g -f best --cookies /tmp/cookie.txt "https://www.youtube.com/watch?v=EKkzbbLYPuI")
##### όπου:
##### mplayer: o player που χρησιμοποιούμε
##### -really-quite: Make console output less verbose. Particularly useful on slow terminals
##### -vo: για να οδηγήσουμε την έξοδο σε περιβάλλον X11 (παράθυρο)
##### caca: χρήση lib caca
##### -cookies -cookies-file /tmp/cookie.txt: για να δηλώσουμε οτι θα χρησιμοποιήσουμε cookies (απαραίτητα για την λειτουργία του youtube). τα οποία και θα βρίσκονται στο δηλωθέν path.
##### $(youtube-dl): η είσοδος του mplayer θα είναι η έξοδος απο την εκτέλεση του youtube-dl
##### youtube-dl -g: για να κανουμε real time streaming και όχι download.
##### -f best: επιλέγουμε βέλτιστη ανάλυση
##### --cookies /tmp/cookie.txt: χρήση cookies
##### "https://www.youtube.com/watch?v=EKkzbbLYPuI": το url μας.
#
##### όλα τα παραπάνω βήματα φαίνονται αναλυτικά στο [link](https://asciinema.org/a/293148)
##### Σημ.: Όπως και στην Άσκηση 1, έχουμε το πρόβλημα οτι στην καταγραφή με το asciinema δεν μπορούμε να ακούσουμε τον ήχο. Για να έχει ο αναγνώστης μια πιο ολοκληρωμένη εικόνα, υπάρχει ένα μικρό ενδεικτικό video [εδώ](https://github.com/p17kagk/myfiles/blob/master/askisi_4.mp4.gz)
#
##### [link](https://github.com/p17kagk/mm/tree/master) στο αποθετήριο του κώδικα:
##### [link](https://github.com/p17kagk/mm/tree/P2017203) στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
##### [link](https://asciinema.org/a/293148) στο εκτελέσιμο:
#
## Συμμετοχικό εκπαιδευτικό υλικό - 2
#
#### [Link](https://mibook.org/) του mibook.org.
#### [Link](https://github.com/p17kagk/gr) του προσωπικού αποθετηρίου του βιβλίου.
#### [Link](https://p17kagk.github.io/gr/) στο δικό μου αντίγραφο του βιβλίου.
#### Τροποποιήσαμε το index.md, έτσι ώστε: 
#### α) Να αφαιρέσουμε μια απο τις 3 αναρτήσεις που είχε στην αρχική σελίδα, και στην θέση της να βάλουμε μια ροή περιεχομένου (χρησιμοποιήσαμε το twitter).
#### β) Αλλαγή της κεντρικής εικόνας στην αρχική σελίδα.
#### Στην συνέχεια, κρίθηκε χρήσιμο και σε κάθε ανάρτηση που είχαμε τροποποιήσει στο Παραδοτέο 1, προστέθηκε η αντίστοιχη ροή πληροφορίας απο την ανάρτηση. Ακολουθούν τα links με τις αλλαγές στις αναρτήσεις (στο δικό μας αντίγραφο).
#### [Link](https://p17kagk.github.io/gr/case-study/arduino/) Arduino
#### [Link](https://p17kagk.github.io/gr/case-study/www/) World Wide Web
#### [Link](https://p17kagk.github.io/gr/case-study/wikipedia/) Wikipedia
#### [Link](https://p17kagk.github.io/gr/case-study/windows/) Microsoft Windows
#### [Link](https://p17kagk.github.io/gr/remix/keyboard-input/) Keyboard input
#### [Link](https://p17kagk.github.io/gr/remix/menu-pie/) Menu pie
#### [Link](https://p17kagk.github.io/gr/remix/calculator/) Calculator
# 






























