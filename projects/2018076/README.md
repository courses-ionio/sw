# Τεχνολογία Λογισμικού 

### Προσωπικό Github προφίλ: [aggelos2000430](https://github.com/aggelos2000430)
### Ονοματεπώνυμο: Μπουικλής Άγγελος
### Αριθμός Μητρώου: Π2018076
### [Ο οργανισμός μου](https://github.com/lapis-lazuli-ore-block)
### [Το Asciinema μου](https://asciinema.org/~p18boui)


| Εβδομάδα | [Όλα τα παραδοτέα βρίσκονται στην ίδια σελίδα της τελικής αναφοράς](https://epidrome.github.io/teaching/deliverables/) με τα προσωπικά στοιχεία σας (Όνομα, ΑΜ, github profile) και μαζί με αυτόν εδώ τον πίνακα περιεχομένων | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | Δημιουργία ομάδας + [Φορκ και δημιουργία σελίδας τελικής αναφοράς](https://epidrome.github.io/teaching/guide/), [προσθήκη πίνακα περιεχομένων](https://raw.githubusercontent.com/courses-ionio/sw/master/README.md), [συγγραφή της εισαγωγής](https://epidrome.github.io/teaching/intro/), αποστολή της εισαγωγής [για σχολιασμό στην συζήτηση](https://github.com/courses-ionio/sw/discussions/categories/show-and-tell) και καταγραφή του συνδέσμου συζήτησης δίπλα --> |[Link to discussions](https://github.com/courses-ionio/sw/discussions/1142)| |
| 2 | Γραμμή εντολών (systemd) και διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας | [Link to discussions](https://github.com/courses-ionio/sw/discussions/1262) | |
| 3 | Γραμμή εντολών (no systemd) | [Link to discussions](https://github.com/courses-ionio/sw/discussions/1335) | |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά) | | |
| 5 | Συμμετοχικό περιεχόμενο A1 + A2 | | |
| 6 | Γραμμή εντολών (custom static blog generator) | | |
| 7 | συμμετοχικό περιεχόμενο B1 | | |
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) | | |
| 9 | συμμετοχικό περιεχόμενο B2 | | |
| 10 | Τελική αναφορά* | | |

# Εισαγωγή

Μιας και στόχος μου είναι η ενασχόληση με την ανάπτυξη λογισμικού, στην επαγγελματική μου καριέρα, θεωρώ πως η τεχνολογία λογισμικού θα με φέρει σε επαφή με σημαντικά εργαλεία. Η εξοικείωση για παράδειγμα με την γραμμή εντολών, αποτελεί μια ικανότητα κομβική για έναν επαγγελματία του χώρου της ανάπτυξης λογισμικού, γι' αυτό και με ενδιαφέρει σε μεγάλο βαθμό. Οι άνθρωποι που ασχολούνται πολύ σοβαρά με το λογισμικό, θα πρέπει να φτιάξουν το δικό τους υλικό- Alan Kay. Όπότε κι εγώ με τη σειρά μου, στην ενασχόληση μου με το λογισμικό, θα ήθελα στο μέλλον να αναπτύξω ένα "μποτ συναλλαγών" το οποίο θα με διευκολύνει στην κύρια εργασία μου, το Foreign Exchange trading. To "μποτ" αυτό θα μπορεί να βλέπει ευκαιρίες για συναλλαγές που εγώ ίσως δεν παρατήρησα ή φοβήθηκα να εκτελέσω, αφού στον χώρο είναι πολύ σημαντική η καταπολέμηση των συναισθημάτων, γι αυτό ένα ρομπότ δίχως συναισθήματα θα μου φανεί πολύ χρήσιμο όχι για δογματική ακολούθηση αλλά ως συμπληρωματική βοήθεια. Αργότερα ίσως αυτό το λογισμικό εφαρμοστεί και σε φυσικό υλικό, όπου ο χρήστης θα μπορεί να ρυθμίσει το μέγεθος των συναλλαγών, το μέγιστο ρίσκο αυτών και τέλος το ελάχιστο κέρδος που θα πρέπει να προσφέρει μια συναλαγή για να "αξίζει τον κόπο". Επιπλέον μέσω τον βίντεο μας δίνεται η ευκαιρία να παρακολουθήσουμε κομβικές στιγμές από την εξέλιξη του ηλεκτρονικού υπολογιστή και φυσικά από πολύ σημαντικές προσωπικότητες που το όραμά τους αποτελεί πηγή έμπνευσης για εμάς τους μελλοντικούς επιστήμονες της Πληροφορικής. Εν κατακλείδι μέσω του μαθήματος, ευελπιστώ να μου δοθούν ερεθίσματα που θα με βοηθήσουν να έρθω, ένα βήμα τη φορά, πιο κοντά στο μεγαλύτερο μου όραμα.


# Λειτουργικό Σύστημα Syestemd & NoSystemd
## Για το Παραδοτέο02
Η ανάπτυξη του systemd ήρθε να αντικαταστήσει το παλιαότερο SysV init και είχε στόχο να αντιμετωπίσει διάφορα προβλήματα στα συστήματα εκκίνησης σε διανομές Linux. Κάποια από αυτά τα προβλήματα ήταν:
- η έλλειψη παραλληλισμού και απλού συστήματος
- διαχείρισης εξαρτώμενων πακέτων λογισμικού, όπως και η κεντρική διαχείριση των προγραμμάτων που αρχίζουν την εκτέλεση τους κατά την εκκίνηση του υπολογιστή.

Το systemd υποστήριζε:
- την εκκίνηση εφαρμογών μέσω Dbus,
- την επαναφορά προηγούμενων καταστάσεων συστήματος,
- την παρακολούθηση διεργασιών μέσω των cgroups του πυρήνα Linux,
- τον ορισμό εξειδικευμένων τοποθεσιών στο σύστημα για πρόσθεση και αφαίρεση υλικού (mounting και unmounting)
- και την λογική διαχείρισης εργασιών και προγραμμάτων με ένα σκεπτικό αλληλοεξαρτήσεων,

Συνολικά προσέφερε στον μέσο χρήστη καλύτερη εμπειρία και αρκετό έλεγχο, χωρίς ταυτόχρονα να απαιτεί υπερβολικό χρόνο εκμάθησης.

### Καθημερινό Λειτουργικό Σύστημα ArchLinux

<h1 align=center></b>
<p align="center">
<a href="" target="_blank"></a>

[Neofetch](https://asciinema.org/a/535951)

<p align="center">
<a href="https://asciinema.org/a/535951" target="_blank"><img src="https://asciinema.org/a/535951.svg" width="70%" /></a>

## Για το Παραδοτέο03

Κάποια μέλη της κοινότητας δυσαρέστήθηκαν με το systemd λόγω:
- της αρχιτεκτονικής του συστήματος αρχείων,
- της χρήσης του λογισμικού Dbus
- το μέγεθος του πολύ μεγαλύτερο

> __*Since Funtoo is a source-based meta-distribution and packages are built with Portage, we exist in the living wilderness, among raw creative energy of the wild free software ecosystem. Like a wolf, our connection to the vibrant and sustaining open source wilderness is tangible and real. We avoid the over-developed, sanitized, isolated and boring pre-packaged world where disconnected users simply ‘consume’ what was pre-made for them, preferring the more authentic and connected life where we are in control of our destiny.*__

Για τις ανάγκες του μαθήματος αποφάσισα να εγκαταστήσω τη διανομή Funtoo Linux, το οποίο επιτρέπει στο χρήστη να δημιουργήσει έναν Linux kernel προσαρμοσμένο στο συγκεκριμένο υλικό του υπολογιστή τους. Επιτρέπει τον έλεγχο των εγκατεστημένων και εκτελέσιμων, συμπεριλαμβανομένης της επιλογής επιλογής OpenRC ως προεπιλεγμένου συστήματος έναρξης. Επίσης η χρήση μνήμης μπορεί να μειωθεί σε σύγκριση με άλλες διανομές παραλείποντας περιττές λειτουργίες και υπηρεσίες πυρήνα.
- [x] Επιτυχής εγκατάσταση του συστήματος σε εικονική μηχανή
- [x] Μερική προσαρμογή του ώστε να καλύπτει τις ανάγκες του μαθήματος
- [x] Προσθήκη γραφικού περιβάλλοντος
### Χειροποίητο Σύστημα Λογισμικού Funtoo Linux

<h1 align=center></b>
<p align="center">
<a href="" target="_blank"></a>

[Neofetch](https://asciinema.org/a/563441)

<p align="center">
<a href="https://asciinema.org/a/563441" target="_blank"><img src="https://asciinema.org/a/563441.svg" width="70%" /></a>



# **Static Blog**

Ανέπτυξα ένα shell script το οποίο όταν εκτελείται παράγει ένα αρχείο index.html που αποτελεί ένα static blog το οποίο έπειτα μπορεί να τροποποιηθεί κατάλληλα για να καλύπτει της ανάγκες του χρήστη επεξεργάζοντας το αρχικά τοπικά. Έπειτα δημιούργησα ένα αποθετήριο στο github το οποίο φιλοξενεί το Blog.

- [Το repository του Blog](https://github.com/aggelos2000430/forexBlog.github.io)
- [#!/bin/bash](https://github.com/aggelos2000430/forexBlog.github.io/blob/main/blog.sh)
- [Το Blog](https://aggelos2000430.github.io/forexBlog.github.io/)

# **Άσκηση Γραμμής εντολών**

Επέλεξα να στείλω notification απο το terminal του Funtoo Linux προς το κινητό μου. Αρχικά κατέβασα την εφαρμογη του ntfy στο Android κι έπειτα εκτέλεσα την εντολή **curl -d "myMessage" ntfy.sh/mytopic**

<p align="center">
<a href="https://asciinema.org/a/564362" target="_blank"><img src="https://asciinema.org/a/564362.svg" width="70%" /></a>

<img src="https://github.com/aggelos2000430/sw/blob/2018076/projects/2018076/github.jpg" alt="Alt Text" width="70%" />



# **Βίντεο Quiz**

| X | Τίτλος | Ολοκληρώθηκαν | Εμπρόθεσμα |
| ---- | ---- | ---- | ---- |
| 1 | Alan Kay at MIT-EECS 1998 Fall Semester Colloquium Series | :heavy_check_mark: | :heavy_check_mark: |
| 2 | Ted Nelson -- Computers for Cynics [full version] | :heavy_check_mark: | :heavy_check_mark: |
| 3 | Alan Kay - Could Computing Be Simpler Than It Seems To Be? | :heavy_check_mark: | :heavy_check_mark: |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |
