### ΟΝΟΜΑΤΕΠΩΝΥΜΟ: ΦΩΤΕΙΝΗ ΠΑΛΛΙΔΟΥ

### ΑΜ: Π2014201

### [Github Profile](https://github.com/p14pall/)

### [Προσωπικό Site (Netlify)](https://p14pall.netlify.app/)

| Εβδομάδα* | Παραδοτέο |
| --- | --- |
| 1 | <sup><a href="#1"> Φορκ του αποθετηρίου και δημιουργία της σελίδας της αναφοράς με τα προσωπικά στοιχεία σας, της σύνοψης με αυτόν τον πίνακα περιεχομένων, και συγγραφή της εισαγωγής με περιγραφή των αναγκών και των στόχων σας για το αντίστοιχο μάθημα </a></sup> |
| 2 | <sup><a href="#2"> βιογραφικό </a></sup> | 
| 3 | <sup><a href="#3"> Αίτημα ενσωμάτωσης στην ιστοσελίδα: Προσθήκη ανακοίνωσης </a></sup> |
| 4 | <sup><a href="#4"> Άσκηση γραμμής εντολών: create your own static site and blog generator </a></sup> |
| 5 | <sup><a href="#5"> Συμμετοχικό περιεχόμενο: A1 και Α2 </a></sup> |
| 6 | <sup><a href="#6"> Άσκηση γραμμής εντολών: create notifications on your server </a></sup> |
| 7 | <sup><a href="#7"> βιογραφικό: Δημιουργία PDF </a></sup> |
| 8 | Αίτημα ενσωμάτωσης στην ιστοσελίδα </a></sup> |
| 9 | <sup><a href="#9"> Άσκηση γραμμής εντολών: performance monitoring </a></sup> |
| 10 | <sup><a href="#10"> Συμμετοχικό περιεχόμενο: B1 και Β2 </a></sup> |
| 11 | <sup><a href="#11"> Άσκηση γραμμής εντολών: send notifications to your desktop-mobile </a></sup> |
| 12 | Τελική αναφορά |


##### [1]

## Εισαγωγή:
Μετά την πρώτη επαφή που είχαμε, μέσα από το μάθημα "Επικοινωνία Ανθρώπου-Υπολογιστή", με το github, επιθυμώ μέσα από το μάθημα της "Τεχνολογίας Λογισμικού" να εμβαθύνω και να μάθω καλύτερα τον τρόπο λειτουργίας του. Είναι μία από τις βασικές πλατφόρμες ανάπτυξης λογισμικού και ένα από τα χαρακτηριστικά του είναι ότι μπορούμε να γράφουμε έναν κώδικα σε τμήματα, να διαγράφουμε, να προσθέτουμε, να κάνουμε αλλαγές. Είναι πολύ χρήσιμο για την εκπόνηση της συγκεκριμένης εργασίας που έχουμε να βγάλουμε εις πέρας. Το μάθημα ευνοεί στην καλύτερη κατανόηση της θεωρίας και της σχεδίασης συστημάτων ανάπτυξης λογισμικού μέσω τεχνολογιών. Μέσα από την παρακολούθηση της θεωρίας και των εργαστηρίων, ο στόχος, που είναι η βελτίωση των δεξιοτήτων του φοιτητή, θα είναι περισσότερο εφικτός.

##### [2]

## Βιογραφικό:

**Link βιογραφικού:** https://p14pall.github.io/online-cv/

**Link αποθετηρίου βιογραφικού:** https://github.com/p14pall/online-cv

## Βήματα:

◉ Fork αποθετηρίου βιογραφικού https://github.com/sharu725/online-cv

◉ Διαγραφή και δημιουργία νέου branch **gh-pages** για το hosting με βάση τις οδηγίες

◉ Προσθήκη προσωπικών στοιχείων, εικόνας προφίλ και αλλαγή θέματος μέσω επεξεργασίας των **data.yml**, **config_yml**.

## Αποτέλεσμα:

