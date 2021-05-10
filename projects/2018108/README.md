## Προσωπικά στοιχεία

- **Ονοματεπώνυμο:** Πανακάκης Σταύρος
- **Email:** p18pana@ionio.gr
- **ΑΜ:** 2018108

## Περιεχόμενα

| Εβδομάδα* | Παραδοτέο |
| --- | --- |
| 1 | <a href="#introduction">Φορκ του αποθετηρίου και δημιουργία της σελίδας της αναφοράς με τα προσωπικά στοιχεία σας, της σύνοψης με αυτόν τον πίνακα περιεχομένων, και συγγραφή της εισαγωγής με περιγραφή των αναγκών και των στόχων σας για το αντίστοιχο μάθημα</a> |
| 2 | <a href="#bio1">Βιογραφικό</a> |
| 3 | <a href="#site1">Αίτημα ενσωμάτωσης στην ιστοσελίδα</a> |
| 4 | <a href="#term1">Άσκηση γραμμής εντολών</a> |
| 5 | <a href="#sym1">Συμμετοχικό περιεχόμενο</a> |
| 6 | <a href="#term2">Άσκηση γραμμής εντολών</a> |
| 7 | <a href="#bio2">Βιογραφικό</a> |
| 8 | <a href="#site2">Αίτημα ενσωμάτωσης στην ιστοσελίδα</a> |
| 9 | <a href="#term3">Άσκηση γραμμής εντολών</a> |
| 10 | <a href="#sym2">Συμμετοχικό περιεχόμενο</a> |
| 11 | <a href="#term4">Άσκηση γραμμής εντολών</a> |
| 12 | <a href="#final">Τελική αναφορά*</a> |

## <div id="introduction">1. Εισαγωγή</div>
Ο στόχος μου για το μάθημα "Τεχνολογίες Λογισμικού" είναι η επιτυχής ολοκλήρωση των ασκήσεων, η εκμάθηση των εργαλείων που θα διδαχθούμε
και η πρακτική εξάσκηση πάνω σε αυτά. Πιο συγκεκριμένα, θα ήθελα να δουλέψω περισσότερο με CI/CD (πχ Travis, Github Actions etc), με Docker (είτε για 
development είτε για deployment) και να δω και static site generators.


## <div id="bio1">2. Βιογραφικό</div>
Αυτή την εβδομάδα είχαμε το πρώτο παραδοτέο για το βιογραφικό. Αρχικά, δημιούργησα από την αρχή ένα δικό μου template για το βιογραφικό διότι
δεν με κάλυπτε κάποιο έτοιμο theme, και θεωρώ πως δεν είχε νόημα να κάνω την άσκηση απλώς κάνοντας fork γιατί δεν θα είχα την ευκαιρία να πειραματιστώ
αρκετά με το jekyll.

Επειδή πέρασα αρκετή ώρα με αυτό, δεν είχε νόημα να καταγράψω όλη τη διαδικασία με το Asciinema. Παρόλα αυτά, κατέγραψα το πως τρέχω το website και έκανα ένα HTTP Request με το Curl στο deployed site για να δείτε ότι δουλεύει κανονικά. Πιο αναλυτικά:

**Τι έκανα για το πρώτο παραδοτέο;**
1. Δημιούργησα ένα theme from scratch
2. Έγραψα ένα docker-compose.yml file για να αυτοματοποιήσω τη διαδικασία της εγκατάστασης και του server
3. Μετέτρεψα το site να είναι compatible με A4 page με σκοπό στο μέλλον να γίνει σε μορφή pdf
4. Έκανα deploy το site στο Github Pages με δικό μου domain

**Τι άφησα για το επόμενο παραδοτέο;**
1. Continuous Integration
2. Παραγωγή PDF με τα εργαλεία pandoc και latex 

