> [!WARNING]
> Η δειγματοληψία δεν συνιστάται πλέον στο MCP `2026-07-28`. Αυτό το μάθημα διατηρείται για
> υλοποιήσεις κληρονομιάς. Οι νέοι διακομιστές θα πρέπει να ενσωματώνονται απευθείας με ένα API
> παρόχου LLM.

# Δειγματοληψία στο Πρωτόκολλο Πλαισίου Μοντέλου

> Η δειγματοληψία παραμένει στην προδιαγραφή `2026-07-28` για συμβατότητα και είναι
> επιλέξιμη για αφαίρεση στην πρώτη αναθεώρηση που θα κυκλοφορήσει στις ή μετά τις 28 Ιουλίου,
> 2027. Παραδείγματα σε αυτό το μάθημα ενδέχεται να χρησιμοποιούν SDK APIs που υλοποιούν το `2025-11-25`.
> Δείτε [Τι Αλλάζει στο MCP: Η Προδιαγραφή 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

Στις υλοποιήσεις κληρονομιάς του MCP, η δειγματοληψία επιτρέπει στους διακομιστές να ζητούν
ολοκληρώσεις LLM μέσω του πελάτη. Αυτό το μάθημα εξηγεί αυτή την αποσυρθμένη ροή πρωτοκόλλου
για σκοπούς συμβατότητας και μετάβασης.

## Εισαγωγή

Σε αυτό το μάθημα, θα εξερευνήσουμε πώς να διαμορφώσουμε παραμέτρους δειγματοληψίας σε αιτήματα MCP και να κατανοήσουμε τους υποκείμενους μηχανισμούς πρωτοκόλλου της δειγματοληψίας.

## Στόχοι Μάθησης

Στο τέλος αυτού του μαθήματος, θα μπορείτε να:

- Κατανοήσετε τις βασικές παραμέτρους δειγματοληψίας διαθέσιμες στο MCP.
- Διαμορφώσετε παραμέτρους δειγματοληψίας για διαφορετικές χρήσεις.
- Υλοποιήσετε οριστική δειγματοληψία για αναπαραγώγιμα αποτελέσματα.
- Προσαρμόζετε δυναμικά τις παραμέτρους δειγματοληψίας βάσει πλαισίου και προτιμήσεων χρήστη.
- Εφαρμόσετε στρατηγικές δειγματοληψίας για την ενίσχυση της απόδοσης μοντέλου σε διάφορα σενάρια.
- Κατανοήσετε πώς λειτουργεί η δειγματοληψία στη ροή πελάτη-διακομιστή του MCP.

## Πώς Λειτουργεί η Δειγματοληψία στο MCP

Η ροή δειγματοληψίας στο MCP ακολουθεί τα εξής βήματα:

1. Ο διακομιστής στέλνει ένα αίτημα `sampling/createMessage` στον πελάτη
2. Ο πελάτης εξετάζει το αίτημα και μπορεί να το τροποποιήσει
3. Ο πελάτης παίρνει δείγματα από ένα LLM
4. Ο πελάτης εξετάζει το αποτέλεσμα ολοκλήρωσης
5. Ο πελάτης επιστρέφει το αποτέλεσμα στο διακομιστή

Αυτός ο σχεδιασμός με ανθρώπινη συμμετοχή εξασφαλίζει ότι οι χρήστες διατηρούν τον έλεγχο πάνω σε ό,τι βλέπει και παράγει το LLM.

## Επισκόπηση Παραμέτρων Δειγματοληψίας

Το MCP ορίζει τις ακόλουθες παραμέτρους δειγματοληψίας που μπορούν να διαμορφωθούν στα αιτήματα πελάτη:

| Παράμετρος | Περιγραφή | Τυπικό Εύρος |
|-----------|-------------|---------------|
| `temperature` | Ελέγχει την τυχαιότητα στην επιλογή token | 0.0 - 1.0 |
| `maxTokens` | Μέγιστος αριθμός token για παραγωγή | Ακέραιος αριθμός |
| `stopSequences` | Προσαρμοσμένες ακολουθίες που σταματούν την παραγωγή όταν εμφανίζονται | Πίνακας συμβολοσειρών |
| `metadata` | Πρόσθετες παραμέτρους ειδικές του παρόχου | Αντικείμενο JSON |

Πολλοί πάροχοι LLM υποστηρίζουν επιπλέον παραμέτρους μέσω του πεδίου `metadata`, που μπορεί να περιλαμβάνουν:

| Κοινή Παράμετρος Επέκτασης | Περιγραφή | Τυπικό Εύρος |
|-----------|-------------|---------------|
| `top_p` | Δειγματοληψία πυρήνα - περιορίζει tokens στην κορυφαία σωρευτική πιθανότητα | 0.0 - 1.0 |
| `top_k` | Περιορίζει την επιλογή token στις κορυφαίες K επιλογές | 1 - 100 |
| `presence_penalty` | Επιβάλλει ποινή σε tokens ανάλογα με την παρουσία τους στο κείμενο μέχρι τώρα | -2.0 - 2.0 |
| `frequency_penalty` | Επιβάλλει ποινή σε tokens ανάλογα με τη συχνότητα τους στο κείμενο μέχρι τώρα | -2.0 - 2.0 |
| `seed` | Συγκεκριμένος τυχαίος σπόρος για αναπαραγώγιμα αποτελέσματα | Ακέραιος αριθμός |

## Παράδειγμα Μορφής Αιτήματος

Εδώ είναι ένα παράδειγμα αιτήματος δειγματοληψίας από πελάτη στο MCP:

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "thisServer",
    "maxTokens": 100,
    "temperature": 0.7
  }
}
```

## Μορφή Απόκρισης

Ο πελάτης επιστρέφει ένα αποτέλεσμα ολοκλήρωσης:

```json
{
  "model": "string",  // Name of the model used
  "stopReason": "endTurn" | "stopSequence" | "maxTokens" | "string",
  "role": "assistant",
  "content": {
    "type": "text",
    "text": "string"
  }
}
```

## Έλεγχοι Ανθρώπινης Εμπλοκής

Η δειγματοληψία στο MCP έχει σχεδιαστεί με επιτήρηση από ανθρώπους:

- **Για προτροπές**:
  - Οι πελάτες πρέπει να δείχνουν στους χρήστες την προτεινόμενη προτροπή
  - Οι χρήστες πρέπει να μπορούν να τροποποιούν ή να απορρίπτουν τις προτροπές
  - Οι συστημικές προτροπές μπορούν να φιλτράρονται ή να τροποποιούνται
  - Η συμπερίληψη πλαισίου ελέγχεται από τον πελάτη

- **Για ολοκληρώσεις**:
  - Οι πελάτες πρέπει να δείχνουν στους χρήστες το αποτέλεσμα ολοκλήρωσης
  - Οι χρήστες πρέπει να μπορούν να τροποποιούν ή να απορρίπτουν τις ολοκληρώσεις
  - Οι πελάτες μπορούν να φιλτράρουν ή να τροποποιούν τις ολοκληρώσεις
  - Οι χρήστες ελέγχουν ποιο μοντέλο χρησιμοποιείται

Με αυτές τις αρχές κατά νου, ας δούμε πώς να υλοποιήσουμε τη δειγματοληψία σε διάφορες γλώσσες προγραμματισμού, εστιάζοντας στις παραμέτρους που υποστηρίζονται ευρέως από παρόχους LLM.

## Ζητήματα Ασφαλείας

Όταν υλοποιείτε τη δειγματοληψία στο MCP, λάβετε υπόψη αυτές τις βέλτιστες πρακτικές ασφαλείας:

- **Ελέγξτε όλο το περιεχόμενο των μηνυμάτων** πριν το αποστείλετε στον πελάτη
- **Καθαρίστε ευαίσθητες πληροφορίες** από προτροπές και ολοκληρώσεις
- **Υλοποιήστε όρια ρυθμού** για την πρόληψη κατάχρησης
- **Παρακολουθείτε τη χρήση δειγματοληψίας** για ασυνήθιστα μοτίβα
- **Κρυπτογραφήστε τα δεδομένα κατά τη μετάδοση** χρησιμοποιώντας ασφαλή πρωτόκολλα
- **Διαχειριστείτε την ιδιωτικότητα των δεδομένων χρηστών** σύμφωνα με τους σχετικούς κανονισμούς
- **Ελέγξτε τα αιτήματα δειγματοληψίας** για συμμόρφωση και ασφάλεια
- **Ελέγξτε το κόστος** με κατάλληλα όρια
- **Υλοποιήστε χρονικά όρια** για τα αιτήματα δειγματοληψίας
- **Διαχειριστείτε τα σφάλματα μοντέλου με ευκολία** χρησιμοποιώντας κατάλληλα εναλλακτικά σχέδια

Οι παράμετροι δειγματοληψίας επιτρέπουν την λεπτομερή ρύθμιση της συμπεριφοράς των γλωσσικών μοντέλων για την επίτευξη της επιθυμητής ισορροπίας μεταξύ οριστικών και δημιουργικών αποτελεσμάτων.

Ας δούμε πώς να διαμορφώσουμε αυτές τις παραμέτρους σε διάφορες γλώσσες προγραμματισμού.

# [.NET](#tab-dotnet)

```csharp
// .NET Example: Configuring sampling parameters in MCP
public class SamplingExample
{
    public async Task RunWithSamplingAsync()
    {
        // Create MCP client with sampling configuration
        var client = new McpClient("https://mcp-server-url.com");
        
        // Create request with specific sampling parameters
        var request = new McpRequest
        {
            Prompt = "Generate creative ideas for a mobile app",
            SamplingParameters = new SamplingParameters
            {
                Temperature = 0.8f,     // Higher temperature for more creative outputs
                TopP = 0.95f,           // Nucleus sampling parameter
                TopK = 40,              // Limit token selection to top K options
                FrequencyPenalty = 0.5f, // Reduce repetition
                PresencePenalty = 0.2f   // Encourage diversity
            },
            AllowedTools = new[] { "ideaGenerator", "marketAnalyzer" }
        };
        
        // Send request using specific sampling configuration
        var response = await client.SendRequestAsync(request);
        
        // Output results
        Console.WriteLine($"Generated with Temperature={request.SamplingParameters.Temperature}:");
        Console.WriteLine(response.GeneratedText);
    }
}
```

Στον παραπάνω κώδικα έχουμε:

- Δημιουργήσει έναν πελάτη MCP με συγκεκριμένη διεύθυνση URL διακομιστή.
- Διαμορφώσει ένα αίτημα με παραμέτρους δειγματοληψίας όπως `temperature`, `top_p`, και `top_k`.
- Στείλει το αίτημα και εκτυπώσει το παραγόμενο κείμενο.
- Χρησιμοποιήσει:
    - `allowedTools` για να καθορίσουμε ποια εργαλεία μπορεί να χρησιμοποιήσει το μοντέλο κατά την παραγωγή. Σε αυτή την περίπτωση, επιτρέψαμε τα εργαλεία `ideaGenerator` και `marketAnalyzer` για βοήθεια στη δημιουργική παραγωγή ιδεών εφαρμογών.
    - `frequencyPenalty` και `presencePenalty` για να ελέγξουμε την επανάληψη και τη διαφορετικότητα στην έξοδο.
    - `temperature` για να ρυθμίσουμε την τυχαιότητα της εξόδου, όπου υψηλότερες τιμές οδηγούν σε πιο δημιουργικές απαντήσεις.
    - `top_p` για να περιορίσουμε την επιλογή των token σε εκείνα που συμβάλλουν στο κορυφαίο σωρευτικό ποσοστό πιθανότητας, ενισχύοντας την ποιότητα του παραγόμενου κειμένου.
    - `top_k` για να περιορίσουμε το μοντέλο στα κορυφαία K πιο πιθανά token, που μπορεί να βοηθήσει στην παραγωγή πιο συνεκτικών απαντήσεων.
    - `frequencyPenalty` και `presencePenalty` για να μειώσουμε την επανάληψη και να ενθαρρύνουμε τη διαφορετικότητα στο παραγόμενο κείμενο.

# [JavaScript](#tab/javascript)

```javascript
// Παράδειγμα JavaScript: Διαμόρφωση θερμοκρασίας και δειγματοληψίας Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Αρχικοποίηση του πελάτη MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Διαμόρφωση αιτήματος με διαφορετικές παραμέτρους δειγματοληψίας
  const creativeSampling = {
    temperature: 0.9,    // Υψηλότερη θερμοκρασία = περισσότερη τυχαιότητα/δημιουργικότητα
    topP: 0.92,          // Λαμβάνονται υπόψη tokens με μάζα πιθανότητας κορυφής 92%
    frequencyPenalty: 0.6, // Μείωση της επανάληψης ακολουθιών token
    presencePenalty: 0.4   // Τιμωρία tokens που έχουν εμφανιστεί στο κείμενο μέχρι στιγμής
  };
  
  const factualSampling = {
    temperature: 0.2,    // Χαμηλότερη θερμοκρασία = πιο ντετερμινιστικό/πραγματικό
    topP: 0.85,          // Ελαφρώς πιο εστιασμένη επιλογή token
    frequencyPenalty: 0.2, // Ελάχιστη ποινή επανάληψης
    presencePenalty: 0.1   // Ελάχιστη ποινή παρουσίας
  };
  
  try {
    // Αποστολή δύο αιτημάτων με διαφορετικές διαμορφώσεις δειγματοληψίας
    const creativeResponse = await client.sendPrompt(
      "Generate innovative ideas for sustainable urban transportation",
      {
        allowedTools: ['ideaGenerator', 'environmentalImpactTool'],
        ...creativeSampling
      }
    );
    
    const factualResponse = await client.sendPrompt(
      "Explain how electric vehicles impact carbon emissions",
      {
        allowedTools: ['factChecker', 'dataAnalysisTool'],
        ...factualSampling
      }
    );
    
    console.log('Creative Response (temperature=0.9):');
    console.log(creativeResponse.generatedText);
    
    console.log('\nFactual Response (temperature=0.2):');
    console.log(factualResponse.generatedText);
    
  } catch (error) {
    console.error('Error demonstrating sampling:', error);
  }
}

