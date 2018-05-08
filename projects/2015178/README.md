# Μάθημα: Τεχνολογίες Λογισμικού

## Τίτλος Εργασίας: Οπτικοποίηση δεδομένων χορηγιών (UK)

#### Αριστοτέλης Συμεωνίδης
#### ΑΜ: Π2015178
#### e-mail: p15syme@ionio.gr

#### [Link προσωπικόυ αποθετήριου κώδικα](https://github.com/p15syme/D3js-uk-political-donations)

#### [Link εκτελέσιμου κώδικα](https://p15syme.github.io/D3js-uk-political-donations/)

#### [Link Παραδοτέου 1](https://github.com/p15syme/D3js-uk-political-donations/tree/%CE%A02015178---%CE%A0%CE%B1%CF%81%CE%B1%CE%B4%CE%BF%CF%84%CE%AD%CE%BF-1)

#### [Link Παραδοτέου 2](https://github.com/p15syme/D3js-uk-political-donations/tree/2015178---%CE%A0%CE%B1%CF%81%CE%B1%CE%B4%CE%BF%CF%84%CE%AD%CE%BF-2)

#### [Link Τελικής Αναφοράς](https://p15syme.github.io/Final-Report-2018-ST/)

## Σύνοψη:

Η παρούσα εργασίας αποτελεί τροποποίηση της εργασίας https://ioniodi.github.io/D3js-uk-political-donations/full-viz., στην οποία μέσω των HTML, CSS και Javascript γίνεται οπτικοποίηση δεδομένων. Έτσι, κάνοντας fork το αποθετήριο του ioniodi, το τροποποιούμε στο προσωπικό μας αποθετήριο, σύμφωνα με τις οδηγίες των παραδοτέων.


## Παραδοτέο 1: Αρχικό έργο και ενδιάμεση αναφορά προόδου - 14 Μαρτίου (25%)

Για το πρώτο παραδοτέο έγιναν οι εξής ενέργειες:

* Αρχικά, τροποποίησα το URL του προσωπικού μου αποθετηρίου από https://github.com/p15syme/D3js-uk-political-donations/full-viz.html --> https://github.com/p15syme/D3js-uk-political-donations, διαγράφοντας την κατάληξη full_viz.html και αλλάζοντας την ονομασία του αρχείου full_viz.html --> index.html.
* Προσέθεσα των ήχο όταν κάνει κάποιος click στα κουμπιά, μέσω της συνάρτησης onmousedown() στη κεφαλίδα του <ul></ul>.
* Χρησιμοποιώντας τα rgba και των HEX κώδικα, άλλαξα τα χρώματα από τις μπάλες. 
* Χρησιμοποιώντας τη συνάρτηση SpeechSynthesisUtterance(), εντός της συνάρτησης mouseover(), στον κώδικα του αρχείου chart.js, προσέθεσα την φωνή που θα ακούγεται για να λέει το όνομα και το ποσό του δωρήτη.
Χρησιμοποιώντας το κομμάτι του κώδικα που προσέθεσα στο αρχείο index.html, κάνω zoom στα texts της ιστοσελίδας, τοποθετώντας το class=zoom εντός των κεφαλιδών των texts.
* Προσέθεσα μία ακόμη ομαδοποίηση δεδομένων.
* Εντός της συνάρτησης start() του αρχείου chart.js προσθέτοντας το .on("click", function(d) { window.open("http://www.google.com/search?q=" + d.donor);});, κάνοντας κλικ πάνω σε κάποια μπάλα ο χρήστης θα κάνει αναζήτηση σε καινούργιο παράθυρο.
* Τέλος, για το δεύτερο σκέλος σύμφωνα με τις οδηγίες δέσμευσα και έστειλα 5 φωτογραφίες από δωρητές στους οποίους δεν υπήρχαν και δημιούργησα ένα αρχείο 2015178.csv με τα στοιχεία μου.

### Ενδεικτικά στιγμιότυπα:

