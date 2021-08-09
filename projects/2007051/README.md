<h1>ΤΕΧΝΟΛΟΓΙΑ ΛΟΓΙΣΜΙΚΟΥ</h1>

<h4>ΟΝΟΜΑΤΕΠΩΝΥΜΟ: ΓΕΩΡΓΙΟΣ ΠΑΛΑΝΤΖΑΣ </h4>

<h4>ΑΜ: Π2007051 </h4>

# Παραδοτέα

## Πίνακας με σύνοψη των προθεσμιών και των παραδοτέων

| Εβδομάδα* | Παραδοτέο |
| --- | --- |
| 1 | <sup><a href="#1"> Περιγραφή των αναγκών και των στόχων για το μάθημα </a></sup> |
| 2 | <sup><a href="#2"> βιογραφικό: Ιστοσελίδα με χρήση Jekyll </a></sup> | 
| 3 | <sup><a href="#3"> Αίτημα ενσωμάτωσης στην ιστοσελίδα: Προσθήκη ανακοίνωσης </a></sup> |
| 4 | <sup><a href="#4"> Άσκηση γραμμής εντολών: create your own static site and blog generator </a></sup> |
| 5 | <sup><a href="#5"> Συμμετοχικό περιεχόμενο: A1 & A2 </a></sup> |
| 6 | <sup><a href="#6"> Άσκηση γραμμής εντολών: send notifications to your desktop-mobile </a></sup> |
| 7 | <sup><a href="#7">  </a></sup> |
| 8 | <sup><a href="#8">  </a></sup> |
| 9 | <sup><a href="#9"> Άσκηση γραμμής εντολών: create notifications on your server </a></sup> |
| 10 | <sup><a href="#10"> Άσκηση γραμμής εντολών: performance monitoring </a></sup> |
| 11 | <sup><a href="#11"> </a></sup> |
| 12 | <sup><a href="#12"> </a></sup> |

###### [1]

## Περιγραφή των αναγκών και των στόχων για το μάθημα:

Μέσω του μαθήματος "Τεχνολογία Λογισμικού", στοχεύω στη κατανόηση της θεωρίας και σχεδίασης των συστημάτων ανάπτυξης λογισμικού.
Κύριος στόχος μου για το μάθημα είναι ο εμπλουτισμός των βασικών γνώσεών μου γύρω από την πλατφόρμα του Github, ένα από τα σημαντικότερα εργαλεία για την αποδοτικότερη οργάνωση και σύνταξη αλλαγών σε μορφή κώδικα. Σαφώς επιβάλλεται η συνεχής παρακολούθηση των διαλέξεων και εργαστηρίων για την κατανόηση της διαδικασίας και της οργάνωσης του λογισμικού, καθώς και για την ανάπτυξη και συντήρηση αυτού.
Εφόσον τα παραπάνω εφαρμοστούν στην πράξη, θεωρώ πως η προσαρμογή μου στο αντικείμενο του μαθήματος θα είναι πιο ομαλή.

###### [2]

Online Βιογραφικό/Bio: https://geopala.github.io/online-cv/

Repository βιογραφικού: https://github.com/geopala/online-cv

## Υλοποίηση:
Μετά την επιλογή του θέματος jekyll "Thunder" από **sharu725** προχώρησα σε fork του repository και αντικατέστησα το **gh-pages** branch με το δικό μου, ώστε να χρησιμοποίει ως
root τις αλλαγές που θα πραγματοποιώ στο master branch.

Το νέο branch **gh-pages** χρησιμεύει στο hosting του resume και μόνο.

Πραγματοποίησα εισαγωγή των στοιχείων, της εικόνας προφίλ στο φάκελο **assets/images** και στην αλλαγή του θέματος από ```blue``` σε ```ceramic```.

Όλα τα παραπάνω πραγματοποιήθηκαν μέσω επεξεργασίας των αρχείων **data.yml** και **_config.yml**.

**Αποτελέσματα:**

