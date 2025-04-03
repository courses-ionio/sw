
# Τα Στοιχεία Μου
| Πλατφόρμα | Όνομα | Επώνυμο | Username | AM | Email |
| --- | --- | --- | --- | --- | --- |
| [Github](https://github.com/nkanagno) | Νικόλας | Αναγνωστόπουλος | nkanagno | inf2021013 | inf2021013@ionio.gr |

Όνομα ομάδας: OMADA 13 <br>
GitHub organisation url: [OMADA11](https://github.com/OMADA-13)

# Εισαγωγή Μαθήματος και Αρχική Στόχοι (Προχωρημένα Θέματα Τεχνολογίας Λογισμικού)
Μέσω του μαθήματος Προχωρημένα Θέματα Τεχνολογίας Λογισμικού, το οποίο δίνει βάση σε προχωρημένες διαδικασίες ανάπτυξης λογισμικού καθώς και σε εργαλεία που χρησιμοποιούνται σε αυτού του είδους διαδικασίες, ευελπιστώ να εξελίξω τον τρόπο σκέψης μου όσον αφορά την σχεδίαση και την ανάπτυξη λογισμικού μαθένοντας περισσότερα εργαλεία και τρόπους ανάπτυξης λογισμικού από αυτά/ους που ήδη γνωρίζω. 

Συγκεκριμένα, έχοντας εργαστεί ως software engineer τους περασμένους 7 μήνες με τεχνολογίες ανάπτυξης web εφαρμογών (όπως `React js, PostgreSQL και graphql`), έχω μάθει να μπορώ να αναλύω ένα πρόβλημα και να μπορώ να το μεταφέρω σε μορφή κώδικα προκειμένου να εξελίσσεται συνεχώς η κύρια web εφαρμογή της εταιρείας.

Παρότι της τρέχουσας εμπειρίας μου σε αυτόν τον τομέα, πιστεύω ότι πάντα υπάρχει χώρος για εξέλιξη και ότι μέσω των πολλαπλών και ξεχωριστών εργαλείων που θα αποκτήσω εμπειρία μέσω αυτού του μαθήματος, θα μπορέσω να εξελιχθώ περισσότερο και στην τρέχον δουλειά μου αλλά και για την μετέπειτα μελλοντική καριέρα μου ως software engineer.

# Alan kay chat - Απαλλακτική Εργασία

## Περίληψη
Κατά την διάρκεια του μαθήματος, πραγματοποιήθηκε η ανάπτυξη ενός AI chatbot που προσωποποιεί τον χαρακτήρα του Alan kay, έναν σπουδαίο και πρωτοπόρο επιστήμονα στον κόσμο της τεχνολογίας. Έχοντας στην διάθεση μου τις πιο πρόσφατες τεχνολογίες τεχνητής νοημοσύνης όπως εξελιγμένα εργαλεία της OpenAi, η υλοποίηση αυτού του project μπόρεσε και ήταν εφικτή. Σημαντικά εργαλεία της OpenAi αποτέλεσαν το API, embedding μοντέλα τεχνητής νοημοσύνης και μία vector database. Η ένωση των παραπάνω εργαλειών, έκαναν εφικτή την υλοποίηση της προχωρημένου επιπέδου τεχνικής που είναι υπεύθυνη για την όλη ανάπτυξη της συγκεκριμένης εφαρμογής, και ονομάζεται Retrieval Augmented Generation ή αλλιώς RAG. Η τεχνική αυτή επιτρέπει την ανάπτυξη εξελιγμένων ΑΙ chatbots τα οποία είναι εκπαιδευμένα και απαντούν ερωτήσεις χρηστών πάνω σε ειδικά δεδομένα που είναι αποθηκευμένα σε μορφή αρχείου κειμένου όπως PDF, txt, markdown κλπ. Σε αυτή την περίπτωση οι γνώσεις του Alan kay chatbot βασίζονται σε δεδομένα ερωτοαπαντήσεων του Alan Kay, που βρίσκονται στο κεντρικό profile του στο QUORA και η επεξεργάσια τους έγινε μέσω της γλώσσας προγραμματισμού, Python. Τέλος, το μεγαλύτερο μέρος της εφαρμογής έγινε μέσω Python με τις πιο σημαντικές βιβλιοθήκες να είναι η streamlit για το User Ιnterface, η pandas για την επεξεργασία των δεδομένων, η OpenAi για το RAG και την FastApi για να ακούει σε post requests να επιστρέφει την απάντηση του Alan Kay.

## Εισαγωγή



## Retrieval Augmented Generation (RAG)
Η τεχνική `RAG` περιλαμβάνει 3 στάδια (`Retrieval` -> `Augmented` -> `Generation`).

To πρώτο είναι το `Retrieval` που ο χρήστης κάνει μία ερώτηση και λαμβάνει τα πιο σχετικά κομμάτια κειμένου που είναι αποθηκευμένα στην vector database. Μετά το `Augmented` όπου δίνονται αυτά τα κομμάτια ως context μαζί με την αρχική ερώτηση του χρήστη στο AI όπου έχει λάβει και ορισμένες οδηγίες. Τέλος είναι τo `Generation` όπου με βάση το context που του έχει δωθεί ως βαση γνώσης, το AI απαντάει πάνω στην αρχική ερώτηση του χρήστη κανόντας generate την τελική απάντηση.

![rag](https://github.com/user-attachments/assets/d0f20bb1-e2df-4cf8-93ca-841f72eb0083)

### Δημιουργία vector database - προεπεξεργασία δεδομένων
Για να μπορέσει να εφαρμοστεί αυτή η τεχνική απαιτείται πρώτα η ανάπτυξη της vector database. Δηλαδή, το κείμενο κάθε αρχείου αρχικά χωρίζεται σε κομμάτια ορισμένου μεγέθους που ονομάζονται text chunks. Το κάθε κομμάτι μέσω ενός μοντέλου τεχνητής νοημοσύνης μετατρέπεται σε μια σειρά αριθμών ή αλλιώς αριθμητικών διανυσμάτων που ονομάζονται embeddings. Αυτά τα embeddings αποθηκεύονται στην vector database η οποία χρειάζεται για το retrieval στάδιο της τεχνικής RAG.

### Λεπτομερής περιγραφή σταδίων
Με βάση το θεωρητικό υπόβραθρο της τεχνικής αυτής, παρακάτω γίνεται μια πιο λεπτομερής περιγραφή των 3 σταδίων (`Retrieval` -> `Augmented` -> `Generation`):
- `Retrieval` : Σε αυτό το στάδιο ο χρήστης κάνει μία ερώτηση στο Ai. Αυτή η ερώτηση μετρέπεται μέσω ενός Word2vec μοντέλου με βάση πιθανοτήτων σε ένα διάνυσμα αριθμών. Έπειτα γίνεται μία συσχέτιση με το διάνυσμα αυτό με άλλα διανύσματα στο vector database που δημιουργήθηκε νωρίτερα. Το vector database μετά επιστρέφει τα text chunks τα οποία συσχετίζονται περισσότερο με την αρχική ερώτηση του χρήστη. 
- `Augmented` : Τα relevant chunks μορφοποιούνται με τέτοιο τρόπο ώστε να είναι ευανάγνωστα σε μορφή κειμένου ή παραγράφου και ορίζονται ως context. Αυτό το context μαζί και η αρχική ερώτηση του χρήστη, δίνονται σε ένα ai prompt με αρχικές οδηγίες ότι είναι ένα rag μοντέλο το οποία απαντάει ερωτήσεις με την χρήση μιας βάσης γνώσης ή αλλιώς το context. 
- `Generation` : Στο τελικό στάδιο αυτής της τεχνικής, έχοντας λάβει της κατάλληλες οδηγίες με σαφής αρχική ερώτηση και ακριβές context, κάνει generate την τελική απάντηση και επιστρέφεται πίσω στον χρήστη.

## Ανάπτυξη Εφαρμογής
### Ανάκτηση δεδομένων
Τα δεδομένα της εφαρμογής βασίζονται πάνω σε όλες τις ερωτοαπαντήσεις του alan kay που βρίσκονται στο κεντρικό του [profile στο Quora](https://www.quora.com/profile/Alan-Kay-11). Η ανάκτηση τους χρειάστηκε να γίνει χειροκίνητα καθώς παρουσιάστηκαν αρκέτες δυσκολίες με διάφορα εργαλεία web scraping που δοκιμάστηκαν. Ωστόσο, παρότι τα προβλήματα αυτά, τα δεδομένα αποθηκεύτηκαν σε ένα csv αρχείο της μορφής:


| | questions | answers | 
|----------|----------|----------|
|1| Computer scientist Edsger W. Dijkstra said tha...	  | I’ll start by saying that I don’t clearly unde... |
|2|Was one byte ever less than eight bits in the ...	  | When I started “programming as a job” in the U... |
|...|...|...|
|690 | Who was specifically responsible for the inven... | Mr Rao has a good slant on this, in particular...|
|691 | Why isn't Alan Kay's FoNC (Fundamentals of New... | I can't answer the question directly, but I ca...|

(691 rows × 2 columns)

Όπου οποιοσδήποτε χρήστης στο github έχει πρόσβαση στο συγκεκριμένο αρχείο csv καθώς είναι ανεβασμένο σε δήμοσιο αποθετήριο [quora_q&a_alan_kay.csv](https://github.com/nkanagno/alan-kay-chatbot/blob/main/data/quora_q%26a_alan_kay.csv).

### Προεπεξεργασία δεδομένων
Λόγο το ότι η τεχνική RAG εφαρμόζεται πιο αποδοτικά σε αρχεία κειμένου χρειάστηκε να μεταφερθούν αυτές οι ερωτοαπαντήσεις σε ένα αρχείο txt. Η διαδικασία αυτή πραγματοποιήθηκε μέσω python με τον παρακάτω κώδικα:
```
with open("./data/alan_kay_knowledge/quora_q&a_alan_kay.txt", "w") as f:
    for index,row in df.iterrows():
        f.write(f"Interview's Question: { row['questions']}\n")
        f.write(f"Alan's kay Answer: {row['answers']}\n\n\n")
```
όπου για κάθε γραμμή του πίνακα γράφετε σε ένα αρχείο κειμένου txt, σε αυτή την μορφή:

```
Interview's Question: Is programming learned inductively or deductively?
Alan's kay Answer:  "I don’t feel I completely understand this question (or perhaps don't understand the intention ...”"
```
ώστε να μπορεί να αναγνωρίζει το AI την ερώτηση που τέθηκε και ύστερα την απάντηση που δώθηκε από τον alan kay.

Παρομοίως με απο πάνω όλες οι χρήστες του github έχει πρόσβαση σε αυτό το αρχείο txt γιατί βρίσκεται σε δήμοσιο αποθετήριο [quora_q&a_alan_kay.txt](https://github.com/nkanagno/alan-kay-chatbot/blob/main/data/alan_kay_knowledge/quora_q%26a_alan_kay.txt).

### Δημιουργία Embeddings και vector database
Σε πρακτικό επίπεδο, όσον αφορά την δημιούργια των embeddings οι κύριες βιβλιοθήκες της python που χρησιμοποιήθηκαν είναι της openai και της chromadb. Η openai χρειάστηκε για την επαφή με τα μοντέλα τεχνιτής νοημοσύνης όπως το `gpt-3.5` για το text generation API και το `text-embedding-3-small` το οποίο φτιάχνει τα embeddings για την vector database. Η chromadb χρειάστηκε για την δημιουργία της vector database και την διαχείριση της embedding function της openai. Συγκεκριμένα, παρακάτω φαίνεται η αρχικοποίηση του api και της vector database:

```
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai_key, model_name="text-embedding-3-small",
)
chroma_client = chromadb.PersistentClient(path="./data/chroma_persistent_storage")
collection_name = "document_qa_collection"
collection = chroma_client.get_or_create_collection(
    name=collection_name,embedding_function=openai_ef
)
client = OpenAI(api_key=openai_key)
```

Στο επόμενο στάδιο έγινε η ανάπτυξη 4ων συναρτήσεων:

 - Η πρώτη είναι η `load_documents_from_directory()` όπου λαμβάνει ως παράμετρο ένα directory path και διαβάζει τα ονόματα όλων των txt αρχείων που είναι μέσα. Τα αρχεία αυτά αποθηκεύονται και επιστρέφονται σε μία object list που ονομάζεται documents όπου για κάθε document (txt αρχείο) δημιουργείται ένα αντικείμενο που δέχεται το όνομα του αρχείου και το εσωτερικό του κείμενο. 
    ```
    def load_documents_from_directory(directory_path):
        # print("==== Loading documents from directory ====")
        documents = []
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt"):
                with open(os.path.join(directory_path,filename), "r", encoding="utf-8") as file:
                    documents.append({"id": filename, "text": file.read()})
        return documents
    ```

 - Η δεύτερη είναι η `split_text()`. Ως παραμέτρους εισόδου δέχεται μία μεταβλητή text, το μέγεθος των chunks στο οποίο θα γίνει ο διαχωρισμός, και το chunk_overlap το οποίο παίρνει και ένα μέρος από το προηγούμενο chunk. Ουσιαστικά χωρίζει το text ανά χίλιους χαρακτήρες προσθέτωντας επιπλέον και τους 20 προηγούμενους χαρακτήρες για να μην χαθεί κάποια σημαντική πληροφορία. Επιστρέφοντας τα chunks του στο τέλος.
    ```
    def split_text(text,chunk_size=1000,chunk_overlap=20):
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start = end - chunk_overlap
        return chunks
    ```

- H συνάρτηση `get_openai_embedding()` παίρνει ένα κείμενο και μέσω της embedding function της openai που ορίστηκε πιο πάνω το μετατρέπει σε ένα δίανυσμα αριθμητικό με την χρήση του μοντέλου `text-embedding-3-small`.
    ```
      def get_openai_embedding(text):
        response = client.embeddings.create(input=text, model="text-embedding-3-small")
        embedding = response.data[0].embedding
        print("==== Generating embeddings... ====")
        return embedding
    ```

- H τέταρτη συνάρτηση και η πιο σημαντική είναι η `split_text_and_generate_embeddings()`. Με λίγα λόγια φορτώνει όλα τα αρχεία txt που βρίσκονται στο path `./data/alan_kay_knowledge/`, σε αυτή την περίπτωση υπάρχει μόνο ένα το `quora_q&a_alan_kay.txt`. Στη συνέχεια, το διαχωρίζει σε chunks και τα τοποθετεί σε μία object λίστα για μετέπειτα χρήση. Μετά το κάθε chunk το μετατρέπει σε embedding και τέλος το εισάγει στην vector database.
    ```
    def split_text_and_generate_embeddings():
        directory_path = "./data/alan_kay_knowledge/"
        documents = load_documents_from_directory(directory_path)
        print(f"loaded {len(documents)} files")
    
        chunked_documents = []
        for doc in documents:
            chunks = split_text(doc['text'])
            # print(f"== Splitting docs into chunks ==")
            for i, chunk in enumerate(chunks):
                chunked_documents.append({"id": f"{doc['id']}_chunk{i+1}", "text": chunk})
                
        print(len(chunked_documents))
    
        for doc in chunked_documents:
            print("==== Generating embeddings... ====")
            doc["embedding"] = get_openai_embedding(doc["text"])
        
    
        for doc in chunked_documents:
            print("==== inserting chunks into db;; ====")
            collection.upsert(ids=[doc["id"]], documents=[doc["text"]],embeddings=[doc['embedding']])
    ```
όλες οι παραπάνω συναρτήσεις βρίσκονται μέσα στο αρχείο [`process_data.ipynb`](https://github.com/nkanagno/alan-kay-chatbot/blob/main/process_data.ipynb). 



