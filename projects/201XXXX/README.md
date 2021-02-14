## ΤΕΧΝΟΛΟΓΙΑ ΛΟΓΙΣΜΙΚΟΥ
### Αντρέας Παππούτας
### Α.Μ.: Π2017148
### [Τελική Αναφορά](https://github.com/andreaspappoutas/sw-FINAL_REPORT)

## Παραδοτέο 1:
try different terminals and shells - repeat some of the previous exercises with a different terminal-shell and create a custom configuration that fits your needs

#### Για να γίνει αυτή η εργασία έκανα χρήση των τερμιναλ guake, konsole, Tilda, Terminology, fish και zsh

```
 sudo apt-get -f install guake

 sudo apt-get -f install konsole

 sudo apt-get -f install tilda

 sudo apt-get -f install yakuake

 sudo apt-get -f install terminology

 sudo apt-add-repository ppa:fish-shell/release-3
 sudo apt-get update
 sudo apt-get install fish

 sudo apt-get install zsh
```
#### Στο κάθε τερμιναλ έφτιαξα ένα αρχείο και το τροποποίησα έτσι ώστε να φανούν οι διαφορές μεταξύ τους.

### GUAKE

#### guake: Το guake είναι ένα drop-down τερμιναλ που για να το ανοίξει ο χρήστης πατάει το f12

### Asciinema : [guake](https://asciinema.org/a/336895)

### Screenshot