![bio](https://github.com/geopala/sw-images/blob/main/bio.png)

**Πηγή:** https://github.com/sharu725/online-cv#installation

###### [3]

## Αίτημα ενσωμάτωσης στην ιστοσελίδα: Προσθήκη ανακοίνωσης

## Υλοποίηση:
### Προσθήκη ανακοίνωσης "Επίσκεψη της Προέδρου της Δημοκρατίας Κατερίνας Σακελλαροπούλου στο Εργαστήριο Βιοπληροφορικής και Ανθρώπινης Ηλεκτροφυσιολογίας του Τμήματος Πληροφορικής του Ι.Π." με ημερομηνία δημοσίευσης 21-05-2021 στο site του τμήματος.

**Issue**: https://github.com/ioniodi/sitegr/issues/219

**green light**: ❌

**Αποθετήριο αιτήματος**: https://github.com/geopala/sitegr/tree/2007051

**Αρχείο .md ανακοίνωσης**: https://github.com/geopala/sitegr/blob/2007051/all_collections/_posts/2021-05-21-episkepsi-proedrou.md

**pull request**: ❌

**Pull Request**:

**Netlify**:

###### [4]

## Άσκηση γραμμής εντολών: create your own static site and blog generator

Δημιουργία webpage με hugo: https://asciinema.org/a/429707

## Υλοποίηση:
• Εγκατάσταση των απαραίτητων πακέτων:```sudo apt install hugo```.

• Έναρξη καταγραφής terminal: ```asciinema rec -i 0.2```.

• Δημιουργία site: ```hugo new site quickstart```.

• Ορισμός location site: ```cd quickstart```, ```git init```.

• Εγκατάσταση θέματος: ```git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke```

• Πληκτρολόγηση εντολής hosting: ```hugo server -D```.

• Δημιουργία post: ```hugo new posts/my-latest-post.md```.

• Επεξεργασία post: ```nano content/posts/my-latest-post.md```.

• Build site: ```hugo -D```.

• Ολοκλήρωση asciicast: ```exit```.

**Αποτελέσματα:**

![quickstart](https://github.com/geopala/sw-images/blob/main/quickstart.png)

![hugo](https://github.com/geopala/sw-images/blob/main/hugo.png)

**Πηγή:** https://github.com/gohugoio/hugo

###### [5]

###### [6]

## Άσκηση γραμμής εντολών: send notifications to your desktop-mobile

Παραδείγματα notification ntfy: https://asciinema.org/a/428638

Telegram setup και παράδειγμα χρήσης: https://asciinema.org/a/428738

## Υλοποίηση:
• Εγκατάσταση των απαραίτητων πακέτων: ```sudo apt-get install pip``` και ```sudo pip install ntfy```.

• Έναρξη καταγραφής terminal: ```asciinema rec -i 0.2```.

• Δοκιμή ειδοποιήσεων: ```notify-send --urgency=CRITICAL "Hello world"```, ```notify-send --urgency=LOW "How are you today?"``` & ```ntfy done sleep 5``` ως timer.

• Setup **ntfy** για **Telegram**: ```ntfy -b telegram send "Telegram configured for ntfy"```.

• Ορισμός νέου bot στην εφαρμογή **Telegram** μέσω οδηγιών του **BotFather**(εικόνες).

• Paste token στο terminal για σύνδεση με την εφαρμογή.

• Δοκιμή αποστολής μηνύματος μέσω terminal: ```ntfy -b telegram send "Hello world!"```

• Επιτυχής λήψη μηνύματων στη συσκευή μου.

• Ολοκλήρωση asciicast: ```exit```.

**Αποτελέσματα:**

![hello-crit](https://github.com/geopala/sw-images/blob/main/hellocrit.png)

![howru-low](https://github.com/geopala/sw-images/blob/main/howru-low.png)

![ntfy-sleep](https://github.com/geopala/sw-images/blob/main/ntfy-sleep.png)

![teleg-setup](https://github.com/geopala/sw-images/blob/main/teleg-setup.jpg)

![teleg-test](https://github.com/geopala/sw-images/blob/main/teleg-test.jpg)

**Πηγή:** https://github.com/dschep/ntfy#telegram---telegram

###### [7]
###### [8]
###### [9]

## Άσκηση γραμμής εντολών: create notifications on your server

Εκκίνηση mosquitto: https://asciinema.org/a/428255

Παράδείγμα λήψης μηνύματος μέσω mosquitto: https://asciinema.org/a/428265

## Υλοποίηση:
• Εγκατάσταση των απαραίτητων πακέτων: ```sudo apt-get install mosquitto``` και ```sudo apt-get install mosquitto-clients```.

• Έναρξη καταγραφής terminal: ```asciinema rec -i 0.2```.

• Εκκίνηση του mosquitto: ```mosquitto```.

• Εγγραφή σε topic π.χ **test**: ```mqtt_sub -h localhost -t test```.

• Ορισμός νέου topic στην εφαρμογή **MQTT Client** μέσω **+**(εικόνες).

• Εντοπισμός IP terminal: ```ifconfig``` και πληκτρολόγηση αυτής στην ενότητα **Host** του app.

• Πληκτρολόγηση της εντολής ```mqtt_pub -h localhost -t test -m "What's up?"```.

• Επιτυχής λήψη μηνύματων στη συσκευή μου.

• Ολοκλήρωση asciicast: ```exit```.

**Αποτελέσματα:**

![mqtt-pub](https://github.com/geopala/sw-images/blob/main/mqtt-pub.png)

![mqtt-setup](https://github.com/geopala/sw-images/blob/main/mqtt-setup.jpg)

![mqtt-test](https://github.com/geopala/sw-images/blob/main/mqtt-test.jpg)

**Πηγή:** https://www.arubacloud.com/tutorial/how-to-install-and-secure-mosquitto-on-ubuntu-20-04.aspx

###### [10]

## Άσκηση γραμμής εντολών: performance monitoring

Χρήση του py-spy: https://asciinema.org/a/429431

Χρήση του hyperfine: https://asciinema.org/a/429434

Flamegraph profile.svg: https://github.com/geopala/sw-images/blob/main/profile.png

Output του hyperfine: https://github.com/geopala/sw-images/blob/main/output.png

## Υλοποίηση:
• Εγκατάσταση των απαραίτητων πακέτων: ```sudo pip3 install py-spy```, ```git clone --depth 1 https://github.com/brendangregg/FlameGraph```, ```apt-get install wget```, ```wget https://github.com/sharkdp/hyperfine/releases/download/v1.11.0/hyperfine_1.11.0_amd64.deb``` & ```sudo dpkg -i hyperfine_1.11.0_amd64.deb```.

• Έναρξη καταγραφής terminal: ```asciinema rec -i 0.2```.

• Χρήση 2 print script: **testscript.py**[https://github.com/geopala/sw-images/blob/main/testscript.py]
  & **testscript2.py**[https://github.com/geopala/sw-images/blob/main/testscript2.py].

• Performance monitoring του **testscript.py** μέσω **py-spy**: ```py-spy record -o profile.svg -- python3 testscript.py```.

• Πληκτρολόγηση των εντολών: ```cat testscript.py``` και ```cat testscript2.py```.

• Benchmarking μέσω **hyperfine**: ```hyperfine 'python testscript.py' 'python testscript2.py'```.

• Εξαγωγή αποτελέσματος: ```hyperfine -i --export-json output 'python testscript.py' 'python testscript2.py'```.

• Ολοκλήρωση asciicast: ```exit```.

**Αποτελέσματα:**

![profile](https://github.com/geopala/sw-images/blob/main/profile.png)

![output](https://github.com/geopala/sw-images/blob/main/output.png)

**Πηγές:**

https://github.com/benfred/py-spy#usage

https://github.com/sharkdp/hyperfine#usage

###### [11]
###### [12]
