# Τεχνολογία Λογισμικού

## 1)	Δήλωση και δέσμευση θέματος
*	**Ονοματεπώνυμο:** Ηρώ Σπύρου
*	**Αριθμός Μητρώου:** Π2014120
*	**Θέμα εργασίας:** "Δημιουργία Pacman"
*	**[Προσωπικό αποθετήριο κώδικα](https://github.com/irospyrou/pacman "Iro's Repository")**
*	**[Εκτελέσιμο](https://irospyrou.github.io/pacman/ "Iro's Pacman")**

## 2)	Aρχικός σχεδιασμός εφαρμογής
### Ζητούμενα:
  *	Αντί για τον Pacman χρησιμοποίησε έναν άλλο χαρακτήρα για πρωταγωνιστή του παιχνιδιού.
  *	Αντί ο πρωταγωνιστής να μαζεύει μόνο dots θα μπορούσε να μαζεύει διάφορα αντικείμενα (κέρματα, λουλούδια, φρούτα κτλ).
  *	Δημιούργησε μια νέα πίστα για το παιχνίδι χρησιμοποιώντας το Tiled.

### Υλοποίηση:
  * Αντικατέστησα τον χαρακτήρα του Pacman με τον χαρακτήρα του Mario.
  ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/mario2.png "Mario")
  * Πλέον, ο πρωταγωνιστής του παιχνιδιού δεν μαζεύει dots, αλλά μαζεύει κέρματα (coins), όπως κάνει και στο αυθεντικό παιχνίδι του Mario.
  ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/coin1.png "Coins")
  * Δημιούργησα μια νέα πίστα με βάση την πίστα που υπήρχε στον φάκελο assets.
  ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/pacman-map1.png "Level1")

### Αποτέλεσματα:
 ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/Screenshot.png "Screenshot")
 
## 3) Τελικό προσχέδιο έργου για σχολιασμό και βελτιώσεις 
### Ζητούμενα:
  * Προσθήκη αντικειμένου που εμφανίζεται και μετά από κάποιο χρονικό διάστημα εξαφανίζεται.
  * Προσθήκη score, bonus και ζωών.
  * Προσθήκη ήχων.
  
### Υλοποίηση:
  * Πρόσθεσα στην κάτω αριστερή γωνία ένα μανιτάρι, το οποίο εξαφανίζεται μετα από ορισμένο χρονικό διάστημα.
  * Πρόσθεσα score, το οποίο αυξάνεται κατά ένα κάθε φορά που ο Mario τρώει ένα κέρμα. 
  * Πρόσθεσα επίσης bonus, τα οποία συμβολίζονται από μανιτάρια στην πίστα του παιχνιδιού, με τα οποία σε επόμενο παραδοτέο θα μπορεί να τρώει τους εχθρούς που θα προστεθούν.
  ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/mushroom1.png "Mushrooms")
  * Επιπλέον έχουν προστεθεί 3 ζωές, τις οποίες συμβολίζω με αστέρια, οι οποίες θα χάνονται αν κάποιος εχθρός που θα προστεθεί φάει τον Mario.
  ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/star2.png "Stars")
  * Τέλος, έχω προσθέσει το theme song του Mario, έναν ήχο όταν τρώει νομίσματα και έναν ξεχωριστό ήχο για όταν τρώει μανιτάρια.

### Αποτελέσματα:
 ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/Screenshot2.png "Screenshot")
