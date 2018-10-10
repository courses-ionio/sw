**Ονοματεπωνυμο:** Σουπιώνη Αικατερίνη.

**ΑΜ:** Π2013007. 

**Εργασία:** D3js-uk-political-donations.

**Ο σύνδεσμος της σελίδας με την εφαρμογή:**  https://github.com/p13soup/D3js-uk-political-donations

**To link της εφαρμογής:** https://p13soup.github.io/D3js-uk-political-donations/


**Σημείωση:** Για λόγους ευκολίας και ταχύτερου ελέγχου των αποτελεσμάτων κάθε αλλαγής έκανα clone το repository μου τοπικά. Επιπλέον, τα αρχεία charting.js, indexNG.html και styleNG.css αφορούν στο νέο διάγραμμα χρησιμοποιόντας τα ίσια δεδομένα. Τα difData.js, difData.html και difData.css αποτελούν την υλοπόιηση ενός γραφήματος χησιμοποιώντας διαφορετικό dataset. Τα δεδομένα αυτά αντλήθηκαν από την Eurostat και αποτελούν μέρος του dataset με το οπόιο υλοποιήείται η πτυχιακή μου εργασία.


# Παραδοτέο 1ο

**Εφαρμόστε τις κατάλληλες αλλαγές έτσι ώστε το url της εφαρμογής σας να μην χρειάζεται να καταλήγει σε "full-viz.html":**

Μετατροπή του αρχείου full-viz.html σε index.html
 https://github.com/p13soup/D3js-uk-political-donations


**Αλλαγή χρωμάτων στις μπάλες με τα δεδομένα, καθώς και στα αντίστοιχα 3 πεδία της ομαδοποίησης  Split by party.**

Για την αλλαγή των χρωμάτων τροποποιήθηκε το εξής κομμάτι κώδικα του αρχείου chart.js από:

var fill = d3.scale.ordinal().range(["#F02233", "#087FBD", "#FDBB30"]); 

σε:

var fill = d3.scale.ordinal().range(["#bd00bb", "#47bd00", "#ff7800"]);

μωβ, πορτοκαλί και πράσινο αντίστοιχα.

**Να ακούγεται ήχος κάθε φορά που ο χρήστης της εφαρμογής κάνει κλικ σε μία από τις επιλογές/κουμπιά ομαδοποίησης των δεδομένων.**

Προστέθηκε στο tag <head> ο εξής κώδικας:

```
<audio src="audio.mp3" id="audio"></audio>

<script language="javascript" type="text/javascript">
function sound(){
var audio = document.getElementById('audio');
audio.play();
}
</script>
```

Με το tag ```<audio>``` ορίζω τον ήχο που θέλω να χρησιμοποιήσω. Κάθε φορά που καλείται η συνάρτηση sound() παίζεται ο ήχος. Στη συνέχεια προστέθηκε σε κάθε κουμπί το event onclick=“sound()”.

**Ορισμένοι από τους αναγνώστες της εφαρμογής ενδεχομένως να είναι άτομα με περιορισμένη όραση. Τροποποιήστε τον κώδικα της εφαρμογής έτσι ώστε το ποντίκι να λειτουργεί και ως μεγεθυντικός φακός όταν μεταφέρεται επάνω από τις λέξεις του κειμένου.**

Αρχικά προστέθηκε στα κυρίως ```<div>``` επιπλέον element “ class=“zoomed” ”. Προστέθηκε στο index.html script ηια κάθε τύπο κειμένου (p, h1, h2, h3, h4, h5), Κατά το οποίο επιλέγονται όλα τα στοιχεία που βρίσκονται μέσα σε κλάση zoomed και είναι μία από τις επιμέρους μορφές κειμένου. Στη σθνέχεια χωρίζει το κείμενου σε επιμέρους λέξεις και τις τοποθετεί σε ένα tag ```<span>```. Έπειτα αντικαθιστά τις λέξεις στην αρχική τους θέση.

```
<script language="javascript" type="text/javascript">
document.querySelectorAll(".zoomed p")
.forEach(function(x){
var replacement;
replacement=x.innerHTML.replace(/\b(\w+(?![^<>]*>))\b/g,"<span class=\"wordzoom\">$1</span>");
x.innerHTML=replacement;
});
</script>
```