demonstrateSampling();
```

Στον παραπάνω κώδικα έχουμε:

- Αρχικοποιήσει έναν πελάτη MCP με διεύθυνση URL διακομιστή και κλειδί API.
- Διαμορφώσει δύο σύνολα παραμέτρων δειγματοληψίας: ένα για δημιουργικές εργασίες και ένα για εργασίες πραγματολογίας.
- Στείλει αιτήματα με αυτές τις διαμορφώσεις, επιτρέποντας στο μοντέλο να χρησιμοποιεί συγκεκριμένα εργαλεία για κάθε εργασία.
- Εκτυπώσει τις παραγόμενες απαντήσεις για να δείξει τις επιδράσεις διαφορετικών παραμέτρων δειγματοληψίας.
- Χρησιμοποιήσει `allowedTools` για να καθορίσουμε ποια εργαλεία μπορεί να χρησιμοποιήσει το μοντέλο κατά την παραγωγή. Σε αυτή την περίπτωση, επιτρέψαμε τα εργαλεία `ideaGenerator` και `environmentalImpactTool` για δημιουργικές εργασίες και `factChecker` και `dataAnalysisTool` για πραγματολογικές εργασίες.
- Χρησιμοποιήσει `temperature` για να ελέγξει την τυχαιότητα της εξόδου, όπου υψηλότερες τιμές οδηγούν σε πιο δημιουργικές απαντήσεις.

- Χρησιμοποιήθηκε το `top_p` για να περιοριστεί η επιλογή των tokens σε εκείνα που συμβάλλουν στη συνολική πιθανότητα κορυφής, βελτιώνοντας την ποιότητα του παραγόμενου κειμένου.
- Χρησιμοποιήθηκε το `frequencyPenalty` και το `presencePenalty` για μείωση της επανάληψης και ενθάρρυνση της ποικιλίας στην έξοδο.
- Χρησιμοποιήθηκε το `top_k` για να περιοριστεί το μοντέλο στα κορυφαία K πιο πιθανά tokens, κάτι που μπορεί να βοηθήσει στην παραγωγή πιο συνεκτικών απαντήσεων.

---

## Ντετερμινιστικό Δειγματοληψία

Για εφαρμογές που απαιτούν συνεπή αποτελέσματα, η ντετερμινιστική δειγματοληψία εξασφαλίζει αναπαραγώγιμα αποτελέσματα. Αυτό επιτυγχάνεται με τη χρήση σταθερού τυχαίου σπόρου και ρύθμιση της θερμοκρασίας στο μηδέν.

Ας δούμε ένα παρακάτω παράδειγμα υλοποίησης που δείχνει τη ντετερμινιστική δειγματοληψία σε διαφορετικές γλώσσες προγραμματισμού.

# [Java](#tab/java)

```java
// Παράδειγμα Java: Ντετερμινιστικές απαντήσεις με σταθερό σπόρο
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Χρήση σταθερού σπόρου για ντετερμινιστικά αποτελέσματα
        
        // Πρώτο αίτημα με σταθερό σπόρο
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Μηδενική θερμοκρασία για μέγιστη ντετερμινιστικότητα
            .build();
            
        // Δεύτερο αίτημα με τον ίδιο σπόρο
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Εκτέλεση και των δύο αιτημάτων
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Οι απαντήσεις πρέπει να είναι ταυτόσημες λόγω του ίδιου σπόρου και θερμοκρασίας=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Στον προηγούμενο κώδικα έχουμε:

