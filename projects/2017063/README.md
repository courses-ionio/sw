# ***ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ ΙΟΝΙΟΥ ΠΑΝΕΠΙΣΤΗΜΙΟΥ***
## ***Τεχνολογία Λογισμικού***
### ***Αναφορά***

### ***Στοιχεία φοιτητή:*** 

Όνομα: Φουτσιτζή Σοφρονία

AM: Π2017063

### ***Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος***

   
   ### ***Άσκηση 1 "Send notifications to your desktop-mobile"***
   
   #### [Link για την άσκηση](https://asciinema.org/a/wZhReoAb7YDQq6O8ZlLZVWfbw)
   
   Για την υλοποίηση της συγκεκριμένης εργασίας χρησιμοποιήσα το [ntfy](https://github.com/dschep/ntfy), με την χρήση του οποίου μπορούσα "μέσα" από το terminal (με την χρήση command-line εντολών), να στείλω ειδοποιήσεις στην επιφάνεια εργασίας του υπολογιστή μου. Παράλληλα, με την χρήση του συγκεκριμένου προγράμματος κάθε φορά που υλοποιούσα με διεργασία που διαρκούσε παραπάνω από 10sec (πχ να ακτεβάσω μία εφαρμογή ή να χρησιμοποιήσω μία εφαρμογή πχ το asciinema) μου εμφάνιζε, αυτομάτως, ειδοποίηση.

                                      1.Αλλαγή του τιτλού/Αποστολή ειδοποίησης
![image](https://github.com/fsofronia/sw/blob/P2017063/projects/2017063/screen03.jpg)


 
                                 2.Ειδοποίση/Επιτυχία διεργασίας/Χρόνος διεργασίας   
![image](https://github.com/fsofronia/sw/blob/P2017063/projects/2017063/screen04.jpg)
   
   
   
   
    
    
    
    
### ***Άσκηση 2 "try different terminals and shells"***
   #### ***repeat some of the previous exercises with a different terminal-shell and create a custom configuration that fits your needs***
   
   #### [Link για την άσκηση](https://asciinema.org/a/oTJZq0Fe6blPNT40QYy13irV8)
   
   Για την υλοποίηση της συγκεκριμένης εργασίας χρησιμοποιήσα το [the simple (suckless) terminal](https://github.com/LukeSmithxyz/st) και [Z shell](https://en.wikipedia.org/wiki/Z_shell). 
   
   Με την χρήση του συγκεκριμένου κελιού και τερματικού αλλά και με την χρήση του το [imagemagick](https://www.howtogeek.com/109369/how-to-quickly-resize-convert-modify-images-from-the-linux-terminal/), εργαλείο το οποίο χρησιμοποίησα για την επεξεργασία εικόνων, υλοποίησα μία από τις προηγούμενες εργασίες και συγκεκριμένα την εργασία "batch image conversion (convert your image files to different sizes and formats)" από τα Πολυμέσα αλλάζοντας το format των φωτογραφιών και απο .jpg σε .jpeg. Με τη χρήση της εντολής `convert *jpg *jpeg` δημιουργήθηκαν στον φάκελο  τέσσερις νέες φωτογραφίες αντίγραφα των προηγούμενων αλλά και σε .jpeg (στον φάκελο υπάρχουν και οι εικόνες σε .jpg).

   Έπειτα, με την εντολή `mv *jpeg /root/Downloads/New` μεταφέρθηκαν οι φωτογραφίες σε κατάληξη .jpeg σε έναν άλλο φάκελο όπου και επεξεργάστηκαν οι διαστάσεις τους, συγκεκριμένα υλοποιήθηκε αλλαγή στο μέγεθος των εικόνων κατά 20% με την χρήση της εντολής ` convert *.jpeg -resize 20% NewImage.jpeg`. Τέλος, με την εντολή `identify *.jpeg ` εμφανίστηκαν οι πληροφορίες για όλες τις φωτογραφίες σε .jpeg που όπως φαίνεται είναι, πλεόν, οι διπλάσιες, καθώς υπάρχουν οι αρχικές εικόνες αλλά και τα αντίγραφα τους με όνομα NewImage-().jpeg, στις οποίες οι διαστάσεις τους έχουν διαμορφωθεί αντίστοιχα.

   
 - Η εμφάνιση του ονόματος του κελιόυ-shell που χρησιμοποίησα γίνεται με τη χρήση της εντολής: (Output: zsh)
 
        $ echo $0
  
  - Η εμφάνιση του ονόματος του τερματικού-terminal που χρησιμοποίησα γίνεται με τη χρήση της εντολής: (Output: st-256color)
         
        $ echo $TERM 


  ## Συμμετοχικό Υλικό- Α'Παραδοτέο
  
  [*Link του βιβλίου*](https://www.mibook.org/)
  
  [*Link του αντιγράφου του αποθετηρίου του βιβλίου*](https://github.com/fsofronia/gr/tree/master)
  
 
 #### [*Link της σελίδας μου*](https://fsofronia.github.io/gr/)
 
   Για την υλοποίηση της πρώτης εργασίας του συμμετοχικού υλικού ανάρτησα στο δικό μου αντίγραφο του αποθετηρίου του βιβλίου δύο εικόνες με λεζάντα που συνοδεύονται από τα κατάλληλα πνευματικά δικαιώματα. Η πρώτη εικόνα, αρχικά δημιουργήθηκε από διάφορες άλλες εικόνες με ελεύθερα πνευματικά δικαιώματα και απεικονίζει [shells](https://en.wikipedia.org/wiki/Unix_shell) για Linux. Το κέλυφος (shell) παρέχει μία διεπαφή command line για τον χρήστη σε λειτουργικά συστήματα τύπου Unix. Η δεύτερη εικόνα αναφέρεται σε ένα λογισμικό επεξεργασίας εικόνων το [ImageMagick](https://en.wikipedia.org/wiki/ImageMagick), με την χρήση του οποίου είναι εφικτή η επεξεργασία μιας εικόνας τόσο κατα μέγεθος, όσο κατά χρώμα, αλλά και μορφής(πχ από *.jpg σε *.png). Ωστόσο, το λογισμικό αυτό δεν έχει ένα ιδιαίτερα ίσχυρο γραφικό περιβάλλον, αντιθέτως για το χειρισμό των εικόνων χρησιμοποιεί command-line-interface.

  
* [Link πρώτης εικόνας/UnixShells](https://fsofronia.github.io/gr/gallery/shell/)
  
* [Link δεύτερης εικόνας/Imagemagick](https://fsofronia.github.io/gr/gallery/imagmagick/)
  

### ***Άσκηση 3 "set-up a system for python development"***
   #### ***install and configure in a user folder a python project that is not available through the package manager***
   
   #### [Link για την άσκηση](https://asciinema.org/a/Zv6sOUewENlvlqYaX7BMIArQm)
   
  Για την υλοποίηση της τρίτης εργασίας χρησιμοποίησα το [Pipenv](https://docs.python-guide.org/dev/virtualenvs/), με την χρήση του οποίου δημιούργησα ένα εικονικό περιβάλλον της python σε ένα directory και μέσα σε αυτό "έτρεξα" ένα πρόγραμμα της python. Στο σύνδεσμο που οδηγεί στην άσκηση φαίνεται τόσο η εγκατάσταση όσο και η εκτέλεση του προγράμματος.\
  
  
  ### ***Άσκηση 4 "use the terminal as an IDE"***
   #### ***edit your files (e.g., cv, website, code, etc) in vim or emacs and compile it in a different panel or use a plug-in***
   
   #### [Link για την άσκηση](https://asciinema.org/a/zLviqngSyDGLd3y7HwJHSxrrs)
   
  Για την υλοποίηση της τέταρτης εργασίας χρησιμοποίησα το [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor)), πάνω στο οποίο "πρόσθεσα" για να κάνω ελέγχους και να τρέξω τον κώδικα μου τα εξής:
  
  * [pylint](https://www.pylint.org/)
  * [python-mode](https://github.com/python-mode/python-mode)
  * [vim-flake8](https://github.com/nvie/vim-flake8)
  * [vim-syntastic](https://github.com/vim-syntastic/syntastic)
  
  
   ### ***Άσκηση 5 "performance monitoring"***
   #### ***monitor the performance of your python scripts and visualize them with colors and/or spark lines***
   
   #### [Link για την άσκηση](https://asciinema.org/a/7IrpoqsZXnNmE69gTdoIknAD5)
   
  Για την υλοποίηση της πέμπτης εργασίας χρησιμοποίησα το [hyperfine](https://github.com/sharkdp/hyperfine). Με την χρήση του συγκεκριμένου εργαλείου έτρεξα δύο προγράμματα python τα οποία με την βοήθεια του hyperfine χρονομέτρησα. Έπειτα, σύγκρινα μεταξύ τους τα δύο προγράμματα με την χρήση της εντολής:
  
          $ hyperfine --warmup 3 'python heapsort.py 100' 'python bubblesort.py 100'
          
 όπου μου εμφάνισε το κατά πόσο ήταν γρηγορότερο το ένα πρόγραμμα (εδω το πρώτο πρόγραμμα έτρεξε γρηγορότερα).
 Στην συνέχεια, έτρεξα ένα πρόγραμμα που μου εμφάνιζε ένα σφάλμα για να δείξω την χρήση του "-i" με το οποίο όταν έτρεξα το ίδιο πρόγραμμα δεν μου εμφάνισε τα σφάλματα.
 
 
   ### ***Άσκηση 6 "create your own static site and blog generator"***
   #### ***the generator should consider posts, pages, and templates***
   
   #### [Link για την άσκηση](https://asciinema.org/a/smRig3uSNNuwNxO9UhxjXSO3P)
   
  Για την υλοποίηση της πέμπτης εργασίας χρησιμοποίησα το [hugo](https://gohugo.io/). Με την χρήση του συγκεκριμένου εργαλείου δημιούργησα ένα στατικό σάιτ, το οποίο και επεξεργάστικα. Αρχικά, άλλαξα θέμα και έπειτα δημιούργησα το πρώτο που post, όπως φαίνεται παρακάτω.
 
 ![image]( https://github.com/fsofronia/sw/blob/P2017063/projects/2017063/hugo.png)
 
 
 
   ## Συμμετοχικό Υλικό- B'Παραδοτέο
  
  [*Link του βιβλίου*](https://www.mibook.org/)
  
  [*Link του αντιγράφου του αποθετηρίου του βιβλίου*](https://github.com/fsofronia/gr/tree/master)
  
 
 #### [*Link της σελίδας μου*](https://fsofronia.github.io/gr/)
 
   Για την υλοποίηση της δεύτερης εργασίας του συμμετοχικού υλικού ενσωμάτωσα μία νέα μελέτη περίπτωσης, τη μελέτη περίπτωσης σχετικά με το github. Το github είναι το εργαλείο το οποίο χρησιμοποιούμε για την υλοποίηση του μαθήματος "Τεχνολογία Λογισμικού" και είναι, επίσης, ένα εργαλείο που χρησιμοποιούν εκατομμύρια χρήστες/ προγραμματιστές ανα τον κόσμο. Είναι ιδιαίτερα σημαντικό, καθώς, προωθεί την συνεργασία διαφόρων προγραμματιστών και εταιρειών επάνω σε διάφορα projects. Παράλληλα, συνδιάζει πληθώρα χαρακτηριστικών τόσο command line όσο και με γραφικό περιβάλλον, θυμίζοντας αρκετά ένα μέσο κοινωνικής δικτύωσης.

  
 [Link μελέτης περίπτωσης/Github](https://fsofronia.github.io/gr/case-study/github/)
 
 Για την τεκμηρίωση της εργασίας συμμετοχικού περιεχομένου και της συγκεκριμένης μελέτης περίπτωσης χρησιμοποίησα διάφορες εικόνες που είτε προυπήρχαν είτε τις πρόσθεσα για την ολοκλήρωση της εργασίας. Συγκεκριμένα, χρησιμοποίησα την εικόνα που αναφέρεται ως [Github Contributions](https://fsofronia.github.io/gr/gallery/github-contributions/) και ως [Github Profile](https://fsofronia.github.io/gr/gallery/github-profile/), οι οποίες προυπήρχαν στο βιβλίο. Ωστόσο, πρόσθεσα και μία εικόνα που αναφέρεται ως [github repository](https://fsofronia.github.io/gr/gallery/repository/) και περιγράφει την έννοια και τα περιεχόμενα του εκάστοτε αποθετηρίου.


 ## Πρόσθετες εργασίες αντί για τελική εξέταση 
 
 ### Eργασία συμμετοχικού περιεχομένου
 
   Για την υλοποίηση της πρόσθετης εργασίας συμμετοχικού περιεχομένου, υλοποίησα μία βιογραφία. Συγκεκριμένα, υλοποίησα την βιογραφία του Linus Benedict Torvalds, ιδρυτή του πυρήνα των Linux άλλα και του Git, το οποίο είναι ένα command-line εργαλείο που χρησιμοποιείται στο Github, το οποίο έχω μελετήσει στην παραπάνω εργασία συμμετοχικού περιεχομένου.
  
 [Link βιογραφίας/ Linus Torvalds](https://fsofronia.github.io/gr/biography/Linus-Torvalds/)

Για την υλοποίηση της εργασίας παράλληλα χρησιμοποίησα και διάφορες εικόνες που προυπήρχαν ήδη στο mibook όπως την εικόνα από το λειτουργικό σύστημα των [Linux](https://fsofronia.github.io/gr/gallery/linux/). Επίσης, πρόσθεσα δύο εικόνες μία που αφορά το [Git](https://fsofronia.github.io/gr/gallery/git/), και μία για τον άνθρωπο που αναφέρεται στην παραπάνω βιογραφία τον [Linus Torvalds](https://fsofronia.github.io/gr/gallery/LinusTorvalds/).
 
 