Στη συνέχεια προστέθηκαν στο αρχείο style.css δύο νέα rules έτσι ώστε να δημιουργηθεί ο “μεγεθυντικός φακός”.  Το πρώτο(.wordzoom) αφορά την ομαλή μετατροπή του κειμένου, ενώ στο δεύτερο (.wordzoom:hover) αλλάζουμε το σχήμα του κέρσορα σε μεγεθυντικό φακό και αυξάνεται η γραμματοσειρά εφόσον κάνουμε hover πάνω από τις γραμματοσειρές που έχουμε υποδείξει.

```
.wordzoom{
transition: 0.3s all;
display: inline-block;
}
.wordzoom:hover{
cursor:zoom-in;
font-size:1.7em;
}
```

**Τροποποιήστε τον κώδικα έτσι ώστε όταν κάνετε κλικ σε κάθε μπάλα να ανοίγει ένα νέο παράθυρο με τα αποτελέσματα της αναζήτησης στο google για τον αντίστοιχο δωρητή. **

Στο αρχείο chart.js και συγκεκριμένα στο function start() προστέθηκε το event onclick, το οποίο κάνει αναζήτηση συμπληρώνοντας το όνομα του αντίστοιχου δωρητή.

```
.on("click",function(){
location.href="https://google.com/search?q="+this.getAttribute("donor")
}) 
```

**Δημιουργήστε τουλάχιστον μία ακόμα επιλογή ομαδοποίησης των δεδομένων.**

Επιλέχθηκε να ομαδοποιηθούν τα δεδομένα ως προς το ποσό της εκάστοτε δωρεάς. Για το σκοπό αυτό προστέθηκαν στο αρχείο index.html κώδικάς δημιουργίας μίας ακόμη καρτέλας στο μενού:

```
<li><a href="#" role="button" class="pure-button switch" id="group-by-donation-amount" onclick="sound()">Split by amount of donation</a> </li>
```

Στο ίδιο αρχείο προστέθηκε κώδικάς με το κείμενο/πληροφορίες που θα εμφανίζεταιμαζί με τη νέα επιλογή ομαδοποίησης:

```
<div id="view-donation-amount" class="zoomed">
<h2>Separation By Amount Of Donation</h2>
<div id="mil">
<p>Over 500.000 million pounds</p>
</div>
<div id="halfMil">
<p>Up to 500.000 pounds</p>
</div>
<div id="hunK">
<p>Up to 100.000 pounds</p>
</div>
<div id="fiftyK">
<p>Up to 50.000 pounds</p>
</div>
<div id="twenK">
<p>Up to 25.000 pounds</p>
</div>
</div>
```

Επιπλέον τρποποιήθηκε το αρχείο chart.js ως εξής:

Δημιουργήθηκαν τα κέντρα για κάθε γκρουπ τιμών.

```
var amountCentres = { 
mil: { x: w / 3, y: h /3.5}, 
halfMil: {x: w / 3, y: h /2.6}, 
hunK: {x: w / 3	, y: h /2.2},
fiftyK: {x: w / 3, y: h /1.7},
twenK: {x: w /3, y: h /1.3},
};

Στο function transition προστέθηκε μία ακόμα if για την εμφάνιση των σωστών στοιχείων.

if (name === "group-by-donation-amount"){
$("#initial-content").fadeOut(250);
$("#value-scale").fadeOut(250);
$("#view-donor-type").fadeOut(250);
$("#view-source-type").fadeOut(250);
$("#view-party-type").fadeOut(250);
$("#view-donation-amount").fadeIn(1000);
return donAmountGroup();
}
Ταυτοχρονα προστέθηκε σε όλες τις υπόλοιπες if της συνάρτησης η εντολή:

$("#view-donation-amount").fadeOut(250);

Επίσης δημιουργήθηκαν οι συναρτήσεις :

function fundsType() {
force.gravity(0)
.friction(0.75)
.charge(function(d) { return -Math.pow(d.radius, 2.0) / 3; })
.on("tick", types)
.start();
}
```

Και:

