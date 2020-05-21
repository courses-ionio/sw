# ΜΑΘΗΜΑ: ΤΕΧΝΟΛΟΓΙΑ ΛΟΓΙΣΜΙΚΟΥ
### ΥΠΕΥΘΥΝΟΣ ΚΑΘΗΓΗΤΗΣ: Κ. ΧΩΡΙΑΝΟΠΟΥΛΟΣ
### ΕΞΑΜΗΝΟ ΦΟΙΤΗΣΗΣ: ΣΤ'
### ΟΝΟΜΑΤΕΠΩΝΥΜΟ: ΛΑΣΟΠΟΥΛΟΥ ΒΑΛΕΡΙΑ
### ΑΜ: Π2017Ο62
#
#
## ΑΣΚΗΣΗ 1
### Τίτλος: Τry different terminals and shells
#
#### Για την εγκατάσταση του suckless terminal (st):
1. Εγκατάσταση git, αν είναι απαραίτητη 
    - sudo apt install git
2. Στο Ubuntu συνήθως χρειάζεται η εγκατάσταση του εξής πακέτου με την εντολή:
    - apt install libxft-dev
3. Αντιγραφή της εντολής από το επίσημο site του st: https://st.suckless.org/
    - git clone https://git.suckless.org/st
4. Εγκατάσταση του st με την εντολή 
    - sudo make install
    
    
#### Για την εγκατάσταση του zsh αναλυτικές οδηγίες υπάρχουν στον παρακάτω σύνδεσμο

* https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH

Για τη ρύθμιση των παραμέτρων του zsh εγκατάσταση του open source, community-driven framework Oh My Zsh.
Οδηγίες για την εγκατάσταση καθώς και για τις διάφορες δυνατότητες που προσφέρει το Oh My Zsh βρίσκονται στο παρακάτω link

* https://github.com/ohmyzsh/ohmyzsh

Μπορεί κάποιος να βρεί να διάφορα θέματα που προσφέρει το Oh My Zsh στον εξής σύνδεσμο:

* https://github.com/ohmyzsh/ohmyzsh/wiki/Themes

Καθώς και ορισμένα επιπρόσθετα εξωτερικά θέματα που απαιτούν κάποια προεργασία παρακάτω:

* https://github.com/ohmyzsh/ohmyzsh/wiki/External-themes

Για την εφαρμογή επιπρόσθετων plugins:

* https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins
* https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins-Overview
* https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins
* https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md

#### Για την εγκατάσταση του fish και του framework του oh-my-fish ακολούθησα τις οδηγίες που περιέχονται στα παρακάτω site:

* https://www.vultr.com/docs/installing-fish-shell-on-ubuntu
* https://github.com/oh-my-fish/oh-my-fish

Βοηθητικά βίντεο στο YouTube για τις ίδιες ενέργειες:

* https://www.youtube.com/watch?v=utNQHmoH9E8&list=PLoq6SapG-dw5L3V8-74nsJQiRt4VzJS9m&index=30&t=0s
* https://www.youtube.com/watch?v=76aEqJJVRZY

Link για fish plugins:

* https://github.com/oh-my-fish

Για την σύγκριση των τριών shell επέλεξα να χρησιμοποιήσω την υπηρεσία πρόγνωσης καιρού wttr.in η οποία είναι άμεσα προσβάσιμη μέσω shell. Επιπρόσθετα θα χρησιμοποιηθούν και άλλες απλούστερες εντολές οι οποίες είναι απαραίτητες για την περιήγηση σε αρχεία με χρήση γραμμής εντολών. Θα γίνει εγκατάσταση μερικών plugin που προσφέρουν τα ενίοτε shells για την διευκόλυνση των χρηστών και την αποδοτικότερη λειτουργία τους καθώς και περιήγηση στα θέματα του κάθε κελύφους. Η αλλαγή των χρωμάτων του τερματικού ανάλογα με τις προτιμήσεις του κάθε χρήστη καθώς και η χρήση του st terminal δε θα εμφανιστεί στο ντέμο καθώς και οι δύο διαδικασίες μας οδηγούν σε νέα παράθυρα τα οποία το asciinema δε μπορεί να καταγράψει. Για την περίπτωση του st θα τραβηχτεί κάποιο στιγμιότυπο καθώς και ένα νέο asciinema για το παράθυρο που ανοίγει.

