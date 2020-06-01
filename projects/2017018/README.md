# Τμήμα Πληροφορικής Ιονίου Πανεπιστημίου
### Μάθημα: Τεχνολογίες Λογισμικού
* Σύνδεσμος Αποθετηρίου: https://github.com/mmits/sw

#### Στοιχεία Φοιτητή
* Ονοματεπώνυμο: Ελένη Μαρία Μητσοπούλου
* ΑΜ: Π2017018

#### Επιβλέπων Καθηγητής
* Χωριανόπουλος Κωνσταντίνος

---

# Ασκήσεις Dokey
## Άσκηση 1:
**Τίτλος:** Use the terminal as an IDE<br>
**Περιγραφή:** Edit your files (e.g., cv, website, code, etc) in vim or emacs and compile it in a different panel or use a plug-in<br>
**Asciinema link:** https://asciinema.org/a/gZHBJVEWIjmmnLhfNecxSHq7U

Χρησιμοποίησα το [SpaceVim](https://spacevim.org/), μια επέκταση του text editor Vim η οποία διαθέτει εργαλεία για την ανάπτυξη κώδικα με διάφορες γλώσσες προγραμματισμού και πολλά άλλα.
![1](/projects/2017018/images/vim1.png)

Μετά την εγκατάσταση του SpaceVim, αλλάζω και προσθέτω νέες παραμέτρους στο config file του προγράμματος, ώστε να υποστηρίζει error checking, autocompletion και compiling της γλώσσας Python.<br>
![2](/projects/2017018/images/vim2.png)
Το κομμάτι κώδικα που πρόσθεσα είναι το παρακάτω:<br>
```
[[layers]]
name = 'lang#python
auto-completion-return-key-behavior = "complete"
auto-completion-tab-key-behavior = "cycle"
```

Ύστερα, μπορώ να γράψω ένα πρόγραμμα, το οποίο μετά το SpaceVim εκτελεί μέσα από το δικό του shell.
![3](/projects/2017018/images/vim4.png)

*Ύστερα από συνενόηση με τον καθηγητή, δημιούργησα ένα δεύτερο asciinema link το οποίο παρουσιάζει την εκτέλεση ενός διαφορετικού, πιο περίπλοκου προγράμματος.*<br>
**Asciinema link 2:** https://asciinema.org/a/GLjWrzWaNbj6BP91j2HuE30Rg

![4](/projects/2017018/images/vim5.png)
Το παραπάνω πρόγραμμα εκτελεί μια διαδικασία merge sort ενός μονοδιάστατου πίνακα και παρουσιάζει το αποτέλεσμα.

![5](/projects/2017018/images/vim6.png)
Τροποίησα επίσης το πρόγραμμα ώστε ο πίνακας να περιέχει περισσότερα στοιχεία.

## Άσκηση 2:
**Τίτλος:** Send notifications to you desktop-mobile<br>
**Περιγραφή:** Send a notifcation when a big task completes, eg download, compiling, etc

Χρησιμοποίησα το [ntfy](https://github.com/dschep/ntfy), μια python-based εφαρμογή η οποία στέλνει notifications στο περιβάλλον του υπολογιστή μου.

Σε περιβάλλοντα Linux απαιτείται η εντολή `eval "$(ntfy shell-integration)"` στο config file του bash του συστήματος για να στέλνεται ειδοποίηση κάθε φορά που τερματίζεται μια διεργασία.

Λόγω της λειτουργίας της εφαρμογής μόνο στο περιβάλλον του υπολογιστή και όχι στο terminal, αντί για asciicast έφτιαξα ένα gif που δείχνει λειτουργία του ntfy
![1](/projects/2017018/images/ntfy1.gif)

Επίσης, με τη χρήση του intergration με την υπηρεσία αποστολής μηνυμάτων Pushbullet, έστειλα μια ειδοποίηση από το terminal στο κινητό μου.
![2](/projects/2017018/images/ntfy2.png)

Μόνη απαίτηση ήταν να προσθέσω το παρακάτω κομμάτι κειμένου στο config αρχείο του ntfy (ntfy.yml), το οποίο περιέχει το access token που μου δίνει το Pushbullet:
```
---
pushbullet:
    access_token: ***
```

## Άσκηση 3:
**Τίτλος:** Create an agent for news<br>
**Περιγραφή:** The demo should display the new content added on a news web site<br>
**Asciinema link:** https://asciinema.org/a/yuiKvg8udLPi7SibET3t9Xh7X<br>
  *Σημείωση: Το παραπάνω asciicast έχει μακριά διάρκεια, αλλά απεικονίζει το παρασκήνιο της διαδικασίας ανοίγματος σύνδεσης, δημιουργίας νέων agents και τρεξίματος των agents αυτών.*

Χρησιμοποίησα το [Huginn](https://github.com/huginn/huginn). Επιτρέπει τη δημιουργία custom agents για την παρακολούθηση ιστοσελίδων με ειδήσεις, μεταφορά ειδοποιήσεων από μέσα κοινωνικής δικτύωσης (Twitter, Tumblr, Weibo, etc.) σε πραγματικό χρόνο και άλλα.

Μόλις ενεργοποιηθεί το πρόγραμμα μέσα από το terminal, προσφέρει από μόνο του μερικά ήδη έτοιμα agents, τα οποία όμως δεν είναι up-to-date και δεν λειτουργούν.<br>
Έτσι δημιούργησα τρεις δικούς μου agents:

![1](/projects/2017018/images/huginn1.png)

Ο agent URL Receiver λαμβάνει το link με τα καιρικά δεδομένα από την ιστοσελίδα της National Weather Service για την πρωτεύουσα των ΗΠΑ, Washington DC:
```
{
  "expected_update_period_in_days": "365",
  "url": "https://api.weather.gov/points/38.904722,-77.016389",
  "type": "json",
  "mode": "merge",
  "extract": {
    "url": {
      "path": "$.properties.forecast"
    }
  },
  "user_agent": "Exocortex v0.4.1 Weather Forecast Bot (contact: huginn-test-user at huginn dot example dot com)"
}
```

Ο agent Weather Details συλλέγει τα καιρικά δεδομένα από το link που έλαβε προηγουμένως ο agent URL Receiver:
```
{
  "expected_update_period_in_days": "365",
  "url": "{{ url }}",
  "type": "json",
  "mode": "merge",
  "extract": {
    "today": {
      "path": "$.properties.periods.[0].detailedForecast"
    },
    "tonight": {
      "path": "$.properties.periods.[1].detailedForecast"
    },
    "datestamp": {
      "path": "$.properties.updateTime"
    }
  },
  "user_agent": "Exocortex v0.4.1 Weather Forecast Bot (contact: huginn-test-user at huginn dot example dot com)"
}
```

Τέλος, ο agent Formatting παίρνει τα raw δεδομένα απ' τον agent Weather Details και τα εμφανίζει μορφοποιημένα ώστε να είναι ευανάγνωστα προς τον χρήστη:
```
{
  "instructions": {
    "message": "As of {{ datestamp | date: '%A, %d %B %Y' }} at {{ datestamp | date: '%l:%M%p (%z)' | strip }}, the National Weather Service forecast for {{ location }} is: {{ today }}{% line_break %}Tonight's forecast is: {{ tonight }}"
  },
  "mode": "clean"
}
```

Παρακάτω φαίνονται τα events που δημιούργησαν οι τρεις agents καθώς συλλέγουν τα δεδομένα.
![2](/projects/2017018/images/huginn2.png)

## Άσκηση 4:
**Τίτλος:** Create your own static site and blog generator<br>
**Περιγραφή:** The generator should consider posts, pages, and templates<br>
**Asciinema link:** https://asciinema.org/a/vNKkRansbyBQIjO2fJEzBgNE4

Χρησιμοποίησα το [Hugo](https://gohugo.io/). 

Μετά την εγκατάσταση του Hugo, εγκατέστησα το θέμα της ιστοσελίδας στο οποίο θέλω να αλλάξω τη σελίδα μου, το [Fuji](https://themes.gohugo.io/hugo-theme-fuji/) και μετά έφτιαξα δύο μικρά posts τα οποία φαίνονται παρακάτω.

Το θέμα Fuji επιτρέπει την προσθήκη tags στα posts, τα οποία μετά εμφανίζει στο sidebar της σελίδας. Απλά προσθέτω ένα νέο πεδίο στα αρχεία των posts μου. Μπορώ επίσης να προσθέσω μερικά ξεχωριστά links στο ίδιο sidebar, προσθέτοντας το πεδίο ```[[menu.link]]```.

![1](/projects/2017018/images/hugo1.png)

## Άσκηση 5:
**Τίτλος:** Performance monitoring<br>
**Περιγραφή:** Monitor the performance of your python scripts and visualize them with colors and/or spark lines<br>
**Asciinema link:** https://asciinema.org/a/dZMJ2XSyOhdkNAAn8ZWo69ZjS

Χρησιμοποίησα το [hyperfine](https://github.com/sharkdp/hyperfine). Είναι ένα πολύ απλό και εύχρηστο πρόγραμμα το οποίο εξετάζει την απόδοση προγραμμάτων αλλά και εντολών.

Το hyperfine τρέχει το πρόγραμμα αρκετές φορές και κάθε φορά καταγράφει τον χρόνο εκτέλεσής του. Μετά επιστρέφει το μέσο χρόνο εκτέλεσης καθώς και τον μεγαλύτερο και μικρότερο χρόνο.

![1](/projects/2017018/images/hyperfine1.png)

## Άσκηση 6:
**Τίτλος:** Set-up cloud services<br>
**Περιγραφή:** SSH to a remote machine and demonstrate your remote cli user land (e.g., email, editor, cv, code, etc)<br>
**Asciinema link:** https://asciinema.org/a/9zIhVI2nlGBIstHsjKex9ZQTj

Χρησιμοποίησα το [OpenSSH](https://www.openssh.com/).

Επειδή δε διαθέτω άλλη συσκευή η οποία μπορεί να λάβει σύνδεση SSH με ευκολία, προσπάθησα να εκτελέσω την άσκηση αυτή κάνοντας SSH στο ίδιο μηχάνημα που χρησιμοποιώ, δηλαδή στον localhost του μηχανήματός μου με την εντολή ```ssh localhost```.

Σε μια εναλλακτική περίπρωση θα εκτελούσα μια εντολή σαν την ```ssh <device_username>@<ip_address>``` όπου device_username είναι το όνομα χρήστη στον οποίο θέλω να κάνω SSH, και ip_address η διέυθυνση IP του χρήστη αυτού.

Μόλις συνδεθώ με τους κωδικούς του localhost μου (το password μου), μπορώ να περιηγηθώ μέσα στο file system του, ακόμα και να μετακινήσω και να εκτελέσω αρχεία μέσα του "απομακρυσμένα".

## Άσκηση 7:
**Τίτλος:** Create a docker image for your development stack<br>
**Περιγραφή:** Demonstrate the custom image for CI of your cv and site<br>
**Asciinema link:** https://asciinema.org/a/u2MZZEgTFMO9ZCTW3DhZJt6bf

Χρησιμοποίσηα το [alpine](https://hub.docker.com/_/alpine).

Σε έναν ξεχωριστό φάκελο, dockerproject, έχω το Dockerfile μου:
```
FROM nginx:alpine
COPY index.html /usr/share/nginx/html
```
το οποίο όταν εκτελέσω μέσα στον localhost sever μου θα έχει αντικαταστήσει την αρχική σελίδα index.html με το παρακάτω:
```
<h3>cats cats cats cats cats</h3>
```

Είναι σημαντική η ονομασία του παραπάνω αρχείου index.html καθώς αλλιώς ο localhost θα εμφανιζει την default αρχική σελίδα του nginx του alpine.

![1](/projects/2017018/images/docker1.png)

Εκτελώ στο τέλος την εντολή ```sudo service docker restart``` ώστε να ελευθερωθεί το internal domain localhost. Αυτό βοηθά σε περίπτωση που θέλω να διορθώσω κάποιο λάθος με το deployment της σελίδας μου.

---

# Συμμετοχικό Εκπαιδευτικό Υλικό
*Σημείωση: Το αποθετήριό μου gr είναι από παλαιό έτος για το μάθημα HCI και δεν είχα χρόνο να κάνω deploy τη σελίδα μου με τις ενημερωμένες απαιτήσεις. Αποτέλεσμα αυτού κάποιες εικόνες δεν εμφανίζονται σωστά.*

## Γ
[Βιογραφία του Bill Buxton](https://mmits.github.io/gr/biography/bill-buxton/)

[Βιογραφία του Bret Victor](https://mmits.github.io/gr/biography/bret-victor/)

[Case study της Γλώσσας Assembly](https://mmits.github.io/gr/case-study/assembly/)
