## ΠΡΟΣΩΠΙΚΑ ΣΤΟΙΧΕΙΑ:

### Βασίλειος Γαβριηλίδης
### ΑΜ: Π2018151
### [Github Profile](https://github.com/vxsilis)

| Εβδομάδα* | Παραδοτέο |
| --- | --- |
| 1 | <a href="#P-1">Φορκ του αποθετηρίου και δημιουργία της σελίδας της αναφοράς με τα προσωπικά στοιχεία σας, της σύνοψης με αυτόν τον πίνακα περιεχομένων, και συγγραφή της εισαγωγής με περιγραφή των αναγκών και των στόχων σας για το αντίστοιχο μάθημα* </a>|
| 2 | <a href="#P-2"> Βιογραφικό</a> |
| 3 | <a href="#P-3">Αίτημα ενσωμάτωσης στην ιστοσελίδα</a> |
| 4 | <a href="#P-4">Άσκηση γραμμής εντολών</a> |
| 5 | <a href="#P-5">Συμμετοχικό περιεχόμενο</a> |
| 6 | <a href="#P-6">Άσκηση γραμμής εντολών</a> |
| 7 | <a href="#P-7">Βιογραφικό</a> |
| 8 | Αίτημα ενσωμάτωσης στην ιστοσελίδα |
| 9 | <a href="#P-9">Άσκηση γραμμής εντολών</a> |
| 10 | <a href="#P-10">Συμμετοχικό περιεχόμενο</a> |
| 11 | <a href="#P-11">Άσκηση γραμμής εντολών</a> |
| 12 | Τελική αναφορά* |


## <a name="P-1">Παραδοτέο 1 - ΕΙΣΑΓΩΓΗ:</a>
Στο μάθημα Τεχνολογίες Λογισμικού ελπίζω και έχω στόχο να μάθω πράγματα για τον σχεδιασμό και την αρχιτεκτονική πίσω απο το λογισμικό. Να αναπτύξω κάποιου είδους διεπαφή με τον χρήστη αλλά και να μάθω τρόπους συντήρησης αυτών των τεχνολογιών, ώστε το λογισμικό να παραμένει σύγχρονο και ψυχαγωγικό.

---

## <a name="P-2">Παραδοτέο 2 - ΒΙΟΓΡΑΦΙΚΟ:</a>

Για το δεύτερο παραδοτέο δημιούργησα ένα εικονικό ubuntu σύστημα σε docker με την βοήθεια απο το εργαστήριο του κ.Ρίγγα. Έφτιαξα ένα νέο repository "cv-1" στο οποίο άρχισα να βάζω το κώδικα μου και συγκεκριμένα τα 2 βασικά αρχεία index.html και details.yml. Τα έκανα για πρώτη φορά commit και push από το τερματικό και έπειτα απο το github.com όρισα το github page source και επέλεξα ένα theme. Είχα κάνει ήδη κάποια πρόοδο κατα την διάρκεια των εργαστηρίων με τον κ.Ρίγγα οπότε στο παρακάτω σύνδεσμο του asciinema παρουσιάζω τυπικά κάποιες αλλαγές στα 2 αρχέια index και details για να φανεί η διαδικασία και χρήση του git από το τερματικό.

- Link ιστοσελίδας φτιαγμένης με Jekyll: https://vxsilis.github.io/cv-1/

- Link asciinema με την εγγραφή τερματικού που φαίνεται η διαδικασία επεξεργασίας των html και yml αρχείων και έπειτα το commit και push στο master branch: https://asciinema.org/a/395041

- Link του repository της σελίδας: https://github.com/vxsilis/cv-1

---

## <a name="P-3">Παραδοτέο 3 - ΑΙΤΗΜΑ ΕΝΣΩΜΑΤΩΣΗΣ ΣΤΗΝ ΙΣΤΟΣΕΛΙΔΑ:</a>

