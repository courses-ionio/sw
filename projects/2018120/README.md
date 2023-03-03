Ονοματεπόνυμο: ΓΙΩΡΓΟΣ ΜΠΑΣΙΑΡΗΣ

Αριθμός Μητρώου: Π2018120

Github link: https://github.com/paranaloma

Οργανισμός: is_init_right?


# Τεχνολογία Λογισμικού


| Εβδομάδα | [Όλα τα παραδοτέα βρίσκονται στην ίδια σελίδα της τελικής αναφοράς](https://epidrome.github.io/teaching/deliverables/) με τα προσωπικά στοιχεία σας (Όνομα, ΑΜ, github profile) και μαζί με αυτόν εδώ τον πίνακα περιεχομένων | Σύνδεσμος στην [εβδομαδιαία παρουσίαση προόδου στις συζητήσεις](https://github.com/courses-ionio/help/discussions/categories/show-and-tell) | Αυτοαξιολόγηση σύμφωνα με τα κριτήρια της αντίστοιχης άσκησης |
| --- | --- | --- | --- |
| 1 | [Δημιουργία ομάδας](https://epidrome.github.io/teaching/team/) + [Φορκ και δημιουργία σελίδας τελικής αναφοράς](https://epidrome.github.io/teaching/guide/), [προσθήκη πίνακα περιεχομένων](https://raw.githubusercontent.com/courses-ionio/sw/master/README.md), [συγγραφή της εισαγωγής](https://epidrome.github.io/teaching/intro/), αποστολή της εισαγωγής [για σχολιασμό στην συζήτηση](https://github.com/courses-ionio/sw/discussions/categories/show-and-tell) και καταγραφή του συνδέσμου συζήτησης δίπλα --> |https://github.com/courses-ionio/sw/discussions/1190 | |
| 2 | [Γραμμή εντολών](https://epidrome.github.io/teaching/cli) (systemd) και [διαδικασία συνεργασίας με pull request στον οργανισμό της ομάδας σας](https://epidrome.github.io/teaching/team) |https://github.com/courses-ionio/sw/discussions/1312 | |
| 3 | Γραμμή εντολών (no systemd) |https://github.com/courses-ionio/sw/discussions/1318 |  |
| 4 | Κατασκευή του βιβλίου Α2 (συνεργατικά) | | |
| 5 | Συμμετοχικό περιεχόμενο A1 + A2 | | |
| 6 | Γραμμή εντολών (no systemd, custom static blog generator) | | |
| 7 | συμμετοχικό περιεχόμενο B1 | | |
| 8 | Κατασκευή του βιβλίου Β2 (συνεργατικά) | | |
| 9 | συμμετοχικό περιεχόμενο B2 | | |
| 10 | Τελική αναφορά* | | |

# Εισαγωγή
Το μάθημα τεχνολογία λογισμικού πιστεύω ότι θα με βοηθήσει στην κατανόηση του τρόπου λειτουργίας των λειτουργικών συστημάτων, όπως το τι είναι το systemd και το πως εποπτέυει τις υπόλοιπες διεργασίες σαν daemon καθώς και εναλλακτικές του. Επιπλέον θεωρώ ότι τα εβδομαδιαία βίντεο κουίζ θα με βοηθήσουν στο να καταλάβω τους προβληματισμούς και την ιστορία της ανάπτυξης λογισμικού από μεγάλους επιστήμονες της Πληροφοριής. Πιστεύω πώς το συνεργατικό κομματί του μαθήματος θα με βοηθήσει στο να μάθω να συνεργάζομαι με τους υπόλοιπους συμφοιτητές μου και να μάθουμε μαζί. Τέλος η γραμμή εντολών θα με βοηθήσει στο να μάθω να έχω πλήρη ελευθερία πάνω στον τρόπο λειτουργίας του συστήματος μιας και η γραμμή εντολών σου δίνει μια ελευθερία που η κλασική διάδραση όχι.

# Άσκηση γραμμής εντολών
Δημιουργήθηκε ένα αρχείο checkweather.sh που κάθε φορά που εκτελείται μου στέλνει τον καιρό στο Telegram χρησιμοποιώντας το curl στο wttr.in.
Για να πραγματοποιηθεί με επιτυχία πρέπει να υπάρχει εγκατεστημένα τα python, python-pip, ntfy, ntfy[telegram], curl.
```sh
#!/bin/bash

# City name for Corfu, Greece
CITY_NAME="Corfu,Kerkyra,Greece"

# URL to get the weather data for Corfu
URL="https://wttr.in/${CITY_NAME}?format=%C:%t,%f"

# Get the weather data using curl
WEATHER=$(curl -s "${URL}")

# Send notification using ntfy
ntfy -b telegram send "${WEATHER}"
```



![prntscrn](https://user-images.githubusercontent.com/56626790/222225366-c0520312-975d-4ca2-84a2-a6de39c11a9e.png)

[Show and Tell](https://github.com/courses-ionio/sw/discussions/1312)

# Άσκηση γραμμής εντολών
Δημιουργήθηκε ένα αρχείο [autobench.sh](https://github.com/paranaloma/shellscripting/commit/795389ee6f346f24caac16ca4acc49224da017e5),απαρτίζεται από ένα Menu με τρεις διαφορετικές επιλογές το οποίο κάνει 3 διαφορετικά benchmark και αποθηκεύει τα αποτελέσματα σε ανάλογο αρχείο (π.χ για το standard_benchmark -> standard_benchmark_results.json)

[![asciicast](https://asciinema.org/a/c4uxlSI9m7ZmDYWX0HWQ5Yzc9.svg)](https://asciinema.org/a/c4uxlSI9m7ZmDYWX0HWQ5Yzc9)

```bash
#!/bin/bash

# Function to print the menu
print_menu() {
    echo "Choose an option:"
    echo "1. Simple Program Comparison"
    echo "2. Standard Benchmark Test"
    echo "3. Extreme Benchmark Test"
    echo "4. Exit"
}

# Function to perform simple program comparison
simple_program_comparison() {
    read -p "Enter the first program command: " program1
    read -p "Enter the second program command: " program2

    echo "Running $program1..."
    py-spy record --nonblocking -- $program1 &>/dev/null &
    PID1=$!
    sleep 1

    echo "Running $program2..."
    py-spy record --nonblocking -- $program2 &>/dev/null &
    PID2=$!
    sleep 1

    echo "Comparing $program1 vs $program2..."
    hyperfine --warmup 3 "$program1" "$program2" --export-json comparison_results.json

    echo "Killing Py-Spy processes..."
    kill $PID1 $PID2 &>/dev/null
}

# Function to perform standard benchmark test
standard_benchmark_test() {
    read -p "Enter the program command: " program

    echo "Running benchmark for $program..."
    hyperfine --warmup 3 "$program" --export-json standard_benchmark_results.json
}

# Function to perform extreme benchmark test
extreme_benchmark_test() {
    read -p "Enter the program command: " program

    echo "Running extreme benchmark for $program..."
    hyperfine --warmup 10 --runs 50 "$program" --export-json extreme_benchmark_results.json
}

# Main loop
while true; do
    print_menu
    read -p "Enter your choice: " choice

    case $choice in
        1)
            simple_program_comparison
            ;;
        2)
            standard_benchmark_test
            ;;
        3)
            extreme_benchmark_test
            ;;
        4)
            exit 0
            ;;
        *)
            echo "Invalid choice!"
            ;;
    esac

    echo ""
done
```


