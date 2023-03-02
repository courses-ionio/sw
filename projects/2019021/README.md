### Σταυρούλα Ανατολάκη
### ΑΜ: Π2019021
### Οργανισμός : [GENESIS](https://github.com/Genesis-The-Beginning)

| Εβδομάδα | Παραδοτέο | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/sw/discussions) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | [Εισαγωγή](https://github.com/StavroulaAnatolaki/sw/blob/2019021/projects/2019021/README.md#%CE%B5%CE%B2%CE%B4%CE%BF%CE%BC%CE%AC%CE%B4%CE%B1-1-%CE%B5%CE%B9%CF%83%CE%B1%CE%B3%CF%89%CE%B3%CE%AE) | [link](https://github.com/courses-ionio/sw/discussions/1153) |Επιτυχής ολοκλήρωση του παραδοτέου εντός προθεσμίας |
| 2 | [Γραμμή εντολών (systemd) και διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας](https://github.com/StavroulaAnatolaki/sw/blob/2019021/projects/2019021/README.md#%CE%B5%CE%B2%CE%B4%CE%BF%CE%BC%CE%AC%CE%B4%CE%B1-2-%CE%AC%CF%83%CE%BA%CE%B7%CF%83%CE%B7-%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%AE%CF%82-%CE%B5%CE%BD%CF%84%CE%BF%CE%BB%CF%8E%CE%BD) |[link](https://github.com/courses-ionio/sw/discussions/1301) |Επιτυχής ολοκλήρωση του παραδοτέου εντός προθεσμίας |
| 3 | [Γραμμή εντολών (no systemd)](https://github.com/StavroulaAnatolaki/sw/blob/2019021/projects/2019021/README.md#%CE%B5%CE%B2%CE%B4%CE%BF%CE%BC%CE%AC%CE%B4%CE%B1-3-%CE%AC%CF%83%CE%BA%CE%B7%CF%83%CE%B7-%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%AE%CF%82-%CE%B5%CE%BD%CF%84%CE%BF%CE%BB%CF%8E%CE%BDno-systemd) |link | |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά) |link | |
| 5 | Συμμετοχικό περιεχόμενο A1 + A2 |link | |
| 6 | Γραμμή εντολών (custom static blog generator) |link | |
| 7 | συμμετοχικό περιεχόμενο B1 |link | |
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) |link | |
| 9 | συμμετοχικό περιεχόμενο B2 |link | |
| 10 | Τελική αναφορά* |link | |

| Εβδομάδα | Βίντεο Κουιζ | Ολοκληρώθηκε | Εμπρόθεσμα | 
| --- | --- | --- | --- |
| 1 |Alan Kay at MIT-EECS 1998 Fall Semester Colloquium Series (VPRI 834) |  ✔️  | ✔️ | 
| 2 |Ted Nelson -- Computers for Cynics (full version) | ✔️ | ✔️ | 
| 3 |Alan Kay - Could Computing Be Simpler Than It Seems To Be? |  |  | 

# Εβδομάδα 1: Εισαγωγή
Στο μαθημα "Τεχνολογια Λογισμικου" σκοπευω να μελετησω και να συμμετασχω στην αναπτυξη και την σχεδιαση λογισμικου. Περα απο αυτο υπαρχουν τα εβδομαδιαια κουιζ μεσα απο τα οποια πιστευω οτι θα αποκτησω πολλες χρησιμες γνωσεις. Ελπιζω μεχρι το τελος του μαθηματος να εχω πετυχει τους παρακατω στοχους:

* Ολοκληρωση εργασιων και ασκησεων μεσα σε πολυ μικρο χρονικο διαστημα
* Αποκτηση εμπειριας και γνωσεων σχετικα με το περιβαλλον και τον τροπο λειτουργιας του λογισμικου
* Αναπτυξη της ομαδικοτητας μου
* Καλυτερη κατανοηση του λειτουργικου συστηματος Linux

# Εβδομάδα 2: Άσκηση γραμμής εντολών(systemd)

Για αυτο το παραδοτεο χρησιμοποιησα το λειτουργικο συστημα Arch Linux εγκατεστημενο σε VirtualBox. Μετα ετρεξα τις εντολες neofetch ([asciinema recording](https://asciinema.org/a/3k6f5xbQeGjKxWKmL43lbC1kF)) και journalctl -b ([asciinema recording](https://asciinema.org/a/aNxUZ1oos2iW33pgc8fCspAZO)).


![VirtualBox_Arch Linux_25_02_2023_00_11_48](https://user-images.githubusercontent.com/72880868/221351050-3b3a5907-704c-4d91-b127-cf0f3341e821.png)

![VirtualBox_Arch Linux_25_02_2023_00_09_37](https://user-images.githubusercontent.com/72880868/221351058-183b2dd3-6b1a-47a2-bac0-1d4f39b4442a.png)

Ως ασκηση διαλεξα να τρεξω την εντολη ntfy ([asciinema recording](https://asciinema.org/a/bPGO52HUtwnTGtH0LnBxhPlmp)) στο λογισμικο. Με αυτη την εντολη μπορεις να στειλεις μηνυματα, ανακοινωσεις κτλ απο το λογισμικο στο κινητο σου.
Χρειαστηκε να εγκαταστησω και την εφαρμογη στο κινητο μου, ωστε να λαμβανω αυτα που στελνω απο το λογισμικο.

![VirtualBox_Arch Linux_25_02_2023_00_06_27](https://user-images.githubusercontent.com/72880868/221536314-c6222bca-4438-425f-9c0e-2b247b4cf3ac.png)

![IMG_0595](https://user-images.githubusercontent.com/72880868/221539621-ed2c79ce-b0ae-4fde-853b-8dc633c37e63.gif) ![IMG_0596](https://user-images.githubusercontent.com/72880868/221539653-879f314f-cbf0-4bd0-a5a9-1387ab917b0a.gif)



### Πηγές
* [link](https://www.youtube.com/watch?v=u9EcWrsjE20)
* [link](https://ntfy.sh/)

# Εβδομάδα 3: Άσκηση γραμμής εντολών(no systemd)

# Ομαδικότητα
https://github.com/courses-ionio/sw/discussions/1162

https://github.com/courses-ionio/sw/discussions/1259#discussioncomment-5113354