![guake2](https://user-images.githubusercontent.com/44147982/83910858-edbebf00-a773-11ea-9274-e330d94bc3b2.gif)


### Konsole

#### Konsole: Το konsole είναι ένα τερμιναλ το οποίο είναι ενσωματωμένο σε πολλές άλλες εφαρμογές κάνοντας το αρκετά χρήσιμο 

### Asciinema : [Konsole](https://asciinema.org/a/336896)

### Screenshot

![konsole](https://user-images.githubusercontent.com/44147982/83910843-e8617480-a773-11ea-84ef-62ae3cf97d7b.gif)

### TILDA

#### tilda: Το tilda είναι ένα τερμιναλ που μπορεί εύκολα να ρυθμιστή από το χρήστη έτσι ώστε να έχει hotkeys για όπια λειτουργία χρειάζεται(π.χ να αλλάζει τοποθεσία το τερμιναλ)

### Asciinema : [tilda](https://asciinema.org/a/336897)

### Screenshot
![tilda](https://user-images.githubusercontent.com/44147982/83910772-cf58c380-a773-11ea-9712-21aa0d01e432.gif)


### TERMINOLOGY

#### terminology: Το terminology είναι ένα εύκολα διαμορφούμενο τερμιναλ το οποίο κατανοεί πλήρεις διαδρομές αρχείων, συνδέσεις URL και εμαιλ. Επιπλέον έχει progress bar για τις λήψης αρχείων

### Asciinema : [terminology](https://asciinema.org/a/336903)
### Screenshot.
![terminology3](https://user-images.githubusercontent.com/44147982/83910805-dc75b280-a773-11ea-847b-5ae7b55217e6.gif)


### YAKUAKE


#### yakuake: Το yakuake είναι ένα drop-down τερμιναλ που μπορεί να είναι στο πάνω ή κάτω μέρος της οθόνης.

### Asciinema : [yakuake](https://asciinema.org/a/336904)
### Εικόνα του τέρμιναλ "yakuake".
![yakuake](https://user-images.githubusercontent.com/44147982/83910768-cd8f0000-a773-11ea-8e42-1e8276888ebe.gif)



### FISH

#### fish shell: Το fish είναι ένα γρήγορο τερμιναλ με πολλές λειτουργίες.

### Asciinema : [fish](https://asciinema.org/a/336906)
### Screenshot.
![fish](https://user-images.githubusercontent.com/44147982/83910872-f44d3680-a773-11ea-9b8a-fb1941a0a24f.gif)


### ZSH

#### zsh: Το zsh είναι ένα τερμιναλ με με χιλιάδες χρήσιμες λειτουργίες, βοηθούς και plugins

### Asciinema : [zsh](https://asciinema.org/a/336907)
### Screenshot.
![zsh](https://user-images.githubusercontent.com/44147982/83910766-ca940f80-a773-11ea-9a24-84a0f8cb8ed4.gif)



---



## Παραδοτέο 2
create a docker image for your development stack - demonstrate the custom image for CI of your cv and site

#### Για αυτό το παραδοτέο έκανα χρήση του Nginx και Alpine.

#### Αρχικά δημιούργησα και τροποποίησα το Dockerfile. Έκανα copy όλα τα αρχεία από το directory μου στο server του Nginx

```
FROM nginx:alpine                                                               
COPY index.html /usr/share/nginx/html
```

#### Ακολούθως δημιούργησα το docker image με το html server

```
sudo docker build -t html-server-image:v1 .
```

#### Για να ελέγξω αν φτιάχτηκαν τα images του alpine και nginx γραφω τη εντολη
```
sudo docker images
```

#### Μέτα τρέχω τη εικόνα που έχω φτιάξει σε port 80 για να ενφανιστη στο locahost
```
sudo docker run -d -p 80:80 html-server-image:v1
```



### Ιστοσελίδα:


![localhost](https://user-images.githubusercontent.com/44147982/77859623-1a55d800-7213-11ea-9830-6937af4649b9.png)

### Asciinema : [Nginx-Alpine](https://asciinema.org/a/336890)


---



## Παραδοτέο 3

set-up cloud services - ssh to a remote machine and demonstrate your remote cli user land (e.g., email, editor, cv, code, etc)

#### Χρησημοποιησα το openSSH για αυτο το παραδοτέο
```
sudo apt-get install openssh-server
```

#### Μετα συνδεθικα με το raspberry pi το οποιο έχει ετοιμο το ssh και απλα γινετε enable
#### Τέλος, για την σύνδεση δύο συστημάτων και επεξεργασία κώδικα χρησιμοποίησα την παρακάτω εντολή:
```
ssh pi@ip_address
nano kodikas.py
```

### Screenshots
![shh1](https://user-images.githubusercontent.com/44147982/77859749-cc8d9f80-7213-11ea-8c30-bbbff5cf8e56.png)
![ssh2](https://user-images.githubusercontent.com/44147982/77859751-ceeff980-7213-11ea-9b32-0c00db6f7a15.png)
![ssh3](https://user-images.githubusercontent.com/44147982/77859753-d0212680-7213-11ea-9d92-606b6e3a6841.png)




### Asciinema : [SSH](https://asciinema.org/a/336911)




---



## Παραδοτέο 4
send notifications to your desktop-mobile - send a notifcation when a big task completes, eg download, compiling, etc

#### Για τη εργασία αυτή χρησιμοποίησα το ntfy.
#### Με το ntfy μπορείς να σου έρχονται ειδοποιήσεις στο υπολογιστή σου όταν τελείωση μια διαδικασία μέσα στο τερμιναλ. Επίσης μπορείς να αλλάξεις αρκετές λειτουργίες του μέσο επεξεργασίας του config

```
sudo pip install ntfy
```
#### Στη συνέχεια έκανα επεξεργασία το αρχείο .bashrc και έβαλα στο τέλος τη παρακάτω εντολή έτσι ώστε να έρχονται ειδοποίησης για οτιδήποτε γίνετε

```
eval "$(ntfy shell-integration)"
```
#### Μπορείς να στείλεις μια ειδοποίηση μέσο

```
ntfy send "notification"
```

#### Ακολούθως επέλεξα ένα αρχείο mp3 και στο τέλος μου ήρθε notification

```
ffplay sound.mp3
```



![ntfy3](https://user-images.githubusercontent.com/44147982/83910828-e39cc080-a773-11ea-9a8f-3a9221631c1d.gif)



### Asciinema : [ntfy](https://asciinema.org/a/336910)



---



## Παραδοτέο 5
performance monitoring - monitor the performance of your python scripts and visualize them with colors and/or spark lines

#### Αρχικά έκανα εγκατάσταση το hyperfine

```
wget https://github.com/sharkdp/hyperfine/releases/download/v1.9.0/hyperfine_1.9.0_amd64.deb
sudo dpkg -i hyperfine_1.9.0_amd64.deb
```

#### Με το hyperfine μπόρεσα να ελέγξω το χρόνο εκτέλεσης 2 προγραμμάτων python. Επιπλέον έβαλα warmup και πόσες φόρες να τρέξουν τα προγράμματα.

```
hyperfine 'python3 file1.py' 'python3 file2.py' --warmup 40 --min-runs 40

```


#### Επίσης με το πρόγραμμα έκανα export πληροφορίες σε μορφή json αρχείου.

```
hyperfine --export-json output 'python3 file1.py' 'python3 file2.py' 
--warmup 40  
```

### JSON:
![json results](https://user-images.githubusercontent.com/44147982/77860133-1c6d6600-7216-11ea-961f-fec20de52155.png)


### Asciinema : [hyperfine](https://asciinema.org/a/336892)


---


## Παραδοτέο 6:

set-up continuous integration - build and deploy your static site and your cv dynamically every time you make a small change in the source files

### Για αυτό το παραδοτέο έκανα χρήση του github μαζί με το travis ci. Αρχικά έφτιαξα ένα νέο repository με το CV μου και το έκανα publish μέσο του github pages. Στη συνέχεια έκανα εγγραφή στο travis ci μέσο του github και το έκανα install στο repository του CV. Μετά έφτιαξα το .travis.yml αρχείο έτσι ώστε με οποιαδήποτε αλλαγή να γίνετε build και deploy η ιστοσελίδα. Μέσα στο .travis.yml έπρεπε να βάλω ένα νέο GITHUB_TOKEN το οποίο δημιούργησα με public repo δικαιώματα και ενώθηκε εφόσον το έβαλα και στο travis ci settings. Μέσα στο asciinema κάνω μια αλλαγή μέσο του git και μόλις κάνω push η σελίδα γίνετε αυτόματα build.

### Πρώτα έκανα clone του repository και config το git.
```
git clone https://github.com/andreaspappoutas/mycv
git config --global user.name "FIRST_NAME LAST_NAME"
git config --global user.email "MY_NAME@email.com"
```

### Ακολούθως έγινε χρήση των παρακάτω εντολών για να τροποποιήσω το αρχείο.
```
cd mycv
ls
nano index.html
```

### Τέλος έκανα commit και push ολα τα αρχεία που άλλαξα μαζί με μήνυμα Autobuild.
```
git commit -a -m AutoBuild 
git push
```

![AutoBuildedTravis](https://user-images.githubusercontent.com/44147982/83910884-f7e0bd80-a773-11ea-80d6-9e53d794a6e3.png)


### Asciinema : [Travis Ci](https://asciinema.org/a/336891)

---

## Παραδοτέο 7:

set-up a system for python development - install and configure in a user folder a python project that is not available through the package manager

### Για αυτή τη εργασία έκανα χρήση του pipenv και virtualenv.
```
pip install --user pipenv
pip install virtualenv
```

### Έφτιαξα ένα νέο φάκελο μέσα στο οποίο δημιούργησα ένα νέο enviroment.
```
mkdir MyProject
cd MyProject
virtualenv Enviroment
```

### Στη συνέχεια ενεργοποίησα το enviroment αυτό και έδειξα ότι δεν ήτανε ίδιο με το κανονικό που υπήρχε ήδη στο ubuntu εφόσον δεν υπάρχουν βιβλιοθήκες εγκατεστημένες σε αυτό.
```
source Enviroment/bin/activate
which python
which pip
```

### Ακόλουθος έκανα εγκατάσταση της νέας βιβλιοθήκης math μέσο του pipenv και δημιούργησα ένα νέο πρόγραμμα που τη χρησιμοποιούσε αυτή.
```
pipenv install math
touch program.py
nano program.py
from math import exp
print(exp(6))
```

### Τέλος έτρεξα το νέο μου πρόγραμμά και εφόσον δεν έβγαλε πρόβλημα τότε το virtual enviroment λειτουργεί κανονικά.
```
pipenv run python main.py
```

### Απενεργοποίηση του virtual enviroment.
```
deactivate
```


### Asciinema : [Python Virtual Enviroment](https://asciinema.org/a/336893)

---


## Παραδοτέο 8:
use the terminal as an IDE - edit your files (e.g., cv, website, code, etc) in vim or emacs and compile it in a different panel or use a plug-in

### Για αυτή τη εργασία έκανα εγκατάσταση το SpaceVim και το Neovim.
```
curl -sLf https://spacevim.org/install.sh | bash
sudo apt-get install neovim
```

### Το spacevim ενώνεται μαζί με το neovim και όταν τρέξεις για πρώτη φορά το Neovim τα plugins από το SpaceVim γίνονται αυτόματα εγκατάσταση.
### Αρχικά όταν ξεκίνησα το NeoVim δημιούργησα ένα νέο αρχείο με το keybind "e". Έγραψα μέσα ένα απλό κωδικά της python για να φανεί το plugin αυτό , το έκανα αποθήκευση και έκλεισα το NeoVim.
```
:save
:exit
```

### Μπορείς να αλλάξεις το config μέσο αλλαγής του αρχείου "init.toml." μέσα στο SpaceVim ή για το NeoVim ":help vimrc"

#### Documentation του Neovim:
https://neovim.io/doc/user/



### Asciinema : [Spacevim-Noevim](https://asciinema.org/a/336894)


---


### Συμμετοχικό Εκπαιδευτικό Υλικό.

### mibook : [mibook](https://andreaspappoutas.netlify.com)

### Αποθετήριο mibook: [link](https://github.com/andreaspappoutas/gr)
### A.

Η πρώτη είκονα που ανέβασα είναι του iPad.

### [iPad](https://andreaspappoutas.netlify.com/gallery/ipad/)

H δεύτερη εικόνα είναι του Arduino Nano.

### [Arduino Nano](https://andreaspappoutas.netlify.com/gallery/arduino-nano/)


### B.

Στο Β έβαλα ενα διαδραστικό παράδειγμα του MKR1000 dashboard του arduino από το codepen. Είναι ένα παράδειγμα όπου ο χρήστης μπόρει να αλλάξει τις τιμές μέσα στο κώδικα του codepen και να προσέξει πως λειτουργά ενα dashboard του arduino.

### [Arduino Example](https://andreaspappoutas.netlify.app/remix/arduino-example/)
### [Αποθετήριο](https://github.com/andreaspappoutas/gr/blob/master/_remix/arduino-example.md)

### Γ.

Μελέτη περίπτωσης Arduino

### [Arduino Case Study](https://andreaspappoutas.netlify.app/case-study/arduinonew/)
### [Αποθετήριο](https://github.com/andreaspappoutas/gr/blob/master/_case-study/arduinoNew.md)



