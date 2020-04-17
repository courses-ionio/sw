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

- Άνοιγμα του zsh με την εντολή **zsh** (Αν θέλω να το ορίσω ως default,εγώ δεν το υλοποίησα, θα βρω το path του zsh μέσω της εντολής **whereis zsh** κι έπειτα θα το ορίσω με την εντολή chsh -s /usr/bin/zsh root).

- Για να ελέγξω και να δείξω σε ποιό shell βρίσκομαι εκτελώ την εντολή **echo $0**

- To επόμενο βήμα είναι να εγκαταστήσουμε το **oh-my-zsh framework for managing z-shell.** Αυτό επιτυγχάνεται μέσω ενός installer script και μέσω της εγκατάστασης άλλων απαιτούμενων προγραμμάτων συμπεριλαμβανομένου του wget για το κατέβασμα του installer script και το git για να το κατέβει το oh-my-zsh από το github. Αυτά επιτυγχανονται με τις ακόλουθες εντολές: **apt install wget git** και **wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh**

- Επομένως το oh-my-zsh εγκαταστάθηκε στο **home directory ~/.oh-my-zsh**

- Στη συνέχεια χρειαζόμαστε ένα **.zshrc configuration file** , το οποίο είναι διαθέσιμο στο oh-my-zsh templates directory

- Αντιγράφουμε το template .zshrc.zsh-template configuration file στο  home directory .zshrc και εφαρμόζουμε το configuration τρέχοντας το source. **cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc** και **source ~/.zshrc**

- Επειτα, άλλαξα το θέμα του shell. Αρχικά το zsh χρησιμοποιεί το "rubbyusell". Για να βρω την ποικιλία από τα θέματα που υπάρχουν στο zsh τρεχω την εντολή **cd ~/.oh-my-zsh/themes/ και ls -a**. Η αλλαγή θα γίνει στο configuration file.

- Άρα τροποιποιώ το config file μέσω του **vim ~/.zshrc** και θέτω σαν θέμα το **"agnoster".**

- Για να δω αν τρέχει ελέγχω με το **source ~/.oh-my-zsh**

- To oh-my-zsh προσφέρει επιπλέον κάποια plugins στο directory **cd ~/.oh-my-zsh/plugins/ και ls -a**

- Για να ενεργοποιήσουμε και κάποια άλλα plugins χρειάζεται να αλλάξουμε το .zshrc config file.
Στη παρένθεση με τα plugin προσθέτω τα εξής: **web-search** , **zsh-autosuggestions** , **zsh-syntax-highlighting**
To πρώτο είναι για αναζήτηση σε ιστότοπους μέσω πολλών εφαρμογων (π.χ youtube, google, bing, ddgr), το δεύτερο είναι για αυτόματη διόρθωση και το τρίτο είναι για να τονίζει τυχόν λάθη.

- Για έξοδο-> exit

- Στη συνέχεια ανοίγω το fish shell με την εντολή **fish**

- Εφόσον έχω εγκαταστήσει το oh-my-fish, αυτό προσφέρει πολλά plugins. Ένα από αυτά είναι η εμφάνιση του καιρού.
Για να γίνει αυτό έγιναν πρώτα οι εξής εγκαταστάσεις: **omf install weather** , **sudo apt-get install jq** και στη συνέχεια για εμφάνιση του καιρού: **omf weather**

- Στο βιντεο χρησιμοποίησα και άλλα features του **oh-my-fish.**

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

Στη συνέχεια, οι εντολές που ακολούθησα ήταν οι εξής:

- font:Sans 13 για τη αλλαγή γραμματοσειράς

- | set $terminals "1:terminals" | bindsym $mod+1 workspace $terminals | bindsym $mod+shift+1 move container to workspace $terminals |

- Αντίστοιχα και για τα επόμενα δύο workspaces τα οποία μετονομάστηκαν σε "web" και "documents"

- workspace_auto_back_and_forth yes το οποίο δίνει τη δυνατότητα να επιστρέψεις στο προηγούμενο orkspace με το ίδιο πλήκτρο.

- assign [class]





















### Third Assignment-SW (Send notifications to your desktop-mobile)


