# Οπτικοποίηση δεδομένων χορηγιών (UK)

Δήλωση και δέσμευση θέματος εργασίας στο μάθημα Τεχνολογία Λογισμικού

* Ονοματεπώνυμο: Βασιλική Πολυχρόνη
* Α.Μ.:Π2015084
* Εξάμηνο Φοίτησης: ΣΤ'

### Σύνδεσμοι
* Προσωπικό αποθετήριο του κώδικα : https://github.com/p15poly/D3js-uk-political-donations/tree/gh-pages
* Link για το εκτελέσιμο: https://p15poly.github.io/D3js-uk-political-donations/

# 1ο Παραδοτέο
* σύνδεσμος με την σελίδα της εφαρμογής 
https://p15poly.github.io/D3js-uk-political-donations/

* Αλλαγή χρωμάτων στις μπάλες και στα 3 πεδία της ομαδοποίησης Split by party.
#### πριν
![screenshot_1](https://user-images.githubusercontent.com/22655118/37254304-b53b797e-2544-11e8-99d5-9c1c649d0f3b.png)
### μετά
![screenshot_3](https://user-images.githubusercontent.com/22655118/37254439-8af0a11a-2546-11e8-8005-8c202cd7f0ab.png)
![screenshot_2](https://user-images.githubusercontent.com/22655118/37254424-5b6a6886-2546-11e8-9dfc-f4de29c0c894.png)
 
* Ήχος κάθε φορά που ο χρήστης της εφαρμογής κάνει κλικ σε μία από τις επιλογές/κουμπιά ομαδοποίησης των δεδομένων.

Τον ήχο τον βρήκα από αυτή την σελίδα -->( https://www.zapsplat.com/music/sleigh-bells-pick-up-from-table/ ) και τον ανέβασα στο αποθετήριο της εφαρμογής μου --> ( https://github.com/p15poly/D3js-uk-political-donations/blob/gh-pages/sound.mp3 ).
Τις αλλαγές τις έκανα στο αρχείο index.html .

*  Άνοιγμα νέου παραθύρου με τα αποτελέσματα της αναζήτησης στο google για τον αντίστοιχο δωρητή.

Για να ανοίγει ένα νέο παράθυρο με τα αποτελέσματα της αναζήτησης με κάθε κλικ σε μπάλα για τον αντίστοιχο δωρητή, δημιούργησα μία συνάρτηση (με όνομα gS ) στο αρχείο chart.js, στο οποίο και έκανα τις αντίστοιχες αλλαγές που χρειάζονταν όπως φαίνεται -->( https://github.com/p15poly/D3js-uk-political-donations/blob/gh-pages/chart.js )

![screenshot_1](https://user-images.githubusercontent.com/22655118/37286051-85c676ec-2609-11e8-8a71-45e7c31ed12c.png)
![screenshot_2](https://user-images.githubusercontent.com/22655118/37286076-978428c0-2609-11e8-83c6-3871e2e3e19e.png)


* Μεγενθυντικός φακός

Δημιούργησα μια κλάση zoom έτσι ώστε να αλλάζει το μέγεθος της γραμματοσειράς στο αρχείο style.css. Οι αντίστοιχες αλλαγές φαίνονται-->( https://github.com/p15poly/D3js-uk-political-donations/blob/gh-pages/style.css )
Πρόσθεσα επίσης στο αρχείο index.html (στο τέλος) κάποιο script έτσι ώστε να γίνεται μεγένθυση στις ετικέτες που πρέπει.Οι αντίστοιχες αλλαγές φαίνονται-->( https://github.com/p15poly/D3js-uk-political-donations/blob/gh-pages/index.html )
(δεν κατάφερα βέβαια να το κάνω να λειτουργήσει)

* Δημιουργία νέας επιλογής ομαδοποίησης των δεδομένων: Split by the amount of the donation

Στο αρχείο index.html  πρώτα δημιούργησα το νέο κουμπί (Split by the amount of the donation) στην περιοχή που υπήρχαν και τα υπόλοιπα κουμπιά και στη συνέχεια πρόσθεσα το &lt;div id="view-donation-amount"&gt;. Oι αντίστοιχες αλλαγές φαίνονται--> ( https://github.com/p15poly/D3js-uk-political-donations/blob/gh-pages/index.html )
 
![screenshot_3](https://user-images.githubusercontent.com/22655118/37287566-c2f33cae-260d-11e8-9576-392e5745cf1b.png)
![screenshot_4](https://user-images.githubusercontent.com/22655118/37287851-6de9a878-260e-11e8-8876-bd52f53ed9ab.png)
 