**Links:**
- [CV Link](https://cv.stavrospanakakis.com/)
- [CV Repository](https://github.com/Stavrospanakakis/cv)

<a href="https://asciinema.org/a/394764" target="_blank"><img src="https://asciinema.org/a/394764.svg" /></a>

**Βελτιώσεις:**
Λόγω του ότι μου άρεσε το αποτέλεσμα της άσκησης, το μετέτρεψα σε jekyll template. Γι' αυτόν τον λόγο άλλαξα τα links παραπάνω. Παρόλα αυτά, αν μπείτε στο commit history του template repository, θα δείτε κανονικά ότι είναι εκπρόθεσμη η παράδοση της άσκησης.

## <div id="site1">3. Αίτημα ενσωμάτωσης στην ιστοσελίδα</div>
Η συνεισφορά που έκανα στη σελίδα του τμήματος ήταν η προσθήκη περιεχομένου διοικητικού υπαλλήλου Παναγιώτα Χασάπη.

**Issue:** https://github.com/ioniodi/sitegr/issues/37

**Pull Request:** https://github.com/ioniodi/sitegr/pull/59

**Demo:** https://peaceful-torvalds-02fd7d.netlify.app

## <div id="term1">4. Άσκηση γραμμής εντολών</div>

create a docker image for your development stack

Σε αυτό το παραδοτέο δημιούργησα ένα Docker Image για το site του βιογραφικού μου.
Έτσι, κάθε φορά που θέλω να κάνω run ή build το βιογραφικό, δεν χρειάζεται να έχω 
ruby ή jekyll στον υπολογιστή μου. Αυτό μου κάνει είναι το να κάνει pull το official
docker image του jekyll, να κάνει copy τα αρχεία του βιογραφικού στο working directory,
να κάνει expose το port 4000 και να κάνει serve τον κώδικα στον server. Τέλος, δημιούργησα
έναν docker container ο οποίος χρησιμοποιεί αυτό το image για να δείτε ότι δουλεύει κανονικά.

[![asciicast](https://asciinema.org/a/397673.svg)](https://asciinema.org/a/397673)

## <div id="sym1">5. Συμμετοχικό περιεχόμενο</div>
Σε αυτό το παραδοτέο οι προσθήκες μου ήταν το DuckDuckGo και το Jira. Το DuckDuckGo το πρόσθεσα, διότι 
είναι ένα software το οποίο πήγε να χτυπήσει μία τεράστια εταιρία (Google) και έχει δώσει μεγάλη σημασία
στο privacy του χρήστη. Το Jira το πρόσθεσα διότι είναι ένα λογισμικό το οποίο χρησιμοποιείται για project
management και για να γίνει η συνεργασία των προγραμματιστών και η συγγραφή software πιο αποδοτική.

- [DuckDuckGo Image](https://github.com/Stavrospanakakis/images/blob/cb0ed5ad2d36edfb4f67d424873a570bedf741dc/duckduckgo.jpg)
- [DuckDuckGo Thumbnail](https://github.com/Stavrospanakakis/images/blob/cb0ed5ad2d36edfb4f67d424873a570bedf741dc/duckduckgo-thumb.jpg)
- [DuckDuckGo Gallery](https://github.com/Stavrospanakakis/_gallery/blob/9153040416880e7874576d1a3ce5a28c992c62aa/duckduckgo.md)
- [DucKDuckGo Slides](https://github.com/Stavrospanakakis/site/blob/master/_slides/archetypes.md)
- [DuckDuckGo Timeline](https://github.com/Stavrospanakakis/site/blob/master/_timeline/systems.md)

- [Jira Image](https://github.com/Stavrospanakakis/images/blob/master/jira.jpg)
- [Jira Thumbnail](https://github.com/Stavrospanakakis/images/blob/master/jira-thumb.jpg)
- [Jira Gallery](https://github.com/Stavrospanakakis/_gallery/blob/9153040416880e7874576d1a3ce5a28c992c62aa/jira.md)
- [Jira Slides](https://github.com/Stavrospanakakis/site/blob/master/_slides/tools.md)
- [Jira Timeline](https://github.com/Stavrospanakakis/site/blob/master/_timeline/collaboration.md)

- [Pibook Repository](https://github.com/Stavrospanakakis/site)
- [Gallery Repository](https://github.com/stavrospanakakis/_gallery)
- [Images Repository](https://github.com/stavrospanakakis/images)

[![asciicast](https://asciinema.org/a/400505.svg)](https://asciinema.org/a/400505)

## <div id="term2">6. Άσκηση γραμμής εντολών</div>
create a cli app for your favorite site

Σε αυτό το παραδοτέο δημιούργησα ένα command line interface το οποίο μου είναι χρήσιμο
όλο τον χρόνο διότι αυτοματοποείο κάποιες διεργασίες τις οποίες κάνω συνεχώς. Πιο συγκεκριμένα,
μπορώ να περάσω μέσα τα ονόματα των μαθημάτων του τμήματος πληροφορικής μαζί με τα link τηλεδιασκέψεων τους
και με ένα command στο terminal να ανοίξω το zoom link της επιλογής μου. Έτσι, κάθε φορά δεν χρειάζεται να ψάχνω
για τα links και τους κωδικούς. Στα παρακάτω links μπορείτε να δείτε το repository της εφαρμογής και την 
ιστοσελίδα της.
- [App repository](https://github.com/Stavrospanakakis/lfl)
- [Αpp website](https://lfl.stavrospanakakis.com/)

Το asciinema δειχνει την εγκατάσταση της εφαρμογής.
[![asciicast](https://asciinema.org/a/401581.svg)](https://asciinema.org/a/401581)

## <div id="bio2">7. Βιογραφικό</div>
Αυτή την εβδομάδα έκανα τις ενέργειες που χρειαζόταν για να ολοκληρώσω τα παραδοτέα του βιογραφικού. Πιο συγκεκριμένα έκανα:
1. Continuous Integration με τη δημιουργία Github Action
2. Παραγωγή PDF με τα εργαλεία pandoc και latex 

- [Repository Link](https://github.com/Stavrospanakakis/cv)
- [CV Website](http://cv.stavrospanakakis.com/)
- [CI Link](https://github.com/Stavrospanakakis/cv/blob/main/.github/workflows/main.yml)
- [PDF](https://github.com/Stavrospanakakis/cv/blob/main/assets/cv.pdf)

[![asciicast](https://asciinema.org/a/405432.svg)](https://asciinema.org/a/405432)

## <div id="site2">8. Αίτημα ενσωμάτωσης στην ιστοσελίδα</div>
Παρακάτω υπάρχουν τα links απο τα issues που άνοιξα ή ήμουν σχετικός συνεργάτης στην ιστοσελίδα του τμήματος για 
αυτό το παραδοτέο.

1. [Minify Code in production](https://github.com/ioniodi/sitegr/issues/195)
2. [Προσθήκη Docker](https://github.com/ioniodi/sitegr/issues/192)
3. [Προσθήκη Documentation](https://github.com/ioniodi/sitegr/issues/199)

## <div id="term3">9. Άσκηση γραμμής εντολών</div>
create your own static site and blog generator

Σε αυτό το παραδοτέο, δημιούργησα from scratch ένα static site generator.
Η γλώσσα που αποφάσισα να το κάνω είναι η Golang. Ο λόγος είναι επειδή 
είμαι οικείος με τη γλώσσα και είναι πάρα πολύ γρήγορα για αυτές τις περιπτώσεις.
Παρακάτω μπορείτε να δείτε το repository όπου υπάρχουν οδηγίες εγκατάστασης και το 
σχετικό asciinema για να δείτε το πώς μπορεί να χρησιμοποιηθεί.

- [CLI Repository](https://github.com/Stavrospanakakis/yasg)
[![asciicast](https://asciinema.org/a/408729.svg)](https://asciinema.org/a/408729)

## <div id="sym2">10. Συμμετοχικό περιεχόμενο</div>
Σε αυτό το παραδοτέο έπρεπε να προσθέσω μια βιογραφία και μία μελέτη περίπτωσης. Η βιογραφια 
που πρόσθεσα αφορά τον Uncle Bob και η μελέτη περίπτωσης τα Apple Airpods. Ο λόγος για τον
Uncle Bob ήταν επειδή έχει παίξει μεγάλο ρόλο στο software με τα βιβλία του και είναι ένας
άνθρωπος ο οποίος θαυμάζω προσωπικά και τα Apple Airpods διότι πρόσθεσαν αρκετό software 
σε ένα προιόν που τόσα χρόνια αφορούσε κυρίως το Hardware.

- [Apple Airpods Image](https://github.com/Stavrospanakakis/images/blob/master/airpods.jpg)
- [Apple Airpods Thumbnail](https://github.com/Stavrospanakakis/images/blob/master/airpods-thumb.jpg)
- [Apple Airpods Case Study](https://github.com/Stavrospanakakis/site/blob/master/_case-study/airpods.md)
- [Apple Airpods Extras](https://github.com/Stavrospanakakis/extras/blob/master/airpods.md)

- [Uncle Bob Image](https://github.com/Stavrospanakakis/images/blob/master/uncle-bob.jpg)
- [Uncle Bob Thumbnail](https://github.com/Stavrospanakakis/images/blob/master/uncle-bob-thumb.jpg)
- [Uncle Bob Biography1](https://github.com/Stavrospanakakis/site/blob/master/_biography/uncle-bob.md)
- [Uncle Bob Biography2](https://github.com/Stavrospanakakis/site/blob/master/_biography/bio-bob.md)

- [Pibook Repository](https://github.com/Stavrospanakakis/site)
- [Gallery Repository](https://github.com/stavrospanakakis/_gallery)
- [Images Repository](https://github.com/stavrospanakakis/images)
- [Extra Repository](https://github.com/stavrospanakakis/extras)

## <div id="term4">11. Άσκηση γραμμής εντολών</div>
build and deploy your static site and your cv dynamically every time you make a small change in the source files

Σε αυτό το παραδοτέο, λόγω των δωρεάν credits που είχα στην AWS σκέφτηκα να εκμεταλλευτώ την ευκαιρία
και να δημιουργήσω ένα CI το οποίο θα κάνει integrate με την υπηρεσία της Amazon S3. Κάθε φορά που 
κάνω μία αλλαγή στο repository, το CI κάνει build το site και το κάνει deploy στο S3 Bucket που έχω 
δημιουργήσει. Παρακάτω μπορείτε να δείτε το repository του site και το file του Github Action.

- [Project Repository](https://github.com/Stavrospanakakis/aws-s3-actions-website)
- [Action file](https://github.com/Stavrospanakakis/aws-s3-actions-website/blob/main/.github/workflows/main.yml)

[![asciicast](https://asciinema.org/a/413094.svg)](https://asciinema.org/a/413094)
Action Screenshot
![image](https://user-images.githubusercontent.com/53979866/117645707-900cd100-b193-11eb-84d0-a47f515c470c.png)

## Συμπεράσματα
Τέλος, θεωρώ πως πέτυχα όλους τους στόχους που είχα για το μάθημα. Όπως αναφέρω
και στην εισαγωγή ήθελα να δώσω βάση στο CI, Docker και Static Site Generators.
Κάνοντας όλα τα παραδοτέα χρησιμοποίησα το CI τόσο στην άσκηση για το βιογραφικό
όπου έκανα generate ένα pdf αρχείο σε κάθε push όσο και σε ένα παραδοτέο γραμμής
εντολών όπου υπήρχε μέσω CI integration μεταξύ Github και AWS. Χρησιμοποίησα το
Docker στο παραδοτέο για την άσκηση γραμμής εντολών, στο CI μέσω των Github Actions
αλλά και σε προσωπικό development για την διευκόλυνση επικοινωνίας του stack μου.
Όσον αφορά τους static site generators τους χρησιμοποιήσα επίσης στα παραδοτέα και
έμαθα πως λειτουργούν low level φτιάχνοντας έναν δικό μου σε ένα παραδοτέο γραμμής εντολών.

## Quiz

#### Quiz 1
**Ποια είναι σύμφωνα με τον Αλαν Κεη η μεγαλύτερη παγίδα σε ένα μάθημα υπολογιστών και ποια είναι κατά την γνώμη σας η αντίστοιχη της ΙΒΜ τεχνολογία λογισμικού στις μέρες μας;**

Η μεγαλύτερη παγίδα σε ένα μάθημα υπολογιστών σύμφωνα με τον Alan Kay είναι το να προσπαθείς να περάσεις τις απόψεις σου στους μαθητές. Ο καθηγητής του Alan Kay μισούσε την IBM διότι η αποδοτικότητά της έκανε τους χρήστες να νομίζουν ότι η IBM ήταν ο μόνος τρόπος να κάνουν πράγματα. Θα μπορούσαμε να πούμε ότι η αντίστοιχη της IBM σήμερα είναι η Microsoft με τα Windows.

**Ποια είναι η αναλογία του πραγματικού κόσμου για την αρχιτεκτονική και για τα υλικά και για ποιο λόγο δεν είναι εφαρμόσιμη στην περίπτωση του λογισμικού;**

Ο Alan Kay έδωσε σαν παράδειγμα για την αναλογία το σπίτι ενός σκύλου. Πιο συγκεκριμένα τόνισε πως έχοντας καλά υλικά ακόμη και ένα παιδί πέντε χρονών θα μπορούσε να το φτιάξει. Αντιθέτως, στο λογισμικό ισχυεί το αντίθετο, δηλαδή πως πρέπει να έχεις τις γνώσεις για να το κάνεις.

#### Quiz 2
**Ποιος είναι ορισμός της τεχνολογίας λογισμικού για τον Ted Nelson και ποια είναι η διαφορά με το πακετάρισμα και τις πολιτικές της τεχνολογίας; Να δώσετε ένα τουλάχιστον παράδειγμα όπου φαίνονται οι διαφορές.**

O ορισμός της τεχνολογίας λογισμικού για τον Ted Nelson είναι η επίλυση ενός προβλήματος που σχετίζεται με το λογισμικό. Η διαφορά με το πακετάρισμα είναι πως το πακετάρισμα είναι στην ουσία ένας συνδιασμός τεχνολογιών όπου παράγουν ένα προϊόν. πχ iPhone

**Ποια ήταν η αρχική χρησιμότητα της τεχνολογίας των αρχείων; Είναι τα αρχεία ο καλύτερος τρόπος για την οργάνωση της πληροφορίας από την πλευρά του χρήστη;**

Η αρχική χρησιμότητα της τεχνολογίας των αρχείων ήταν για την οργάνωση της πληροφορίας. Τα αρχεία δεν είναι ο καλύτερος τρόπος για την οργάνωση της πληροφορίας λόγω της ποικιλίας και της ασυμβατότητας μεταξύ των εταιριών.


#### Quiz 3

**Γιατί υπάρχει αντίσταση απέναντι στις νέες γλώσσες προγραμματισμού υψηλού επιπέδου; Να δώσετε ένα παράδειγμα από την δική σας εμπειρία.**

Ο λόγος που υπάρχει αντίσταση απέναντι στις νέες γλώσσες προγραμματισμού υψηλού επιπέδου είναι διότι οι προγραμματιστές πρέπει να σταματήσουν να σκέφτονται με τον τρόπο που έχουν μάθει και συνηθίσει και πρέπει να μάθουν να σκέφτονται με διαφορετικό τρόπο. 

**Προγραμματίζουμε την ιστοσελίδα της σχολής χωρίς στυλ και ετικέτες! Πέτυχε την πρόβλεψη του ή εμείς κάνουμε κάτι διαφορετικό από τον συνηθισμένο προγραμματισμό ιστοσελίδας;**

Δεν υπάρχει ακριβώς σωστή απάντηση για αυτή την ερώτηση. Γενικά στον προγραμματισμό ιστοσελίδας έχουμε την επιλογή ενός έτοιμου theme αλλά μπορούμε να χρήσιμοποιήσουμε και στυλ και ετικέτες στον προγραμματισμό. Άρα, δεν πέτυχε την πρόβλεψη του διότι το στυλ, ετικέτες, markup γλώσσες κλπ χρησιμοποιούνται ακόμη

**Προγραμματίζουμε την ιστοσελίδα της σχολής με κείμενο. Γιατί πέφτει τόσο έξω στην πρόβλεψη του;**

Πέφτει έξω στην πρόβλεψη του διότι πίστευε πως υπάρχουν πολλοί διαφορετικοί τρόποι για να αποτυπώσουμε την πληροφορία.

**Ποιος είναι υπεύθυνος για το προγραμματιστικό δόγμα των ημερών μας και πως θα μπορούσαμε να σκεφτούμε με νέους τρόπους;**

Θα μπορούσαμε να σκεφτούμε με νέους τρόπους αν σκεφτούμε ότι δεν ξέρουμε τι ακριβώς κάνουμε. Έτσι θα μπούμε στη διαδικασία να δοκιμάσουμε καινούριες ιδέες πέρα από τις συνηθισμένες


