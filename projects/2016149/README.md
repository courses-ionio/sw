## Μάθημα
### Τεχνολογίες Λογισμικού  
*  Ονοματεπώνυμο: **Γεώργιος Μαντέλλος**
*  Αριθμός Μητρώου: **Π2016149**
*  Προσωπικό αποθετήριο του κώδικα: [Link Αποθετηρίου του κώδικα εργασίας ανάπτυξης](https://github.com/geocfu/site-gr)
*  Link για το εκτελέσιμο: [Link Εκτελέσιμου](https://geocfu.github.io/site-gr)
*  Αποθετήριο κώδικα Μπόνους Εργασίας: [Link αποθετηρίου του κώδικα της σελίδας βιογραφικού](https://github.com/geocfu/cv)
*  Link για το εκτελέσιμο μπόνους: [Link Bonus Σελίδας Βιογραφικού](https://geocfu.github.io/cv)  
## Επιλογή Εργασίας Bonus
### Δημιουργία βιογραφικού με το σύστημα Github Pages  

## Σύνοψη Εργασίας Βοnus
&nbsp;&nbsp;&nbsp;&nbsp;Σκοπός της bonus εργασίας ήταν να δημιουργήσουμε ένα βιογραφικό σημείωμα χρησιμοποιόντας το σύστημα github pages και να εξάγουμε αυτόματα ένα pdf του, χρησιμοποιόντας την αυτόματη διαδικασία που προσφέρει ένα CI εργαλειο.

## Μέθοδος Ανάπτυξης εργασίας Bonus
&nbsp;&nbsp;&nbsp;&nbsp;Αρχικά, έγινε αλλαγή του default θέματος. Άλλαξε η γραμματοσειρά, τα χρώματα, προστέθηκε μία πράσινη γραμμή στο πάνω μέρος της σελίδας και προστέθηκε ενα επιπλέον εικονίδιο προκειμένου κάποιος να μπορεί να κατεβάσει το αυτόματα δημιουργημένο pdf.

## Παραδοτέα
### Παραδοτέο 1ο
* Επιλογή θέματος απο τα διαθέσιμα. Αλλαγή θέματος οπως περιγράφεται στην μέθοδο ανάπτυξης.
* Συπλήρωση βιογραφικού

### Παραδοτέο 2ο
* Χρησιμοποιόντας την γραμμή εντολών και τα εργαλεία Pandoc και LaTeX, από το ίδιο αρχείο που χρησιμοποιεί το github pages (_config.yml) για να φτιάξει την ιστοσελίδα, παράχθηκε το resume.pdf αρχείο.
* Πλέον, το resume.pdf αρχείο δημιουργείται αυτόματα απο το CI εργαλειο, Travis-CI.

![travis_build_output](https://raw.githubusercontent.com/geocfu/sw/2016149/projects/2016149/ci-build.png)

![travis_gif](https://raw.githubusercontent.com/geocfu/sw/2016149/projects/2016149/ci.gif)

## Επιλογή Εργασίας
### Συνεργατική κατασκευή ιστοσελίδας του τμήματος.

## Σύνοψη Εργασίας
&nbsp;&nbsp;&nbsp;&nbsp;Σκοπός της εργασίας αυτής ήταν να προσθέσουμε συγκεκριμένη λειτουργικότητα στην ιστοσελίδα του τμήματος, ακολουθώντας το αρχικό road-map. 

## Μέθοδος Ανάπτυξης 
&nbsp;&nbsp;&nbsp;&nbsp;Για την πραγματοποίηση της εργασίας χρησιμοποιήθηκε το pwa-plugin. Ουσιαστικά, το plugin αυτό, διευκολύνει την δημιουργία ανάπτυξης Progressive Web App εφαρμογών. Ωστόσο, κάποια από τα ζητούμενα δεν ήταν δυνατόν να υλοποιηθούν λόγω του ίδιου του plugin. Μια progressive Web App εφαρμογή, χρειάζεται για να λειτουργήσει σωστά, εναν service worker, ένα manifest και εναν service worker registrator. Επειδή το plugin χρησιμοποιεί, προφανώς, τον κώδικα του προγραμματιστή που το έφτιαξε, δεν γίνεται να κάνουμε κάποια αλλαγή σε αυτό το επίπεδο. Άρα, το ενδεχόμενο να προσθέσουμε την λειτουργικότητα που εμείς επιθυμούμε, όπως εμφάνιση μίας συγκεκριμένης σελίδας όταν ο χρήστης είναι εκτός σύνδεσης, να προτρέψουμε το χρήστη να εγκαταστήσει τοπικά την εφαρμογή και οι ειδοποιήσεις push, αποκλείεται. Συνεπώς, αυτό με το οποίο υλοποιήθηκε η Progressive Web App εφαρμογή για την ιστοσελίδα είναι, ένας service worker, ένας service worker registrator και ενα manifest. Συνεπώς, η ιστοσελίδα αποτελεί μία λειτουργική pwa εφαρμογή, με λειτουργία caching για τις τελευταίες 5 ανακοινώσεις και για ολες τις σελίδες της ιστοσελίδας.

## Παραδοτέα
### Παραδοτέο 1ο
#### Εύκολα
- [ ] Προσθήκη χάρτη και σύνδεση με την εφαρμογή πλοήγησης στο κινητό του χρήστη
- [ ] Δοκιμή-Αξιολόγηση: https://github.com/juusaw/amp-jekyll [AMP+minimal-mistakes](https://github.com/mmistakes/minimal-mistakes/issues/584)
- [x] Δοκιμή-Αξιολόγηση: https://github.com/lavas-project/jekyll-pwa
- [ ] Metadata provided for Add to Home screen (Web App Manifest)
- [ ] Site appropriately informs the user when they're offline (Network Information API)

#### Δύσκολα
- [ ] Ενημέρωση προδιαγραφών ανάλογα με την έκβαση των αρχικών δοκιμών με έτοιμα συστήματα?
- [x] All (or some? which ones?) app URLs load while offline (Service Worker)
- [x] Site uses cache-first networking (Service Worker)
- [ ] Push Notifications (Service Worker)
- [ ] CI for non-white-listed plug-ins  

### Παραδοτέο 2ο
#### Εύκολα
- [ ] Προσθήκη χάρτη και σύνδεση με την εφαρμογή πλοήγησης στο κινητό του χρήστη
- [ ] Δοκιμή-Αξιολόγηση: https://github.com/juusaw/amp-jekyll [AMP+minimal-mistakes](https://github.com/mmistakes/minimal-mistakes/issues/584)
- [x] Δοκιμή-Αξιολόγηση: https://github.com/lavas-project/jekyll-pwa
- [x] Metadata provided for Add to Home screen (Web App Manifest)
- [ ] Site appropriately informs the user when they're offline (Network Information API)

#### Δύσκολα
- [x] Ενημέρωση προδιαγραφών ανάλογα με την έκβαση των αρχικών δοκιμών με έτοιμα συστήματα?
- [x] Posts URLs load while offline (Service Worker)
- [x] Site uses cache-first networking (Service Worker)
- [x] move pwa/js to minimal-ionio theme?
- [ ] Push Notifications (Service Worker)
- [ ] https://github.com/nickgarlis/jekyll-ghdeploy
- [ ] CI for non-white-listed plug-ins

## Στιγμιότυπα οθόνης για την εφαρμογή
![pwa_service_worker](https://raw.githubusercontent.com/geocfu/sw/2016149/projects/2016149/pwa_service_worker.png)  

![pwa_manifest](https://raw.githubusercontent.com/geocfu/sw/2016149/projects/2016149/pwa_manifest.png)  

![pwa_cached_posts](https://github.com/geocfu/sw/blob/2016149/projects/2016149/pwa_cached_posts.png)  

![pwa_in_action](https://raw.githubusercontent.com/geocfu/sw/2016149/projects/2016149/pwa.gif)

## Συμπεράσματα  
&nbsp;&nbsp;&nbsp;&nbsp;Τέλος, μπορώ να δηλώσω με σιγουριά ότι η συγκεκριμένη εργασία μου έμαθε πως να χρησιμοποιώ το περιβάλλον github pages προκειμένου να παράγω μια ιστοσελίδα και πώς να χρησιμοποιώ ενα gem plugin για να προσθέσω επιπλέον λειτουργικότητα σε αυτήν. 

## Σελίδα Τελικής Αναφοράς  
### todo
