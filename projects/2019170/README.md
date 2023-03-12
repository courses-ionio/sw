Τεχνολογία Λογισμικού 
========================
### Ονοματεπώνυμο: Μάρκου Δήμητρα
### ΑΜ: Π2019170
### Organization: [Paneksypnes Diepafes](https://github.com/PaneksypnesDiepafes/Main)
#### GitHub Profile: [marked-d](https://github.com/marked-d "Μάρκου Δήμητρα") | Asciinema: [markedd](https://asciinema.org/~markedd) | Υποστηρικτικό Υλικό: [SW+](https://github.com/marked-d/SW_plus/tree/main)

| Εβδομάδα | Παραδοτέα | [Εβδομαδιαία Παρουσίαση Προόδου](https://github.com/courses-ionio/sw/discussions/categories/show-and-tell) | Αυτοαξιολόγηση |
| --- | --- | --- | --- |
| 1 | Εισαγωγή και Δημιουργία ομάδας|[Εισαγωγή](https://github.com/courses-ionio/sw/discussions/1212) και [Ομάδα](https://github.com/PaneksypnesDiepafes/Main)| |
| 2 | [Γραμμή εντολών](https://epidrome.github.io/teaching/cli) (systemd) και [διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας](https://epidrome.github.io/teaching/team) |[Ntfy](https://github.com/courses-ionio/sw/discussions/1285)| |
| 3 | Γραμμή εντολών (no systemd) |[Funtoo](https://github.com/courses-ionio/sw/discussions/1340)| |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά) |[Reactable](https://github.com/courses-ionio/sw/discussions/1391)| |
| 5 | Συμμετοχικό περιεχόμενο A1 + A2 | | |
| 6 | Γραμμή εντολών (no systemd, custom static blog generator) | | |
| 7 | Συμμετοχικό περιεχόμενο B1 | | |
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) | | |
| 9 | Συμμετοχικό περιεχόμενο B2 | | |
| 10 | Τελική αναφορά* | | |

1<sup>o</sup> Παραδοτέο 
========================
Εισαγωγή
-------------------------------------------------------------------
Από το μάθημα Τεχνολογία Λογισμικού έχω σκοπό να μάθω καινούρια εργαλεία και δεξιότητες και να μάθω τη διαφορά μεταξύ systemd και no systemd προγραμμάτων. Μέσω της συνεργατικότητας του μαθήματος θέλω να μάθω να δουλεύω πιο ομαδικά και να βοηθάω τους συνεργάτες μου καθώς και να είμαι πιο πρόθυμη στο να ζητήσω βοήθεια, το οποίο θα με βοηθήσει και στην καθημερινότητα μου μιας και είναι κάτι δύσκολο για εμένα.

Ομάδα
------------------------------------------------------------------------------------------
### ***Paneksypnes Diepafes***
![dynacat](https://avatars.githubusercontent.com/u/125203571?s=200&v=4)

|#|Μέλη|ΑΜ|Admin|Assigned Members|
|---|---|---|---|---|
|1|[Λιθαρής Νίκος](https://github.com/NickLitharis)|Π2019083|:bust_in_silhouette:||
|2|[Μάρκου Δήμητρα](https://github.com/marked-d)|Π2019170||:busts_in_silhouette:|
|3|[Οικονόμου Οδυσσέας](https://github.com/odysseasEko/)|Π2019060||:busts_in_silhouette:|
|4|[Τουρτσάκης Κωνσταντίνος](https://github.com/KonstantinosTourtsakis)|Π2019140||:busts_in_silhouette:|
|5|[Παναγιωταράκης Νίκος](https://github.com/tarakhs/)|Π2019152|:bust_in_silhouette:||
|6|[Αρτινόπουλος Ορέστης](https://github.com/voltmaister)|Π2019153||:busts_in_silhouette:|
|7|[Θώμος Άγγελος](https://github.com/Angeloth1/)|Π2019095||:busts_in_silhouette:|

2<sup>o</sup> Παραδοτέο 
========================
Για αυτό το παραδοτέο έγραψα ένα [script](https://github.com/marked-d/SW_plus/blob/main/cpu_ram_ntfy.py) σε python το οποίο υπολογίζει το CPU Usage και το Memory που χρησιμοποιείται και μέσω του Ntfy στέλνω ειδοποίηση στο desktop και στο κινητό μου, μέσω της εφαρμογής του Ntfy. Η άσκηση έγινε σε Arch Linux (σύστημα με systemd), το οποίο είχα ήδη εγκατεστημένο λόγω του μαθήματος Επικοινωνία Ανθρώπου - Υπολογιστή.

[![asciicast](https://asciinema.org/a/563099.svg)](https://asciinema.org/a/563099)

Ειδοποίηση στο desktop: <br/>
![ntfy](https://github.com/marked-d/SW_plus/blob/main/ntfy.png) 

Ειδοποίηση στο κινητό:<br/>
![ntfy_push](https://github.com/marked-d/SW_plus/blob/main/ntfy_push.png)

Επιπλέον, αυτή την εβδομάδα με τον οργανισμό συντάξαμε ένα "Μανιφέστο" όπου περιγράφουμε τις υποχρεώσεις κάθε ρόλου του οργανισμού, το workflow καθώς και κάποιους κανόνες όσων αφορά τα pull request που θα γίνονται προς τον οργανισμό. Προς το παρών είναι private repository αλλά θα γίνει σύντομα public.

3<sup>o</sup> Παραδοτέο 
========================
Για αυτό το παραδοτέο έγινε εγκατάσταση του Funtoo στο Virtual Box ακολουθώντας τις οδηγίες του [guide](https://github.com/PaneksypnesDiepafes/cookbook/blob/main/funtoo-installation.md) που γράψαμε με τον οργανισμό μου. 

[![asciicast](https://asciinema.org/a/564879.svg)](https://asciinema.org/a/564879)

4<sup>o</sup> Παραδοτέο 
========================
Για αυτό το παραδοτέο έκανα μια προσθήκη στο 4ο κεφαλαιο στην υποενότητα 4.5 "Η περίπτωση του Reactable".

![contribution](https://github.com/marked-d/SW_plus/blob/main/contibution.png)