- Δημιουργήσει έναν πελάτη MCP με συγκεκριμένη διεύθυνση διακομιστή.
- Ρυθμίσει δύο αιτήσεις με το ίδιο prompt, σταθερό σπόρο και μηδενική θερμοκρασία.
- Αποστείλει και τις δύο αιτήσεις και εκτυπώσει το παραγόμενο κείμενο.
- Επιδείξει ότι οι απαντήσεις είναι ταυτόσημες λόγω της ντετερμινιστικής φύσης της ρύθμισης δειγματοληψίας (ίδιος σπόρος και θερμοκρασία).
- Χρησιμοποιήσει το `setSeed` για να ορίσει σταθερό τυχαίο σπόρο, εξασφαλίζοντας ότι το μοντέλο παράγει το ίδιο αποτέλεσμα για την ίδια είσοδο κάθε φορά.
- Ρυθμίσει το `temperature` στο μηδέν για μέγιστη ντετερμινιστικότητα, πράγμα που σημαίνει ότι το μοντέλο θα επιλέγει πάντα το πιο πιθανό επόμενο token χωρίς τυχαιότητα.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Παράδειγμα JavaScript: Ντετερμινιστικές απαντήσεις με έλεγχο σπόρου
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Πρώτο αίτημα με σταθερό σπόρο
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Μηδενική θερμοκρασία για μέγιστο ντετερμινισμό
    });
    
    // Δεύτερο αίτημα με τον ίδιο σπόρο και θερμοκρασία
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Τρίτο αίτημα με διαφορετικό σπόρο αλλά ίδια θερμοκρασία
    const response3 = await client.sendPrompt(prompt, {
      seed: 67890,
      temperature: 0.0
    });
    
    console.log('Response 1:', response1.generatedText);
    console.log('Response 2:', response2.generatedText);
    console.log('Response 3:', response3.generatedText);
    console.log('Responses 1 and 2 match:', response1.generatedText === response2.generatedText);
    console.log('Responses 1 and 3 match:', response1.generatedText === response3.generatedText);
    
  } catch (error) {
    console.error('Error in deterministic sampling demo:', error);
  }
}

