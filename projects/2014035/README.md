**Ονοματεπώνυμο: Μιχαήλ- Χρυσοβαλάντης Παγκρακιώτης**

**Αριθμός Μητρώου: Π2014035**

**Links:**
* [Link Προσωπικού Αποθετηρίου](https://github.com/Mikepag/pacman).
* [Link Εκτελέσιμου](https://mikepag.github.io/pacman/pacman.html).
* [Link Τελικής Αναφοράς](https://mikepag.github.io/pacman/) σε μορφή GitHub Pages **_(Bonus1, 1 μονάδα)_**.
_________________________
## Παραδοτέο 1 - Δήλωση και δέσμευση θέματος, 20 Φεβρουαρίου
Θέμα εργασίας: **Pacman**
_________________________
## Παραδοτέο 2

**Οι αλλαγές που έγιναν είναι οι εξής:**
* Αλλαγή του Pacman με άλλον χαρακτήρα (Κάβουρας), μεσω αντικατάστασης της εικόνας pacman.png στον φάκελο assets. Η εικόνα δεν βρέθηκε έτοιμη αλλά επεξεργάστηκε ώστε να λειτουργεί σωστά το animation και να φαίνεται ότι ο κάβουρας κινεί τα πόδια του και ανοιγο-κλείνει τις δαγκάνες του. Επίσης έγινε αλλαγή στο χρώμα.
* Αλλαγή των dots με άλλη εικόνα (Πλανγκτόν), μέσω αντικατάστασης της εικόνας dots.png στον φάκελο assets.
* Δημιουργία νέας πίστας με το Tiled, κάνοντας χρήση της υπάρχουσας πίστας (pacman-map.json) καθώς και των πλακιδίων (pacman-tiles.png), στα οποία όμως πρώτα έγινε αλλαγή του χρώματος.

**Βιβλιογραφία:**
* Η τελική εικόνα pacman.png προέκυψε από επεξεργασία της εικόνας: https://goo.gl/HH3fTi
* Η εικόνα dots.png είναι η εικόνα: https://goo.gl/O048qq
_________________________
## Παραδοτέο 3

**Οι προσθήκες που έγιναν είναι οι εξής:**
* Προσθήκη Score.
* Προσθήκη Lives.
* Προσθήκη Bonus:
   1. Τροποποίηση εικόνας pacman-tiles για να προστεθεί καινούριο πλακίδιο (Burger).
   2. Προσθήκη του καινούριου πλακιδίου στον χάρτη pacman-map.json.
   3. Προσθήκη μικρού τμήματος κώδικα στο pacman.html ώστε να γίνεται ψευδοτυχαία εμφάνιση/απόκρυψη των bonus πλακιδίων.
   4. Τροποποίηση κώδικα ώστε κάθε φορά που ο Pacman τρώει ένα burger το score να αυξάνεται κατά πενήντα (50) μονάδες, αντί για πέντε (5) που αυξάνεται όταν τρώει ένα απλό dot.
 * Προσθήκη ήχων:
   1. Ήχος background.
   2. Ηχητικό εφέ κάθε φορά που ο Pacman τρώει ένα dot.
   3. Ηχητικό εφέ κάθε φορά που ο Pacman τρώει ένα burger.

**Βιβλιογραφία:**
* SuperMarioFireFlowerSoundFX: https://www.youtube.com/watch?v=bGdCgkQYBTo
* SuperMarioPipeTravelSoundFX: https://www.youtube.com/watch?v=Q8ukcO_Oc8s
* TheChainsmokersAllWeKnow8Bit: https://www.youtube.com/watch?v=AIimEDlIaG0
* Brgr.png: http://www.pngall.com/wp-content/uploads/2016/03/Food.png

_________________________
_________________________
## Παραδοτέο 4 - ΤΕΛΙΚΗ ΑΝΑΦΟΡΑ
**Ονοματεπώνυμο: Μιχαήλ- Χρυσοβαλάντης Παγκρακιώτης**

**Αριθμός Μητρώου: Π2014035**

**Links:**
* [Link Προσωπικού Αποθετηρίου](https://github.com/Mikepag/pacman).
* [Link Εκτελέσιμου](https://mikepag.github.io/pacman/pacman.html).
* [Link Τελικής Αναφοράς](https://mikepag.github.io/pacman/) σε μορφή GitHub Pages **_(Bonus1, 1 μονάδα)_**.

### Tίτλος Εργασίας: *Δημιουργία Pacman*

### Εισαγωγή
Σκοπός της εργασίας ήταν η επέκταση υπάρχουσας έκδοσης του παιχνιδιού Pacman με τη χρήση της γλώσσας HTML5 και τη βοήθεια της βιβλιοθήκης Phaser, παράλληλα με τον στόχο του μαθήματος που ήταν η εξάσκηση στην σχεδίαση και την ανάπτυξη λογισμικού.

### Επιλογή Εργαλείων 
**Τα εργαλεία που χρησιμοποιήθηκαν ήταν τα εξής:**
* **Tiled**, για την δημιουργία νέας πίστας η οποία είναι βασισμένη στην προϋπάρχουσα (pacman-map.json).
* **Microsoft Paint**, για την επεξεργασία των εικόνων pacman.png, pacman-tiles.png. 
* **Adobe Photoshop CS6 Portable**, για την επεξεργασία των εικόνων pacman.png, pacman-tiles.png, dots.png.
* **Sublime Text 3**, για την επεξεργασία του HTML5 κώδικα.
* **XAMPP**, για την εκτέλεση του κώδικα τοπικά στον προσωπικό μου υπολογιστή.

### Διαδικασία Ανάπτυξης
**Προκειμένου να φτάσει στη τελική της μορφή η εργασία έγιναν οι παρακάτω ενέργειες:**
* Αρχικά έγινε fork στο κεντρικό αποθετήριο του project όπου υπήρχε έτοιμο σε πρώιμο στάδιο το παιχνίδι.
* Αντικατάσταση της εικόνας [pacman.png](https://github.com/Mikepag/pacman/blob/master/assets/pacman.png) από νέα. Η καινούρια εικόνα επεξεργάστηκε στο paint ώστε να χωριστεί σε 3 στιγμιότυπα (για το animation) και μέσω του photoshop έγινε το resize στις επιθυμητές διαστάσεις και αποθηκεύτηκε σε format PNG.
* Αντικατάσταση της εικόνας [dot.png](https://github.com/Mikepag/pacman/blob/master/assets/dot.png). Στη νέα εικόνα έγινε resize στις επιθυμητές διαστάσεις καθώς και αποθήκευση σε format PNG μέσω του Photoshop.
* Δημιουργία νέας πίστας με το Tiled, κάνοντας χρήση της υπάρχουσας πίστας [pacman-map.json](https://github.com/Mikepag/pacman/blob/master/assets/pacman-map.json) καθώς και των πλακιδίων [pacman-tiles.png](https://github.com/Mikepag/pacman/blob/master/assets/pacman-tiles.png), στα οποία όμως πρώτα έγινε αλλαγή του χρώματος.
* Προσθήκη [κώδικα](https://github.com/Mikepag/pacman/blob/master/pacman.html) για την προβολή Score. Το score αρχικά είναι μηδέν (0) και κάθε φορά που ο Pacman "τρώει" ένα dot το score αυξάνεται κατά πέντε (5) μονάδες.
* Προσθήκη [κώδικα](https://github.com/Mikepag/pacman/blob/master/pacman.html) για την προβολή Lives. Αρχικά οι ζωές είναι τρείς (3). (Δεν αναπτύχθηκε λειτουργία που να αυξάνει ή να μειώνει αυτή τη μεταβλητή).
* Προσθήκη Bonus:
	1. Τροποποίηση εικόνας [pacman-tiles.png](https://github.com/Mikepag/pacman/blob/master/assets/pacman-tiles.png) για να προστεθεί καινούριο πλακίδιο (Burger).
	2. Προσθήκη του καινούριου πλακιδίου στον χάρτη [pacman-map.json](https://github.com/Mikepag/pacman/blob/master/assets/pacman-map.json).
	3. Προσθήκη μικρού τμήματος κώδικα στο [pacman.html](https://github.com/Mikepag/pacman/blob/master/pacman.html) ώστε να γίνεται ψευδοτυχαία εμφάνιση/απόκρυψη των bonus πλακιδίων.
	4. Τροποποίηση [κώδικα](https://github.com/Mikepag/pacman/blob/master/pacman.html) ώστε κάθε φορά που ο Pacman τρώει ένα burger το Score να αυξάνεται κατά πενήντα (50) μονάδες, αντί για πέντε (5) που αυξάνεται όταν τρώει ένα απλό dot.
* Προσθήκη ήχων:
	1. [Ήχος background](https://github.com/Mikepag/pacman/blob/master/assets/TheChainsmokersAllWeKnow8Bit.mp3).
	2. [Ηχητικό εφέ](https://github.com/Mikepag/pacman/blob/master/assets/SuperMarioFireFlowerSoundFX.mp3) κάθε φορά που ο Pacman τρώει ένα dot.
	3. [Ηχητικό εφέ](https://github.com/Mikepag/pacman/blob/master/assets/SuperMarioPipeTravelSoundFX.mp3) κάθε φορά που ο Pacman τρώει ένα burger.
 
### Ενδεικτικές Εικόνες
* Πριν την εμφάνιση των Bonus:
![s1](https://cloud.githubusercontent.com/assets/15000701/26785919/5f5ceb18-4a0d-11e7-891a-315c3455cfc2.JPG) 

* Μετά την εμφάνιση των Bonus:
![s2](https://cloud.githubusercontent.com/assets/15000701/26785918/5f5aa3ee-4a0d-11e7-9e59-264422423fe8.JPG)

### Βιβλιογραφία
* [Κεντρικό αποθετήριο project](https://github.com/ioniodi/pacman) από το οποίο δημιουργήθηκε αντίγραφο (fork).
* Η τελική εικόνα [pacman.png](https://github.com/Mikepag/pacman/blob/master/assets/pacman.png) προέκυψε από επεξεργασία της εικόνας: [https://goo.gl/HH3fTi](https://goo.gl/HH3fTi).
* [ https://goo.gl/O048qq]( https://goo.gl/O048qq): Εικόνα [Dot.png](https://github.com/Mikepag/pacman/blob/master/assets/dot.png).
* [https://goo.gl/RbVHBC](https://goo.gl/RbVHBC): Εικόνα [Brgr.png](https://github.com/Mikepag/pacman/blob/master/assets/brgr.png).
* [https://goo.gl/z9tmnP](https://goo.gl/z9tmnP): Ηχητικό Εφέ [SuperMarioFireFlowerSoundFX.mp3](https://github.com/Mikepag/pacman/blob/master/assets/SuperMarioFireFlowerSoundFX.mp3).
* [https://goo.gl/PPpNPE](https://goo.gl/PPpNPE): Ηχητικό Εφέ [SuperMarioPipeTravelSoundFX.mp3](https://github.com/Mikepag/pacman/blob/master/assets/SuperMarioPipeTravelSoundFX.mp3).
* [https://goo.gl/ceqL9Y](https://goo.gl/ceqL9Y): Ήχος Background [TheChainsmokersAllWeKnow8Bit.mp3](https://github.com/Mikepag/pacman/blob/master/assets/TheChainsmokersAllWeKnow8Bit.mp3).
  
### Συμπεράσματα
Η εργασία αυτή αποτέλεσε έναν δημιουργικό και πολύ ενδιαφέρων τρόπο ενασχόλησης με τη γλώσσα HTML5, τη βιβλιοθήκη Phaser και τo Github για την ανάπτυξη μιας ψυχαγωγικής εφαρμογής. Η τελική μορφή του παιχνιδιού μπορεί να μην είναι η βέλτιστη δυνατή αλλά δεν παύει να είναι αρκετά λειτουργική και φυσικά αφήνει πολλά περιθώρια μελλοντικής βελτίωσης.
