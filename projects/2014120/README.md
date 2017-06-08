# Τεχνολογία Λογισμικού

## 1)	Δήλωση και δέσμευση θέματος
*	**Ονοματεπώνυμο:** Ηρώ Σπύρου
*	**Αριθμός Μητρώου:** Π2014120
*	**Θέμα εργασίας:** "Δημιουργία Pacman"
*	**[Προσωπικό αποθετήριο κώδικα](https://github.com/irospyrou/pacman "Iro's Repository")**
*	**[Εκτελέσιμο](https://irospyrou.github.io/pacman/ "Iro's Pacman")**
* **[Github Page](https://irospyrou.github.io/Pacman_Anafora_2017/ "Iro's Final Report")**

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
 
## 4) Τελική αναφορά και έργο
### Προτεινόμενες αλλαγές:
  * Προσθήκη εχθρών.
  * Αντιμετώπιση εχθρών με την συλλογή του κατάλληλου αντικειμένου.
  * Δυνατότητα teleport για τον πρωταγωνιστή σε συγκεκριμένα σημεία της πίστας.

### Υλοποίηση:
  * Πρόσθεσα εχθρούς, συγκεκριμένα τα Goomba που είναι και οι εχθροί του Mario στο αυθεντικό παιχνίδι.
 ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/goomba.png "Goomba")
  
  * Πλέον, με την συλλογή των μανιταριών ο Mario αποκτά την δυνατότητα να αντιμετωπίσει τους εχθρούς του.
  * Πρόσθεσα σημεία στα οποία ο χαρακτήρας μας θα κάνει teleport προς την θέση εκκίνησης του χαρακτήρα, τα σημεία αυτά συμβολίζονται με μία πόρτα, όπως στο αυθεντικό παιχνίδι του Mario.
 ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/door.png "Door")
  
  * Επιπλέον, πρόσθεσα χρόνο στο παιχνίδι.
  * Τέλος πρόσθεσα και μία εικόνα background.
  
 ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/bg.png "Background")

### Αποτελέσματα:
 ![alt text](https://github.com/irospyrou/pacman/blob/master/assets/Screenshot3.png "Screenshot")
 
### Τελική αναφορά:
Η τελική αναφορά έγινε σε Github Pages, με Bonus 1 μονάδα.

**[Github Page](https://irospyrou.github.io/Pacman_Anafora_2017/ "Iro's Final Report")**
