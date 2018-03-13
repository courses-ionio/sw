**Data visualization, Ζαμπούνης Χρήστος, Π2015079

Παραδοτέο 1

Forked sw repository: https://github.com/Zabzuki/sw

Forked Data Visualisation repository: https://github.com/Zabzuki/D3js-uk-political-donations

Personal Data Visualisation Github Page: https://zabzuki.github.io/D3js-uk-political-donations/#

Για την απαλοιφή της κατάληξης ```.html``` στο url της εφαρμογής, αρκεί να μετονομάσουμε το αρχείο ```full-viz.html``` σε ```index.html```.

Για την αλλαγή χρωμάτων στις μπάλες με τα δεδομένα τροποποιούμε τον κώδικα στο ```chart.js``` 

```var fill = d3.scale.ordinal().range(["#76ff03", "#ea80fc", "#ff6e40"]);```

καθώς και για τα αντίστοιχα 3 πεδία της ομαδοποίησης split by party τροποποιούμε τον κώδικα στο ```style.css```
```
/*  Party view */
#conservative, #labour, #libdem { padding: 10px; }
#conservative {
    background: #ea80fc;
    top: 110px;
}
#labour {
    background: #76ff03;
    top: 330px;
}
#libdem {
    background: #ff6e40;
    top: 550px;
}
```
και
```
}
.lab {
    fill: #76FF03;
}
.lib {
    fill: #FF6E40;
}
.con {
    fill: #EA80FC;
}
```

Για να προσθέσουμε ήχο ο οποίος θα ακούγεται κάθε φορά που κάνουμε κλίκ στα buttons αρκεί να διαλέξουμε και να κατεβάσουμε το mp3 απο το internet και να το προσθέσουμε στο repository 

