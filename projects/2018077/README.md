<h1> Τεχνολογία Λογισμικού </h1>

<h2> Ονοματεπώνυμο : Λάζαρη Αικατερίνη - Μαρία</h2>
<h2> ΑΜ : Π2018077</h2>

------------------------------------------------------------------------------------------------------------------------------------------------------------------

| Εβδομάδα | Παραδοτέο |                                                                                                           
| --- | --- |                                                                                                                        
| 1 | [Στόχοι](#Στόχοι) |
| 2 | [Βιογραφικό Jekyll](#Βιογραφικό-Jekyll) |
| 3 | [Αίτημα ενσωμάτωσης στην ιστοσελίδα](#Αίτημα-ενσωμάτωσης-στην-ιστοσελίδα) |        
| 4 | [Άσκηση γραμμής εντολών Weather & Internet Speed Notification](#Άσκηση-γραμμής-εντολών-Weather-&-Internet-Speed-Notification) |
| 5 | [Συμμετοχικό περιεχόμενο HTML5 & Rasberry Pi OS](#Συμμετοχικό-περιεχόμενο-HTML5-&-Rasberry-Pi-OS) |
| 6 | [Άσκηση γραμμής εντολών Static Site with GitHub Pages](#Άσκηση-γραμμής-εντολών-Static-Site-with-GitHub-Pages) |
| 7 | [Βιογραφικό παραγωγή PDF](#Βιογραφικό-παραγωγή-PDF) |
| 8 | [Αίτημα ενσωμάτωσης στην ιστοσελίδα 2](#Αίτημα-ενσωμάτωσης-στην-ιστοσελίδα-2) |
| 9 | [Άσκηση γραμμής εντολών Twilio API](#Άσκηση-γραμμής-εντολών-Twilio-API) |
| 10 | [Συμμετοχικό περιεχόμενο Sonic Pi & Eben Upton](#Συμμετοχικό-περιεχόμενο-Sonic-Pi-&-Eben-Upton) |
| 11 | [Άσκηση γραμμής εντολών Docker Image](#Άσκηση-γραμμής-εντολών-Docker-Image)|
| 12 | [Συμπέρασμα](#Συμπέρασμα) |


|Εβδομαδιαίο βίντεο κουίζ|:heavy_check_mark: OR :x:| |
| --- | --- | --- |
|Alan Kay - at MIT EECS|:heavy_check_mark:| Απάντηση μέσο εφαρμογής |
|Τed Νelson - Computers for Cynics|:heavy_check_mark:| Απάντηση μέσο εφαρμογής |
|Alan Kay - Computing Simply|:heavy_check_mark:| Απάντηση στο README |
|Bret Victor - The Future of Programming|:heavy_check_mark:| Απάντηση μέσο εφαρμογής |
|Alan Kay - Programming|:heavy_check_mark:| Απάντηση μέσο εφαρμογής |
|Αlan Κay - Τuring Αward Lecture|:heavy_check_mark:| Απάντηση μέσο εφαρμογής |
|Alan Kay - Invention|:heavy_check_mark:| Απάντηση μέσο εφαρμογής |
|Jaron Lanier - Intertwingled |:heavy_check_mark:| Απάντηση μέσο εφαρμογής |
|Alan Kay - Scaling |:heavy_check_mark:| Απάντηση μέσο εφαρμογής |
|alan kay future |:heavy_check_mark:| Απάντηση μέσο εφαρμογής |

##
## Στόχοι

**Στόχοι :**
Σύμφωνα με την βιβλιογραφία, του [λίνκ του μαθήματος στην ιστοσελίδα του τμήματος](https://di.ionio.gr/gr/studies/undergraduate-studies/courses/614/) , το [GitHub λίνκ](https://github.com/courses-ionio/sw) και μετά από τα εισαγωγικά μαθήματά, προσδοκώ την ενασχόληση με τον τρόπο κατασκευής διαδραστικού λογισμικού. Ουσιαστικά, θα είναι η “συνέχεια” από το αντίστοιχο μάθημα Επικοινωνία Ανθρώπου Υπολογιστή. Στο προηγούμενο μάθημα, ασχοληθήκαμε με τον τρόπο που γίνετε η δίαδραση  και τώρα θα εστιάσουμε στον τρόπο με τον οποίο πραγματοποιείται. Αλώστε, σύμφωνα με τις ασκήσεις που έχουμε κληθεί να παραδώσουμε εντός του εξαμήνου αποδεικνύεται η φύση του μαθήματος.



##
## Βιογραφικό Jekyll

Τα πρώρα cimmites αφορούσαν ένα από τα προτεινόμενα έτυμα βιογραφικά. Τροποποίησα κατάλληλα το `data.yml` αρχείο ώστε να εμφανίζονται τα  προσωπικά μου στοιχεία και άλλαξα το χρωματικό θέμα από μπλε σε πορτοκαλί. [Github Repo](https://github.com/KaterinaLaz/online-cv) [Link](https://katerinalaz.github.io/online-cv/) πρώτου βιογραφικού. 

![εικόνα](https://user-images.githubusercontent.com/56299928/117570139-b407de00-b0d1-11eb-9944-ed6018610113.png)

Κατά το πέρας των εβδομάδων, βρήκα ένα δωρεάν [HTML/CSS Resume](https://sampleresumetemplate.net/) και εργάστηκα πάνω σε αυτό. Το αρχικό Resume αποτελούταν από ένα `.html` και `.scc` αρχείο. Έτσι  λοιπόν, δημιούργησα ένα `details.yml` αρχείο το οποίο περιέχει τα στοιχεία μου.  Στην συνέχεια, τροποποίησα τον **HTML** κώδικα έτσι ώστε να αντλεί τα στοιχεία από το `details.yml` αρχείο. 
Με οδηγό της [οδηγίες του εργαστηρίου](https://github.com/courses-ionio/sw-lab) έκανα **build** το βιογραφικό ως site και στην συνέχεια με την εντολή `jekyll serve - -host 0.0.0.0 &` το site γίνετε προσβάσιμο από τον **browser**. 

![εικόνα](https://user-images.githubusercontent.com/56299928/117570362-735c9480-b0d2-11eb-989c-41b7d3b23dd3.png)

* [link βιογραφικού](https://katerinalaz.github.io/site-cv/)
* [GitHub Repo](https://github.com/KaterinaLaz/site-cv)

*Asciinema*

 [![asciicast](https://asciinema.org/a/EdxpKLGNbtpoOboy5sgSzZB1F.svg)](https://asciinema.org/a/EdxpKLGNbtpoOboy5sgSzZB1F)


##
## Αίτημα ενσωμάτωσης στην ιστοσελίδα

Πραγματοποιήθηκε αίτημα ενσωμάτωσης στην [ανεπίσημη ιστοσελίδα του τμήματος](https://epic-hamilton-da9ac8.netlify.app/). Συγκεκριμένα έγινε προσθήκη του διηθητικού υπαλλήλου Κατερίνα Ράπτη. Το αντίστοιχο [Issue](https://github.com/ioniodi/sitegr/issues/64) .

 [Netlify](https://quirky-jennings-23151c.netlify.app/people/)
 
 ![εικόνα](https://user-images.githubusercontent.com/56299928/117575496-c7737300-b0ea-11eb-85e6-72be0a0e305c.png)

Λόγο του ότι η ιστοσελίδα που χρησιμοποιούμε για τα εβδομαδιαία βίντεο δεν μου εμφάνιζε την τελευταία ερώτηση, πρόσθεσα τις απαντήσεις μου στην αναφορά.
Οι απαντήσεις μου στο εβδομαδιαίο βίντεο  `Alan Kay computing simply` 
```

  * Ποιες ήταν οι βασικές ιδέες που επηρέασαν τον Αλαν Κεη στην κατασκευή νέου λογισμικού;
Sketch pad, δίκτυα και η simula. Ουσιαστικά τον επηρέασαν σε επίπεδο hardware αλλά και software.

  * Να δώσετε παράδειγμα από την προσωπική σας εμπειρία για λογισμικό με καλή και με κακή αρχιτεκτονική με αναφορά στα κριτήρια της επιλογής σας.
Θεωρώ οτι το λειτουργικό Linux είναι ένα παράδειγμα καλής αρχιτεκτονικής, υπάρχει ένας σταθερός πυρήνας και μπορείς  ανάλογα με το hardware και τις αποτίσεις σου να φτιάξεις ένα κέλυφος στα μέτρα σου ή ακόμα και αν πάρεις μια έτυμη διανομή μπορείς να την παραμετροποιήσεις σε ένα ικανοποιητικό επίπεδο.Ουσιαστικά, μπορεί να υπάρξει μια συνεργατική διαδικασία για την δημιουργία του λογισμικού. 

  * Ποια είναι τα βασικά δομικά στοιχεία στην αρχιτεκτονική του λογισμικού etoys και από που άντλησε ο Αλαν Κέη την έμπνευση για αυτά;
To etoys βασίζετε σε ένα γραφικό περιβάλλον όπου τα αντικείμενα της γλώσσας απεικονίζονται με εικόνες. 

  * Ποια είναι κάποια από τα λάθη των σύγχρονων λειτουργικών συστημάτων σύμφωνα με τον Αλαν Κέη;
Ότι δεν έχουν έναν δυναμικό σχεδιασμό 
```

##
## Άσκηση γραμμής εντολών Weather & Internet Speed Notification

Στην πρώτη άσκηση στην γραμμή εντολών χρησιμοποίησα τα εργαλεία `wttr`  ,  `speedtest-cli`  και  `notify`. Αυτό που πραγματοποιείτε είναι μέσο ενός `.sh` αρχείου να έρχεται ειδοποίηση για τον καιρό της σημερινής μέρα καθώς και για την ταχύτητα της σύνδεσης μου στο διαδίκτυο την συγκεκριμένη χρονική στιγμή.\
**Ο τρόπος που εργάστηκα**: Για αρχή δημιούργησα ένα αρχείο `day.sh` που μέσα στο οποίο τοποθέτησα τις εντολές  
`curl wttr.in/Corfu.Greece?format=3`  και  `speedtest-cli` ώστε στην αρχή να έρθει η ειδοποίηση για τον καιρό της σημερινής μέρας στην περιοχή μου και έπειτα να γίνει το **speed test**. Η εντολή `speedtest-cli` αργεί λίγο όπως παρατηρούμε από το **GIF** οπότε επέλεξα να προσθέσω ένα ενδιάμεσο μήνυμα που ειδοποιεί για αυτήν την καθυστέρηση. Προτίμησα για τις  κύριες λειτουργίες του αρχείου, δηλαδή **καιρός** και **speed test**, να εμφανίζετε το εικονίδιο στα αριστερά του πάνελ ένα `i (info)`.   
Στην  συγκεκριμένη άσκηση υπάρχει εκτός από το asciinema και **GIF** επιδίδει τα αποτελέσματα της άσκησης εμφανίζονται στο γραφικό περιβάλλον του υπολογιστή μου.
 
 *GIF*
 
 ![simplescreenrecorder-2021-03-14](https://user-images.githubusercontent.com/56299928/115073725-68627a00-9f01-11eb-8c55-e0ceea44c189.gif)
 
 *Asciinema*
 
  [![asciicast](https://asciinema.org/a/LdAuPrkG9fXmhe9mUTJb3VAP2.svg)](https://asciinema.org/a/LdAuPrkG9fXmhe9mUTJb3VAP2)
  
 *Πηγές :*\
 Για το [wttr](https://github.com/chubin/wttr.in) \
 Για το [speedtest-cli](https://github.com/sivel/speedtest-cli)
 

##
## Συμμετοχικό περιεχόμενο HTML5 & Rasberry Pi OS

Στην αρχή αντιμετώπισα προβλήματα με την εισαγωγή των **submodules** στο repository μου. Μετά από την βοηθητική συζήτηση στα [Discussions](https://github.com/courses-ionio/sw/discussions/936) και σε συνδυασμό με το [netlify DOC – Deploy keys](https://docs.netlify.com/configure-builds/repo-permissions-linking/#git-submodules) και [Connecting to GitHub with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) κατάφερα και πρόσθεσα τα submodules  `_gallery`  και  `images`  με επιτυχία.

Οι δύο φωτογραφίες που επέλεξα να προσθέσω είναι οι  `html5`  και  `raspberry pi os` . Η  `html5`  είναι ένα εργαλείο με το οποίο μπορούν να δημιουργηθούν ιστοσελίδες και διαδραστικό υλικό. Από την άλλη πλευρά, το  `pi – OS`  είναι ένα παραμετροποιήσιμο λειτουργικό σύστημα.

Είχα εντοπίσει το ακόλουθο πρόβλημα με το **netlify demo** : Οι αλλαγές που έχω πραγματοποιήσει στο χρονολόγιο δεν φαίνονται καθώς επίσης στις διαφάνειες και στις εικόνες εμφανίζετε ένα κενό πλαίσιο αντί της εικόνας. Αν ώμος γίνει “κλικ” πάνω στο κενό αυτό πλαίσιο η εικόνα εμφανίζετε κανονικά.\
Πλέον έχω επιλύσει το πρόβλημα και το **netlify demo** δουλεύει κανονικά .


**Links για nrtlify :**
  * Εικόνες netlify - site : [html5](https://affectionate-lewin-ee77b9.netlify.app//gallery/html5/) , [raspberry pi os](https://affectionate-lewin-ee77b9.netlify.app//gallery/raspberry-pi-os/) 
  * Διαφάνειες netlify - site : [html5](https://affectionate-lewin-ee77b9.netlify.app//slides/programming/) , [raspberry pi os](https://affectionate-lewin-ee77b9.netlify.app//slides/gui/)
  * Χρονολόγιο netlify - site : [html5](https://affectionate-lewin-ee77b9.netlify.app//timeline/programming/) , [raspberry pi os](https://affectionate-lewin-ee77b9.netlify.app//timeline/systems/)
  
**Links για GitHub Repo :**  
  * Εικόνες GitHub : [html5 image](https://github.com/KaterinaLaz/images/blob/ecae0d51112c5007cef15e00e177ebd055bdbfc2/html5.png) , [html5 thumd](https://github.com/KaterinaLaz/images/blob/ecae0d51112c5007cef15e00e177ebd055bdbfc2/html5-thumb.png) , [html5 gallery](https://github.com/KaterinaLaz/_gallery/blob/2bae51b2d88b9f76ebaac28bcab28fa9fd04caf4/html5.md) , [rasberry pi os image](https://github.com/KaterinaLaz/images/blob/ecae0d51112c5007cef15e00e177ebd055bdbfc2/raspberry-pi-os.png) , [rasberry pi os thumb](https://github.com/KaterinaLaz/images/blob/ecae0d51112c5007cef15e00e177ebd055bdbfc2/raspberry-pi-os-thumb.png) , [rasberry pi os gallery](https://github.com/KaterinaLaz/_gallery/blob/2bae51b2d88b9f76ebaac28bcab28fa9fd04caf4/raspberry-pi-os.md)
  * Διαφάνεις GitHub : [html5 slides](https://github.com/KaterinaLaz/site/blob/master/_slides/programming.md) , [raspbery pi os slides](https://github.com/KaterinaLaz/site/blob/master/_slides/gui.md)
  * Χρονολόγιο GitHub : [html5 timeline](https://github.com/KaterinaLaz/site/blob/master/_timeline/programming.md) , [raspbery pi os timeline](https://github.com/KaterinaLaz/site/blob/master/_timeline/systems.md)
  
  **Netlify Status badges :** [![Netlify Status](https://api.netlify.com/api/v1/badges/7dd38f91-23c2-4dfd-958a-a1106049f7df/deploy-status)](https://app.netlify.com/sites/affectionate-lewin-ee77b9/deploys)

*Πηγές :*\
Για το Pi-OS : [Raspderry Pi OS - Wiki](https://en.wikipedia.org/wiki/Raspberry_Pi_OS),
               [Raspderry Pi OS - official Site](https://www.raspberrypi.org/documentation/raspbian/),
               [Raspderry Pi OS - official Site](https://www.raspberrypi.org/software/)

Για την HTML5 : [HTML5 - Wiki](https://en.wikipedia.org/wiki/HTML5),
                [HTML5 - W3Schools](https://www.w3schools.com/html/html_media.asp),
                [HTML5: MULTIMEDIA - pdf](http://www.uobabylon.edu.iq/eprints/publication_6_4882_1610.pdf),


##
## Άσκηση γραμμής εντολών : Static Site with GitHub Pages

Στα πλαίσια της άσκησης *Βιογραφικό Jekyll* δημιούργησα ένα **static site** το οποίο στην αρχή δημιουργήταο με **jekyll** και μετά το κάνω host στο **GitHub Pages**.

 [GitHub Repo](https://github.com/KaterinaLaz/site-cv)
 
 *Asciinema*
 
 [![asciicast](https://asciinema.org/a/EdxpKLGNbtpoOboy5sgSzZB1F.svg)](https://asciinema.org/a/EdxpKLGNbtpoOboy5sgSzZB1F)


##
## Βιογραφικό παραγωγή PDF

Χρησιμοποίησα το εργαλείο Pandoc για να παράγετε ένα αρχείο .pdf στο οποίο να απεικονίζετε ορθά το περιεχόμενο του βιογραφικού μου. Η μεθοδολογία, *η οποία έχει καταγραφτεί*, είναι η ακόλουθη.\ 
Στην αρχή, παράγω ένα αρχείο με κατάληξη .pdf με μη αυτοματοποιημένο τρόπο και στην πορεία το κάνω push στο GitHub repo του βιογραφικού. Έπειτα, χρησιμοποιώ GitHub Hooks `post-commit` και `pre-commit` ώστε όταν γίνετε commit μια αλλαγή στο repo να παράγετε αυτόματα το αρχείο pdf και να γίνετε push στο  GitHub repo του βιογραφικού.\

Στο asciinema γίνετε και ένα συγκριτικό μεταξύ του πρώτου cv.pdf που προσαράχθηκε με τον χειροκίνητο τρόπο και του `cv.pdf` που παράχθηκε έπειτα από αλλαγή στο `index.html` αρχείο, αφού έγινε **commit στο GitHub repo του βιογραφικού**.\

Αντιμετώπισα αρκετές δυσκολίες κατά την διεξαγωγή αυτής της άσκησης. Αρχικά προσπαθούσα ανεπιτυχώς να δημιουργήσω ένα νέο αρχείο `cv.pdf` αντλούμενη από το `index.html` και με μεταδομένα το `_data/details.yml`. Στην πορεία, αφού άλλαξα μέθοδο, αντλούσα τα δεδομένα από το https://katerinalaz.github.io/site-cv/. Έπειτα από πολλές δοκιμές κατέληξα στο συμπέρασμα ότι αν πραγματοποιήσω μια αλλαγή στο σε κάποιο αρχείο του βιογραφικού, το GitHub Pages εμφανίζει τις αλλαγές μετά από κάποια δευτερόλεπτα, με αποτέλεσμα το cv.pdf που γινόταν push να μην ήταν ενημερωμένο. Έτσι κατέληξα να αντλώ την πληροφορία από τον σύνδεσμο http://0.0.0.0:4000 ο οποίος χρησιμοποιείται ως **localhost για το jekyll page του βιογραφικού**.

![εικόνα](https://user-images.githubusercontent.com/56299928/117571133-cdab2480-b0d5-11eb-91a4-936ca6c13b12.png)
  
*Asciinema*

   [![asciicast](https://asciinema.org/a/E8DL0NfUUWtg3iCsyh5uPVNlt.svg)](https://asciinema.org/a/E8DL0NfUUWtg3iCsyh5uPVNlt)

*Πηγές :*\
Για το cv-to-pdf : [Stackoverflow](https://stackoverflow.com/questions/26395374/what-can-i-control-with-yaml-header-options-in-pandoc),
                   [Stackoverflow](https://stackoverflow.com/questions/30376741/run-script-before-commit-and-include-the-update-in-this-commit)


##
## Αίτημα ενσωμάτωσης στην ιστοσελίδα 2

Το συγκεκριμένο παραδοτέο δεν υλοποιήθηκε.
Παίρνοντας ως οδηγό της μη ανανεωμένες οδηγίες “Για τα θέματα ενδιάμεσης δυσκολίας στο 2ο-3ο αίτημα ενσωμάτωσης το ζητούμενο είναι μια συνεισφορά που δείχνει μεγαλύτερη κατανόηση του συστήματος (π.χ., βελτίωση της τεκμηρίωσης ή της διαδικασίας συνεισφοράς, προσθήκη νέων σελίδων, βελτιώσεις στον κώδικα λίκουηντ, κτλ)” αποφάσισα να δημιουργήσω μια καινούρια στατική καρτέλα στο navigation bar με τίτλο “Ιδρυση” που θα ήταν στα πρότυπα του επίσημου σάιτ. Έπειτα από διευκρίνηση του διδάσκοντα κάτι τέτοιο δεν είναι αποδεκτό για δεύτερο έτυμα ενσωμάτωσης στην ιστοσελίδα. [Issue](https://github.com/ioniodi/sitegr/issues/185)\
Παραθέτω το [Netlify Demo](https://adoring-archimedes-ab72fc.netlify.app/) 

![εικόνα](https://user-images.githubusercontent.com/56299928/117576450-bfb5cd80-b0ee-11eb-92d7-36fd3a70e085.png)


##
## Άσκηση γραμμής εντολών Twilio API

Έγραψα το ακόλουθο κώδικα σε python (φαίνεται και στο asciinema) στην συνέχεια τον εκτέλεσα και μου ήρθε ένα μήνυμα στο κινητό μου (φαίνεται στο GIF).

~~~
from twilio.rest import Client                                                                                                                                  # Your Account SID from twilio.com/console                                      
account_sid = "ACda125daa4cb0e5fe521725e73ee9d660"                              
# Your Auth Token from twilio.com/console                                       
auth_token  = "xxxxxxxxxxxxxxxxxxxx"   //add my authorization token
client = Client(account_sid, auth_token)                                                                                                                      
message = client.messages.create(                                                   
   to="+xxxxxxxxxx",   //add my phone                                                          
   from_="+17027613349",                                                          
   body="Hello World ! ")                                                                                                                                      print(message.sid) 
~~~

*Asciinema*

[![asciicast](https://asciinema.org/a/cOauGslTKXkTtbb3mo6PcI88s.svg)](https://asciinema.org/a/cOauGslTKXkTtbb3mo6PcI88s)

*GIF*

![twilio](https://user-images.githubusercontent.com/56299928/115073303-ce023680-9f00-11eb-93b2-fd3e103ab9b0.gif)

*Πηγές :*\
[twilio GitHub](https://github.com/twilio/twilio-python),
[twilio messages DOC](https://www.twilio.com/docs/sms/send-messages)

##
## Συμμετοχικό περιεχόμενο Sonic Pi & Eben Upton

Στο δεύτερο παραδοτέο για το συμμετοχικό περιεχόμενο ασχολήθηκα με την γλώσσα Sonic Pi και τον δημιουργό του Raspberry Pi, Eden Upton. Η γλώσσα Sonic Pi είναι μια ιδιάζουσα περίπτωση καθώς αφορά τον κλάδου του μουσικού προγραμματισμού. 

Δεν κατάφερα να κάνω με επιτυχία Deploy το σάιτ στο Netlify με αποτέλεσμα να παραθέτω τα λίνκ από τα αντίστοιχα repository. 

| | | |
|---|---|---|
| site | [Sonic Pi](https://github.com/KaterinaLaz/site/blob/sw-test/_case-study/sonic-pi.md) | [Eben Upton](https://github.com/KaterinaLaz/site/blob/sw-test/_biography/eben-upton.md) |
| extras | [Sonic Pi](https://github.com/KaterinaLaz/extras/blob/master/sonic-pi.md) | [Eben Upton](https://github.com/KaterinaLaz/extras/blob/master/bio-eben-upton.md) | 

*Πηγές :*\
Για Sonic pi : [What is sonic pi](https://www.fdmgroup.com/what-is-sonic-pi-2/),
               [Sonic Pi - Getting Started With Sonic Pi](https://projects.raspberrypi.org/en/projects/getting-started-with-sonic-pi),
               [Sonic Pi - official site](https://sonic-pi.net/),
               [Live Coding Education - pdf](https://sonic-pi.net/files/articles/Live-Coding-Education.pdf),
               [Code Music with Sonic Pi - pdf](https://www.raspberrypi.org/magpi-issues/Essentials_Sonic_Pi-v1.pdf)
               
Για Eben Upton : [Eben Upton - Archivesit -> Interview with Eben Upton CBE](https://archivesit.org.uk/interviews/eben-upton-cbe/),
                 [Eben Upton - Wiki](https://en.wikipedia.org/wiki/Eben_Upton),
                 [Eben Upton - Linkedin](https://uk.linkedin.com/in/ebenupton)
              

##
## Άσκηση γραμμής εντολών Docker Image

Δημιούργησα ένα Docker Image για το site του βιογραφικού μου. 

*Asciinema*

[![asciicast](https://asciinema.org/a/JKEbuh1YCTQmqvsFolBpdL94K.svg)](https://asciinema.org/a/JKEbuh1YCTQmqvsFolBpdL94K)

*Πηγές :*\
[YouTube -> Creating your first Dockerfile, image and container](https://www.youtube.com/watch?v=hnxI-K10auY),
[Docker -> develop images](https://docs.docker.com/develop/develop-images/baseimages/)

##
## Συμπέρασμα 

Εντός του εξαμήνου ασχοληθήκαμε με τον αποδοτικό τρόπο δημιουργίας λογισμικού. Είδαμε πολλά παραδείγματα  λογισμικού είτε στις διαλέξεις είτε στις βιντεοδιαλέξεις και συγκρίναμε τους τρόπους δημιουργίας του λογισμικού του τότε με το σήμερα. Παράλληλα, συζητήσαμε τα οφέλη που έχει η δημιουργία λογισμικού συνεργατικά και πραγματοποιήθηκε μια σύγκριση μεταξύ open source λογισμικού και μη. 
