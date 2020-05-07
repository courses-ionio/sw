# Μάθημα: Τεχνολογία Λογισμικού
* ### A.M.: Π2015009

* ### Ονοματεπώνυμο: Τιμόθεος Αυγερινός

## Προαπαιτούμενα 
#### Έγινε αλλαγή στο .bashrc με τις παρακάτω εντολές ώστε να δείχνει τον αριθμό μητρώου
       vim .bashrc
       export PS1='Π2015139:\w$ '
       source .bashrc
#### Για όλες τις ασκήσεις χρησιμοποιήθηκε το εργαλείο  **asciinema**
 - Για την εγκατάσταση του _asciinema_ 
       
       sudo apt-add-repository ppa:zanchey/asciinema

       sudo apt-get update
       
       sudo apt-get install asciinema

## 1. Use the terminal as an IDE
* ### Edit your files (e.g., cv, website, code, etc) in vim or emacs and compile it in a different panel or use a plug-in.

### Αντιμετόπιση Προβλήματος 
####  1. Για την επήλυση του προβλήματος χρησιμοποιήθηκε το εργαλείο **Vim**(text editor)
   - Για την εγκατάσταση του **Vim** εκτελέστηκε η εντολή :
   
             sudo apt install vim
             
#### 2. Φτιάχτηκε ένα βιογραφικό σημείωμα με την βοήθεια του https://latexresu.me/
#### 3. Εγκαταστήθηκε το εργαλείο _Tex_ _Live_ και η επέκταση του _Xe_ _Tex_
         
         sudo apt-get install texlive-xetex
         
#### 4. Πέγαμε στο φάκελο _resume_   
         cd resume 
#### 5. Επεξεργασία του αρχείου _resume.tex_
         vim resume.tex
#### 6. Αποθήκευση των αλλαγών και δημιουργία αρχείου _resume.pdf_ 
         xelatex resume.tex
#### Το video με όλη τη διαδικασία βρήσκεται εδω : https://asciinema.org/a/327709

## 2. Τry different terminals and shells
nfiguration that fits your needs

#### 1. Για την άσκηση χρησιμοποιήθηκε το _fish shell_
  - Για την εγκατάσταση του **fish** εκτελέστηκαν οι εντολές :
  
         sudo apt-add-repository ppa:fish-shell/release-3
         sudo apt-get update
         sudo apt-get install fish
         
#### 2. Εκτελέστικαν οι εντολές μέσα στο _fish_ :
         pwd 
         
         ll
         
         cd 
         
         for i in 1 2 3; echo $i; end
         
         math 2+2
         
         random 
         
 - Για την έξοδο απο το _fish_ χρησιμοποιήθικε η εντολή
 
          exit
          
          
 #### Το video με όλη τη διαδικασία βρήσκεται εδω : https://asciinema.org/a/327717
## 3. Send notifications to your desktop-mobile  
* ### Send a notifcation when a big task completes, eg download, compiling, etc 

#### 1. Για την αποστολή ειδοποίησης στο desktop χρησιμοποιήθηκε το εργαλείο ```ntfy```
-  Για την εγκατάσταση του ```ntfy``` χρησιμοποιήθηκε η εντολή :

            sudo pip install ntfy
            
- Για να εμφανιστεί ειδοποίηση στο desktop χρησιμοποιήθηκε η εντολή :
           
           ntfy -t 'ntfy' send "I am Timos"
           
           
           
  ![smartphone desktop](https://github.com/p15avge/sw/blob/2015009/projects/2015009/91521402_2589657554605073_3860983493806784512_n.png) 
    
#### 2. Για την αποστολή ειδοποίησης στο _smartphone_  χρησιμοποιήθηκε το εργαλείο Telegram        
 - Για την εγκατάσταση των πακέτων του _telegram_ χρησιμοποιήθηκε η εντολή :
 
             pip install ntfy[telegram]
 
- Εγκατάσταση της εφαρμογης _Telegram_ στο smartphone και μέσο αυτης δημιουργίθηκε ενα bot με όνομα Samsung2 

- Εισαγωγή του API αριθμού(token) του bot

- Αποστολή της ειδοποίησης με την εντολή 
    
            ntfy -b telegram send "hello"


![smartphone screenshot](https://github.com/p15avge/sw/blob/2015009/projects/2015009/91907340_240904060399225_4735137358632976384_n.jpg)


#### Το video με όλη τη διαδικασία βρήσκεται εδω :https://asciinema.org/a/PT14IIIVa37bZbqUpgGFpwtm1

