# Έλεγχοι Ασφαλείας MCP - Ενημέρωση Δεκεμβρίου 2025

> **Τρέχον Πρότυπο**: Αυτό το έγγραφο αντικατοπτρίζει τις απαιτήσεις ασφαλείας της [Προδιαγραφής MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) και τις επίσημες [Καλύτερες Πρακτικές Ασφαλείας MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Το Πρωτόκολλο Πλαισίου Μοντέλου (MCP) έχει ωριμάσει σημαντικά με ενισχυμένους ελέγχους ασφαλείας που αντιμετωπίζουν τόσο την παραδοσιακή ασφάλεια λογισμικού όσο και τις απειλές ειδικές για την ΤΝ. Αυτό το έγγραφο παρέχει ολοκληρωμένους ελέγχους ασφαλείας για ασφαλείς υλοποιήσεις MCP από τον Δεκέμβριο του 2025.

## **ΥΠΟΧΡΕΩΤΙΚΕΣ Απαιτήσεις Ασφαλείας**

### **Κρίσιμες Απαγορεύσεις από την Προδιαγραφή MCP:**

> **ΑΠΑΓΟΡΕΥΕΤΑΙ**: Οι διακομιστές MCP **ΔΕΝ ΠΡΕΠΕΙ** να αποδέχονται οποιαδήποτε διακριτικά δεν εκδόθηκαν ρητά για τον διακομιστή MCP  
>
> **ΑΠΑΓΟΡΕΥΕΤΑΙ**: Οι διακομιστές MCP **ΔΕΝ ΠΡΕΠΕΙ** να χρησιμοποιούν συνεδρίες για αυθεντικοποίηση  
>
> **ΑΠΑΙΤΕΙΤΑΙ**: Οι διακομιστές MCP που υλοποιούν εξουσιοδότηση **ΠΡΕΠΕΙ** να επαληθεύουν ΟΛΑ τα εισερχόμενα αιτήματα  
>
> **ΥΠΟΧΡΕΩΤΙΚΟ**: Οι διακομιστές μεσολάβησης MCP που χρησιμοποιούν στατικά αναγνωριστικά πελατών **ΠΡΕΠΕΙ** να λαμβάνουν τη συγκατάθεση του χρήστη για κάθε δυναμικά εγγεγραμμένο πελάτη

---

## 1. **Έλεγχοι Αυθεντικοποίησης & Εξουσιοδότησης**

### **Ενσωμάτωση Εξωτερικού Παρόχου Ταυτότητας**

**Τρέχον Πρότυπο MCP (2025-06-18)** επιτρέπει στους διακομιστές MCP να αναθέτουν την αυθεντικοποίηση σε εξωτερικούς παρόχους ταυτότητας, αντιπροσωπεύοντας σημαντική βελτίωση στην ασφάλεια:

### **Ενσωμάτωση Εξωτερικού Παρόχου Ταυτότητας**

**Τρέχον Πρότυπο MCP (2025-11-25)** επιτρέπει στους διακομιστές MCP να αναθέτουν την αυθεντικοποίηση σε εξωτερικούς παρόχους ταυτότητας, αντιπροσωπεύοντας σημαντική βελτίωση στην ασφάλεια:

**Οφέλη Ασφαλείας:**
1. **Εξάλειψη Κινδύνων Προσαρμοσμένης Αυθεντικοποίησης**: Μειώνει την επιφάνεια ευπάθειας αποφεύγοντας προσαρμοσμένες υλοποιήσεις αυθεντικοποίησης  
2. **Ασφάλεια Επιπέδου Επιχείρησης**: Αξιοποιεί καθιερωμένους παρόχους ταυτότητας όπως το Microsoft Entra ID με προηγμένα χαρακτηριστικά ασφαλείας  
3. **Κεντρική Διαχείριση Ταυτότητας**: Απλοποιεί τη διαχείριση κύκλου ζωής χρήστη, τον έλεγχο πρόσβασης και τον έλεγχο συμμόρφωσης  
4. **Πολυπαραγοντική Αυθεντικοποίηση**: Κληρονομεί δυνατότητες MFA από παρόχους ταυτότητας επιχειρήσεων  
5. **Πολιτικές Υπό Όρους Πρόσβασης**: Επωφελείται από ελέγχους πρόσβασης βάσει κινδύνου και προσαρμοσμένη αυθεντικοποίηση

**Απαιτήσεις Υλοποίησης:**
- **Επαλήθευση Κοινού Διακριτικού**: Επαλήθευση ότι όλα τα διακριτικά εκδόθηκαν ρητά για τον διακομιστή MCP  
- **Επαλήθευση Εκδότη**: Επαλήθευση ότι ο εκδότης του διακριτικού ταιριάζει με τον αναμενόμενο πάροχο ταυτότητας  
- **Επαλήθευση Υπογραφής**: Κρυπτογραφική επαλήθευση της ακεραιότητας του διακριτικού  
- **Επιβολή Λήξης**: Αυστηρή επιβολή ορίων διάρκειας ζωής διακριτικού  
- **Επαλήθευση Πεδίων**: Διασφάλιση ότι τα διακριτικά περιέχουν τις κατάλληλες άδειες για τις ζητούμενες λειτουργίες

### **Ασφάλεια Λογικής Εξουσιοδότησης**

**Κρίσιμοι Έλεγχοι:**
- **Ολοκληρωμένοι Έλεγχοι Εξουσιοδότησης**: Τακτικές ανασκοπήσεις ασφαλείας όλων των σημείων λήψης αποφάσεων εξουσιοδότησης  
- **Προεπιλεγμένες Ασφαλείς Ρυθμίσεις**: Άρνηση πρόσβασης όταν η λογική εξουσιοδότησης δεν μπορεί να λάβει οριστική απόφαση  
- **Όρια Δικαιωμάτων**: Σαφής διαχωρισμός μεταξύ διαφορετικών επιπέδων προνομίων και πρόσβασης σε πόρους  
- **Καταγραφή Ελέγχου**: Πλήρης καταγραφή όλων των αποφάσεων εξουσιοδότησης για παρακολούθηση ασφαλείας  
- **Τακτικοί Έλεγχοι Πρόσβασης**: Περιοδική επικύρωση δικαιωμάτων χρηστών και αναθέσεων προνομίων

## 2. **Ασφάλεια Διακριτικών & Έλεγχοι Anti-Passthrough**

### **Αποτροπή Διέλευσης Διακριτικών**

**Η διέλευση διακριτικών απαγορεύεται ρητά** στην Προδιαγραφή Εξουσιοδότησης MCP λόγω κρίσιμων κινδύνων ασφαλείας:

**Αντιμετωπιζόμενοι Κίνδυνοι Ασφαλείας:**
- **Παραβίαση Ελέγχων**: Παρακάμπτει βασικούς ελέγχους ασφαλείας όπως περιορισμό ρυθμού, επαλήθευση αιτημάτων και παρακολούθηση κυκλοφορίας  
- **Κατάρρευση Υπευθυνότητας**: Καθιστά αδύνατη την ταυτοποίηση πελάτη, διαφθείροντας τα αρχεία ελέγχου και την έρευνα περιστατικών  
- **Εξαγωγή Δεδομένων μέσω Μεσολαβητή**: Επιτρέπει σε κακόβουλους παράγοντες να χρησιμοποιούν διακομιστές ως μεσολαβητές για μη εξουσιοδοτημένη πρόσβαση σε δεδομένα  
- **Παραβιάσεις Ορίων Εμπιστοσύνης**: Παραβιάζει τις υποθέσεις εμπιστοσύνης υπηρεσιών σχετικά με την προέλευση διακριτικών  
- **Πλευρική Κίνηση**: Διακριτικά που έχουν παραβιαστεί σε πολλαπλές υπηρεσίες επιτρέπουν ευρύτερη επέκταση επιθέσεων

**Έλεγχοι Υλοποίησης:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### **Πρότυπα Ασφαλούς Διαχείρισης Διακριτικών**

**Καλύτερες Πρακτικές:**
- **Βραχυπρόθεσμα Διακριτικά**: Ελαχιστοποίηση παραθύρου έκθεσης με συχνή ανανέωση διακριτικών  
- **Έκδοση Κατά Ζήτηση**: Έκδοση διακριτικών μόνο όταν απαιτείται για συγκεκριμένες λειτουργίες  
- **Ασφαλής Αποθήκευση**: Χρήση υλικού ασφαλείας (HSM) ή ασφαλών θυρίδων κλειδιών  
- **Δέσμευση Διακριτικών**: Δέσμευση διακριτικών σε συγκεκριμένους πελάτες, συνεδρίες ή λειτουργίες όπου είναι δυνατόν  
- **Παρακολούθηση & Ειδοποίηση**: Ανίχνευση σε πραγματικό χρόνο κακής χρήσης διακριτικών ή μη εξουσιοδοτημένων προτύπων πρόσβασης

## 3. **Έλεγχοι Ασφαλείας Συνεδριών**

### **Αποτροπή Απαγωγής Συνεδρίας**

**Διανύσματα Επίθεσης που Αντιμετωπίζονται:**
- **Έγχυση Εντολών Απαγωγής Συνεδρίας**: Κακόβουλα συμβάντα εγχέονται στην κοινόχρηστη κατάσταση συνεδρίας  
- **Προσποίηση Συνεδρίας**: Μη εξουσιοδοτημένη χρήση κλεμμένων αναγνωριστικών συνεδρίας για παράκαμψη αυθεντικοποίησης  
- **Επιθέσεις Επαναφοράς Ροής**: Εκμετάλλευση επανεκκίνησης συμβάντων που αποστέλλονται από διακομιστή για έγχυση κακόβουλου περιεχομένου

**Υποχρεωτικοί Έλεγχοι Συνεδρίας:**
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```

**Ασφάλεια Μεταφοράς:**
- **Επιβολή HTTPS**: Όλη η επικοινωνία συνεδρίας μέσω TLS 1.3  
- **Ασφαλή Χαρακτηριστικά Cookie**: HttpOnly, Secure, SameSite=Strict  
- **Πινάκωση Πιστοποιητικών**: Για κρίσιμες συνδέσεις για αποτροπή επιθέσεων MITM

### **Σκέψεις για Κατάσταση με Κατάσταση vs Χωρίς Κατάσταση**

**Για Υλοποιήσεις με Κατάσταση:**
- Η κοινόχρηστη κατάσταση συνεδρίας απαιτεί επιπλέον προστασία έναντι επιθέσεων έγχυσης  
- Η διαχείριση συνεδρίας με ουρά απαιτεί επαλήθευση ακεραιότητας  
- Πολλαπλές παρουσίες διακομιστών απαιτούν ασφαλή συγχρονισμό κατάστασης συνεδρίας

**Για Υλοποιήσεις χωρίς Κατάσταση:**
- Διαχείριση συνεδρίας με βάση JWT ή παρόμοια διακριτικά  
- Κρυπτογραφική επαλήθευση ακεραιότητας κατάστασης συνεδρίας  
- Μειωμένη επιφάνεια επίθεσης αλλά απαιτεί ισχυρή επαλήθευση διακριτικών

## 4. **Έλεγχοι Ασφαλείας Ειδικοί για ΤΝ**

### **Άμυνα κατά της Έγχυσης Εντολών**

**Ενσωμάτωση Microsoft Prompt Shields:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**Έλεγχοι Υλοποίησης:**
- **Καθαρισμός Εισόδου**: Ολοκληρωμένη επαλήθευση και φιλτράρισμα όλων των εισόδων χρήστη  
- **Ορισμός Ορίων Περιεχομένου**: Σαφής διαχωρισμός μεταξύ οδηγιών συστήματος και περιεχομένου χρήστη  
- **Ιεραρχία Οδηγιών**: Κατάλληλοι κανόνες προτεραιότητας για αντικρουόμενες οδηγίες  
- **Παρακολούθηση Εξόδου**: Ανίχνευση πιθανώς επιβλαβών ή παραποιημένων εξόδων

### **Αποτροπή Δηλητηρίασης Εργαλείων**

**Πλαίσιο Ασφάλειας Εργαλείων:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**Δυναμική Διαχείριση Εργαλείων:**
- **Ροές Εργασίας Έγκρισης**: Ρητή συγκατάθεση χρήστη για τροποποιήσεις εργαλείων  
- **Δυνατότητες Επαναφοράς**: Ικανότητα επαναφοράς σε προηγούμενες εκδόσεις εργαλείων  
- **Έλεγχος Αλλαγών**: Πλήρες ιστορικό τροποποιήσεων ορισμών εργαλείων  
- **Αξιολόγηση Κινδύνου**: Αυτοματοποιημένη αξιολόγηση της στάσης ασφάλειας εργαλείων

## 5. **Αποτροπή Επίθεσης Confused Deputy**

### **Ασφάλεια Proxy OAuth**

**Έλεγχοι Αποτροπής Επίθεσης:**
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**Απαιτήσεις Υλοποίησης:**
- **Επαλήθευση Συγκατάθεσης Χρήστη**: Ποτέ να μην παραλείπονται οθόνες συγκατάθεσης για δυναμική εγγραφή πελατών  
- **Επαλήθευση URI Ανακατεύθυνσης**: Αυστηρή επαλήθευση λίστας επιτρεπτών προορισμών ανακατεύθυνσης  
- **Προστασία Κωδικού Εξουσιοδότησης**: Βραχυπρόθεσμοι κωδικοί με επιβολή μονοχρησίας  
- **Επαλήθευση Ταυτότητας Πελάτη**: Ισχυρή επαλήθευση διαπιστευτηρίων και μεταδεδομένων πελάτη

## 6. **Ασφάλεια Εκτέλεσης Εργαλείων**

### **Sandboxing & Απομόνωση**

**Απομόνωση με Βάση Κοντέινερ:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**Απομόνωση Διαδικασιών:**
- **Ξεχωριστά Πλαίσια Διαδικασιών**: Κάθε εκτέλεση εργαλείου σε απομονωμένο χώρο διαδικασίας  
- **Διαδικασιακή Επικοινωνία**: Ασφαλείς μηχανισμοί IPC με επαλήθευση  
- **Παρακολούθηση Διαδικασιών**: Ανάλυση συμπεριφοράς κατά την εκτέλεση και ανίχνευση ανωμαλιών  
- **Επιβολή Πόρων**: Αυστηρά όρια σε CPU, μνήμη και λειτουργίες I/O

### **Υλοποίηση Ελάχιστων Δικαιωμάτων**

**Διαχείριση Δικαιωμάτων:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## 7. **Έλεγχοι Ασφάλειας Εφοδιαστικής Αλυσίδας**

### **Επαλήθευση Εξαρτήσεων**

**Ολοκληρωμένη Ασφάλεια Συστατικών:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### **Συνεχής Παρακολούθηση**

**Ανίχνευση Απειλών Εφοδιαστικής Αλυσίδας:**
- **Παρακολούθηση Υγείας Εξαρτήσεων**: Συνεχής αξιολόγηση όλων των εξαρτήσεων για ζητήματα ασφαλείας  
- **Ενσωμάτωση Πληροφοριών Απειλών**: Ενημερώσεις σε πραγματικό χρόνο για αναδυόμενες απειλές εφοδιαστικής αλυσίδας  
- **Ανάλυση Συμπεριφοράς**: Ανίχνευση ασυνήθιστης συμπεριφοράς σε εξωτερικά συστατικά  
- **Αυτοματοποιημένη Αντίδραση**: Άμεσος περιορισμός παραβιασμένων συστατικών

## 8. **Έλεγχοι Παρακολούθησης & Ανίχνευσης**

### **Διαχείριση Πληροφοριών Ασφαλείας και Συμβάντων (SIEM)**

**Ολοκληρωμένη Στρατηγική Καταγραφής:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### **Ανίχνευση Απειλών σε Πραγματικό Χρόνο**

**Ανάλυση Συμπεριφοράς:**
- **Ανάλυση Συμπεριφοράς Χρηστών (UBA)**: Ανίχνευση ασυνήθιστων προτύπων πρόσβασης χρηστών  
- **Ανάλυση Συμπεριφοράς Οντοτήτων (EBA)**: Παρακολούθηση συμπεριφοράς διακομιστών MCP και εργαλείων  
- **Ανίχνευση Ανωμαλιών με Μηχανική Μάθηση**: Αναγνώριση απειλών ασφαλείας με τεχνητή νοημοσύνη  
- **Συσχέτιση Πληροφοριών Απειλών**: Ταύτιση παρατηρούμενων δραστηριοτήτων με γνωστά πρότυπα επιθέσεων

## 9. **Αντιμετώπιση Περιστατικών & Ανάκτηση**

### **Αυτοματοποιημένες Δυνατότητες Αντίδρασης**

**Άμεσες Ενέργειες Αντίδρασης:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### **Δυνατότητες Διερεύνησης**

**Υποστήριξη Έρευνας:**
- **Διατήρηση Αρχείου Ελέγχου**: Αμετάβλητη καταγραφή με κρυπτογραφική ακεραιότητα  
- **Συλλογή Αποδεικτικών**: Αυτοματοποιημένη συγκέντρωση σχετικών αντικειμένων ασφαλείας  
- **Ανακατασκευή Χρονολογίου**: Λεπτομερής αλληλουχία γεγονότων που οδήγησαν σε περιστατικά ασφαλείας  
- **Αξιολόγηση Επιπτώσεων**: Εκτίμηση εύρους παραβίασης και έκθεσης δεδομένων

## **Κύριες Αρχές Αρχιτεκτονικής Ασφαλείας**

### **Άμυνα σε Βάθος**
- **Πολλαπλά Επίπεδα Ασφαλείας**: Καμία μοναδική σημείο αποτυχίας στην αρχιτεκτονική ασφαλείας  
- **Πλεονασματικοί Έλεγχοι**: Επικαλυπτόμενα μέτρα ασφαλείας για κρίσιμες λειτουργίες  
- **Μηχανισμοί Ασφαλούς Αποτυχίας**: Ασφαλείς προεπιλογές όταν τα συστήματα αντιμετωπίζουν σφάλματα ή επιθέσεις

### **Υλοποίηση Μηδενικής Εμπιστοσύνης**
- **Ποτέ Μη Εμπιστεύεστε, Πάντα Επαληθεύετε**: Συνεχής επικύρωση όλων των οντοτήτων και αιτημάτων  
- **Αρχή Ελάχιστου Δικαιώματος**: Ελάχιστα δικαιώματα πρόσβασης για όλα τα συστατικά  
- **Μικρο-Τμηματοποίηση**: Λεπτομερείς έλεγχοι δικτύου και πρόσβασης

### **Συνεχής Εξέλιξη Ασφαλείας**
- **Προσαρμογή στο Τοπίο Απειλών**: Τακτικές ενημερώσεις για αντιμετώπιση αναδυόμενων απειλών  
- **Αποτελεσματικότητα Ελέγχων Ασφαλείας**: Συνεχής αξιολόγηση και βελτίωση των ελέγχων  
- **Συμμόρφωση με Προδιαγραφές**: Ευθυγράμμιση με εξελισσόμενα πρότυπα ασφαλείας MCP

---

## **Πόροι Υλοποίησης**

### **Επίσημη Τεκμηρίωση MCP**
- [Προδιαγραφή MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Καλύτερες Πρακτικές Ασφαλείας MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Προδιαγραφή Εξουσιοδότησης MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Λύσεις Ασφαλείας Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Πρότυπα Ασφαλείας**
- [Καλύτερες Πρακτικές Ασφαλείας OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 για Μεγάλα Μοντέλα Γλώσσας](https://genai.owasp.org/)
- [Πλαίσιο Κυβερνοασφάλειας NIST](https://www.nist.gov/cyberframework)

---

> **Σημαντικό**: Αυτοί οι έλεγχοι ασφαλείας αντικατοπτρίζουν την τρέχουσα προδιαγραφή MCP (2025-06-18). Επαληθεύετε πάντα με την πιο πρόσφατη [επίσημη τεκμηρίωση](https://spec.modelcontextprotocol.io/) καθώς τα πρότυπα εξελίσσονται γρήγορα.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->