deterministicSampling();
```

Στον προηγούμενο κώδικα έχουμε:

- Αρχικοποιήσει έναν πελάτη MCP με διεύθυνση διακομιστή.
- Ρυθμίσει δύο αιτήσεις με το ίδιο prompt, σταθερό σπόρο και μηδενική θερμοκρασία.
- Αποστείλει και τις δύο αιτήσεις και εκτυπώσει το παραγόμενο κείμενο.
- Επιδείξει ότι οι απαντήσεις είναι ταυτόσημες λόγω της ντετερμινιστικής φύσης της ρύθμισης δειγματοληψίας (ίδιος σπόρος και θερμοκρασία).
- Χρησιμοποιήσει το `seed` για να ορίσει σταθερό τυχαίο σπόρο, εξασφαλίζοντας ότι το μοντέλο παράγει το ίδιο αποτέλεσμα για την ίδια είσοδο κάθε φορά.
- Ρυθμίσει το `temperature` στο μηδέν για μέγιστη ντετερμινιστικότητα, που σημαίνει ότι το μοντέλο επιλέγει πάντα το πιο πιθανό επόμενο token χωρίς τυχαιότητα.
- Χρησιμοποιήσει διαφορετικό σπόρο για την τρίτη αίτηση για να δείξει ότι η αλλαγή σπόρου έχει ως αποτέλεσμα διαφορετικές εξόδους, ακόμα και με το ίδιο prompt και θερμοκρασία.

---

## Δυναμική Διαμόρφωση Δειγματοληψίας

Η έξυπνη δειγματοληψία προσαρμόζει τις παραμέτρους ανάλογα με το πλαίσιο και τις απαιτήσεις κάθε αίτησης. Αυτό σημαίνει δυναμική ρύθμιση παραμέτρων όπως θερμοκρασία, top_p και ποινές βάσει του τύπου της εργασίας, των προτιμήσεων του χρήστη ή της ιστορικής απόδοσης.

Ας δούμε πώς να υλοποιήσουμε δυναμική δειγματοληψία σε διάφορες γλώσσες προγραμματισμού.

# [Python](#tab/python)

```python
# Παράδειγμα Python: Δυναμική δειγματοληψία βασισμένη στο πλαίσιο του αιτήματος
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Ορίστε προκαθορισμένες ρυθμίσεις δειγματοληψίας για διαφορετικούς τύπους εργασιών
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Επιλέξτε βασική προκαθορισμένη ρύθμιση
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Προσαρμόστε βάσει των προτιμήσεων χρήστη εάν παρέχονται
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Κλιμακώστε τη θερμοκρασία βάσει της προτίμησης δημιουργικότητας (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Προσαρμόστε το top_p βάσει της επιθυμητής ποικιλότητας απάντησης
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Δημιουργήστε και στείλτε το αίτημα με προσαρμοσμένες παραμέτρους δειγματοληψίας
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Επιστρέψτε την απάντηση με μεταδεδομένα δειγματοληψίας για διαφάνεια
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Στον προηγούμενο κώδικα έχουμε:

- Δημιουργήσει μια κλάση `DynamicSamplingService` που διαχειρίζεται προσαρμοστική δειγματοληψία.
- Ορίσει προεπιλογές δειγματοληψίας για διαφορετικούς τύπους εργασιών (δημιουργικές, πραγματολογικές, κώδικα, αναλυτικές).
- Επιλέξει μια βασική προεπιλογή δειγματοληψίας ανάλογα με τον τύπο εργασίας.
- Προσαρμόσει τις παραμέτρους δειγματοληψίας βάσει των προτιμήσεων του χρήστη, όπως το επίπεδο δημιουργικότητας και ποικιλίας.
- Αποστείλει την αίτηση με τις δυναμικά ρυθμισμένες παραμέτρους δειγματοληψίας.
- Επέστρεψε το παραγόμενο κείμενο μαζί με τις εφαρμοσμένες παραμέτρους δειγματοληψίας και τον τύπο εργασίας για διαφάνεια.
- Χρησιμοποιήσει το `temperature` για να ελέγξει την τυχαιότητα της εξόδου, όπου υψηλότερες τιμές οδηγούν σε πιο δημιουργικές απαντήσεις.
- Χρησιμοποιήσει το `top_p` για να περιορίσει την επιλογή των tokens σε εκείνα που συμβάλλουν στη συνολική πιθανότητα κορυφής, βελτιώνοντας την ποιότητα του παραγόμενου κειμένου.
- Χρησιμοποιήσει το `frequency_penalty` για να μειώσει τις επαναλήψεις και να ενθαρρύνει την ποικιλία στην έξοδο.
- Χρησιμοποιήσει το `user_preferences` για να επιτρέψει την προσαρμογή των παραμέτρων δειγματοληψίας βάσει των επιπέδων δημιουργικότητας και ποικιλίας που ορίζει ο χρήστης.
- Χρησιμοποιήσει το `task_type` για να καθορίσει την κατάλληλη στρατηγική δειγματοληψίας για την αίτηση, επιτρέποντας πιο προσαρμοσμένες απαντήσεις ανάλογα με τη φύση της εργασίας.
- Χρησιμοποιήσει τη μέθοδο `send_request` για να στείλει το prompt με τις διαμορφωμένες παραμέτρους δειγματοληψίας, εξασφαλίζοντας ότι το μοντέλο παράγει κείμενο σύμφωνα με τις καθορισμένες απαιτήσεις.
- Χρησιμοποιήσει το `generated_text` για να ανακτήσει την απάντηση του μοντέλου, η οποία επιστρέφεται μαζί με τις παραμέτρους δειγματοληψίας και τον τύπο εργασίας για περαιτέρω ανάλυση ή εμφάνιση.
- Χρησιμοποιήσει τις συναρτήσεις `min` και `max` για να εξασφαλίσει ότι οι προτιμήσεις του χρήστη περιορίζονται εντός έγκυρων ορίων, αποτρέποντας μη έγκυρες διαμορφώσεις δειγματοληψίας.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// Παράδειγμα JavaScript: Δυναμική ρύθμιση δειγματοληψίας με βάση το περιβάλλον χρήστη
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Ορισμός βασικών προφίλ δειγματοληψίας
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Παρακολούθηση ιστορικής απόδοσης
    this.performanceHistory = [];
  }
  
  // Ανίχνευση τύπου εργασίας από το prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Απλός ευρετικός εντοπισμός - μπορεί να βελτιωθεί με ταξινόμηση ML
    if (context.taskType) return context.taskType;
    
    if (promptLower.includes('code') || 
        promptLower.includes('function') || 
        promptLower.includes('program')) {
      return 'code';
    }
    
    if (promptLower.includes('explain') || 
        promptLower.includes('what is') || 
        promptLower.includes('how does')) {
      return 'factual';
    }
    
    if (promptLower.includes('creative') || 
        promptLower.includes('imagine') || 
        promptLower.includes('story')) {
      return 'creative';
    }
    
    // Προεπιλογή σε συνομιλιακό αν δεν ανιχνευτεί σαφής τύπος
    return 'conversational';
  }
  
  // Υπολογισμός παραμέτρων δειγματοληψίας βάσει περιεχομένου και προτιμήσεων χρήστη
  getSamplingParameters(prompt, context = {}) {
    // Ανίχνευση τύπου εργασίας
    const taskType = this.detectTaskType(prompt, context);
    
    // Λήψη βασικού προφίλ
    let params = {...this.samplingProfiles[taskType]};
    
    // Προσαρμογή βάσει προτιμήσεων χρήστη
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Κλιμάκωση από 1-10 στο κατάλληλο εύρος θερμοκρασίας
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Υψηλότερη ακρίβεια σημαίνει χαμηλότερο topP (περισσότερο εστιασμένη επιλογή)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Υψηλότερη συνέπεια σημαίνει χαμηλότερες ποινές
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Εφαρμογή ρυθμίσεων που μαθαίνονται από το ιστορικό απόδοσης
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Απλή προσαρμοστική λογική - μπορεί να βελτιωθεί με πιο εξελιγμένους αλγόριθμους
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Λήψη υπόψη μόνο του πρόσφατου ιστορικού
    
    if (relevantHistory.length > 0) {
      // Υπολογισμός μέσων βαθμολογιών απόδοσης
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Αν η απόδοση είναι κάτω από το όριο, προσαρμόστε τις παραμέτρους
      if (avgScore < 0.7) {
        // Ελαφριά προσαρμογή προς πιο ασφαλείς τιμές
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Καταγραφή απόδοσης για μελλοντικές ρυθμίσεις
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Βαθμολόγηση από 0 έως 1 για την ποιότητα της απόκρισης
    });
    
    // Περιορισμός μεγέθους ιστορικού
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Λήψη βελτιστοποιημένων παραμέτρων δειγματοληψίας
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Αποστολή αιτήματος με βελτιστοποιημένες παραμέτρους
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Αν ο χρήστης παρέχει ανατροφοδότηση, καταγράφεται για μελλοντική βελτιστοποίηση
    if (context.recordPerformance) {
      this.recordPerformance(prompt, samplingParams, response, context.feedbackScore || 0.5);
    }
    
    return {
      response,
      appliedSamplingParams: samplingParams,
      detectedTaskType: this.detectTaskType(prompt, context)
    };
  }
}

