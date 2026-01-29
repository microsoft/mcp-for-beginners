# Δειγματοληψία στο Πρωτόκολλο Πλαισίου Μοντέλου (Model Context Protocol)

Η δειγματοληψία είναι μια ισχυρή λειτουργία του MCP που επιτρέπει στους διακομιστές να ζητούν ολοκληρώσεις LLM μέσω του πελάτη, επιτρέποντας σύνθετες συμπεριφορές πρακτόρων, διατηρώντας παράλληλα την ασφάλεια και το απόρρητο. Η σωστή ρύθμιση της δειγματοληψίας μπορεί να βελτιώσει σημαντικά την ποιότητα και την απόδοση των απαντήσεων. Το MCP παρέχει έναν τυποποιημένο τρόπο ελέγχου του πώς τα μοντέλα παράγουν κείμενο με συγκεκριμένες παραμέτρους που επηρεάζουν την τυχαιότητα, τη δημιουργικότητα και τη συνοχή.

## Εισαγωγή

Σε αυτό το μάθημα, θα εξερευνήσουμε πώς να ρυθμίσουμε τις παραμέτρους δειγματοληψίας σε αιτήματα MCP και να κατανοήσουμε τους βασικούς μηχανισμούς του πρωτοκόλλου δειγματοληψίας.

## Στόχοι Μάθησης

Στο τέλος αυτού του μαθήματος, θα μπορείτε να:

- Κατανοείτε τις βασικές παραμέτρους δειγματοληψίας που είναι διαθέσιμες στο MCP.
- Ρυθμίζετε τις παραμέτρους δειγματοληψίας για διαφορετικές περιπτώσεις χρήσης.
- Υλοποιείτε ντετερμινιστική δειγματοληψία για αναπαραγώγιμα αποτελέσματα.
- Προσαρμόζετε δυναμικά τις παραμέτρους δειγματοληψίας με βάση το πλαίσιο και τις προτιμήσεις του χρήστη.
- Εφαρμόζετε στρατηγικές δειγματοληψίας για να βελτιώσετε την απόδοση του μοντέλου σε διάφορα σενάρια.
- Κατανοείτε πώς λειτουργεί η δειγματοληψία στη ροή πελάτη-διακομιστή του MCP.

## Πώς Λειτουργεί η Δειγματοληψία στο MCP

Η ροή δειγματοληψίας στο MCP ακολουθεί τα εξής βήματα:

1. Ο διακομιστής στέλνει ένα αίτημα `sampling/createMessage` στον πελάτη
2. Ο πελάτης εξετάζει το αίτημα και μπορεί να το τροποποιήσει
3. Ο πελάτης πραγματοποιεί δειγματοληψία από ένα LLM
4. Ο πελάτης εξετάζει την ολοκλήρωση
5. Ο πελάτης επιστρέφει το αποτέλεσμα στον διακομιστή

Αυτός ο σχεδιασμός με ανθρώπινη παρέμβαση εξασφαλίζει ότι οι χρήστες διατηρούν τον έλεγχο πάνω σε ό,τι βλέπει και παράγει το LLM.

## Επισκόπηση Παραμέτρων Δειγματοληψίας

Το MCP ορίζει τις ακόλουθες παραμέτρους δειγματοληψίας που μπορούν να ρυθμιστούν στα αιτήματα πελάτη:

| Παράμετρος | Περιγραφή | Τυπικό Εύρος |
|------------|-----------|--------------|
| `temperature` | Ελέγχει την τυχαιότητα στην επιλογή των tokens | 0.0 - 1.0 |
| `maxTokens` | Μέγιστος αριθμός tokens προς παραγωγή | Ακέραιος αριθμός |
| `stopSequences` | Προσαρμοσμένες ακολουθίες που σταματούν την παραγωγή όταν εμφανιστούν | Πίνακας συμβολοσειρών |
| `metadata` | Πρόσθετες παράμετροι ειδικές για τον πάροχο | Αντικείμενο JSON |