```
function donAmount(e) {
node.each(moveToDonAmount(e.alpha));
node.attr("cx", function(d) { return d.x; })
.attr("cy", function(d) {return d.y; });
}

```

Τέλος δημιουργήθηκαν δύο συναρτήσεις. Η getAmountGroup(value) αναθέτει σε κάθε node, ανάλογα το ποσό της δωρεάς που έχει το κατάλληλο String με σκοπό να λετουργήσει σωστά η επόμενη συνάρτηση.

```
function getAmountGroup(value){
if (value<=25000){
return "twenK";
}
if (value<=50000){
return "fiftyK";
}
if (value<=100000){
return "hunK";
}
if (value<=500000){
return "halfMil";
}
else{
return "mil";
}
}

```

Η moveToDonAmount(alpha) μετακινεί/χωρίζει τα nodes προς το κατάλληλο για αυτό κέντρο που έχει οριστεί νωρίτερα.

```
function moveToDonAmount(alpha) {
return function(d) {
var centreX = amountCentres[getAmountGroup(d.value)].x + 50;
var centreY = amountCentres[getAmountGroup(d.value)].y;

d.x += (centreX - d.x) * (brake + 0.02) * alpha * 1.1;
d.y += (centreY - d.y) * (brake + 0.02) * alpha * 1.1;
};
}

```

Επιπλέον στο αρχείο style.css αρχικά προστέθηκε στο id που δώθηκε στο div του κειμένου στο index.html, display:none;  ώστε να μην εμφανίζεται στην αρχική σελίδα της εφαρμογής.

Τέλος προστέθηκε ο κάτωθι κώδικας για τη σωστή τοποθέτηση των επιμέρους κειμένων που αφορούν τα γκρουπς.

```
#view-donation-amount{
left: 700px;
width: 272px;
}
#mil{
top: 70px;
padding-top: 50px;
}

#halfMil{
top: 500px;
padding-top: 200px;
}
#hunK{
top: 390px;
padding-top: 100px;
}
#fiftyK{
top: 530px;
padding-top: 100px;
}
#twenK{
top: 660px;
padding-top: 140px;
}

```

# Παραδοτέο 2ο 

**Όταν το ποντίκι εισέρχεται σε έναν από τους κύκλους του γραφήματος, εμφανίζονται οι πληροφορίες του αντίστοιχου δωρητή. Τροποποιήστε κατάλληλα τον κώδικα της εφαρμογής σας, έτσι ώστε σε μια περιοχή της ιστοσελίδας του γραφήματος που θα ορίσετε, να εμφανίζεται (και να επεκτείνεται δυναμικά) η σειρά των εικόνων με τους δωρητές πάνω από τους οποίους πέρασε ο δείκτης του ποντικιού σας στο γράφημα.**

Στο αρχείο index.html προστέθηκαν δύο <div>, ένα για το container των φωτογραφιών και ένα για της φωτογραφίες. Στο αρχείο chart.js εισήχθει ο παρακάτω κώδικας για την την εισαγωγή των φωτογραφιών στο container:

```
d3.select(".lastSeenContainer").append("img").attr("src","https://raw.githubusercontent.com/ioniodi/D3js-uk-political-donations/master/photos/" + donor + ".ico")

.attr("donor", donor);
```

Τέλος προστέθηκαν στο αρχείο style.css τα εξής κομμάτια κώδικα για μορφοποίηση του container και του περιοχομένου του:

```
.photoHover{
max-height: 400px;
max-width: 400px;
overflow: scroll;
float: left;
}
.lastSeenContainer{
max-width: 50%;
}

```

**Branches ερωτημάτων pull requests:**

1. Εισαγωγή φωτογραφιών 5 δωρητών: https://github.com/p13soup/D3js-uk-political-donations/tree/insertPhotos 

2. Εισαγωγή αρχείου .csv στο φάκελο participants: https://github.com/p13soup/D3js-uk-political-donations/tree/partCSV

3. Δημιουργία αρχείου .html στον φάκελο participants: https://github.com/p13soup/D3js-uk-political-donations/tree/partHTML

4. Επεξεργασία του index.html στο φάκελο participants. Εισαγωγή github username και εικόνας: https://github.com/p13soup/D3js-uk-political-donations/tree/creditsIndex