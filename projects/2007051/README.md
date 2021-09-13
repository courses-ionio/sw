<h1>ΤΕΧΝΟΛΟΓΙΑ ΛΟΓΙΣΜΙΚΟΥ</h1>

<h4>ΟΝΟΜΑΤΕΠΩΝΥΜΟ: ΓΕΩΡΓΙΟΣ ΠΑΛΑΝΤΖΑΣ </h4>

<h4>ΑΜ: Π2007051 </h4>

<h4>Προσωπικό site: https://geopala.netlify.app/ </h4>

<h4>Προφίλ Asciinema: https://asciinema.org/~P2007051 </h4>

# Παραδοτέα

## Πίνακας με σύνοψη των προθεσμιών και των παραδοτέων

| Εβδομάδα* | Παραδοτέο |
| --- | --- |
| 1 | <sup><a href="#1"> Περιγραφή των αναγκών και των στόχων για το μάθημα </a></sup> |
| 2 | <sup><a href="#2"> βιογραφικό: Σελίδα με jekyll </a></sup> | 
| 3 | <sup><a href="#3"> Προσθήκη ανακοίνωσης </a></sup> |
| 4 | <sup><a href="#4"> create your own static site and blog generator </a></sup> |
| 5 | <sup><a href="#5"> Συμμετοχικό περιεχόμενο: A1 & A2 </a></sup> |
| 6 | <sup><a href="#6"> send notifications to your desktop-mobile </a></sup> |
| 7 | <sup><a href="#7"> βιογραφικό: PDF με pandoc & latex </a></sup> |
| 8 | <sup><a href="#8"> Προσθήκη μαθήματος Η' εξαμήνου </a></sup> |
| 9 | <sup><a href="#9"> create notifications on your server </a></sup> |
| 10 | <sup><a href="#10"> Συμμετοχικό περιεχόμενο: Β1 & Β2  </a></sup> |
| 11 | <sup><a href="#11"> performance monitoring </a></sup> |
| 12 | <sup><a href="#12"> Τελική αναφορά </a></sup> |

###### [1]

## Περιγραφή των αναγκών και των στόχων για το μάθημα:

Μέσω του μαθήματος "Τεχνολογία Λογισμικού", στοχεύω στη κατανόηση της θεωρίας και σχεδίασης των συστημάτων ανάπτυξης λογισμικού.
Κύριος στόχος μου για το μάθημα είναι ο εμπλουτισμός των βασικών γνώσεών μου γύρω από την πλατφόρμα του Github, ένα από τα σημαντικότερα εργαλεία για την αποδοτικότερη οργάνωση 
και σύνταξη αλλαγών σε μορφή κώδικα. Με τη συχνή παρακολούθηση των διαλέξεων και εργαστηρίων όσο αφορά στην οργάνωση λογισμικού, καθώς και την έμφαση και αφιέρωση του 
απαραίτητου χρόνου στη διαδικασία ανάπτυξης και συντήρησης αυτού, θεωρώ πως η προσαρμογή μου στο αντικείμενο του μαθήματος θα είναι ικανοποιητική.

###### [2]

## βιογραφικό: Σελίδα με jekyll

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

**green light**: ✔️ 

**Αποθετήριο αιτήματος**: https://github.com/geopala/sitegr/tree/2007051

**Αρχείο .md ανακοίνωσης**: https://github.com/geopala/sitegr/blob/2007051/all_collections/_posts/2021-05-21-episkepsi-proedrou.md

**pull request**: ✔️ 

**Pull Request**: https://github.com/ioniodi/sitegr/pull/222

**Netlify**: https://deploy-preview-222--epic-hamilton-da9ac8.netlify.app/posts/2021/05/21/episkepsi-proedrou/

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
## Συμμετοχικό περιεχόμενο: A1 & A2

## A1

## WhatsApp

Εικόνα: https://geopala.netlify.app/gallery/whatsapp/

Αποθετήριο εικόνας: https://github.com/geopala/_gallery/blob/2007051/whatsapp.md

## Πληροφορίες:
Το WhatsApp Messenger είναι μία ιδιόκτητη εφαρμογή άμεσης ανταλλαγής μηνυμάτων για smartphones. Εκτός από την ανταλλαγή μηνυμάτων κειμένου, οι 
χρήστες μπορούν να στείλουν ο ένας στον άλλο εικόνες, βίντεο, ήχους και μηνύματα πολυμέσων.

**Πηγή:** https://www.whatsapp.com/