Πολλοί πάροχοι LLM υποστηρίζουν επιπλέον παραμέτρους μέσω του πεδίου `metadata`, που μπορεί να περιλαμβάνουν:

| Κοινή Παράμετρος Επέκτασης | Περιγραφή | Τυπικό Εύρος |
|----------------------------|-----------|--------------|
| `top_p` | Δειγματοληψία nucleus - περιορίζει τα tokens στο κορυφαίο σωρευτικό ποσοστό πιθανότητας | 0.0 - 1.0 |
| `top_k` | Περιορίζει την επιλογή tokens στις κορυφαίες K επιλογές | 1 - 100 |
| `presence_penalty` | Επιβάλλει ποινή σε tokens με βάση την παρουσία τους στο κείμενο μέχρι στιγμής | -2.0 - 2.0 |
| `frequency_penalty` | Επιβάλλει ποινή σε tokens με βάση τη συχνότητά τους στο κείμενο μέχρι στιγμής | -2.0 - 2.0 |
| `seed` | Συγκεκριμένος τυχαίος σπόρος για αναπαραγώγιμα αποτελέσματα | Ακέραιος αριθμός |

## Παράδειγμα Μορφής Αιτήματος

Ακολουθεί ένα παράδειγμα αιτήματος δειγματοληψίας από πελάτη στο MCP:

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

## Μορφή Απάντησης

Ο πελάτης επιστρέφει το αποτέλεσμα της ολοκλήρωσης:

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

## Έλεγχοι με Ανθρώπινη Παρέμβαση

Η δειγματοληψία MCP έχει σχεδιαστεί με επίβλεψη από ανθρώπους:

- **Για τα prompts**:
  - Οι πελάτες πρέπει να εμφανίζουν στους χρήστες το προτεινόμενο prompt
  - Οι χρήστες πρέπει να μπορούν να τροποποιούν ή να απορρίπτουν τα prompts
  - Τα συστημικά prompts μπορούν να φιλτράρονται ή να τροποποιούνται
  - Η συμπερίληψη του πλαισίου ελέγχεται από τον πελάτη

- **Για τις ολοκληρώσεις**:
  - Οι πελάτες πρέπει να εμφανίζουν στους χρήστες την ολοκλήρωση
  - Οι χρήστες πρέπει να μπορούν να τροποποιούν ή να απορρίπτουν τις ολοκληρώσεις
  - Οι πελάτες μπορούν να φιλτράρουν ή να τροποποιούν τις ολοκληρώσεις
  - Οι χρήστες ελέγχουν ποιο μοντέλο χρησιμοποιείται

Με αυτές τις αρχές κατά νου, ας δούμε πώς να υλοποιήσουμε τη δειγματοληψία σε διάφορες γλώσσες προγραμματισμού, εστιάζοντας στις παραμέτρους που υποστηρίζονται συνήθως από τους παρόχους LLM.

## Θέματα Ασφαλείας

Κατά την υλοποίηση της δειγματοληψίας στο MCP, λάβετε υπόψη τις ακόλουθες βέλτιστες πρακτικές ασφαλείας:

- **Επικυρώστε όλο το περιεχόμενο των μηνυμάτων** πριν τα στείλετε στον πελάτη
- **Καθαρίστε ευαίσθητες πληροφορίες** από prompts και ολοκληρώσεις
- **Εφαρμόστε όρια ρυθμού** για να αποτρέψετε κατάχρηση
- **Παρακολουθείτε τη χρήση της δειγματοληψίας** για ασυνήθιστα μοτίβα
- **Κρυπτογραφήστε τα δεδομένα κατά τη μεταφορά** χρησιμοποιώντας ασφαλή πρωτόκολλα
- **Διαχειριστείτε το απόρρητο των δεδομένων των χρηστών** σύμφωνα με τις σχετικές ρυθμίσεις
- **Ελέγξτε τα αιτήματα δειγματοληψίας** για συμμόρφωση και ασφάλεια
- **Ελέγξτε το κόστος** με κατάλληλα όρια
- **Εφαρμόστε χρονικά όρια** για τα αιτήματα δειγματοληψίας
- **Διαχειριστείτε τα σφάλματα μοντέλου με ευελιξία** χρησιμοποιώντας κατάλληλες εναλλακτικές λύσεις

