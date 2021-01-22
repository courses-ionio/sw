# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ
# ΜΑΘΗΜΑ Τεχνολογία Λογισμικού

### Στοιχεία φοιτητή

Νίκος Τζιάνας

ΑΜ: Π2014107


# Σύνοψη

Για την τελική βαθμολόγηση υλοποιήθηκαν 5 ασκήσεις λογισμικού , το βιογραφικό καθώς και οι ασκήσεις συμμετοχικού εκπαιδευτικού υλικού


- [Βιογραφικό](#βιογραφικό)
- [dokey](#dokey)
  - [1.Virtual Environment](virtual-environment)
  - [Άσκηση 2](άσκηση-2)  
  - [Άσκηση 3](άσκηση-3)  
  - [Άσκηση 4](άσκηση-4)  
  - [Άσκηση 5](άσκηση-5)
 






# Βιογραφικό

### Links

- [repository](https://github.com/aMimikyu/simple-cv)
- [βιογραφικό](https://amimikyu.github.io/simple-cv/)
- [pdf](https://amimikyu.github.io/simple-cv/nikos-tzianas-cv.pdf)
- [asciinema](https://asciinema.org/a/885P8rQP7OzpKlueZNWHye4Vq)

### Περιγραφή
Για την υλοποίηση του βιογραφικού επιλέχθηκε ένα προτεινόμενα themes της εργασίας.
Καθώς θεώρησα πως τα default sections του βιογραφικού ήταν περιορισμένα δημιούργησα νέα sections κάνοντας τα αντίστοιχα markdown files με τις πληροφορίες που ήθελα να συμπεριλάβω.
Επίσης άλλαξα το font του βιογραφικού.

Το βιογραφικό γίνεται edit τοπικά και push στο remote repository όπου γίνονται οι αλλαγές και δημιουργείται το αντίστοιχο pdf. 

### Δυσκολίες

Αρχικά είχα επιλέξει ένα διαφορετικό theme αλλά δυσκολεύτηκα στο να δημιουργήσω LaTeX theme που να μοιάζει στο theme της ιστοσελίδας.
Τελικά δεν κατάφερα να το ολοκληρώσω και επέλεξα ένα theme που δημιουργεί αυτόματα το LaTex.

# Dokey

## Virtual Environment

**Τίτλος** : set-up a system for python development

**Περιγραφή** : install and configure in a user folder a python project that is not available through the package manager	

**asciinema** : [link](https://asciinema.org/a/JwqeEQvIJ18mt319x0CEKkUV0)

**References** : [pipenv](https://github.com/pypa/pipenv)

Για την συγκεκριμένη άσκηση δημιούργησα ένα virtual environment πάνω σε ένα project που έτρεχα ήδη.
Εκεί έκανα install τοπικά κάποιες βιβλιοθήκες και έτρεξα τον κώδικα.
Η συγκεκριμένη άσκηση με βοήθησε αρκετά γιατί όπως έδειξα και στο asciinema είχα περισσοτερα packages από όσο θα έπρεπε και όλα installed globally.
Το pipenv είναι ένα εργαλείο που βοήθησε αρκετά στο encapsulation του κώδικα.

## Notifications

**Τίτλος** : send notifications to your desktop-mobile	

**Περιγραφή** : send a notifcation when a big task completes, eg download, compiling, etc		

**asciinema** : [link](https://asciinema.org/a/JwqeEQvIJ18mt319x0CEKkUV0)

**References** : [pushbullet](https://docs.pushbullet.com/)


Για αυτήν την άσκηση δημιούργησα ένα μικρό script που χρησιμοποιεί το api του pushbullet για να στέλνει notification στο κινητό μου.
Για να το χρησιμοποιήσω τρέχω μια εντολή για την οποία θέλω να ειδοποιηθώ και κάνω append το execution του script. Έτσι όταν τελειώσει η εντολή έρχεται η ειδοποίηση.

Η ειδοποίηση του asciinema:

![screenshot](https://i.imgur.com/HtRnQti.png)