συγκεκριμένα χρησιμοποίησα mp3 απο το παρακάτω link:
[orange free sounds](http://www.orangefreesounds.com/)
και πρόσθεσα τις παρακάτω γραμμες κώδικα στο ```index.html```
```
<script>
   function PlaySound(melody) {
      var snd = new Audio(melody);
      snd.play();
        }
</script>
```
όπως επίσης το παρακάτω 
```
onclick="PlaySound('Button-click-sound.mp3')"
```
σε κάθε μια απο τις ετικέτες ```<a></a>```
```
 <li><a href="#" role="button" class="pure-button switch" onclick="PlaySound('Button-click-sound.mp3')" id="all-donations">All money</a>
            </li>
            <li><a href="#" role="button" class="pure-button switch" onclick="PlaySound('Button-click-sound.mp3')" id="group-by-money-source">The public's purse</a>
            </li>
            <li><a href="#" role="button" class="pure-button switch" onclick="PlaySound('Button-click-sound.mp3')" id="group-by-party">Split by party</a>
            </li>
            <li><a href="#" role="button" class="pure-button switch" onclick="PlaySound('Button-click-sound.mp3')" id="group-by-donor-type">Split by type of donor</a>
            </li>
            <li><a href="#" role="button" class="pure-button switch" onclick="PlaySound('Button-click-sound.mp3')" id="group-by-amount-of-donation">Split by the amount of the donations</a>
            </li>
```

Για να ανοίγει νέο παράθυρο με τα αποτελέσματα της αναζήτησης στο google κάνοντας κλίκ σε κάθε μπάλα, τροποποιήσαμε το ```chart.js```

Ορίσαμε μια νέα συνάρτηση, την ```mouseClick(d)```
```
function mouseClick(d) {
	var donorName = d.donor;
	window.open('http://google.com/search?q='+donorName);
}
```
όπου δέχεται σαν όρισμα τα δεδομένα της μπάλας και στη συνέχεια η window.open εμφανίζει τα αποτελέσματα της αναζήτησης του ονόματος καθενώς δορητή

Στη συνέχεια προσθέτουμε την συνάρτηση on μαζι με την συνάρτηση που δημιουργήσαμε μέσα στην συνάρτηση ```start()```
```
.on("click", mouseClick);
```
Σχετικά με το ζουμάρισμα της κάθε λέξης στις παραγράφους του site χρησιμοποιήσαμε την βοήθεια της παρακάτω βιβλιοθήκης:

[lettering js](http://letteringjs.com/)

στην συνέχεια πρόσθεσα τον παρακάτω κώδικα για να λειτουργήσει αφού κατέβασα πρώτα τοπικά την βιβλιοθήκη (χωρίς να είναι υποχρεωτικό καθώς δουλεύει και με ένα απλό link σε αυτήν) και την χρησιμοποιήσαμε ως εξής.
Τοποθετώ τον παρακάτω κώδικα στο ```index.html``` σε σημείο όπου έχει ήδη φορτώσει η jQuery:
```
 <script src="lettering.js"></script>
    <script>
        $(document).ready(function() {
            $(".word_split").lettering('words');
        });
    </script> 
```
και στο ```style.css``` πρόσθεσα την παρακάτω κλάση:
```
.word_split span:hover {
    font-size: 150%;
    font-weight: bold;
}
```
όπου ενεργοποιείται όταν φτάνει ο κέρσορας σε κάποια λέξη των παραγράφων.
Τέλος όπου υπάρχει η ανάγκη ζουμαρίσματος προσθέτουμε την κλάση ανάμεσα στο ```<p>``` tag. Ως εξής δηλαδή:
```
<p class="word_split">Words to be zoomed</p>
```

Για να ακούγεται το όνομα του δωρητή και το ποσό της δωρεάς του, όταν βρίσκεται το ποντίκι στον κύκλο κάποιου δορητή, αρκεί να προσθέσουμε κάποιες γραμμές κώδικα στην συνάρτηση ```mouseover(d,i)``` όπου θα παίρνει σαν ορίσματα το donor και το amount κάθε κύκλου. Χρησιμοποιήσα την βιβλιοθήκη της responsiveVoice και πρόσθεσα τον παρακάτω κώδικα:
```
responsiveVoice.speak(donor + ' £' + amount , "English Male");
```
επίσης στην συνάρτηση ```mouseout()``` πρόσθεσα το παρακάτω για να σταματάει το μήνυμα όταν το ποντίκι βγαίνει εκτός κύκλου:
```
responsiveVoice.cancel();
```
Επειδή η responsiveVoice είναι εξωτερική βιβλιοθήκη, πέρασα την δήλωση της στο τέλος του ```.html``` αρχείου
```
 <script src="http://code.responsivevoice.org/responsivevoice.js"></script>
```
Πήρα το link απο το [responsive voice](https://responsivevoice.org/api/)


Δημιουργούμε ένα ακόμα button ομαδοποίησης με όνομα Split by the amount of the donation.

Στο αρχείο ```index.html``` :

Δημιουργούμε το button προσθέτοντας 
```
 <li><a href="#" role="button" class="pure-button switch" onclick="PlaySound('Button-click-sound.mp3')" id="group-by-amount-of-donation">Split by the amount of the donations</a>
            </li>
```
κάτω απο τα υπόλοιπα buttons και στην συνέχεια δημιουργούμε ένα καινούργιο ```<div id="view-amount-of-donation">``` και το προσθέτουμε κάτω απο τα υπόλοιπα ```<div>```
```
 </div>
    <div id="view-amount-of-donation">
        <h2 id="amount"> Split by the amount of the donations </h2>
            <div id="amounts-scale">
                  <div id="first">
                        <p><strong>Donations more than &#163;1m </strong></p>
                  </div>
                  <div id="second">
                        <p><strong>Donations more than &#163;500k </strong></p>
                  </div>
                  <div id="third">
                        <p><strong>Donations more than &#163;100k</strong></p>
                  </div>
                  <div id="fourth">
                  <p><strong>Donations more than &#163;50k </strong></p>
                  </div>
                  <div id="fifth">
                  <p><strong>Donations more than &#163;25k </strong></p>
                  </div>
                  <div id="sixth">
                  <p><strong>Smaller donations </strong></p>
                  </div>  
            </div>
    </div>
```
Στο παραπάνω ```<div>``` περιέχεται ο τίτλος της ομαδοποίησης στην ετικέτα ```<h2>``` με ξεχωριστό id, και 6 εμφολευμένα ```<div>``` με ξεχωριστά ids επίσης για την ομαδοποίηση και την μορφοποίηση τους. Στη συνέχεια βάζω τα περιεχόμενα σε ```<p>``` για να γίνουν ξεχωριστές παράγραφοι και τις κάνω ```<strong>``` για να ειναι πιο ευδιάκριτες.


Στη συνέχεια στο αρχείο ```chart.js```:
Προσθέτω στην ```transition()``` την παρακάτω if
```
	if (name === "group-by-amount-of-donation") {
		$("#initial-content").fadeOut(250);
		$("#value-scale").fadeOut(250);
		$("#view-party-type").fadeOut(250);
		$("#view-source-type").fadeOut(250);
		$("#view-amount-of-donation").fadeIn(1000);
		$("#view-donor-type").fadeOut(250);
		return amountGroup();
	}
```
όταν θα επιλέγεται θα κάνει fade in στο ```view-amount-of-donation``` που δημιουργήσαμε και θα επιστρέφει την ```amountGroup()```.

Επίσης βάζουμε την fade out
```
$("#view-amount-of-donation").fadeOut(250);
```
στις υπόλοιπες if της ```transition()```.

Μετά φτιάχνουμε την ```amountGroup()``` με τον ίδιο τρόπο όπως είναι φτιαγμένες και οι αντίστοιχες fundsType, donorType...
```
function amountGroup() {
	force.gravity(0)
		.friction(0.8)
		.charge(function(d) { return -Math.pow(d.radius, 2.0) / 3; })
		.on("tick", donations)
		.start();
}
```
όπου στο ```.on("tick", donations)``` καλείται η ```amount()``` την οποία φτιάχνουμε με τον ίδιο τρόπο όπως ειναι αντίστοιχα φτιαγμένες οι parties, types...
```
function donations(e) {
	node.each(moveToDonations(e.alpha));
		
		node.attr("cx", function(d) { return d.x; })
			.attr("cy", function(d) { return d.y; });
}
```
όπου οι κόμβοι μετακινούνται με την συνάρτηση ```moveToDonations(alpha)``` που είναι παρακάτω. Θέτουμε ένα σταθερό σημείο Y και ανάλογα με τo ποσό της δωρεάς θέτουμε ένα σημείο X σε τιμή που ταιριάζει με τα ποσά που έχουμε ορίσει.
```
function moveToDonations(alpha) {
	return function(d) {
		var centreY = svgCentre.y;
		if (d.value <= 25001) {
			centreX = svgCentre.x + 500;
		} else if (d.value <= 50001) {
			centreX = svgCentre.x + 400;
		} else if (d.value <= 100001) {
			centreX = svgCentre.x + 300;
		} else  if (d.value <= 500001) {
			centreX = svgCentre.x + 200;
		} else  if (d.value <= 1000001) {
			centreX = svgCentre.x + 100;
		} else if (d.value <= maxVal) {
			centreX = svgCentre.x;
		} else {
			centreX = svgCentre.x;
		}

	d.x += (centreX - d.x) * (brake + 0.02) * alpha * 1.1;
	d.y += (centreY - d.y) * (brake + 0.02) * alpha * 1.1;
	};
} 
```
Τέλος κάνουμε μερικές αλλαγές στο ```.css``` αρχείο
αρχικά στο παρακάτω προσθέσαμε το visibility και το ```#view-amount-of-donation``` 
για να εμφανίζεται το περιεχόμενο του split by the amount of the donations μόνο όταν κλικάρουμε το κουμπί.
```
#view-party-type, #view-donor-type, #view-source-type, #view-amount-of-donation {
    display: none;
    visibility: visible;
}
```
επίσης προσθέσαμε τον παρακάτω κώδικα
```
/*donations*/
#amount {
    font-weight: bold;
    font-size: 35px;
    position: absolute;
    top: 50px;
    left: 300px;
    width:1000px;
}
#first {
    font-weight: bold;
    position: absolute;
    top: 185px;
    left: 240px;
    width: 93px;
}

#second {
    font-weight: bold;
    position: absolute;
    top: 185px;
    left: 354px;
    width: 93px;
}

#third {
    font-weight: bold;
    position: absolute;
    top: 185px;
    left: 494px;
    width: 93px;
}

#fourth {
    font-weight: bold;
    position: absolute;
    top: 185px;
    left: 620px;
    width: 93px;
}

#fifth {
    font-weight: bold;
    position: absolute;
    top: 185px;
    left: 751px;
    width: 93px;
}

#sixth {
    font-weight: bold;
    position: absolute;
    top: 185px;
    left: 875px;
    width: 93px;
}
 ```
για την τοποθέτηση των περιγραφών στη σωστή θέση, πάνω απ'τις αντίστοιχες ομαδοποιήσεις