![bio](https://github.com/p14pall/my-sw/blob/main/bio.png)

###### [3]

## Αίτημα ενσωμάτωσης στην ιστοσελίδα: Προσθήκη ανακοίνωσης

## Βήματα:

◉ Επιλογή ανακοίνωσης από την ιστοσελίδα του τμήματος μετά από έλεγχο στη λίστα με τις ήδη αναρτημένες

◉ Δημιουργία νέου issue

◉

◉

**Aρχείο ανακοίνωσης**: https://github.com/p14pall/sitegr/blob/2014201/all_collections/_posts/2021-10-21-ekdilwsi-kalwsorisma.md

**Issue**: https://github.com/ioniodi/sitegr/issues/225

**Pull request**:

**Συνεισφορά στο Netlify**:

## Αποτέλεσμα:

##### [4]

## Άσκηση γραμμής εντολών: create your own static site and blog generator

Asciinema link: https://asciinema.org/a/451954

## Βήματα:

◉ Εγκατάσταση απαραίτητων πακέτων ``sudo pacman -Syu hugo``

◉ Έναρξη εγγραφής τερματικού ``asciinema rec -i 0.2``

◉ Δημιουργία νέας ιστοσελίδας ``hugo new site quickstart``

◉ Επιλογή νέου location ``git init``

◉ Επιλογή και εγκατάσταση theme ``git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke``

◉ Hosting της νέας ιστοσελίδας ``hugo server -D``

◉ Δημιουργία νέας ανάρτησης ``hugo new posts/first-post.md``

◉ Επεξεργασία ανάρτησης ``nano content/posts/first-post.md``

◉ Χτίσιμο τελικής ιστοσελίδας ``hugo -D``

◉ Ολοκλήρωση εγγραφής τερματικού ``exit``

## Αποτέλεσμα:
![hugo](https://github.com/p14pall/my-sw/blob/main/2014201_hugo.png)

**Πηγή:** https://gohugo.io/getting-started/usage/

##### [5]

## Συμμετοχικό περιεχόμενο: A1 και A2

## A1

## WeChat

Είκονα στο προσωπικό site: https://p14pall.netlify.app//gallery/wechat/

Αποθετήριο εικόνας: https://github.com/p14pall/_gallery/blob/master/wechat.md

## Πληροφορίες:
Το WeChat είναι μια κινεζική εφαρμογή άμεσων μηνυμάτων, κοινωνικών μέσων και πληρωμών για κινητά πολλαπλών χρήσεων που αναπτύχθηκε από την Tencent. Κυκλοφόρησε για πρώτη φορά το 
2011, έγινε η μεγαλύτερη αυτόνομη εφαρμογή για κινητά στον κόσμο το 2018, με πάνω από 1 δισεκατομμύριο ενεργούς χρήστες μηνιαίως. Το WeChat είναι κάτι περισσότερο από μια 
εφαρμογή ανταλλαγής μηνυμάτων και κοινωνικής δικτύωσης – είναι ένας τρόπος ζωής για περισσότερους από ένα δισεκατομμύριο χρήστες σε όλο τον κόσμο. Συζητήστε και πραγματοποιήστε 
κλήσεις με φίλους, μοιραστείτε τις αγαπημένες στιγμές της ζωής σας, απολαύστε λειτουργίες πληρωμής μέσω κινητού τηλεφώνου και πολλά άλλα.

**Πηγή:** https://play.google.com/store/apps/details?id=com.tencent.mm&hl=el&gl=US

## Windows Vista

Είκονα στο προσωπικό site: https://p14pall.netlify.app//gallery/windows-vista/ 

Αποθετήριο εικόνας: https://github.com/p14pall/_gallery/blob/master/windows-vista.md

## Πληροφορίες:
Τα Windows Vista είναι μια σημαντική έκδοση του λειτουργικού συστήματος Windows NT που αναπτύχθηκε από τη Microsoft. Ήταν ο άμεσος διάδοχος των Windows XP, τα οποία κυκλοφόρησαν 
πέντε χρόνια πριν, τότε ήταν το μεγαλύτερο χρονικό διάστημα μεταξύ διαδοχικών εκδόσεων λειτουργικών συστημάτων επιτραπέζιων υπολογιστών Microsoft Windows. Η ανάπτυξη 
ολοκληρώθηκε στις 8 Νοεμβρίου 2006 και τους επόμενους τρεις μήνες κυκλοφόρησε σταδιακά σε κατασκευαστές υλικού και λογισμικού υπολογιστών, επιχειρηματικούς πελάτες και κανάλια 
λιανικής. Είναι η πρώτη έκδοση των Windows που διατίθεται μέσω μιας πλατφόρμας ψηφιακής διανομής. Οι νέες δυνατότητες των Windows Vista περιλαμβάνουν ένα ενημερωμένο γραφικό 
περιβάλλον χρήστη και οπτικό στυλ με την ονομασία Aero, ένα νέο στοιχείο αναζήτησης που ονομάζεται Αναζήτηση Windows, επανασχεδιασμένο υποσύστημα δικτύωσης, ήχου, εκτύπωσης και 
εμφάνισης, καθώς και νέα εργαλεία πολυμέσων όπως το Windows DVD Maker. Τα Vista είχαν στόχο να αυξήσει το επίπεδο επικοινωνίας μεταξύ συστημάτων σε ένα οικιακό δίκτυο, 
χρησιμοποιώντας τεχνολογία peer-to-peer για να απλοποιήσει την κοινή χρήση αρχείων και πολυμέσων μεταξύ υπολογιστών και συσκευών. Ο πρωταρχικός στόχος της Microsoft με τα 
Windows Vista ήταν να βελτιώσει την κατάσταση ασφάλειας στο λειτουργικό σύστημα Windows.

**Πηγή:** https://el.wikipedia.org/wiki/Windows_Vista

## Α2

## Διαφάνιες και Χρονολόγιο

Διαφάνιες στο προσωπικό site: https://p14pall.netlify.app//slides/gui/

Αποθετήριο διαφανιών: https://github.com/p14pall/site/blob/master/_slides/gui.md

Χρονολόγιο: https://p14pall.netlify.app//timeline/systems/

Αποθετήριο χρονολογίου: https://github.com/p14pall/site/blob/master/_timeline/systems.md

##### [6]

## Άσκηση γραμμής εντολών: create notifications on your server

Asciinema link: https://asciinema.org/a/453096 

## Βήματα:

◉ Εγκατάσταση απαραίτητων πακέτων ``sudo apt-get install mosquitto-clients``

◉ Έναρξη εγγραφής τερματικού ``asciinema rec -i 0.2``

◉ Εκκίνηση mosquitto service ``mosquitto``

◉ Subscribe σε νέο topic ``mosquitto_sub -h localhost -t example``

◉ Αποστολή δοκιμαστικού μηνύματος σε δεύτερο παράθυρο terminal ``mqtt_pub -h localhost -t example -m "Hi there!"`` 

◉ Εντοπισμός IP ``ifconfig``

◉ Setup του παραπάνω topic στο **MQQT Client** app

◉ Αποστολή μηνύματος στη συσκευή-server ``mqtt_pub -h localhost -t example -m "Hopefully this works :)"``

◉ Ολοκλήρωση εγγραφής τερματικού ``exit``

## Αποτέλεσμα:
![mqqt-hithere](https://github.com/p14pall/my-sw/blob/main/mqtt-hithere.png)
![mqtt-client](https://github.com/p14pall/my-sw/blob/main/mqtt-client.png)
![mqtt-setup](https://github.com/p14pall/my-sw/blob/main/mqqt-setup.png)
![mqtt-topic](https://github.com/p14pall/my-sw/blob/main/mqqt-topic.png)
![mqtt-results](https://github.com/p14pall/my-sw/blob/main/mqtt-results.png)

**Πηγή:** https://mosquitto.org/man/mosquitto-8.html

##### [7]

## Βιογραφικό: Δημιουργία PDF

Asciinema link: https://asciinema.org/a/453279

Αρχείο PDF: https://github.com/p14pall/my-sw/blob/main/my-cv.pdf

Αρχείο log: https://github.com/p14pall/my-sw/blob/main/my-cv.log

Αρχείο tex: https://github.com/p14pall/my-sw/blob/main/my-cv.tex

## Βήματα:

◉ Εγκατάσταση απαραίτητων πακέτων ``sudo apt-get install pandoc``, ``sudo apt-get install texlive-latex-base``

◉ Έναρξη εγγραφής τερματικού ``asciinema rec -i 0.2``

◉ Fork προσωπικού αποθετηρίου βιογραφικού ``git clone https://github.com/p14pall/online-cv.git``

◉ Αλλαγή directory στο παραπάνω forked folder ``cd online-cv``

◉ Δημιουργία φακέλου pdf ``mkdir pdf``

◉ Δημιουργία tex αρχείου ``pandoc https://p14pall.github.io/online-cv/ -o my-cv.tex -s`` 

◉ Δημιουργία pdf αρχείου ``pdflatex my-cv.tex``

◉ Ολοκλήρωση εγγραφής τερματικού ``exit``

## Αποτέλεσμα:
![my-cv](https://github.com/p14pall/my-sw/blob/main/my-cv.png)

**Πηγή:** https://linuxhint.com/convert-tex-latex-file-to-pdf/

##### [8]

## Αίτημα ενσωμάτωσης στην ιστοσελίδα: Προσθήκη ανακοίνωσης

##### [9]

## Άσκηση γραμμής εντολών: performance monitoring

Asciinema link py-spy: https://asciinema.org/a/454328

Asciinema link hyperfine: https://asciinema.org/a/454321

Flamegraph: https://github.com/p14pall/my-sw/blob/main/result.svg

Hyperfine output: https://github.com/p14pall/my-sw/blob/main/output

**Scripts που χρησιμοποιήθηκαν:**

https://github.com/p14pall/my-sw/blob/main/main.py

https://github.com/p14pall/my-sw/blob/main/script1.py

https://github.com/p14pall/my-sw/blob/main/script2.py

## Βήματα:

◉ Εγκατάσταση απαραίτητων πακέτων ``pip3 install py-spy``, ``git clone --depth 1 https://github.com/brendangregg/FlameGraph``, ``apt-get install wget``, ``wget https://github.com/sharkdp/hyperfine/releases/download/v1.11.0/hyperfine_1.11.0_amd64.deb``, ``sudo dpkg -i hyperfine_1.11.0_amd64.deb``

◉ Έναρξη εγγραφής τερματικού ``asciinema rec -i 0.2``

◉ Επιλογή ενός απλού multiprocessing script **main.py**

◉ Αλλαγή location σε Desktop ``cd Desktop``

◉ Performance monitoring **main.py** ``py-spy record -o result.svg -- python3 main.py``

◉ Επιλογή 2 νέων print script και εκτύπωση περιεχομένου αυτών ``cat script1``, ``cat script2``

◉ Σύγκριση με hyperfine ``hyperfine 'python script1.py' 'python script2.py'``

◉ Εξαγωγή αρχείου output ``hyperfine -i --export-json output 'python script1.py' 'python script2.py'``

◉ Ολοκλήρωση εγγραφής τερματικού ``exit``

## Αποτέλεσμα:
![flamegraph](https://github.com/p14pall/my-sw/blob/main/flamegraph.png)

**Πηγή:** 

https://github.com/benfred/py-spy#usage

https://github.com/sharkdp/hyperfine#usage

##### [10]

## Συμμετοχικό περιεχόμενο: B1 και B2

## B1

## Μελέτη Περίπτωσης: Είναι το WeChat ασφαλές;

Αποθετήριο μελέτης περίπτωσης: https://github.com/p14pall/site/blob/master/_case-study/wechat.md

Αποθετήριο κειμένου μελέτης: https://github.com/p14pall/site/blob/master/_case-study/cs-wechat.md

Μελέτη Περίπτωσης: https://p14pall.netlify.app//case-study/wechat/

## Πληροφορίες:
Την τελευταία δεκαετία, το WeChat έχει εγείρει μεγάλη ανησυχία για την ασφάλεια και το απόρρητο των χρηστών.

**Πηγή:** https://foundation.mozilla.org/en/privacynotincluded/wechat/

## B2

## Βιογραφία:

Αποθετήριο βιογραφίας: https://github.com/p14pall/site/blob/master/_biography/allen-zhang.md

Αποθετήριο κειμένου βιογραφίας: https://github.com/p14pall/site/blob/master/_biography/bio-zhang.md

Βιογραφία: https://p14pall.netlify.app//biography/allen-zhang/

## Πληροφορίες:
Ο Allen Zhang είναι Κινέζος προγραμματιστής υπολογιστών και executive στέλεχος του WeChat και του Foxmail.

**Πηγή:** https://supchina.com/2019/01/17/china-business-corner-wechat-founder-allen-zhang-and-the-tencent-conference/

##### [11]

## Άσκηση γραμμής εντολών: send notifications to your desktop-mobile

Asciinema link ntfy: https://asciinema.org/a/454357

Asciinema link ntfy[telegram]: https://asciinema.org/a/454363

## Βήματα:

◉ Εγκατάσταση απαραίτητων πακέτων ``sudo pip install ntfy``, ``pip install ntfy[telegram]``

◉ Έναρξη εγγραφής τερματικού ``asciinema rec -i 0.2``

◉ Testing του ntfy με διάφορα notifications ``notify-send --urgency=(critical, low) "text"``, ``ntfy done sleep 5``

◉ Setup και configure του Telegram στο terminal ``ntfy -b telegram send "Telegram configured for ntfy"``

◉ Setup και configure του Telegram στο κινητό μέσω token από **BotFather**

◉ Αποστολή μηνύματος από terminal στο bot της συσκευής ``ntfy -b telegram send "text"``

◉ Ολοκλήρωση εγγραφής τερματικού ``exit``

## Αποτέλεσμα:
![ntfy_name](https://github.com/p14pall/my-sw/blob/main/ntfy_mynameis.png)

![ntfy_weather](https://github.com/p14pall/my-sw/blob/main/ntfy_weather.png)

![ntfy_umbrella](https://github.com/p14pall/my-sw/blob/main/ntfy_umbrella.png)

![ntfy_sleep](https://github.com/p14pall/my-sw/blob/main/ntfy_sleep.png)

![telegram_setup](https://github.com/p14pall/my-sw/blob/main/telegram_setup.jpg)

![telegram_text](https://github.com/p14pall/my-sw/blob/main/telegram_text.jpg)

**Πηγή:**

https://github.com/dschep/ntfy#telegram---telegram

https://core.telegram.org/bots#3-how-do-i-create-a-bot

##### [12]

## Τελική αναφορά:
