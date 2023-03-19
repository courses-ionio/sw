# <h1 align="center">Τεχνολογία Λογισμικού</h1>

<h3> Ονοματεπώνυμο: Αλεξοπούλου Ολυμπία-Στεργιανή</h3>
<h3> Αριθμός Μητρώου: Π2019166 </h3>
<h3>Email : p19alex@ionio.gr</h3>
<h3>My github account : https://github.com/olumpiaalexopoulou</h3>
<h3>My organization : https://github.com/Ranger-Power</h3>


| Εβδομάδα | [Όλα τα παραδοτέα βρίσκονται στην ίδια σελίδα της τελικής αναφοράς](https://epidrome.github.io/teaching/deliverables/) με τα προσωπικά στοιχεία σας (Όνομα, ΑΜ, github profile) και μαζί με αυτόν εδώ τον πίνακα περιεχομένων | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | [Δημιουργία ομάδας](https://epidrome.github.io/teaching/team/) + [Φορκ και δημιουργία σελίδας τελικής αναφοράς](https://epidrome.github.io/teaching/guide/), [προσθήκη πίνακα περιεχομένων](https://raw.githubusercontent.com/courses-ionio/sw/master/README.md), [συγγραφή της εισαγωγής](https://epidrome.github.io/teaching/intro/), αποστολή της εισαγωγής [για σχολιασμό στην συζήτηση](https://github.com/courses-ionio/sw/discussions/categories/show-and-tell) και καταγραφή του συνδέσμου συζήτησης δίπλα --> | [My link](https://github.com/courses-ionio/sw/discussions/1160) | |
| 2 | Γραμμή εντολών (systemd) και διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας | [My link](https://github.com/courses-ionio/sw/discussions/1258)| |
| 3 | Γραμμή εντολών (no systemd) | [My link](https://github.com/courses-ionio/sw/discussions/1316)| |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά) | [My link](https://github.com/courses-ionio/sw/discussions/1366)| |
| 5 | Συμμετοχικό περιεχόμενο A1 + A2 | [My link](https://github.com/courses-ionio/sw/discussions/1438) | |
| 6 | Γραμμή εντολών (custom static blog generator) | | |
| 7 | συμμετοχικό περιεχόμενο B1 | | |
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) | | |
| 9 | συμμετοχικό περιεχόμενο B2 | | |
| 10 | Τελική αναφορά* | | |

# <h2>Εισαγωγή</h2>

Στο μάθημα Τεχνολογία Λογισμικού σκοπός μου είναι να αποσκοπήσω όσα πιο πολλά και ενδιαφέροντα πράγματα μπορεί να μου προσφέρει. Αρχικά, θα προσπαθήσω να ανταπεξέλθω στην ολοκλήρωση όλων των παραδοτέων με αποτέλεσμα να μπορώ να χειρίζομαι καλύτερα τα συστήματα Unix. Η παρακολούθηση των εβδομαδιαίων βίντεο κουίζ έχει ως αποτέλεσμα την εκμάθηση και κατανόηση πολλών πληροφοριών οι οποίες είναι απαραίτητο να γνωρίζουμε. Ακόμη, το ομαδικό πνεύμα είναι πολύ χρήσιμο στο μάθημα και θα βοηθήσει η συμμετοχή μου σε μία ομάδα. Ως θέμα της αναφοράς μου αποφάσισα να επιλέξω την εκμάθηση με χρήση διαδραστικών μέσων, αφού αυτή την περίοδο παρακολουθώ διαδικτυακά μαθήματα ξένης γλώσσας. Πιστεύω πως μπορεί να γίνει καλύτερη διδασκαλία και σε αυτό θα βοηθούσε η συγκέντρωση πληροφοριών από καινούργια και πιο διαδραστικά συστήματα. Τέλος, θεωρώ πως έχω κάνει μία καλή αρχή με το προηγούμενο μάθημα το HCI, το οποίο με έχει βοηθήσει στη εξοικείωση μου με τα συστήματα και μου έχει προσφέρει πολλά προνόμια, αλλά πιστεύω πως και μετά την ολοκλήρωση του μαθήματος SW θα είναι πιο ολοκληρωμένες οι γνώσεις μου.

# <h2>Γραμμή εντολών με systemd</h2>

Για την ολοκλήρωση αυτού του παραδοτέου χρησιμοποίησα το ntfy ώστε να στείλω ένα notification στο κινητό μου για τον υπολογισμό της ώρας μέσα από ένα python script που έτρεξα. 
Το αποτέλεσμα φαίνεται στο παρακάτω link :
  - [Asciinema Link](https://asciinema.org/a/YTnQ5e1akGJ1DMFek5sILKho9)
  
Και ακολουθεί και το screenshot από το κινητό μου μέσω της εφαρμογής ntfy :


![ntfyphoto](https://user-images.githubusercontent.com/72515404/221370295-c61cf5a7-2b45-4205-9938-df955b8d414c.jpg)


Στο πρόγραμμα που πραγματοποίησα αρχικά έκανα import την βιβλιοθήκη requests και μέσα από μία μέθοδο post σύνδεσα με το ntfy και επέλεξα ποιο θα είναι το μήνυμα που θα εμφανίζει στο notification και ποιος ο τίτλος. Έπειτα για τον υπολογισμό και την εμφάνιση της ώρας αρχικοποίησα μία αρχική τιμή στην ώρα και τα λεπτά ώστε να κάνω από κάτω τους υπολογισμούς και να βγει η σωστή ώρα. Τέλος, μέσω μίας εντολής print εμφάνισα την ώρα στο τερματικό όπως φαίνεται στο [Asciinema Link](https://asciinema.org/a/YTnQ5e1akGJ1DMFek5sILKho9).

Στο παρακάτω Link σας δείχνω με τη χρήση του neofetch τις πληροφορίες του συστήματος :
  - [Neofetch link](https://asciinema.org/a/P54gU7mXHLrSRme4dWjWAUVlH)

# <h2>Γραμμή εντολών χωρίς systemd</h2>

Σε αυτό το παραδοτέο εγκατέστησα το Alpine Linux το οποίο δεν περιέχει systemd αλλά openrc.

Το οποίο φαίνεται στο παρακάτω link στο asciinema :

  - [Asciinema Link](https://asciinema.org/a/16dpc2BwBj86Ldo5M9nq0vPzX)
  
# <h2>Κατασκευή του βιβλίου Α2</h2>

Στο κεφάλαιο 10 (Τεχνολογία) στην σελίδα 161 του βιβλίου σας αναφέρει πως τα μέσα επικοινωνίας βοηθάνε στην ανταλλαγή μηνυμάτων μεταξύ των ανθρώπων και δίνει ένα παράδειγμα του ραδιοφώνου που η εξέλιξη του είναι η τηλεόραση την οποια ονομάζει "ραδιόφωνο με εικόνα". Έτσι αποφάσισα να δώσω και εγώ ένα παράδειγμα που έχει σχέση με την επικοινωνία των ανθρώπων μέσω βιντεοκλήσης η οποία είναι εξέλιξη της ηχητικής κλήσης. Στο συμπέρασμα που κατέληξα είναι πως πλέον με την εξέλιξη της τεχνολογίας μπορείς να επικοινωνείς με ανθρώπους ασχέτως την τοποθεσία που βρίσκονται και με πολύ διαδραστικό τρόπο. Την χρήση βιντεοκλήσης χρησιμοποιώ και εγώ στα διαδικτυακά μαθήματα που παρακολουθώ.

Το screenshot της προσθήκης μου :

![img](https://user-images.githubusercontent.com/72515404/224086897-da5d4768-de9f-4562-99cd-cfca195f66a5.png)

My Links :
  - [my book](https://github.com/olumpiaalexopoulou/kallipos/tree/master/book)
  - [my lua](https://github.com/olumpiaalexopoulou/kallipos/blob/master/media.lua)
  - [my make-latex.sh](https://github.com/olumpiaalexopoulou/kallipos/blob/master/make-latex.sh)
  - [my screenshot](https://github.com/olumpiaalexopoulou/kallipos/blob/master/pictures/img.png)
  
  Δυστυχώς, στη δημιουργία του βιβλίου το πρόβλημα που αντιμετώπισα ήταν ότι δεν μου εμφανίζει τις εικόνες με αποτέλεσμα οι σελίδες να είναι 177 και δεν κατάφερα να βρω κάποια λύση σε αυτό αλλά θα προσπαθήσω να το διορθώσω!

# <h2>Συμμετοχικό περιεχόμενο A1 + A2</h2>

Σε αυτό το παραδοτέο επέλεξα να προσθέσω στο site, δύο εφαρμογές τηλεδιάσκεψης, το "Zoom" και το "Skype". Αυτές οι εφαρμογές είναι χρήσιμες για την ζωντανή επικοινωνία των ανθρώπων, μέσω βιντεοκλήσης. Μία από τις διαφορές μεταξύ τους είναι πως το Skype σου επιτρέπει κλήσεις χωρίς χρέωση για 24 ώρες, ενώ το Zoom σου επιτρέπει να κάνεις κλήσεις για 40 λεπτά εάν δεν έχεις πληρώσει, αν πληρώσεις σου επιτρέπει 30 ώρες. Επιπλέον, στο Zoom επιτρέπετε μέχρι 1.000 άτομα σε μία κλήση ενώ στο Skype μέχρι 100 άτομα. Γενικά, αυτές οι εφαρμογές ενώ δημιουργήθηκαν για τον ίδιο σκοπό, έχουν σημαντικές διαφορές. 

  - [My netlify link](https://olumpiaalexopoulou.netlify.app/)
  
  | _gallery | images | _timeline | _slides | 
| --- | --- | --- | --- | 
| [Skype.md](https://github.com/olumpiaalexopoulou/_gallery/blob/master/skype-to-skype.md)| [skype](https://github.com/olumpiaalexopoulou/images/blob/master/skype-to-skype.jpg) | [Timeline Netlify](https://olumpiaalexopoulou.netlify.app//timeline/os-apps/) |   |
| [Zoom.md](https://github.com/olumpiaalexopoulou/_gallery/blob/master/zoom.md) | [zoom](https://github.com/olumpiaalexopoulou/images/blob/master/zoom.jpg) |  | |
|[Zoom Netlify](https://olumpiaalexopoulou.netlify.app//gallery/zoom/)|  [skype-thumb](https://github.com/olumpiaalexopoulou/images/blob/master/skype-to-skype-thumb.jpg)|    |        |
|[Skype Netlify](https://olumpiaalexopoulou.netlify.app//gallery/skype-to-skype/)|  [zoom-thumb](https://github.com/olumpiaalexopoulou/images/blob/master/zoom-thumb.jpg)      |     |  [Slides Netlify](https://olumpiaalexopoulou.netlify.app//slides/iui/)   | 

# <h2 align="center">Βίντεο Κουίζ</h2>

| - | Τίτλος | Πραγματοποιήθηκαν | Εμπρόθεσμα |
| ---- | ---- | ---- | ---- |
| 1 | Alan Kay at MIT-EECS 1998 Fall Semester Colloquium Series (VPRI 834) |  :+1:  | :+1: | 
| 2 | Ted Nelson -- Computers for Cynics [full version] |  :+1:  | :+1: | 
| 3 | Alan Kay - Could Computing Be Simpler Than It Seems To Be? |  :+1:  | :+1: | 
| 4 | Bret Victor - The Future of Programming  |  :+1:  | :+1: | 
| 5 | Alan Kay - Programming Languages & Programming (2013)  |  :+1:  | :+1: | 
