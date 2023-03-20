# Μάθημα: Τεχνολογία Λογισμικού

### Ονοματεπώνυμο: Ιωάννης Πανόπουλος
### Αριθμός Μητρώου: Π2019217
### Edpuzzle Profile: [P2019217](https://asciinema.org/~P2019217)
### Github Profile: [P2019217](https://github.com/P2019217)<br><br>

# Παραδοτέο 1
*Εισαγωγή*</br>
Το μάθημα πιστεύω θα με βοηθήσει αρκετά μιας και θέλω να ασχοληθώ με το ethical hacking και γίνεται στην περιοχή του Github που είναι μία περιοχή που έχει και αρκετά repositories για ethical hacking όπως πχ.airgeddon. Επιπλέον θα με βοηθήσει να μάθω συστήματα πέρα από το systemd, μιας και τα Kali Linux που χρησιμοποιώ, χρησιμοποιούν το systemd. Επιπλέον οι ασκήσεις γραμμής εντολών πιστεύω θα με βοηθήσουν αρκετά και ειδικά η άσκηση με το [NTFY[telegram]](https://github.com/dschep/ntfy) μιας και θα μπορώ να ενημερώνομαι με μήνυμα μόλις μια διεργασία τελειώσει π.χ ένα [nmap](https://github.com/nmap/nmap) scan σε κάποιον server με πολλά ports. Τέλος θα βοηθηθώ στο να έχω μια πιο πλήρη κατανόηση του τρόπου λειτουργίας των Unix based συστημάτων.

[Discussions](https://github.com/courses-ionio/sw/discussions/1172)

# Παραδοτέο 2
*Γραμμή εντολών*</br>
Tο systemd υπάρχει εγκατεστημένο στα Kali Linux, επομένως χρησιμοποίησα αυτό για την άσκηση,έτσι δημιούργησα ένα πρόγραμμα σε Bash που σκανάρει για ανοιχτά ports στο 192.168.1.1 (router), αποθηκεύει το scan σαν αρχείο txt και έπειτα διαβάζει αυτό το αρχείο txt, το αποθηκεύει σαν μεταβλητή message και χρησιμοποιεί το [NTFY[telegram]](https://github.com/dschep/ntfy) για να αποστείλει αυτό το scan σε μήνυμα από το Panopoulos_bot στο κινητό μου.
Παρακάτω βλέπετε το nmapscantomsg.sh:
```bash
#!/bin/bash
#Κάνει nmap σκαν και δημιουργεί στο directory που βρίσκεται ένα αρχείο message.txt
nmap -oG $(pwd)/message.txt 192.168.1.1
#Διαβάζει με το cat το αρχείο message.txt και το αποθηκεύει σε μία μεταβλητή $message
message=$(cat message.txt)
#Χρησιμοποιεί το ntfy[Telegram] προκειμένου να αποστείλει το περιεχόμενο της μεταβλητής $message
ntfy -b telegram send "$message"
```

[![asciicast](https://asciinema.org/a/NN2x9lToaRAJ85A7SbWFiPKx2.svg)](https://asciinema.org/a/NN2x9lToaRAJ85A7SbWFiPKx2)

Τα μηνύματα στο Telegram σε screenshot:

![screenshot](https://user-images.githubusercontent.com/100226514/220226677-2ceeafb8-51dd-444f-9cc8-01e8b54518c4.png)

[Discussions](https://github.com/courses-ionio/sw/discussions/1236)

## Παραδοτέο 3
*Γραμμή εντολών*</br>
Για αυτήν την εβδομάδα εγκατέστησα τα Antix Linux τα οποία δεν χρησιμοποιούν systemd αλλά μια εναλλακτική του το SysVinit. Επίσης έκανα κατάλληλα configure το ntfy telegram ώστε να μπορώ να στείλω μηνύματα από το shell των antix. Σε επόμενο στάδιο θα προσπαθήσω να συνδέσω το ntfy με κάποιο git project που κάνει bruteforce ώστε να με ειδοποιεί σχετικά με την τελική κατάσταση αυτής της διεργασίας.

[![asciicast](https://asciinema.org/a/WZxXkyIc2elWRK1Df5CEViYMb.svg)](https://asciinema.org/a/WZxXkyIc2elWRK1Df5CEViYMb)

[Discussions](https://github.com/courses-ionio/sw/discussions/1332)

## Παραδοτέο 4 
*PDF Βιβλίο μαθήματος*</br>
Για αυτήν την εβδομάδα τοποθέτησα την υποσημείωση μου στο βιβλίο του μαθήματος σχετικά με τα ολοκληρωμένα περιβάλλοντα ανάπτυξης του λογισμικού(IDE), χρησιμοποιήσα ένα αυτό το [φίλτρο](https://github.com/P2019217/kallipos/blob/master/comment.lua) σε συνδιασμό με τις κατάλληλες αλλαγές στο make-latex.sh, όπως πχ η αφαίρεση μιας εντολής που λειτουργεί μόνο σε Mac συστήματα ενώ υπάρχει και αντίστοιχη σύνταξη για την sed και στα Unix, δημιουργώντας με αυτό τον τρόπο το [βιβλίο](https://github.com/P2019217/kallipos/blob/master/book/p2019217.pdf) του μαθήματος.

![simeiwsi](https://user-images.githubusercontent.com/100226514/224506372-f00f2cb8-999b-441d-955e-4285426384fe.png)

## Παραδοτέο 5 
Για αυτήν την εβδομάδα πρόσθεσα στο site περιεχόμενο σχετικά με δύο λογισμικά που χρησιμοποιούνται στο security το πρώτο είναι ένας Network Mapper (nmap) και το δεύτερο το Metasploit πρόγραμμα που σου δίνει πληροφορίες σχετικά με ευπάθειες (vulnerabilities), το Metasploit έρχεται pre-installed μαζί με τα Kali-Linux.
[Site Repository](https://github.com/P2019217/site) / [Site Netlify](https://calm-marigold-1d4f28.netlify.app/)
[metasploit.md](https://github.com/P2019217/_gallery/blob/f366aca509686a21f6af076a19cccadefc98d276/metasploit.md) / [Metasploit Netlify](https://calm-marigold-1d4f28.netlify.app/gallery/metasploit/)
[nmap](https://github.com/P2019217/_gallery/blob/f366aca509686a21f6af076a19cccadefc98d276/nmap.md) / [nmap Netlify](https://calm-marigold-1d4f28.netlify.app/gallery/nmap/)
[security-tools.md timeline](https://github.com/P2019217/site/blob/master/_timeline/security-tools.md) / [Timeline Netlify](https://calm-marigold-1d4f28.netlify.app//timeline/security-tools/)
[security-tools.md slides](https://github.com/P2019217/site/blob/master/_slides/security-tools.md) / [Slides Netlify](https://calm-marigold-1d4f28.netlify.app//slides/security-tools/) 