## Windows 11 

Εικόνα: https://geopala.netlify.app/gallery/windows11/

Αποθετήριο εικόνας: https://github.com/geopala/_gallery/blob/2007051/windows11.md

## Πληροφορίες:
Τα Windows 11 είναι μια επικείμενη μεγάλη έκδοση του λειτουργικού συστήματος Windows NT που αναπτύχθηκε από τη Microsoft. Θεωρείται ότι είναι ο διάδοχος των Windows 10.
Τα Windows 11 προσφέρουν έναν ήρεμο και δημιουργικό χώρο όπου μπορείτε να ασχοληθείτε με ό,τι σας αρέσει μέσα από μια νέα εμπειρία. Από το ανανεωμένο μενού Έναρξη έως τους νέους τρόπους για να συνδέεστε με τα αγαπημένα σας πρόσωπα, ειδήσεις, παιχνίδια και περιεχόμενο, τα Windows 11 σας χαρίζουν ένα χώρο για να σκέφτεστε, να εκφράζεστε και να δημιουργείτε με φυσικό τρόπο.

**Πηγή:** https://www.microsoft.com/el-gr/windows/windows-11

# A2
## Διαφάνιες και Χρονολόγιο

Διαφάνιες: https://geopala.netlify.app/slides/gui/

Αποθετήριο διαφανιών: https://github.com/geopala/site/blob/master/_slides/gui.md 

Χρονολόγιο: https://geopala.netlify.app/timeline/systems/

Αποθετήριο χρονολογίου: https://github.com/geopala/site/blob/2007051/_timeline/systems.md

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

## βιογραφικό: PDF με pandoc & latex

Αρχείο tex: https://github.com/geopala/sw-images/blob/main/cv.tex

Αρχείο pdf: https://github.com/geopala/sw-images/blob/main/cv.pdf

Αρχείο log: https://github.com/geopala/sw-images/blob/main/cv.log

Δημιουργία αρχείου tex: https://asciinema.org/a/430004

Δημιουργία pdf: https://asciinema.org/a/430005

## Υλοποίηση:
• Εγκατάσταση των απαραίτητων πακέτων: ```sudo apt-get install pandoc```&```sudo apt-get install texlive-latex-base```.

• Έναρξη καταγραφής terminal: ```asciinema rec -i 0.2```.

• Fork αποθετηρίου bio: ```git clone https://github.com/geopala/online-cv.git```

• Δημιουργία pdf location: ```mkdir pdf```

• Δημιουργία αρχείου tex: ```pandoc https://geopala.github.io/online-cv/ -o cv.tex -s```

• Μετατροπή σε pdf: ```pdflatex cv.tex```

• Ολοκλήρωση asciicast: ```exit```.

**Αποτελέσματα:**