![ss1](https://user-images.githubusercontent.com/22681573/36947454-9c079868-1fd4-11e8-900c-df936ad26dd7.png)

![ss2](https://user-images.githubusercontent.com/22681573/36947455-9d7662c4-1fd4-11e8-9b3d-8409cda8c857.png)

## Παραδοτέο 2: 

  Για το Παραδοτέο 2 έγιναν οι εξής αλλαγές:
  
* Τροποποιήθηκε ο κώδικας του αρχείου *chart.js*, προσθέτωντας το παρακάτω block κώδικα, με αποτέλεσμα την εμφάνιση της εικόνας του δωρητή, όταν ο χρήστης κάνει hove over από το bubble που τον αντιπροσωπεύει:
```Javascript
var infoPic = document.createElement("img");
    infoPic.setAttribute("src","http://www.bizreport.com/2011/02/03/android-logo-200x200.jpg");
    infoPic.setAttribute("height","42");
    infoPic.setAttribute("width","42");
    infoPic.setAttribute("onerror",'this.src=\"https://github.com/favicon.ico\";');
    document.getElementById("cssPic").insertBefore(infoPic,document.getElementById("cssPic").firstChild);
    infoPic.src = imageFile;
```
###### Παραδοτέο 2 - Εμφάνιση του ιστορικού

* Στο φάκελο *participants* τροποποίησα το αρχείο *index.html*, στην θέση *position #015*, χρησιμοποιώντας το ακόλουθο block κώδικα, με σκοπό την εμφάνιση των στοιχείων μου(github username & picture):

```
<div style="border: 2px solid; border-radius: 5px; background-color: #4267B2; width: fit-content; float: left; margin: 10px 10px 10px 10px;">
      <h4>
        <span>&nbsp;</span>
        <img src="https://avatars2.githubusercontent.com/u/22681573?s=400&v=4" height="42" width="42">
        <span class="ml1"><span class="letters">&nbsp;p15syme&nbsp;</span></span>
      </h4>
  </div>
  
  <script>
  // Wrap every letter in a span
  $('.ml1 .letters').each(function(){
    $(this).html($(this).text().replace(/([^\x00-\x80]|\w)/g, "<span class='letter'>$&</span>"));
  });
   
   anime.timeline({loop: true}) 
    .add({
    targets: '.ml1 .letters',
    scale: [0,1],
    opacity: [0,1],
    easing: "easeOutElastic",
    duration: 2000,
    delay: function(el, i, l) {
      return 750 * (i+2);
    }
  }).add({
    targets: '.ml1',
    opacity: 0,
    duration: 1000,
    easing: "easeInOutQuint",
    delay: 1000
  });    
  </script>
```
###### Παραδοτέο 2 - Εμφάνιση του ονόματος και του avatar στο αρχείο index.html
* Στο τελευταίο ζητούμενο που έκανα για το Παραδοτέο 2, ζητούσε να δημιουργήσουμε μία σελίδα, όπου θα αντλούσε στοιχεία δυναμικά από το κεντρικό αποθετήριο του ioniodi, μέσω της σελίδας Insights. Έτσι, δημιούργησα το αρχείο 2015178.html. Η άντληση των δεδομένων έγινε μέσω XML HTTP Request.

#### Ενδεικτικά Στιγμιότυπα Παραδοτέου 2:

![ss3](https://user-images.githubusercontent.com/22681573/39723986-236abab2-5250-11e8-9964-7880b1afc77f.png)
###### Παραδοτέο 2 - Εμφάνιση του ιστορικού.

![ss4](https://user-images.githubusercontent.com/22681573/39724154-a397d4d6-5250-11e8-9a30-4076c76eed12.png)
###### Παραδοτέο 2 - Η σελίδα στην οποία φαίνονται τα contributions από τους χρήστες του κεντρικού απεθετηρίου.

![ss5](https://user-images.githubusercontent.com/22681573/39724156-a3c569b4-5250-11e8-8990-3f3b4229c207.png)
###### Παραδοτέο 2 - Εμφάνιση του ιστορικού.