Για το τρίτο παραδοτέο με την βοήθεια του netlify και κάνοντας fork το αποθετήριο της ιστοσελίδας για να κάνω τις κατάλληλες αλλαγές, πρόσθεσα κάποιες βασικές πληροφορίες στην ενότητα “Σπουδές” για τις διδακτορικές σπουδές όπως μία σύντομη περιγραφή και 2 downloadable αρχεία με περαιτέρω πληροφορίες για τον χρήστη, με πήγη της επίσημη ιστοσελίδα της σχολής.

- Link αποθετηρίου της ιστοσελίδας: https://github.com/vxsilis/sitegr/tree/2018151

- Link ιστοσελίδας: https://epic-hamilton-da9ac8.netlify.app/courses/#διδακτορικο

---

## <a name="P-4">Παραδοτέο 4 - ΑΣΚΗΣΗ ΓΡΑΜΜΗΣ ΕΝΤΟΛΩΝ:</a>

Για το 4ο παραδοτέο αποφάσισα να κάνω την πρώτη άσκηση απο τις προτεινόμενες που είχε ως τίτλο “Set-up continuous integration. Build and deploy your static site and your cv dynamically every time you make a small change in the source files.”

Για την πραγματοποίηση αυτού του παραδοτέου χρησιμοποίησα το HUGO για να βρώ ένα framework που γύρω απο αυτό θα χτίσω το site μου. Για host και server χρησιμοποίσα το netlify. Από το έτοιμο template που πήρα χρειάστηκε να αλλάξω αρκετά πράγματα στην δομή του ώστε να το φέρω στα μέτρα μου. Το site ακουλουθεί την λογική html - yaml για να φορτώνει τα δεδομένα από άλλα αρχεία και εννοείται με κάθε commit και push που πραγματοποιείται, η κάθε αλλαγή πραγματοποιείται ζωντανά στον παρακάτω σύνδεσμο.

Στο asciinema, θα επισκεφθώ πρώτα την ιστοσελίδα μου για να δείξω το αρχικό περιεχόμενο της. Έπειτα θα κάνω μια μικρή αλλαγή σε ένα yaml αρχείο και έπειτα θα το κάνω commit και push στο main branch. Μετά θα επισκεφθώ ξανά το site μου για να φανεί η αλλαγή που έγινε ζωντανά. Επειδή έχω το μικρό idle time ίσως χρειαστεί pause σε κάποια σημεία για να δείτε τις διαφορές πριν και μετά τα commits.

- Link asciinema: https://asciinema.org/a/399146

- Link ιστοσελίδας βιογραφικού: https://vgcv.netlify.app

- Link αποθετηρίου: https://github.com/vxsilis/4oCV

---

## <a name="P-5">Παραδοτέο 5 - ΣΥΜΜΕΤΟΧΙΚΟ ΠΕΡΙΕΧΟΜΕΝΟ:</a>

Για το 5ο παραδοτέο έκανα fork αρχικά το repo της ιστοσελίδας. Έκανα επίσης fork τα “_gallery” και “images”. Τώρα, στα δικά μου repos πρόσθεσα στο “_gallery” τα αρχεία:

### - Υποερώτημα Α1

| wordstar.md | https://github.com/vxsilis/_gallery/blob/master/wordstar.md |
| --- | --- |
| freebsd.md | https://github.com/vxsilis/_gallery/blob/master/freebsd.md |

Ακολουθώντας την δομή και το template των άλλων αρχείων, που περιλαμβάνουν την περιγραφή δύο λογισμικών και τις αντίστοιχες εικόνες τους (κανονική και thumbnail) στο repo μου “images”. 

| https://github.com/vxsilis/images/blob/master/wordstar.jpg | https://github.com/vxsilis/images/blob/master/wordstar-thumb.jpg |
| --- | --- |
| https://github.com/vxsilis/images/blob/master/freebsd.jpg | https://github.com/vxsilis/images/blob/master/freebsd-thumb.jpg |