// Παράδειγμα χρήσης
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Δημιουργική εργασία με προσαρμοσμένες προτιμήσεις χρήστη
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Υψηλή δημιουργικότητα (1-10)
          consistency: 3  // Χαμηλή συνέπεια (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Εργασία δημιουργίας κώδικα
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Χαμηλή δημιουργικότητα
          precision: 8,   // Υψηλή ακρίβεια
          consistency: 9  // Υψηλή συνέπεια
        }
      }
    );
    
    console.log('\nCode Task:');
    console.log(`Detected type: ${codeResult.detectedTaskType}`);
    console.log('Applied sampling:', codeResult.appliedSamplingParams);
    console.log(codeResult.response.generatedText);
    
  } catch (error) {
    console.error('Error in adaptive sampling demo:', error);
  }
}

demonstrateAdaptiveSampling();
```

Στον προηγούμενο κώδικα έχουμε:

- Δημιουργήσει μια κλάση `AdaptiveSamplingManager` που διαχειρίζεται τη δυναμική δειγματοληψία βάσει τύπου εργασίας και προτιμήσεων χρήστη.
- Ορίσει προφίλ δειγματοληψίας για διαφορετικούς τύπους εργασιών (δημιουργικές, πραγματολογικές, κώδικα, συνομιλιακές).
- Εφαρμόσει μια μέθοδο για ανίχνευση του τύπου εργασίας από το prompt χρησιμοποιώντας απλά ευρετικά.
- Υπολογίσει παραμέτρους δειγματοληψίας βάσει του ανιχνευθέντος τύπου εργασίας και των προτιμήσεων του χρήστη.
- Εφαρμόσει διόρθωση που έχει μάθει με βάση την ιστορική απόδοση για βελτιστοποίηση των παραμέτρων δειγματοληψίας.
- Καταγράψει την απόδοση για μελλοντικές ρυθμίσεις, επιτρέποντας στο σύστημα να μαθαίνει από προηγούμενες αλληλεπιδράσεις.
- Αποστείλει αιτήσεις με δυναμικά διαμορφωμένες παραμέτρους δειγματοληψίας και επέστρεψε το παραγόμενο κείμενο μαζί με τις εφαρμοσμένες παραμέτρους και τον ανιχνευθέντα τύπο εργασίας.
- Χρησιμοποιήσει:
    - `userPreferences` για να επιτρέψει την προσαρμογή των παραμέτρων δειγματοληψίας βάσει των επιπέδων δημιουργικότητας, ακρίβειας και συνέπειας που ορίζει ο χρήστης.
    - `detectTaskType` για να καθορίσει τη φύση της εργασίας βάσει του prompt, επιτρέποντας πιο προσαρμοσμένες απαντήσεις.
    - `recordPerformance` για να καταγράψει την απόδοση των παραγόμενων απαντήσεων, δίνοντας τη δυνατότητα στο σύστημα να προσαρμόζεται και να βελτιώνεται με την πάροδο του χρόνου.
    - `applyLearnedAdjustments` για να τροποποιεί τις παραμέτρους δειγματοληψίας βάσει της ιστορικής απόδοσης, ενισχύοντας την ικανότητα του μοντέλου να παράγει απαντήσεις υψηλής ποιότητας.
    - `generateResponse` για να περιλαμβάνει ολόκληρη τη διαδικασία παραγωγής απάντησης με προσαρμοστική δειγματοληψία, καθιστώντας εύκολο το κάλεσμα με διαφορετικά prompts και πλαίσια.
    - `allowedTools` για να καθορίσει ποια εργαλεία μπορεί να χρησιμοποιήσει το μοντέλο κατά τη διάρκεια της παραγωγής, επιτρέποντας πιο απαντήσεις με επίγνωση του πλαισίου.
    - `feedbackScore` για να επιτρέψει στους χρήστες να παρέχουν ανατροφοδότηση για την ποιότητα της παραγόμενης απάντησης, η οποία μπορεί να χρησιμοποιηθεί για περαιτέρω βελτίωση της απόδοσης του μοντέλου με την πάροδο του χρόνου.
    - `performanceHistory` για να διατηρεί ένα αρχείο των προηγούμενων αλληλεπιδράσεων, δίνοντας τη δυνατότητα στο σύστημα να μαθαίνει από πετυχημένες ή αποτυχημένες εμπειρίες.
    - `getSamplingParameters` για να προσαρμόζει δυναμικά τις παραμέτρους δειγματοληψίας βάσει του πλαισίου της αίτησης, επιτρέποντας πιο ευέλικτη και ανταποκρινόμενη συμπεριφορά του μοντέλου.
    - `detectTaskType` για να ταξινομεί την εργασία βάσει του prompt, δίνοντας τη δυνατότητα στο σύστημα να εφαρμόζει κατάλληλες στρατηγικές δειγματοληψίας για διαφορετικούς τύπους αιτήσεων.
    - `samplingProfiles` για να ορίζει βασικές ρυθμίσεις δειγματοληψίας για διαφορετικούς τύπους εργασιών, επιτρέποντας γρήγορες προσαρμογές με βάση τη φύση της αίτησης.

---

## Τι ακολουθεί

- [5.7 Scaling](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->