![pdf](https://github.com/geopala/sw-images/blob/main/resume.png)

**Πηγή:** https://pandoc.org/getting-started.html#step-6-converting-a-file

###### [8]

## Αίτημα ενσωμάτωσης στην ιστοσελίδα: Προσθήκη μαθήματος Η' εξαμήνου

## Υλοποίηση:
### Προσθήκη μαθήματος ελεύθερης επιλογής "Μουσείο & Κοινωνικά Δίκτυα" του Η' εξαμήνου.

**Issue**: https://github.com/ioniodi/sitegr/issues/220

**green light**: **good first issue**

**Αποθετήριο αιτήματος**: https://github.com/geopala/sitegr/tree/2007051

**Αρχείο .md μαθήματος**: https://github.com/geopala/sitegr/blob/2007051/all_collections/_courses/museum-and-social-networks.md

**pull request**: ✔️

**Pull Request**: https://github.com/ioniodi/sitegr/pull/224

**Netlify**: https://deploy-preview-224--epic-hamilton-da9ac8.netlify.app/courses/museum-and-social-networks/

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

## Συμμετοχικό περιεχόμενο: Β1 και Β2

# B1
## Μελέτη Περίπτωσης: WhatsApp

Αρχείο μελέτης: https://github.com/geopala/site/blob/2007051/_case-study/whatsapp.md

Κείμενο μελέτης: https://github.com/geopala/site/blob/2007051/_case-study/cs-whatsapp.md

Μελέτη περίπτωσης: https://geopala.netlify.app/case-study/whatsapp/

## Πληροφορίες:
Αναφορά και σύντομη ανάλυση της ιδιωτικότητας και ασφάλειας που προσφέρει το WhatsApp Messenger ως μέσο ανταλλαγής μηνυμάτων και αρχείων.

**Πηγή:** [Is WhatsApp safe?](https://parade.com/1201015/stephanieosmanski/is-whatsapp-safe/)

# B2
## Βιογραφία: Jan Koum

Αρχείο βιογραφίας: https://github.com/geopala/site/blob/2007051/_biography/jan-koum.md

Αρχείο σύντομης βιογραφίας: https://github.com/geopala/site/blob/2007051/_biography/bio-koum.md

Βιογραφία: - (Δεν γινόταν deploy στο netlify, καθώς το fork του repo **images** μέσω branch **2007051** οδηγούσε στο **pibook/images** και όχι στο **geopala/images**)

**Πηγές:**

[Jan Koum](https://www.thefamouspeople.com/profiles/jan-koum-7407.php)

###### [11]

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

###### [12]

## Τελική αναφορά

## Συμπεράσματα:

Συνοψίζοντας, με την ολοκλήρωση του μαθήματος "Τεχνολογία Λογισμικού", θεωρώ πως έχω αποκομίσει πολύ μεγάλα οφέλη.
Έχοντας παραδώσει συνολικά όλα τα παραδοτέα στην επαναληπτική εξεταστική του Σεπτεμβρίου, εξοικειώθηκα σε μεγάλο βαθμό τόσο με την πλατφόρμα του Github όσο και με την χρήση Linux 
Terminal (με το εργαλείο **Oracle VM Virtualbox**), ήρθα σε επαφή για πρώτη φορά με το εργαλείο **Asciinema** για καταγραφή terminal, καθώς και το **Netlify** για deploy του 
προσωπικού μου site.
Στο σύνολό τους τα παραδοτέα με βοήθησαν να αναπτύξω σημαντικές δεξιότητες για την μετέπειτα πορεία μου στην αγορά εργασίας, με γνώσεις που έλαβα και χρησιμοποίησα απ'ευθείας 
πρακτικά στις διάφορες εργασίες που ανέλαβα. Η δομή του μαθήματος ήταν άκρως ενδιαφέρουσα καθώς τα εβδομαδιαία παραδοτέα βοήθησαν στην σταδιακή αφομοίωση και χρήση των εν λόγω 
γνώσεων. Τέλος, θέλω να ευχαριστήσω τον καθηγητή και βοηθούς του μαθήματος για τη διδασκαλία και την άμεση ανταπόκριση, καθώς όταν χρειάστηκα την οποιαδήποτε βοήθεια/οδηγία 
σχετικά με την εκπόνηση των παραδοτέων, με εξυπηρέτησαν άμεσα.

## Ανάλυση παραδοτέων:

**Εβδομάδα 1)** Περιγραφή των αναγκών και των στόχων για το μάθημα | ✔️ (100%)

**Εβδομάδα 2)** βιογραφικό: Σελίδα με jekyll | ✔️ (100%)

**Εβδομάδα 3)** Προσθήκη ανακοίνωσης | ✔️ (100%)

**Εβδομάδα 4)** create your own static site and blog generator | ✔️ (100%)

**Εβδομάδα 5)** Συμμετοχικό περιεχόμενο: A1 & A2 | ✔️ (100%)

**Εβδομάδα 6)** send notifications to your desktop-mobile | ✔️ (100%)

**Εβδομάδα 7)** βιογραφικό: PDF με pandoc & latex | ✔️ (100%)

**Εβδομάδα 8)** Προσθήκη μαθήματος Η' εξαμήνου | ✔️ (80%)

**Εβδομάδα 9)** create notifications on your server | ✔️ (100%)

**Εβδομάδα 10)** Συμμετοχικό περιεχόμενο: Β1 & Β2 | ✔️ (80%)

**Εβδομάδα 11)** performance monitoring | ✔️ (100%)

**Εβδομάδα 12)** Τελική αναφορά | ✔️ (100%)

## Βιβλιογραφία:

[Ubuntu tutorials](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)

[Oracle VM Virtual Box](https://www.virtualbox.org/manual/ch01.html)

[Deleting a submodule](https://asciinema.org/a/3gFABL73VAJ21UoA4SVzlfRaf)

[Adding a submodule](https://asciinema.org/a/9vhZSNlQkO0KwH6lY6gPdWWB8)

[Updating a submodule](https://asciinema.org/a/bUMPJqXb9sepWRdlJPyToMpwl)
