# ΤΕΧΝΟΛΟΓΙΑ ΛΟΓΙΣΜΙΚΟΥ


### Ονοματεπώνυμο: Ευτυχία Δήμητρα Μαρία Φαρμάκη
### Αριθμός Μητρώου: Π2017070


## ΣΥΜΜΕΤΟΧΙΚΟ ΥΛΙΚΟ(30 ΜΑΡΤΙΟΥ)

### Links

[λινκ αποθετηρίου του κώδικα](https://github.com/eftichiafarmaki/gr) 

[λινκ του ιστότοπου](https://github.com/eftichiafarmaki/gr)

[λινκ αποθετηρίου του βιβλίου](https://github.com/mibook/gr)

[λινκ του προφιλ](https://github.com/eftichiafarmaki)

### A' ΠΑΡΑΔΟΤΕΟ (Εισαγωγή δύο νέων εικόνων με λεζάντα)

#### Σύνδεσμοι εικόνων

Για το συμμετοχικό υλικό προστέθηκαν δύο εικόνες απο τα παρακάτω λογισμικά:

- Android "donut". Είναι απο τις πρώτες εκδόσεις Android κατά την οποία έγιναν σημαντικές προσθήκες (επιπλέον μεγέθη οθόνης, δείκτη χρήσης της μπαταρίας, και της τεχνολογιας text-to-speech.
To θεώρησα μια καλή προσθήκη για τις εικόνες του βιβλίου καθώς, αν και δεν λειτουργεί πια, οι προσθήκες ήταν αξιόλογες και συνέβαλαν στην εξέλιξη του Android.

- Prolog. Το Prolog είναι μια λογική γλώσσα προγραμματισμού που σχετίζεται με την τεχνητή νοημοσύνη. Το Prolog ήταν μία από τις πρώτες λογικές γλώσσες προγραμματισμού και παραμένει η πιο δημοφιλής στις γλώσσες αυτές σήμερα, με αρκετές ελεύθερες και εμπορικές εφαρμογές διαθέσιμες. Η γλώσσα έχει χρησιμοποιηθεί για θεώρημα απόδειξη , έμπειρα συστήματα , όρος επανεγγραφή , συστήματα τύπου , και αυτοματοποιημένο σχεδιασμό , καθώς και πρωτότυπα του προορίζεται πεδίο χρήσεως, επεξεργασία φυσικής γλώσσας. Τα σύγχρονα περιβάλλοντα Prolog υποστηρίζουν τη δημιουργία γραφικών διεπαφών χρήστη, καθώς και διοικητικές και δικτυωμένες εφαρμογές.
To θεώρησα μια καλή προσθήκη για το βιβλίο καθώς δεν υπήρχε κάτι παρόμοιο για τον τομέα της τεχνητής νοημοσύνης.

[Polog-link](https://eftichiafarmaki.github.io/gr/gallery/prolog/)

[Android"donut"-link](https://eftichiafarmaki.github.io/gr/gallery/android-donut/)

**Σημείωση! Το πρόβλημα με την ιστοσελίδα του βιβλίου είχε λυθεί απο την εργασία στο μάθημα "Πολυμέσα" του προηγούμενου εξαμήνου.
Ωστόσο, ξαναέκανα fork το mibook/gr και ξαναέκανα από την αρχή τις απαραίτητες αλλαγές.**

## ΑΣΚΗΣΕΙΣ ΣΕ COMMAND-LINE(30 ΜΑΡΤΙΟΥ)

### Dependencies
* virtual box (kali linux)
* command line
* python
* asciinema



### First Assignment-SW (try different terminals and shells)

[first-assignment-link](https://asciinema.org/a/qku8uIjywVdh5wGRGzUir9pNB)

Για την πρώτη εργασία στο μάθημα "Τεχνολογιες Λογισμικου" του ΣΤ' εξαμήνου χρησιμοποιήθηκαν τα παραπάνω εργαλεία για να ανοίξω τουλάχιστον δύο shells και να δοκιμάσω διάφορα plugins.

Εργαλεία: 

        z-shell
        
        fish(friendly interactive shell)
        
        oh-my-zsh(z-shell manager)
        
        oh-my-fish(fish manager)

Σε πρώτη φάση επέλεξα να πλοηγηθώ και να ανοίξω τα δύο αυτά shells (fish,zsh). Σε δεύτερη φάση, εφόσον μπόρω να διορθώσω και να προσθέσω πράγματα στις εργασίες θα προσθέσω και άλλα shells αλλά και terminals.
Για αρχή, χρησιμοποιώ τα δύο αυτά εργαλεία, τους managers και τα διάφορα plugins που αυτοί προσφέρουν.

Αρχικά εγκατέστησα:
**zsh** μέσω της εντολής **sudo apt install zsh**
**fish** μέσω της εντολής **sudo apt-get install fish**.
**oh-my-zsh** με την εντολή **apt install wget git**
**oh-my-fish** με την εντολή **curl -L https://get.oh-my.fish | fish**

Τα βήματα που υλοποιήθηκαν είναι τα εξής:

- Άνοιγμα του zsh με την εντολή zsh (Αν θέλω να το ορίσω ως default,εγώ δεν το υλοποίησα, θα βρω το path του zsh μέσω της εντολής whereis zsh κι έπειτα θα το ορίσω με την εντολή chsh -s /usr/bin/zsh root).

- Για να ελέγξω και να δείξω σε ποιό shell βρίσκομαι εκτελώ την εντολή **echo $0**

- To επόμενο βήμα είναι να εγκαταστήσουμε το oh-my-zsh framework for managing z-shell. Αυτό επιτυγχάνεται μέσω ενός installer script και μέσω της εγκατάστασης άλλων απαιτούμενων προγραμμάτων συμπεριλαμβανομένου του wget για το κατέβασμα του installer script και το git για να το κατέβει το oh-my-zsh από το github. Αυτά επιτυγχανονται με τις ακόλουθες εντολές: **apt install wget git** και **wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh**

- Επομένως το oh-my-zsh εγκαταστάθηκε στο home directory ~/.oh-my-zsh

- Στη συνέχεια χρειαζόμαστε ένα .zshrc configuration file , το οποίο είναι διαθέσιμο στο oh-my-zsh templates directory

- Αντιγράφουμε το template .zshrc.zsh-template configuration file στο  home directory .zshrc και εφαρμόζουμε το configuration τρέχοντας το source. **cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc** και **source ~/.zshrc**

- Επειτα, άλλαξα το θέμα του shell. Αρχικά το zsh χρησιμοποιεί το "rubbyusell". Για να βρω την ποικιλία από τα θέματα που υπάρχουν στο zsh τρεχω την εντολή **cd ~/.oh-my-zsh/themes/ και ls -a**. Η αλλαγή θα γίνει στο configuration file.

- Άρα τροποιποιώ το config file μέσω του **vim ~/.zshrc** και θέτω σαν θέμα το "agnoster".

- Για να δω αν τρέχει ελέγχω με το **source ~/.oh-my-zsh**

- To oh-my-zsh προσφέρει επιπλέον κάποια plugins στο directory **cd ~/.oh-my-zsh/plugins/ και ls -a**

- Για να ενεργοποιήσουμε και κάποια άλλα plugins χρειάζεται να αλλάξουμε το .zshrc config file.
Στη παρένθεση με τα plugin προσθέτω τα εξής: **web-search** , **zsh-autosuggestions** , **zsh-syntax-highlighting**
To πρώτο είναι για αναζήτηση σε ιστότοπους μέσω πολλών εφαρμογων (π.χ youtube, google, bing, ddgr), το δεύτερο είναι για αυτόματη διόρθωση και το τρίτο είναι για να τονίζει τυχόν λάθη.

- Για έξοδο-> exit

- Στη συνέχεια ανοίγω το fish shell με την εντολή **fish**

- Εφόσον έχω εγκαταστήσει το oh-my-fish, αυτό προσφέρει πολλά plugins. Ένα από αυτά είναι η εμφάνιση του καιρού.
Για να γίνει αυτό έγιναν πρώτα οι εξής εγκαταστάσεις: **omf install weather** , **sudo apt-get install jq** και στη συνέχεια για εμφάνιση του καιρού: **omf weather**

- Στο βιντεο χρησιμοποίησα και άλλα features του oh-my-fish.

- Για έξοδο-> exit

- Επιπλέον, η εντολη **cat /etc/shells/** δίνει τα paths από κάποια shells τα οποία είναι ήδη διαθέσιμα, όπως είναι το dash.

#### SOURCES

-https://github.com/ohmyzsh/ohmyzsh/wiki

-https://github.com/ohmyzsh/ohmyzsh/wiki/Themes

-https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins

-https://github.com/oh-my-fish/plugin-weather

-https://github.com/oh-my-fish/oh-my-fish




### Second Assignment-SW (Configure a custom window manager)

[second-assignment-link](https://asciinema.org/a/9HQqJyw9kyUyEsWkVeu5ra8TK)

Εργαλεία:

        i3 Windows Manager
        
        Qtile Windows Manager
        
        
 #### I3 WINDOWS MANAGER
 
Σε πρώτη φάση, επέλεξα τον i3 windows manager. Eίναι ένας ελεύθερος, ανοιχτού κώδικα και πλήρως διαμορφωμένος διαχειριστής παραθύρων και διαθέτει tree data structure που επιτρέπει πιο ευέλικτα layouts από τις εναλλακτικές λύσεις. 

**Γιατί να επιλέξει κανείς τον i3-wm?**

- Minimalist

- Light But Powerful

- Flexible

- The Mouse Is Not Your Best Friend


*Τα βήματα φαίνονται παρακάτω πιο αναλυτικά από το asciinema λόγω της αποκλειστικής σχεδόν χρήσης πληκτρολογίου και λόγω του ότι πολλές ρυθμίσεις που έγιναν στο config file του i3wm χρειάζονταν reboot για να εφαρμοστούν.*

- Αρχικά εγκατέστησα τον i3 windows manager μέσω της εντολής **sudo apt-get install i3-wm**

*Τα βασικά keyboard shortcuts των οποίων οι συνδυασμοί προυπήρχαν στο config file και μου ήταν απαραίτητα για την αρχική μου πλοήγηση είναι συνοπτικά τα εξής:* 

| KEYBOARD SHORTCUTS | ΛΕΙΤΟΥΡΓΙΕΣ |
| -- | -- |
| ALT+ENTER | Open new terminal |
| MOD+SHIFT+J,K,L,; | Move window |
| MOD+0-9 | Switch to another workspace |
| MOD+SHIFT+0-9 | Move a window to another workspace |
| MOD+D | Open application launcher-dmenu |
| MOD+SHIFT+E | Exit i3 |
| MOD+SHIFT+Q | Kill a window |
| MOD+SHIFT+C | Reload the configuration file |
| MOD+SHIFT+R | Restart i3 in place |
| MOD+F | Toggle fullscreen |
| MOD+V | Split a window vertically |
| MOD+H | Split a window horizontally |
| MOD+H | Resize mode |

        

