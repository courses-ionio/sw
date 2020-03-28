# Σιδεράς Γεώργιος

## AM : Π2017164

## Ασκήσεις Terminal : 

### 1η Άσκηση : 

* Assignment : send notifications to your desktop-mobile.

* Deliverables : send a notifcation when a big task completes, eg download, compiling, etc.  

* Σύνδεσμος των εντολών στο [Asciinema](https://asciinema.org/a/312457 "asciinema") 

* Screenshot απο το κινητό για την εμφάνηση της ειδοποίησης ![Smartphone Screenshot](https://snipboard.io/i6vKI5.jpg)

* Εργαλεία που χρησιμοποίησα :
    * [notify(ntfy)](https://github.com/dschep/ntfy/ "ntfy")

* Εφαρμογη για το κινητο : 

    * [Pushbullet](https://www.pushbullet.com "Pushbullet")

* Περιγραφή : Αρχικά κατέβασα το ntfy με την εντολή ```$sudo pip3 install ntfy ```
και πρόσθεσα ως extra dependencies το pid και το pushbullet με τις εντολές ```$pip3 install ntfy[pid]``` ```$pip3 install ntfy[pushbullet]```Στην συνέχεια κατεβασα το app για το smartphone pushbullet και εκανα εγραφη και σύνδεση , έπειτα πήγα -> settings -> account και μετα πατησα να μου δωσει ενα access token.Στο termina δημιουργησα ενα αρχειο με την εντολη 
```$sudo nano ~/.ntfy.yml```και μέσα έγραψα : 
```
backends:
    - pushbullet
pushbullet:
    access_token: o.QTyuazAvmXQE9pp0D8eDCiRcayFigQ21ο
 ```
(οπου στο acces token εβαλα αυτο που πηρα απο την εφαρμογη.)
Με αυτην την τροποποιηση στο αρχειο καθε φορα που τρεχεις την εντολη ```$ntfy send "Notifictaion" ```θα πέρνει ως όρισμα -b το pushbullet και ως -o το access_token: o.QTyuazAvmXQE9pp0D8eDCiRcayFigQ21ο . Μετα με την εντολη ```$eval "$(ntfy shell-integration -f -L 30)" ```καθε φορα που τελειωνει μια εντολη που τρεχει πανω απο 30s στελνει μηνυμα , η επιλογη -f λεει οτι στειλε ακομα και αν ο terminal τρεχει στο background και -L μετα απο ποσο χρονο αν τρεχει μια εντολη να στελνει μηνημα.

* Σχόλια : Δυστυχώς η ανακοίνωση που μου ήρθε στο κινητό ήταν για το πότε τελείωσε η πρώτη εντολή που στην περιπτωσή μας ήταν η ```$asciinema rec ``` αλλά αν έτρεχα κάποια έντολη χώρις να προηγείτε η rec θα μου την εμφάνιζε κανονικά στο κινητό.
___
### 2η Άσκηση : 

* Assignment : performance monitoring

* Deliverables : monitor the performance of your python scripts and visualize them with colors and/or spark lines   

* Περιγραφή : Βρήκα και τροποποίησα δύο python scripts για να καλύπτουν τις ανάγκες της εργασίας απο το διαδίκτυο τα οποία κάνουν brute force σε έναν δωσμένο κωδικό (το πρώτο κάνει χρήση λεξικού ενώ το δεύτερο όχι). Στην συνεχεια , έτρεξα την εντολή ```$hyperfine -i --prepare 'sync; echo 3 | sudo tee /proc/sys/vm/drop_caches' bruteforce1.py bruteforce2.py ```
όπου το ```-i``` βοηθάει στο να αγνόει τυχόν αποτυχίες του script και το ```--prepare 'sync; echo 3 | sudo tee /proc/sys/vm/drop_caches'``` καθαρίζει την cache για να μην υπάρξουν παραβολές , και τελος τα δυο scripts που θέλω να συγκρίνω.

* Σύνδεσμος των εντολών στο [Asciinema](https://asciinema.org/a/312537 "asciinema") 

* Τα scripts που χρησιμοποίησα : [Script_01](https://github.com/geosideras/My_ionio_university_repository/blob/master/Python_Scripts/bruteforce1.py) [Script_02](https://github.com/geosideras/My_ionio_university_repository/blob/master/Python_Scripts/bruteforce2.py)

* Εργαλεία που χρησιμοποίησα :
    * [Hyperfine](https://github.com/sharkdp/hyperfine "Hyperfine")
___

### 3η Άσκηση : 

* Assignment : try different terminals and shells

* Deliverables : repeat some of the previous exercises with a different terminal-shell and create a custom configuration that fits your needs   

* Περιγραφή : Κατέβασα και εγκατέστησα τον z shell , έπειτα κατέβασα την προέκταση oh-my-zsh για να μπορώ να τον τροποποιήσω και να τον προσαρμόσω στα συμφέροντα μου. Πέρασα το θέμα angnoster το οποίο είναι πολύ χρήσιμο για άτομα που χειρίζονται πολύ το git , περασα το z για να μεταπηδάω directories και να πηγαίνω στο προορισμό μου πιο γρήγορα, το fuck για αμα κάνω μικρά λάθοι στις εντολές μου , το οποίο μου βγάζει πιθανά suggestions και το autosuggestions το οποίο πρωτού γράψω μια εντολή μου βγάζει μια προτεινόμενη εντολή την οποία και μπορώ να επιλέξω με τα navigation keys. Μερικές χρήσιμες πληροφοριες που παρέχει το terminal μου τώρα είναι : 
* Ο κεραυνος που βγαζει στα αριστερα του user το οποιο προσδιορίζει αν είμαι root. 
* Το X είναι οτι η προηγούμενη εντολή που έτρεξα απέτυχε. 
* Άμα μπω σε ενα dir το οποίο είναι git repository το βγάζει με άλλο χρωμα . 
* Πρασινο αν δεν έχουν γίνει αλλαγές 
* Κίτρινο αν εχουν γινει αλλαγές και δεν έχει γίνει το commit. 
* Καθώς επίσης μέσα σε αυτό το καρτελάκι γράφει το όνομα του branch που βρίσκομαι 

* Όλα αυτα μπορούμε να τα δούμε στο demo εντολών του [Asciinema](https://asciinema.org/a/312545 "asciinema") 

* Εργαλεία που χρησιμοποίησα :
    * [ZSH](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH "zsh")
    * [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh "ohmyzsh")
    * [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions "autosuggestions")
    * [agnoster-zsh-theme](https://github.com/agnoster/agnoster-zsh-theme "agnoster")
    * [z - jump around](https://github.com/rupa/z "Z")
    * [thefuck](https://github.com/nvbn/thefuck "thefuck")
 ___
    
 ### 4η Άσκηση : 

* Assignment : create an agent for news

* Deliverables : the demo should display the new content added on a news web site 

* Περιγραφή : 

* Σύνδεσμος των εντολών στο [Asciinema](https://asciinema.org/a/312537 "asciinema") 

* Εργαλεία που χρησιμοποίησα :
    * [Huginn](https://github.com/huginn/huginn "huginn")
___
    
  ### 5η Άσκηση : 

* Assignment : use the terminal as an IDE

* Deliverables : edit your files (e.g., cv, website, code, etc) in vim or emacs and compile it in a different panel or use a plug-in

* Περιγραφή : 'Εφερα' τον vim στα μέτρα και στις ανάγκες μου ώστε να τρέχει σαν IDE της python. Πιο συγκεκριμένα , κατεβασα τον vundler ο οποίος είναι vim plug-in manager  και στην συνέχεια κατέβασα διάφορα plugs-in , δηλαδή έκανα τον vim να προβάλει το αποτέλεσμα του κώδικα και μερικά απο τα errors του με το input στο πληκτρολογιο :  ``` \r ``` , επίσης έβαλα χρώματα , έκανα τον φόντο σαν του [sublime-text editor](https://www.sublimetext.com/) και το βήμα που με δυσκόλεψε τέρμα ήταν να βάλω autocomplete κάθε φορά που έγραφα κάτι που είχα ήδη γράψει ή καποία εντολή της python έβγαινε ένα drop-down menu που μπορώ με το <kbd>TAB</kbd> να διαλέξω την εντολή της επιλογής μου.

* Σύνδεσμος των εντολών στο [Asciinema](https://asciinema.org/a/314130 "asciinema") 

* Εργαλεία που χρησιμοποίησα :
    * [vim](https://www.vim.org/ "vim")

* Independencies που χρησιμοποίησα :
    * Το vim θα πρέπει να είναι πάνω απο την έκδοση 7.3 και να υποστηρίζει +python.
    * [pylint](https://www.pylint.org/)
    * [cmake](https://cmake.org/)
    * [mono-complete](https://www.mono-project.com/docs/getting-started/install/linux/)
    * [go](https://golang.org/doc/install)
    * [node.js](https://nodejs.org/en/download/package-manager/)
    
* Plug-in που χρησιμοποίησα :
    * [Vundler](https://github.com/VundleVim/Vundle.vim )
    * [python-mode](https://github.com/python-mode/python-mode)
    * [YouCompleteMe](https://github.com/ycm-core/YouCompleteMe)
    * [color scheme](https://github.com/jnurmine/Zenburn)
    * [flake8](https://github.com/nvie/vim-flake8)
    * [syntastic](https://github.com/vim-syntastic/syntastic)

  ## Συμμετοχικό εκπαιδευτικό υλικό : 
  
  # A) 
  
  * Ζητουμενα : δύο νέες εικόνες με λεζάντα και με ελεύθερα πνευματικά δικαιώματα ή που επιτρέπουν εμπορική χρήση π.χ., apple mouse, οι νέες εικόνες μπορούν να είναι παρόμοιες με υπάρχουσχες αρκεί να συνοδεύονται από τα κατάλληλα πνευματικά δικαιώματα. Εκτός από το αρχείο .md θα πρέπει να γίνει προσθήκη των αντίστοιχων εικόνων (μικρή εικόνα πλάτους 160πίξελ, και μια κανονική) στον φάκελο images, π.χ., προηγούμενη σωστή προσθήκη εικόνας από φοιτήτρια
  
  * link του αποθετήριου βιβλίου :
  * link του βιβλίου 
  * Αρχεία που άλλαξα : [_config.yml](https://github.com/geosideras/gr/blob/master/_config.yml) [3D-printer.md](https://github.com/geosideras/gr/blob/master/_gallery/3D-printer.md) [exoskeleton-glove.md](https://github.com/geosideras/gr/blob/master/_gallery/exoskeleton-glove.md) [3D-printer-thumb.png](https://github.com/geosideras/gr/blob/master/images/3D-printer-thumb.png) [3D-printer.png](https://github.com/geosideras/gr/blob/master/images/3D-printer.png) [exoskeleton-glove-thumb.jpg](https://github.com/geosideras/gr/blob/master/images/exoskeleton-glove-thumb.jpg) [exoskeleton-glove.jpg](https://github.com/geosideras/gr/blob/master/images/exoskeleton-glove.jpg)



