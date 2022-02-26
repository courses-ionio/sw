### :paperclip: Μάθημα: Τεχνολογία Λογισμικού(sw)

<hr>
<h4>
  Ονοματεπώνυμο: Δημοστέν Τζάμα
  <br>
  Αριθμός Μητρώου: Π2019213
</h4>

:newspaper:: [GitHub Profile](https://github.com/p19tzam)<br>
:email:: [Student Mail](mailto:p19tzam)<br>
:video_camera:: edpuzzle.com: <b>p19tzam 2019213</b>

<h3> Πίνακας με σύνοψη των προθεσμιών και των παραδοτέων</h3>


| Εβδομάδα | Παραδοτέα | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | [Εισαγωγή](https://github.com/p19tzam/sw/tree/2019213/projects/2019213#pushpin-%CE%B5%CE%B9%CF%83%CE%B1%CE%B3%CF%89%CE%B3%CE%AE) | <div align="center">[Link](https://github.com/courses-ionio/help/discussions/69)</div> | <div align="center"> - </div> |
| 2 | [βιογραφικό και δημιουργία ομάδας](https://github.com/p19tzam/sw/blob/2019213/projects/2019213/README.md#pushpin-%CE%B2%CE%B9%CE%BF%CE%B3%CF%81%CE%B1%CF%86%CE%B9%CE%BA%CF%8C-%CF%80%CE%B1%CF%81%CE%B1%CE%B4%CE%BF%CF%84%CE%AD%CE%BF-%CE%B1) | <div align="center"> [Link](https://github.com/courses-ionio/help/discussions/168#discussion-3897528) </div> | |
| 3 | Αίτημα ενσωμάτωσης στην ιστοσελίδα | | |
| 4 | Άσκηση γραμμής εντολών | | |
| 5 | Συμμετοχικό περιεχόμενο A1+A2 | | |
| 6 | Άσκηση γραμμής εντολών | | |
| 7 | βιογραφικό | | |
| 8 | Αίτημα ενσωμάτωσης στην ιστοσελίδα | | |
| 9 | Άσκηση γραμμής εντολών | | |
| 10 | συμμετοχικό περιεχόμενο B1+B2 | | |
| 11 | Άσκηση γραμμής εντολών | | |
| 12 | Τελική αναφορά | | |
| 13 | [Συμμετοχή και ομαδικότητα](https://github.com/p19tzam/sw/blob/2019213/projects/2019213/README.md#%CF%83%CF%85%CE%BC%CE%BC%CE%B5%CF%84%CE%BF%CF%87%CE%AE-%CE%BA%CE%B1%CE%B9-%CE%BF%CE%BC%CE%B1%CE%B4%CE%B9%CE%BA%CF%8C%CF%84%CE%B7%CF%84%CE%B1) | | |

## :pushpin:: Εισαγωγή

Έχοντας κάνει εισαγωγή στην πλατφόρμα του Github μέσα από το μάθημα επικοινωνία ανθρώπου υπολογιστή πλέον μπορώ να την χρησιμοποιήσω πιο εξειδικευμένα και το πιο σημαντικό να γράψω την αναφορά μου μέσω τερματικού δηλαδή να μην χρησιμοποιήσω πχ τον editor που μας δίνει το github. Ο βασικός σκοπός μου στο μάθημα τεχνολογία λογισμικού είναι να φτιάξω το δικό μου linux distro μεσα απο το linux from scratch και να το προσαρμόσω στις δικές μου απαιτήσεις(εργαλεία,εμφάνιση κλπ) αναλυτικα σκέφτομαι τα βασικά πράγματα που θα περιέχει να ειναι ενα i3wm δηλαδή να τρέχει window manager μιας και προσωπικά το χρησιμοποιώ στην δουλειά μου λόγω ότι είναι πάρα πολύ γρήγορο(αν ξέρεις να το χειρίζεσαι πχ τα keybinds) και δεν απαιτει πάρα πολλούς πόρους από το σύστημα μας επίσης ξεκινώντας από ένα “καθαρό” linux εγκατεστημένο μαθαίνεις πως είναι δομημένο και πως λειτουργεί.
Πέρα από το linux from scratch θέλω να επεκτείνω τις γνώσεις μου πάνω στα github pages μέσα από τα παραδοτέα βιογραφικού μιας και έχω ασχοληθεί για προσωπική χρήση στο παρελθόν.Τέλος για τις ασκήσεις γραμμής εντολών θα ξεκινήσω το setup για το [lfs](https://www.linuxfromscratch.org/)(Linux From Scratch) με window manager όπως ανέφερα παραπάνω δηλαδή θα το προσαρμόσω στις δικές μου απαιτήσεις για να ολοκληρώσω τις ασκήσεις γραμμής εντολών ΚΑΙ πολύ σημαντικό να γράψω την αναφορά μου μέσα από το lfs.


## Ο τρόπος που θα επεξεργάζομαι την αναφορά μου μέσα από το τερματικό.

Αρχικά όπως είπα στην εισαγωγή θα έχω σαν main το arch linux και μέσα σε αυτό θα έχω ενα docker με archlinux image. <br>
Επέλεξα να βάλω docker arch image μέσα στο arch γιατί αν κατά λάθος χαλάσει κάτι δεν θα επηρεάσει το main λειτουργικό σύστημα που το έχω στήσει και δεν θέλω να χαλάσει.
Την ιδέα με το docker την πήρα στο εργαστήριο με τον κ.Ριγγα. <br>

#### Πως δημιούργησα το arch docker image: 
Αρχικά τρέχω το docker του δίνω όνομα sw_docker και του λέω στο τέλος να πάρει image για archlinux και το image είναι έτοιμο και full καθαρό<br>

`sudo docker run --name sw_docker -it -p 8080:4000 archlinux`

<br>

Για την επεξεργασία πρέπει να εγκαταστήσω το `git` στο docker μου. <br>

`pacman -S git`

<br>

Μετα θα πρέπει να κάνω git clone το repository μoy και να κάνω generate ενα token στα settings για να μπορώ να κάνω αλλαγές στο repo μου <br>

`git clone https://github.com/p19tzam/sw.git` <br>

Για να μπορέσω να κάνω αλλαγές πρέπει να αλλάξω branch <br>

`git checkout 2019213` <br>

Επίσης για να επικοινωνήσει το τερματικό μου με το github θα πρέπει να ορίσω μερικές μεταβλητές στο config του `git`.<br>

`git config --global user.name "p19tzam"` <br>
`git config --global user.email "p19tzam@ionio.gr"`<br>

Και τέλος πρέπει να μπώ στο 2019213 φάκελο να κάνω αλλαγές και να στείλω τις αλλαγές με το `git push` όπως δείχνω στο παρακάτω παράδειγμα <br>
Στο κομμάτι καταγραφής τερματικού αυτή την φορά επέλεξα να χρησιμοποιήσω το  `peek` μιας και το asciinema το έχω μάθει οπότε γιατί να μην μάθω κάτι καινούργιο; <br>

<img src="https://github.com/p19tzam/gifs/blob/main/eisagwgh.gif">



## :pushpin:: Βιογραφικό Παραδοτέο Α

| Ατομικό βιογραφικό | Webring ομάδας |
| --- | --- |
| [Link](https://p19tzam.github.io/online-cv/) | [Link](https://kafeneio-webring.netlify.app/) |   

<br>
Σε αυτό το παραδοτέο είχαμε να κάνουμε ένα βιογραφικό και ενα webring με την υπηρεσία Github Pages ή Netlify. <br> <br>
Συγκεκριμένα εγω επέλεξα να κάνω το ατομικό βιογραφικό μου με github pages κάνοντας fork ένα έτοιμο 

[template](https://github.com/sharu725/online-cv) αλλα τα χρώματα και το στυλ δεν μου άρεσε έτσι αποφάσισα να κάνω αρκετές μετατροπές στον κώδικα απο το έτοιμο template. <br>

Στο template έχω αλλάξει τα εξής:
- [x] Background color πίσω απο το main wrapper
- [x] Προσθήκη shadows στο background του wrapper 
- [x] Αλλαγή favicon με την προσθήκη ενός δικού μου
- [x] Αλλαγή στις γωνίες το wrapper τις έκανα πιο στρογγυλές(περιλαμβάνει το main wrapper και το side wrapper)
- [x] Διαγραφή σε περιττά πράγματα που περιείχε το template (διάφορα χαρακτηριστικά όπως about για το template κτλ)
- [x] Έβαλα ένα καινούργιο skin το κόκκινο το οποίο δεν υπάρχει
- [x] Έβγαλα το παλιό footer που προϋπήρχε και έβαλα κάτι δικό μου

<br>
Παραπάνω επεξεργασίες έγιναν πάνω στα υπάρχοντα αρχεία του template συγκεκριμένα στα scss και html.

## Συμμετοχή και ομαδικότητα
[Show & tell μια λύση που είχα για το πως μπορούμε να κάνουμε deploy το “σπασμένο” webring του maxboeck](https://github.com/courses-ionio/help/discussions/165#discussion-3897013) <br>
[Συμβουλή βιογραφικου και webring σε συναδέλφους](https://github.com/courses-ionio/help/discussions/183#discussioncomment-2256805)<br>
[Σχολιασμός εισαγωγής 1](https://github.com/courses-ionio/help/discussions/75#discussioncomment-2203897) <br>
[Σχολιασμός βιογραγικού συναδέλφου](https://github.com/courses-ionio/help/discussions/166#discussioncomment-2239121)<br>
[Υπενθύμιση συναδέλφου να προσθέσει λινκ στην εισαγωγή του για την αναφορά](https://github.com/courses-ionio/help/discussions/158#discussioncomment-2238385)