[third-assignment-link](https://asciinema.org/a/4yOxIH2rRATuEWdAzLqwzS8kj)

Εργαλεία:

        notify
        
        NotiFyre
        
        Pushover
        
        
 **Τα βήματα που ακολούθησα για την συγκεκριμενη εργασία, με την σειρά που φαίνονται στο βίντεο είναι τα εξής:**
 
 - Αρχικά, εγκατέστησα την εφαρμογή **Pushover** στο κινητό μου και δημιούργησα ενα API με όνομα *terminal*. Η εφαρμογή αυτομάτως μου έδωσε δύο κλειδιά, το **user key** και το **token**. Για να σταλθεί το μήνυμα όταν μία εντολή με μεγάλη διαρκεια ολοκληρωθεί, χρησιμοποίησα μια **function push** στο **.bashrc** η οποία χρησιμοποιεί τα παραπάνω κλειδιά και είναι η εξής:
 
 function push {
 
    curl -s -F "token=a5rxb98us2c39ommwqz68bcnm4c7i6" \
    -F "user=urzf1vkjtj9h8m8pxjyqoidndvc6gx" \
    -F "title=terminal" \
    -F "message=$1" https://api.pushover.net/1/messages.json
    
}

Για την δοκιμή αυτής, χρησιμοποίησα τις παρακάτω δύο εντολές: 

        - sleep 3; push "It Worked\!" 
        - sudo apt-get upadate && push "command finished successfully!" || push "something failed" 
        

Εφόσον αυτές ολοκληρώθηκαν, στάλθηκε κατευθείαν μήνυμα στην εφαρμογη στο κινητό μου όπως φαίνεται παρακάτω:




- Στη συνέχεια εγκατέστησα για να έρχονται μηνύματα αυτόματα στο desktop μου, εγκαταστάθηκαν και υλοποιήθηκαν τα εξής:

        - sudo pip install ntfy
        - sudo apt-get install notify-osd pulseaudio-utils libnotify-bin
        - git clone https://github.com/kaustubhhiware/NotiFyre.git
        - cd NotiFyre
        - cp notifyre.sh bash-preexec.sh ~
        - source ~/notifyre.sh
        - source ~/bash-preexec.sh
        - vim ~/notifyre.sh (στο οποίο μπορούν να γίνουν αλλαγές για ποιες εντολές θα έρχονται ειδοποιήσεις, π.χ για εντολές που εκτελούνται πανω απο 10 δευτερολεπτα, επισης μπορούν να γίνουν αλλαγές στον ήχο της ειδοποίησης κ.λ.π)
        
    
- Ένα δεύτερο εργαλείο είναι το **Undistract-me** για το οποίο χρησιμοποιήθηκαν οι εξής εντολές:
  
        - sudo apt-get install undistract-me
        - echo 'source /etc/profile.d/undistract-me.sh >> ~/.bashrc
        
       
   - Με τον παραπάνω τρόπο θα σταλθούν παλι ειδοποιήσεις για τις εντολες οι οποίες ολοκληρώθηκαν.
  
  
- Ένας τρίτος τρόπος είναι με το εργαλείο **Notify** και τις παρακάτω εντολές:
  
        - sudo pip install ntfy
        - echo 'eval "$(ntfy shell-integration)"' >> ~/.bashrc
        
  
- Τέλος, εκτέλεσα κάποιες απλές εντολές του **Notify**
  
        - notify-send "important!!" - u critical (το critical δείχνει στο μήνυμα ότι είναι urgent! αντίστοιχα υπάρχουν το low και normal)
        
        - notify-send "call admin!" -u critical -i face-wink (το -i εισάγει το αντίστοιχο emoji που φαίνεται δίπλα)
        
        - notify-send "this message will be displayed for 3 sec" -t 3000 ( το -t 3000 δείχνει για πόσο χρόνο θα παραμείνει το μήνυμα στο desktop)
        
        - notify-send Date "'date'" (το συγκεκριμενο μήνυμα θα εμφανίσει την ημερομηνία)
        
        - notify -t "Eftihia" send "tets" (θα εμφανίσει στο μήνυμα τον αποστολέα "Eftihia" και το μήνυμα που στέλνει "test"
        
        
        
        
 ### SOURCES 
 
 https://pushover.net/
 
 https://mikebuss.com/2014/01/03/push-notifications-cli/
 
 https://github.com/kaustubhhiware/NotiFyre
 
 https://github.com/jml/undistract-me
 
 https://www.thegeekstuff.com/2010/12/ubuntu-notify-send/
 
 https://superuser.com/questions/345447/how-can-i-trigger-a-notification-when-a-job-process-ends
 
 https://askubuntu.com/questions/187022/how-can-i-send-a-custom-desktop-notification
 
 https://github.com/dschep/ntfy
 
        
 

        
        







        