| Και τα δύο αυτά repos τα έκανα submodule με την χρήση του τερματικού στο αρχικό fork που φαίνεται στο διπλανό asciinema | https://asciinema.org/a/400647 |
| --- | --- |
| Το repo μου βρίσκεται εδώ που φαίνονται και τα submodules _gallery, images | https://github.com/vxsilis/site |

### - Υποερώτημα Α2

| Έπειτα στο φάκελο _slides, στο αρχείο πρόσθεσα το θέματα των freebsd και worstar. |  https://github.com/vxsilis/site/blob/master/_slides/metaphors.md |
| --- | --- |
| Άλλαξα στο φάκελο _timeline το ήδη υπάρχων αρχείο micros.md για να προσθέσω το event wordstar το οποίο είναι είναι αρκετά σχετικό με αυτό το χρονολόγιο. | https://github.com/vxsilis/site/blob/master/_timeline/micros.md |
| Επίσης στο αρχείο computers.md πρόσθεσα το freebsd που έκρινα εγώ σχετικό το με το υπάρχων χρονολόγιο. | https://github.com/vxsilis/site/blob/master/_timeline/computer.md |

Έπειτα έκανα build την σελίδα με την βοήθεια του netlify.

Παρακάτω φαίνονται οι αλλαγές μου:

| Η αλλαγή μου | ο σύνδεσμος |
| --- | --- |
| Η προσθήκη του wordstar | https://vxs5.netlify.app/gallery/wordstar/ |
| Η προσθήκη του freebsd | https://vxs5.netlify.app/gallery/freebsd/ |
| To set απο θεματικές ενότητες | https://vxs5.netlify.app/slides/metaphors/ |
| Το χρονολόγιο "ορίζοντας τον υπολογισμό" | https://vxs5.netlify.app/timeline/computer/ |

---
## <a name="P-6">Παραδοτέο 6 - ΑΣΚΗΣΗ ΓΡΑΜΜΗΣ ΕΝΤΟΛΩΝ:</a>

Για το παραδοτέο 6 με θέμα άσκηση γραμμής εντολών αποφάσισα να κάνω το παραδοτέο με τίτλο "send notifications to your desktop / send a notification when a big task completes, eg download, compiling" με την βοήθεια του ntfy. Στο παρακάτω asciinema θα δείξω πρώτα το config file μου που το έχω ορίσει έτσι ώστε το output των ενεργειών μου να πηγαίνει στο system log ώστε να δούμε ότι όντως δουλεύει. ΄Επειτα θα τρέξω έναν απλό κώδικα που εμφανίζει κείμενο με καθυστέρηση στο background και έπειτα θα δώσω τον αριθμό PID στο ntfy ώστε να με ενημερώσει όποτε τελειώσει αυτή η διεργασία. Η διεργασία φαίνεται να εκτελείτε αμέσως λόγω του -i 0.25 του asciinema αλλά κανονικά έχει καθυστέρηση 25 δευτερόλεπτα. Τέλος θα εμφανίσω και την πιο πρόσφατη γραμμή του syslog  για να φανεί και η καταγραφή της ολοκλήρωσhς της διεργασίας.

- Link asciinema: https://asciinema.org/a/403171

---
## <a name="P-7">Παραδοτέο 7 - ΒΙΟΓΡΑΦΙΚΟ:</a>

Για το 7ο παραδοτέο πρόσθεσα την δυνατότητα εκτύπωσης του βιογραφικού μου σε μορφή pdf A4 μέσω κουμπιού που εμφανίζεται. Την προσθήκη αυτού του κουμπιού την έκανα εν τέλη με την βοήθεια του weasyprint γιατί δυστυχώς δεν κατάφερα να κάνω επιτυχημένα setup pandoc+latex και μονίμως υπήρχαν error. Επίσης έφτιαξα ένα script για pre-commit και post-commit που ενσωματώνει κάθε αλλαγή που γίνεται στα αρχεία ymal ή html ώστε κάθε τροποποίηση θα ενσωματώνεται αυτόματα και στο αρχείο pdf με κάθε commit που κάνω.

