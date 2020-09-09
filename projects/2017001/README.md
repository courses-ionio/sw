# Τεχνολογία Λογισμικού
**Όνομα:** Αλεξάνδρα  
**Επώνυμο:** Παραμύθα  
**ΑΜ:** Π2017001  
**Προσωπικό Αποθετήριο:** https://github.com/lextale/sw/tree/2017001/projects/2017001  

___

## Εργασία 1: try different terminals and shells
**references:** zsh  
**deliverables:** repeat some of the previous exercises with a different terminal-shell and create a custom configuration that fits your needs  
**asciinema:** https://asciinema.org/a/7Vc9CCpHoDG56NLKevLTwD53D  
**asciinema file in repo:** https://github.com/lextale/sw/blob/2017001/projects/2017001/zsh/zsh.cast  


#### Περιγραφή
Εγκατέστησα το zsh shell με την εντολή:
```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
Στη συνέχεια "πειράζοντας το .zshrc αρχείο που βρίσκονται τα configurations του shell άλλαξα το θέμα, ώστε κάθε φορά που κάνει launch να επιλέγεται ένα τυχαίο θέμα.
```
<span style="background-color:lightblue;border: 1px lightblue;border-radius: 25px;padding:10px;"><code>nano /home/p2017001/.zshrc</code></span>
```
Τέλος, δοκίμασα να ανοίξω διάφορα shells και να τρέξω κάποια εντολή σε ένα από αυτά. 


<p  align="center">
    <em>Asciinema: zsh</em>
  <a href="https://asciinema.org/a/7Vc9CCpHoDG56NLKevLTwD53D?autoplay=1"><img src="https://asciinema.org/a/7Vc9CCpHoDG56NLKevLTwD53D.png" height="500" width="500"/></a>
  <br>
</p>

___
## Εργασία 2: use the terminal as an IDE
**references:** https://www.latex-project.org/  
**deliverables**: edit your files (e.g., cv, website, code, etc) in vim or emacs and compile it in a different panel or use a plug-in  
**asciinema:** https://asciinema.org/a/nbqWuP9mjPOrNq9FLMyHJW76B  
**asciinema file in repo: https://github.com/lextale/sw/blob/2017001/projects/2017001/LaTex/latex.cast  

#### Περιγραφή
Άνοιξα ένα tex αρχείο στο texstudio και το επεξεργάστηκα
```
texstudio sampletex.tex
```
<p align="center">
  <img src="https://github.com/lextale/sw/blob/2017001/projects/2017001/LaTex/latex.gif" height="500 width="550>
</p>

Το έκανα compile σε μορφή pdf με την εντολή:
```
pdftex sampletex.tex
```
<p align="center">
  <img src="https://github.com/lextale/sw/blob/2017001/projects/2017001/LaTex/pdftex.gif" height="500 width="550>
</p>
__