Αναλυτικές οδηγίες για τη χρήση του wttr.in:

* https://github.com/chubin/wttr.in

#### Asciinema link:

[Try Different Shells and Terminals Zsh-Fish](https://asciinema.org/a/2X3bd1Mhcw7o53eTyP2fLtaGl)

[Try Different Shells and Terminals Suckless Terminal (st)](https://asciinema.org/a/AwJCVfolOHH5tbqbSq42cJUIS)


![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/firstimage.png)

## ΑΣΚΗΣΗ 2
### Τίτλος: Create your own static site and blog generator
#
Για τη δημιουργία στατικού site επέλεξα να χρησιμοποιήσω το Static Site Generator [Ηugo](https://gohugo.io/getting-started/quick-start/). Για την επίλυση συτής της άσκησης μια επίσης καλή επιλογή είναι η χρήση του Jekyll ωστόσο το Hugo μου φάνηκε γρηγορότερο και ευκολότερο στη χρήση.

Για να χρησιμοποιήσουμε το Hugo θα πρέπει να εγκαταστήσουμε το Homebrew package manager. Για την εγκατάσταση του:

1. Αντιγράφουμε στο τερματικό την εξής εντολή:
```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
``` 
2. Μόλις ολοκληρωθεί η εγκατάσταση πληκτρολογούμε τις εξής εντολές αφού πρώτα τις έχουμε διαμορφώσει για τα ταιριάζουν στο λειτουργικό σύστημα που χρησιμοποιούμε. Στη δική μου περίπτωση δουλεύω με Ubuntu οπότε οι εντολές γίνονται:

```
    test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
    test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
    test -r ~/.profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
    echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
```
Με τη χρήση του Ηugo δημιούργησα μια στατική σελίδα στην οποία πρόσθεσα δημοσιεύσεις και θέμα της αρεσκείας μου. Tο θέμα που επέλεξα είχε πολλα features τα οποία επέτρεπαν εύκολη εισαγωγή εικόνων στην σελίδα μου καθώς και την αυτόματη μετάβαση στους προσωπικούς μου λογαριασμούς σε μέσα κοινωνικής δικτύωσης (FaceBook, Twitter, Github). Οι μετατροπές που χρειάστηκε να κάνω για να φτάσω στο τελικό αποτέλεσμα φαίνονται στον παρακάτω σύνδεσμο.

#### Asciinema link:

[Create your own static site and blog generator](https://asciinema.org/a/Uz3pi0Z2G6x0Nllc1A4fBk4MK)

### Απεικόνιση σελίδας

1. Μετά την εισαγωγή θέματος χωρίς ωστόσο να έχει γίνει καμία αλλαγή στο default config.toml του.

![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/static-site-before.png)

2. Μετά τις μετατροπές που υπέστη τόσο το config.toml όσο και το layouts για να προσαρμοστεί το θέμα στις προτιμήσεις του χρήστη. Επιπρόσθετα έχουν προστεθεί και 2 δημοσιεύσεις.

![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/static-site-final.png)

![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/static-site-final2.png)

[Σύνδεσμος με πληροφορίες για το θέμα που επέλεξα](https://github.com/eueung/hugo-casper-two)

Οι φωτογραφίες που χρησιμοποιήθηκαν για την σελίδα δεν υπόκεινται σε πνευματικά δικαιώματα και πάρθηκαν από το site:

  * https://www.pexels.com/

#
## ΑΣΚΗΣΗ 3
### Τίτλος: Performance monitoring
#
[Βοηθητικός σύνδεσμος από τον οποίο πήρα τους sorting αλγορίθμους σε Python.](https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889)

Οι μετατροπές των αλγορίθμων ώστε να μπορούν να εκτελεστούν με διαφορετικό νούμερο αριθμών κάθε φορά έγιναν με τη βοήθεια του εξής συνδέσμου (οι μετατροπές θα φανούν αναλυτικότερα στο Asciinema):

  * https://github.com/courses-ionio/sw-lab/tree/master/lab3

 Για την επίλυση της συγκεκριμένης άσκησης δούλεψα με το [hyperfine](https://github.com/sharkdp/hyperfine). Κατέβασα και το [py-spy](https://github.com/benfred/py-spy) ωστόσο μου έβγαζε αρκετά σφάλματα σε κώδικα που δούλευε κανονικά μόνος του οπότε επέλεξα να μην το συμπεριλάβω στο βίντεο του Asciinema. Θα ανέβει ένα στιγμιότυπο απο το αποτέλεσμα που έβγαλε το πρόγραμμα αυτό για την εκτέλεση του insertion-sort (παρόλο που οι εικόνες εμφανίζονταν συνέχιζε να βγάζει σφάλματα). 
 
1. Για την εγκατάσταση του hyperfine πληκτρολόγησα της εξής εντολές:
```
    wget https://github.com/sharkdp/hyperfine/releases/download/v1.9.0/hyperfine_1.9.0_amd64.deb
    sudo dpkg -i hyperfine_1.9.0_amd64.deb
```
2. Για την εγκατάσταση του py-spy χρειάστηκε απλά:
```
    pip install py-spy
```
Μετά την εγκατάσταση του πληκτρολόγησα την εντολή:
```
    py-spy record -o profile.svg -- python insertionsort.py
```
και εμφανίστηκε το εξής αποτέλεσμα:

![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/py-spy-testimage.png)

Άλλη μια χρήσιμη εντολή:
```
    py-spy top -- python insertionsort.py
```
ωστόσο δεν υπάρχει στιγμιότυπο για αυτή.

#### Asciinema link:

[Performance Monitoring](https://asciinema.org/a/tjeIbxbaSmBKJsDoHU90Bdql0)

## ΑΣΚΗΣΗ 4
### Τίτλος: Send notifications to your desktop-mobile
#
 Για την επίλυση της άσκησης αυτής χρησιμοποίησα την εφαρμογή [ntfy](https://github.com/dschep/ntfy) η οποία μας επιτρέπει να στέλνουμε ειδοποιήσεις μέσω γραμμής εντολών τόσο στο desktop όσο και στο κινητό μας. Αρχικά δοκίμασα να στείλω ειδοποιήσεις στο [pushover](https://pushover.net/) μιας και η εφαρμογή δε χρειάζεται καμία επιπλέον εγκατάσταση στο ntfy. 
 Τα βήματα για να επιτευχθεί η αποστολή είναι τα εξής:
 
   1. Εγκατάσταση του pushover στην κινητή συσκευή μέσω Playstore. Μόλις γίνει η συμπλήρωση των στοιχείων χρήστη, το pushover δίνει αυτομάτως ένα κλειδί επικοινωνίας το οποίο μπορούμε να χρησιμοποιήσουμε για να στείλουμε μηνύματα στη συσκευή μας.
   2. Επιπρόσθετα είναι δυνατή η επεξεργασία του αρχείου ntfy.yml ώστε να έρχονται ειδοποιήσεις στο κινητό για κάθε διεργασία που πραγματοποιείται στο τερματικό, ώστοσο δεν επιθυμούσα κάτι τέτοιο.  
   
 Η δεύτερη εφαρμογή στην οποία επιχείρησα να στείλω μηνύματα μέσω γραμμής εντολών είναι το [telegram](https://telegram.org/). Εδώ αντιμετώπισα ορισμένα προβλήματα μιας και για να μπορέσεις να στείλεις μηνύματα είναι απαραίτητη η εγκατάσταση του ntfy extra dependency για το telegram. Παρόλο που πληκτρολογούσα τις εντολές εγκατάστασης των extras (pip install ntfy[emoji,pid,telegram, etc] ή pip3 install ntfy[emoji,pid,telegram,etc])όπως υποδεικνυόταν στις οδηγίες το shell μου έβγαζε συνεχώς σφάλματα. Μετά από διάφορες δοκιμές κατάλαβα πως το shell που χρησιμοποιούσα (zsh) δεν υποστήριζε τις συγκεκριμένες εντολές για κάποιο λόγο, επομένως επέστρεψα στο bash με το οποίο ετρεχαν χωρίς κανένα πρόβλημα.
Για την επίτευξη της αποστολής εδώ, τα πράγματα ήταν ελαφρώς πιο περίπλοκα:

  1. Εγκατάσταση της εφαρμογής telegram στη κινητή συσκευή μέσω Playstore. 
  2. Εκτέλεση της εντολής ```pip3 install ntfy[telegram]``` στο terminal ώστε να εγκατασταθεί το extra dependency για την εφαρμογή το οποίο θα μας επιτρέψει να τη χρησιμοποιήσουμε.
  3. Μετά την εγκατάσταση εκτέλεση της εντολής ``ntfy -b telegram send "Telegram configured for ntfy" `` η οποία θα μας ζητήσει να βρούμε στο κινητό μας ένα χρήστη του telegram ονόματος botfather. 
  4. Μετά την εύρεση του χρήστη στέλνουμε το μήνυμα `` /start `` και στη συνέχεια δημιουργύμε ένα νέο bot με την εντολή `` /newbot `` το οποίο και ονοματίζουμε (αναλυτικά η διαδικασία φαίνεται στο gif παρακάτω).
  5. Επιστρέφουμε στη γραμμή εντολών και πληκτρολογούμε το token του νέου bot που δημιουργήσαμε εκεί που μας υποδεικνύει η εντολή.
  6. Αφότου γίνει αυτό μας δίνεται ένας 5ψήφιος αριθμός που πρέπει να στείλουμε σε μορφή μηνύματος στο bot ώστε να κάνουμε add το bot μας στο telegram. 
  
 Αναλυτικά η όλη διαδικασία θα φανεί στο βίντεο του Asciinema.
 
Είναι σημαντικό να αναφερθεί ότι αυτές οι δύο εφαρμογές χρησιμοποιήθηκαν πρωτίστως για να μπορέσουν να σταλούν μηνύματα εκτέλεσης εργασιών από το τερματικό σε κινητή συσκευή. Η εμφάνιση μηνυμάτων στην οθόνη του υπολογιστή μπορεί να γίνει και μόνο με την εγκατάσταση του ntfy.

#### Χρήσιμα link που βοήθησαν στην επίλυση της άσκησης:

* https://github.com/dschep/ntfy
* https://ntfy.readthedocs.io/en/latest/
* https://pypi.org/project/ntfy/
* https://gist.github.com/stecman/e3f8cacc83878aa5ba77
* https://www.youtube.com/watch?v=bbdQXfReuG0&t=754s

#### Απεικόνιση αποτελεσμάτων

1. Τα μηνύματα όπως εμφανίζονται στην οθόνη του υπολογιστή:

![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/desktopmessage1.png)
![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/desktopmessage2.png)

2. Τα μηνύματα όπως εμφανίζονται στην κινητή συσκευή:

![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/mobilenotifications.png)

3. GIF απεικόνισης telegram

![ntfygif](https://github.com/p17laso/sw/blob/2017062/P2017062/telegram.gif)



#### Asciinema link:

[Send notifications to your desktop-mobile](https://asciinema.org/a/XHKPxBpDgiio7gGMdVgxZM0FO)


## ΑΣΚΗΣΗ 5
### Τίτλος: Choose your stack
#
Για την επίλυση της άσκησης αυτής είναι απαραίτητη η εγκατάσταση του [howdoi](https://github.com/gleitz/howdoi). Το howdoi είναι ενα command line tool το οποίο παρέχει άμεσα απαντήσεις με κώδικα ή χωρίς για οποιαδήποτε σωστά τοποθετημένη προγραμματιστική ερώτηση του απευθύνουμε. Για την επίλυση της άσκησης κατά κύριο λόγο διάβασα τις οδηγίες που υπάρχουν στο παραπάνω link μιας και δεν υπάρχουν πολλές πηγές που αναφέρονται στο συγκεκριμένο εργαλείο στο διαδίκτυο. Ωστόσο, χρήσιμοι μου φάνηκαν και οι εξής σύνδεσμοι:

  * https://www.geeksforgeeks.org/howdoi-in-python/
  * https://packages.debian.org/stretch/howdoi

Τα βήματα που ακολούθησα και οι εντολές που χρησιμοποίησα φαίνονται αναλυτικά στο Asciinema.


#### Asciinema link:

[Choose your stack](https://asciinema.org/a/vo082AjkDEC7Mx8O3ataNugTD)