Στο παρακάτω asciinema θα δείξω το περιεχόμενο του index.html που πρόσθεσα το κουμπί - που ουσιαστικά είναι ένα σύνδεσμος που παραμπέμπει στο φάκελο pdf που περιλαμβάνει το printable αρχείο -, το script του hook post-commit. Έπειτα, θα κάνω μια αλλαγή στο details.yml, θα την κάνω commit (εμφανίζονται κάτι warning όσο αφορά την κωδικοποίηση κάποιων αρχείων αλλά δεν εμποδίζουν την διαδικασία) και push αλλα δυστυχώς, μέσω τέρμιναλ δεν μπορω να αποδείξω οτι ταυτόχρονα αλλάζει επιτυχώς το περιεχόμενο του pdf. Μπορείτε να το δείτε όμως στον παρακάτω σύνδεσμο.

- Link asciinema: https://asciinema.org/a/404946
- Link ιστοσελίδας: https://vxsilis.github.io/cv-1/
- Link repo: https://github.com/vxsilis/cv-1

---
## <a name="P-9">Παραδοτέο 9 - ΑΣΚΗΣΗ ΓΡΑΜΜΗΣ ΕΝΤΟΛΩΝ:</a>

Για το 9ο παραδοτέο αποφάσισα να κάνω το "Create an agent for news" με την βοήθεια του [huginn](https://github.com/huginn/huginn) απλώς με μία παραλλαγή. Πρώτα έφτιαξα έναν agent ο οποίος μέσω ένος API key απο το site https://openweathermap.org τραβάει το καιρό και την θερμοκρασία κάθε ώρα για την Κέρκυρα. Το αποτέλεσμα που επιστέφει είναι σε μόρφη JSON και δείχνει κάπως [έτσι](https://github.com/vxsilis/huginn_t/blob/main/images/API_Key.png). Έπειτα έφτιαξα έναν δεύτερο agent ο οποίος έχει ως source τον προηγούμενο agent και επεξεργάζεται τα δεδομένα σε μορφή που διαβάζονται και έπειτα τα στέλνει στον slack server μου. Παρακάτω έχω μερικά screenshot από το hugin agent, τους κώδικες json που χρησιμοποίσησα στους agent όπως και στιγμιότυπο του αποτελέσματος στο slack server, αφού το συγκεκριμένο παραδοτέο δεν μπορεί να καταγραφεί με asciinema. Edit 12-5-2021: Προσθέτω ένα [link από το asciinema](https://asciinema.org/a/413671) που ξεκινάω το docker container του huginn στο localhost:3000. Το huginn αποτελείτε απο γραφικό περιβάλλον που είναι μόνο προσβάσιμο απο browser οπότε δεν μπορώ να κάνω παραπάνω καταγραφή της διαδικασίας.


| Κώδικας που παίρνει πληροφορίες απο το weather site | Στιγμιότυπο από το hugin agent  |
| --- | --- |
| https://github.com/vxsilis/huginn_t/blob/main/corfuWeather.json | https://github.com/vxsilis/huginn_t/blob/main/images/weatherCorfu.png |


| Κώδικας που παίρνει επεξεργάζεται το json και το στέλνει στο slack | Στιγμιότυπο από το hugin agent  |
| --- | --- |
| https://github.com/vxsilis/huginn_t/blob/main/weatherToSlack.json | https://github.com/vxsilis/huginn_t/blob/main/images/weatherToSlack.png |


| Το αποτέλεσμα που έρχεται στον slack | https://github.com/vxsilis/huginn_t/blob/main/images/slackNotif.png |
|---|---|

---
## <a name="P-10">Παραδοτέο 10 - ΣΥΜΜΕΤΟΧΙΚΟ ΠΕΡΙΕΧΟΜΕΝΟ:</a>

Για το 10ο παραδοτέο πρόσθεσα το βιογραφικό του Seymour Rubinstein, ο οποίος ήταν και ο εφευρέτης του WordStar, λογισμικού που πρόσθεσα στο προηγούμενο παραδοτέο.

Παρατήρησα ότι για τα βιογραφικά που εμφανίζονται σωστά και έχουν περιεχόνενο στο pibook.epidrome.me έχουν και τα 2 αρχεία στο ίδιο φάκελο _biography, οπότε έτσι έκανα και εγώ.

| Λινκ ιστοσελίδας με την προσθήκη: | https://vxs5.netlify.app/biography/seymour_rubinstein/ |
| --- | --- |
| Λινκ αρχείου περιγραφής στο αποθετήριο: | https://github.com/vxsilis/site/blob/master/_biography/seymour_rubinstein.md |
| Λινκ περιεχομένου βιογραφικού: | https://github.com/vxsilis/site/blob/master/_biography/bio-rubinstein.md |

| Αναφορές & Πηγές |
| --- |
| https://seymourrubinstein.wordpress.com |
| https://seymourrubinstein.wordpress.com/bio/ |
| https://en.wikipedia.org/wiki/Seymour_I._Rubinstein |


Για την μελέτη περίπτωσης έγραψα για το Project του FreeBsd

Έκανα δικιά μου έκδοση του repo extras για να βάλω την προσθήκη μου.

| Λινκ ιστοσελίδας με την προσθήκη:| https://vxs5.netlify.app/case-study/freebsd-cs/ |
| --- | --- |
| Λινκ αρχείου περιγραφής στο φάκελο case study: | https://github.com/vxsilis/site/blob/master/_case-study/freebsd-cs.md |
| Λινκ περιεχομένου της μελέτης στο submodule “extras”: | https://github.com/vxsilis/extras/blob/master/cs-freebsd.md |

| Αναφορές & Πηγές | http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.72.9396&rep=rep1&type=pdf |
| --- | --- |

---

## <a name="P-11">Παραδοτέο 11 - ΑΣΚΗΣΗ ΓΡΑΜΜΗΣ ΕΝΤΟΛΩΝ:</a>

Για το 11ο παραδοτέο αποφάσισα να κάνω την άσκηση “performance monitoring” για έναν κώδικα python. Στο asciinema φαίνεται ο κώδικας που θα δοκιμάσω και περιέχει 2 αλγόριθμους ταξινόμησης. Bubble sort, insert sort και υπάρχει ένας πίνακας με 1000 ψηφία προς ταξινόμηση. Με την βοήθεια του [py-spy](https://github.com/benfred/py-spy) και του γραφήματος που μας δίνει και φαίνεται [εδώ](https://github.com/vxsilis/huginn_t/blob/main/images/py-spy-sorts.png), καταλαβαίνουμε ότι η συνάρτηση που εκτέλεσαι το bubble sort πήρε περισσότερη ώρα και ότι το insert sort είναι ένας γρηγορότερος αλγόριθμος. Έπειτα με την βοήθεια του [hyperfine](https://github.com/sharkdp/hyperfine) θα μετρήσω πόση ώρα κάνει κάθε αλγόριθμός να ολοκληρωθεί ξεχωριστά για την ταξινόμηση ενός πίνακα 100000 αριθμών. 

- Link asciinema: https://asciinema.org/a/410955

Φαίνεται πως:

| | BUBBLE SORT | INSERTION SORT |
| --- | --- | --- |
| min time | 0.3ms | 0.1ms |
| max time | 0.5ms | 0.2ms |

Οπότε και πάλι φαίνεται ότι ο insertion sort είναι γρηγορότερος. 
