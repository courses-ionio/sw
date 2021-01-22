# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ
# ΜΑΘΗΜΑ Τεχνολογία Λογισμικού

### Στοιχεία φοιτητή

Νίκος Τζιάνας

ΑΜ: Π2014107


# Σύνοψη

Για την τελική βαθμολόγηση υλοποιήθηκαν 5 ασκήσεις λογισμικού , το βιογραφικό καθώς και οι ασκήσεις συμμετοχικού εκπαιδευτικού υλικού


- [Βιογραφικό](#βιογραφικό)
- [dokey](#dokey)
  - [1.Virtual Environment](#virtual-environment)
  - [2. Notifications](#notifications)  
  - [3. Performance Monitoring](#performance-monitoring)  
  - [4. Custom Window Manager](#custom-window-manager)  
  - [5-6. Static Site && CI](#create-static-site-and-continuous-integration)
 






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


## Performance Monitoring

**Τίτλος** : Performance Monitoring	

**Περιγραφή** : monitor the performance of your python scripts and visualize them with colors and/or spark lines	

**References** : [py-spy](https://github.com/benfred/py-spy),[hyperfine](https://github.com/sharkdp/hyperfine)

Για το  performance monitoring δοκίμασα δύο διαφορετικούς τρόπους.
Ένα είναι το hyperfine.

Αφού το κατέβασα απλά το έτρεξα με το script που θέλω να κάνω monitor.

```
$ hyperfine --export-markdown results.md 'python ais_to_csv.py'
```

Τα αποτελέσματα φαίνονται εδώ: 

![results](https://i.imgur.com/zGfOumC.png)

Το hyperfine είναι αρκετά χρήσιμο για να βγάλει το expected runtime από ένα πρόγραμμα και να μετρήσουμε την απόδοση. 

Ένα άλλο εργαλείο  που δοκίμασα είναι το py-spy. Το py-spy βοηθάει να βρούμε την εντολή που ξοδεύει τον περισσότερο χρόνο.
Καθώς τρέχει ταξινομεί τις εντολές που έχουν περάσει βάση του πόσο χρόνου έχουν χρειαστεί μέχρι τώρα.


![results2](https://i.imgur.com/sgSSJKY.png)

[example-vid](https://streamable.com/ky8l38)


## Custom Window Manager


**Τίτλος** : configure a custom window manager		

**Περιγραφή** : try different wm and configure one to fit your needs	

**References** : [i3wm](https://i3wm.org/)

Για αυτήν την άσκηση επέλεξα έναν tiling window manager, τον i3.
Έκανα κάποια βασικά configurations και δοκίμασα τον δοκίμασα.

[example-gif](https://imgur.com/vxx1a5X)


## Create Static Site and continuous integration


**Τίτλος** : create your own static site and blog generator,  set-up continuous integration	

**References** : [netlify](https://www.netlify.com/),[hexo](https://hexo.io/),[hexo-stun-theme](https://github.com/liuyib/hexo-theme-stun)

**asciinema** : [link](https://asciinema.org/a/GbMj8NR4i4GVOXSRFs51Bcvwf)

**blog** : [learning-stuff](https://blog-by-mimikyu.netlify.app/)


Χρησιμοποίησα το hexo για την δημιουργία ενός blog.
Για το συγκεκριμένο blog πέρα από τα απαραίτητα configurations για την σελίδα , άλλαξα το theme και πρόσθεσα μία νέα σελίδα με μια μικρή περιγραφή για τον εαυτό μου. Μετά για το deploy της σελίδας κατέβασα το command line tool του netlify και έστησα το CI για να κάνω push κάθε φορά που κάνω μια αλλαγή.
Η τυπική διαδικασία φαίνεται στο asciinema.