Οι παράμετροι δειγματοληψίας επιτρέπουν τη λεπτομερή ρύθμιση της συμπεριφοράς των γλωσσικών μοντέλων για να επιτευχθεί η επιθυμητή ισορροπία μεταξύ ντετερμινιστικών και δημιουργικών αποτελεσμάτων.

Ας δούμε πώς να ρυθμίσουμε αυτές τις παραμέτρους σε διάφορες γλώσσες προγραμματισμού.

# [.NET](../../../../05-AdvancedTopics/mcp-sampling)

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

- Δημιουργήσει έναν πελάτη MCP με συγκεκριμένο URL διακομιστή.
- Ρυθμίσει ένα αίτημα με παραμέτρους δειγματοληψίας όπως `temperature`, `top_p` και `top_k`.
- Στείλει το αίτημα και εκτυπώσει το παραγόμενο κείμενο.
- Χρησιμοποιήσει:
    - `allowedTools` για να καθορίσουμε ποια εργαλεία μπορεί να χρησιμοποιήσει το μοντέλο κατά την παραγωγή. Σε αυτή την περίπτωση, επιτρέψαμε τα εργαλεία `ideaGenerator` και `marketAnalyzer` για να βοηθήσουν στη δημιουργία δημιουργικών ιδεών εφαρμογών.
    - `frequencyPenalty` και `presencePenalty` για να ελέγξουμε την επανάληψη και την ποικιλία στην έξοδο.
    - `temperature` για να ελέγξουμε την τυχαιότητα της εξόδου, όπου υψηλότερες τιμές οδηγούν σε πιο δημιουργικές απαντήσεις.
    - `top_p` για να περιορίσουμε την επιλογή των tokens σε εκείνα που συμβάλλουν στο κορυφαίο σωρευτικό ποσοστό πιθανότητας, βελτιώνοντας την ποιότητα του παραγόμενου κειμένου.
    - `top_k` για να περιορίσουμε το μοντέλο στα κορυφαία K πιο πιθανά tokens, κάτι που βοηθά στην παραγωγή πιο συνεκτικών απαντήσεων.
    - `frequencyPenalty` και `presencePenalty` για να μειώσουμε την επανάληψη και να ενθαρρύνουμε την ποικιλία στο παραγόμενο κείμενο.

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Temperature and Top-P sampling configuration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialize the MCP client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configure request with different sampling parameters
  const creativeSampling = {
    temperature: 0.9,    // Higher temperature = more randomness/creativity
    topP: 0.92,          // Consider tokens with top 92% probability mass
    frequencyPenalty: 0.6, // Reduce repetition of token sequences
    presencePenalty: 0.4   // Penalize tokens that have appeared in the text so far
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lower temperature = more deterministic/factual
    topP: 0.85,          // Slightly more focused token selection
    frequencyPenalty: 0.2, // Minimal repetition penalty
    presencePenalty: 0.1   // Minimal presence penalty
  };
  
  try {
    // Send two requests with different sampling configurations
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

- Αρχικοποιήσει έναν πελάτη MCP με URL διακομιστή και κλειδί API.
- Ρυθμίσει δύο σύνολα παραμέτρων δειγματοληψίας: ένα για δημιουργικές εργασίες και ένα για πραγματολογικές εργασίες.
- Στείλει αιτήματα με αυτές τις ρυθμίσεις, επιτρέποντας στο μοντέλο να χρησιμοποιεί συγκεκριμένα εργαλεία για κάθε εργασία.
- Εκτυπώσει τις παραγόμενες απαντήσεις για να δείξει τις επιδράσεις των διαφορετικών παραμέτρων δειγματοληψίας.
- Χρησιμοποιήσει `allowedTools` για να καθορίσουμε ποια εργαλεία μπορεί να χρησιμοποιήσει το μοντέλο κατά την παραγωγή. Σε αυτή την περίπτωση, επιτρέψαμε τα `ideaGenerator` και `environmentalImpactTool` για δημιουργικές εργασίες, και `factChecker` και `dataAnalysisTool` για πραγματολογικές εργασίες.
- Χρησιμοποιήσει `temperature` για να ελέγξει την τυχαιότητα της εξόδου, όπου υψηλότερες τιμές οδηγούν σε πιο δημιουργικές απαντήσεις.
- Χρησιμοποιήσει `top_p` για να περιορίσει την επιλογή των tokens σε εκείνα που συμβάλλουν στο κορυφαίο σωρευτικό ποσοστό πιθανότητας, βελτιώνοντας την ποιότητα του παραγόμενου κειμένου.
- Χρησιμοποιήσει `frequencyPenalty` και `presencePenalty` για να μειώσει την επανάληψη και να ενθαρρύνει την ποικιλία στην έξοδο.
- Χρησιμοποιήσει `top_k` για να περιορίσει το μοντέλο στα κορυφαία K πιο πιθανά tokens, κάτι που βοηθά στην παραγωγή πιο συνεκτικών απαντήσεων.

---

## Ντετερμινιστική Δειγματοληψία

Για εφαρμογές που απαιτούν συνεπή αποτελέσματα, η ντετερμινιστική δειγματοληψία εξασφαλίζει αναπαραγώγιμα αποτελέσματα. Αυτό επιτυγχάνεται με τη χρήση σταθερού τυχαίου σπόρου και ρύθμιση της θερμοκρασίας στο μηδέν.

Ας δούμε ένα παράδειγμα υλοποίησης που δείχνει τη ντετερμινιστική δειγματοληψία σε διάφορες γλώσσες προγραμματισμού.

# [Java](../../../../05-AdvancedTopics/mcp-sampling)

```java
// Java Example: Deterministic responses with fixed seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Using a fixed seed for deterministic results
        
        // First request with fixed seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Zero temperature for maximum determinism
            .build();
            
        // Second request with the same seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Execute both requests
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Responses should be identical due to same seed and temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Στον παραπάνω κώδικα έχουμε:

- Δημιουργήσει έναν πελάτη MCP με συγκεκριμένο URL διακομιστή.
- Ρυθμίσει δύο αιτήματα με το ίδιο prompt, σταθερό σπόρο και θερμοκρασία μηδέν.
- Στείλει και τα δύο αιτήματα και εκτυπώσει το παραγόμενο κείμενο.
- Επιδείξει ότι οι απαντήσεις είναι ταυτόσημες λόγω της ντετερμινιστικής φύσης της ρύθμισης δειγματοληψίας (ίδιος σπόρος και θερμοκρασία).
- Χρησιμοποιήσει `setSeed` για να ορίσει σταθερό τυχαίο σπόρο, εξασφαλίζοντας ότι το μοντέλο παράγει την ίδια έξοδο για την ίδια είσοδο κάθε φορά.
- Ρυθμίσει τη `temperature` στο μηδέν για μέγιστη ντετερμινιστικότητα, που σημαίνει ότι το μοντέλο θα επιλέγει πάντα το πιο πιθανό επόμενο token χωρίς τυχαιότητα.

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Deterministic responses with seed control
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // First request with fixed seed
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Zero temperature for maximum determinism
    });
    
    // Second request with same seed and temperature
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Third request with different seed but same temperature
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

Στον παραπάνω κώδικα έχουμε:

- Αρχικοποιήσει έναν πελάτη MCP με URL διακομιστή.
- Ρυθμίσει δύο αιτήματα με το ίδιο prompt, σταθερό σπόρο και θερμοκρασία μηδέν.
- Στείλει και τα δύο αιτήματα και εκτυπώσει το παραγόμενο κείμενο.
- Επιδείξει ότι οι απαντήσεις είναι ταυτόσημες λόγω της ντετερμινιστικής φύσης της ρύθμισης δειγματοληψίας (ίδιος σπόρος και θερμοκρασία).
- Χρησιμοποιήσει `seed` για να ορίσει σταθερό τυχαίο σπόρο, εξασφαλίζοντας ότι το μοντέλο παράγει την ίδια έξοδο για την ίδια είσοδο κάθε φορά.
- Ρυθμίσει τη `temperature` στο μηδέν για μέγιστη ντετερμινιστικότητα, που σημαίνει ότι το μοντέλο θα επιλέγει πάντα το πιο πιθανό επόμενο token χωρίς τυχαιότητα.
- Χρησιμοποιήσει διαφορετικό σπόρο για το τρίτο αίτημα, για να δείξει ότι η αλλαγή του σπόρου οδηγεί σε διαφορετικά αποτελέσματα, ακόμα και με το ίδιο prompt και θερμοκρασία.

---

## Δυναμική Ρύθμιση Δειγματοληψίας

Η έξυπνη δειγματοληψία προσαρμόζει τις παραμέτρους με βάση το πλαίσιο και τις απαιτήσεις κάθε αιτήματος. Αυτό σημαίνει δυναμική ρύθμιση παραμέτρων όπως `temperature`, `top_p` και ποινές, ανάλογα με τον τύπο εργασίας, τις προτιμήσεις του χρήστη ή την ιστορική απόδοση.

Ας δούμε πώς να υλοποιήσουμε δυναμική δειγματοληψία σε διάφορες γλώσσες προγραμματισμού.

# [Python](../../../../05-AdvancedTopics/mcp-sampling)

```python
# Python Example: Dynamic sampling based on request context
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Define sampling presets for different task types
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Select base preset
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Adjust based on user preferences if provided
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Scale temperature based on creativity preference (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Adjust top_p based on desired response diversity
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Create and send request with custom sampling parameters
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Return response with sampling metadata for transparency
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Στον παραπάνω κώδικα έχουμε:

- Δημιουργήσει την κλάση `DynamicSamplingService` που διαχειρίζεται την προσαρμοστική δειγματοληψία.
- Ορίσει προκαθορισμένες ρυθμίσεις δειγματοληψίας για διαφορετικούς τύπους εργασιών (δημιουργικές, πραγματολογικές, κώδικα, αναλυτικές).
- Επιλέξει βασική ρύθμιση δειγματοληψίας με βάση τον τύπο εργασίας.
- Προσαρμόσει τις παραμέτρους δειγματοληψίας με βάση τις προτιμήσεις του χρήστη, όπως το επίπεδο δημιουργικότητας και ποικιλίας.
- Στείλει το αίτημα με τις δυναμικά ρυθμισμένες παραμέτρους δειγματοληψίας.
- Επέστρεψε το παραγόμενο κείμενο μαζί με τις εφαρμοσμένες παραμέτρους δειγματοληψίας και τον τύπο εργασίας για διαφάνεια.
- Χρησιμοποιήσει `temperature` για να ελέγξει την τυχαιότητα της εξόδου, όπου υψηλότερες τιμές οδηγούν σε πιο δημιουργικές απαντήσεις.
- Χρησιμοποιήσει `top_p` για να περιορίσει την επιλογή των tokens σε εκείνα που συμβάλλουν στο κορυφαίο σωρευτικό ποσοστό πιθανότητας, βελτιώνοντας την ποιότητα του παραγόμενου κειμένου.
- Χρησιμοποιήσει `frequency_penalty` για να μειώσει την επανάληψη και να ενθαρρύνει την ποικιλία στην έξοδο.
- Χρησιμοποιήσει `user_preferences` για να επιτρέψει την προσαρμογή των παραμέτρων δειγματοληψίας βάσει των ορισμένων από τον χρήστη επιπέδων δημιουργικότητας και ποικιλίας.
- Χρησιμοποιήσει `task_type` για να καθορίσει την κατάλληλη στρατηγική δειγματοληψίας για το αίτημα, επιτρέποντας πιο εξατομικευμένες απαντήσεις

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.